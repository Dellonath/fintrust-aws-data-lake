from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct
from .nested.rds import RDS
from .nested.s3 import Bucket

class BatchIngestionStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # self.vpc = ec2.Vpc.from_lookup(self, 'VPC',
        #     is_default=True
        # )
        
        RDS(self, 'RDS')
        Bucket(self, 'Buckets')
