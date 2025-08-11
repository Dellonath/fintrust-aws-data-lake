# my_nested_stack.py
from aws_cdk import (
    NestedStack,
    RemovalPolicy,
    aws_s3 as s3
)
from constructs import Construct

class BucketsStack(NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.bronze_bucket = s3.Bucket(self, 'S3BucketBronze', 
            bucket_name='fintrust-bronze',
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
        self.silver_bucket = s3.Bucket(self, 'S3BucketSilver', 
            bucket_name='fintrust-silver',
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
        self.gold_bucket = s3.Bucket(self, 'S3BucketGold', 
            bucket_name='fintrust-gold',
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
