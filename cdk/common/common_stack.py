from aws_cdk import (
    Stack
)
from constructs import Construct
from .nested.s3 import BucketsStack

class CommonStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        self.buckets_stack = BucketsStack(self, 'BucketsStack')
