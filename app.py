#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.batch_ingestion.batch_ingestion_stack import BatchIngestionStack


app = cdk.App()
env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
BatchIngestionStack(app, 'FintrustAwsDataLake', env=env)
app.synth()
