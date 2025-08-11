from aws_cdk import (
    NestedStack,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
    aws_kinesis as kinesis,
    aws_kinesisfirehose as firehose,
    aws_logs as logs,
    aws_iam as iam,
    RemovalPolicy,
    Duration
)
from constructs import Construct
from ...common.common_stack import CommonStack

class StreamingKinesis(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, common_stack: CommonStack, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        self.buckets_stack = common_stack.buckets_stack
        
        # KINESIS DATA STREAM
        self.stream = kinesis.Stream(
            self, 'KinesisDataStream',
            stream_name='finstrust-data-stream',
            shard_count=1,
            retention_period=Duration.hours(24),
            stream_mode=kinesis.StreamMode.PROVISIONED,
            removal_policy=RemovalPolicy.DESTROY
        )

        # FIREHOUSE
        self.firehose_name = 'fintrust-datastream-s3-delivery'
        self.firehose_role = iam.Role(self, 'FirehoseRole',
            assumed_by=iam.ServicePrincipal('firehose.amazonaws.com'),
            description='Role used for consuming data from Kinesis Data Stream and push data into S3'
        )
        self.stream.grant_read(self.firehose_role)
        self.buckets_stack.bronze_bucket.grant_read_write(self.firehose_role)
        
        self.firehose_log_group = logs.LogGroup(self, 'FirehoseLogGroup',
            log_group_name=f'/aws/lambda/{self.firehose_name}',
            removal_policy=RemovalPolicy.DESTROY,
            retention=logs.RetentionDays.ONE_WEEK
        )
        self.firehose = firehose.DeliveryStream(self, 'FirehoseToS3',
            delivery_stream_name=self.firehose_name,
            source=firehose.KinesisStreamSource(self.stream),
            destination=firehose.S3Bucket(
                bucket=self.buckets_stack.bronze_bucket, 
                buffering_interval=Duration.seconds(30),
                file_extension='.json',
                data_output_prefix='firehose_'
            ),
            role=self.firehose_role
        )

        # LAMBDAS
        self.lambdas_role = iam.Role(self, 'LambdasRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            description='Role for Kinesis processing Lambda'
        )
        self.lambdas_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole')
        )
        
        # LAMBDA producer
        self.lambda_producer_function_name = 'fintrust-streaming-producer-lambda'
        self.lambda_producer_log_group = logs.LogGroup(self, 'LambdasLogGroup',
            log_group_name=f'/aws/lambda/{self.lambda_producer_function_name}',
            removal_policy=RemovalPolicy.DESTROY,
            retention=logs.RetentionDays.ONE_WEEK
        )
        self.lambda_producer = lambda_.Function(self, 'StreamingProducerLambda',
            function_name=self.lambda_producer_function_name,
            runtime=lambda_.Runtime.PYTHON_3_13,
            code=lambda_.Code.from_asset('cdk/streaming/lambda'),
            handler='producer.handler',
            role=self.lambdas_role,
            log_group=self.lambda_producer_log_group
        )

        # # LAMBDA consumer
        # self.lambda_consumer = lambda_.Function(self, 'StreamingConsumerLambda',
        #     function_name='fintrust-streaming-consumer-lambda',
        #     runtime=lambda_.Runtime.PYTHON_3_13,
        #     code=lambda_.Code.from_asset('cdk/streaming/lambda'),
        #     handler='consumer.handler',
        #     role=self.lambdas_role,
        #     environment={
        #         'RAW_BUCKET': self.buckets_stack.bronze_bucket.bucket_name,
        #         'STREAM_NAME': self.stream.stream_name
        #     }
        # )

        # connecting lambda to kinesis stream
        # self.lambda_consumer.add_event_source(
        #     lambda_event_sources.KinesisEventSource(
        #         self.stream,
        #         batch_size=10, # how many records per invocation
        #         starting_position=lambda_.StartingPosition.TRIM_HORIZON, # from earliest
        #         enabled=True
        #     )
        # )

        # grant Lambda permissions to read from the stream
        self.stream.grant_read_write(self.lambdas_role)

        # grant Lambda permissions to read/write to necessary buckets
        self.buckets_stack.bronze_bucket.grant_read_write(self.lambdas_role)
        self.buckets_stack.silver_bucket.grant_read_write(self.lambdas_role)
