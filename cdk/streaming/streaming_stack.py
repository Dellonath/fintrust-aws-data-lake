from aws_cdk import (
    Stack
)
from constructs import Construct
from .nested.kinesis import StreamingKinesis
from ..common.common_stack import CommonStack

class StreamingStack(Stack):
    def __init__(self, scope: Construct, id: str, common_stack: CommonStack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        StreamingKinesis(self, 'StreamingKinesis', common_stack)
