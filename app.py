#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.common.common_stack import CommonStack
from cdk.batch.batch_stack import BatchStack
from cdk.streaming.streaming_stack import StreamingStack


app = cdk.App()
common_stack = CommonStack(app, 'FintrustCommonStack')
# batch_stack = BatchStack(app, 'FintrustBatchStack', common_stack)
streaming_stack = StreamingStack(app, 'FintrustStreamingStack', common_stack)
app.synth()
