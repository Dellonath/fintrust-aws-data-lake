# my_nested_stack.py
from aws_cdk import (
    NestedStack,
    aws_s3 as s3
)
from constructs import Construct

class Bucket(NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bronze_bucket = s3.Bucket(self, 'BronzeBucket', bucket_name='fintrust-bronze')
        silver_bucket = s3.Bucket(self, 'SilverBucket', bucket_name='fintrust-silver')
        gold_bucket   = s3.Bucket(self, 'GoldBucket', bucket_name='fintrust-gold')
