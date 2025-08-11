from aws_cdk import (
    Stack
)
from constructs import Construct
from .nested.rds import RDS
from ..common.common_stack import CommonStack

class BatchStack(Stack):
    def __init__(self, scope: Construct, id: str, common_stack: CommonStack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # self.vpc = ec2.Vpc.from_lookup(self, 'VPC',
        #     is_default=True
        # )
        
        RDS(self, 'RDS')
