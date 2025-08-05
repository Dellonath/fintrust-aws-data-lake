import os
from dotenv import load_dotenv
from aws_cdk import (
    NestedStack,
    aws_secretsmanager as secretsmanager,
    aws_rds as rds,
    aws_ec2 as ec2,
    SecretValue,
    RemovalPolicy
)
from constructs import Construct

load_dotenv()

class RDS(NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        pgdb_secret_name = 'dev/rds/dbcredentials'
        
        pgdb_credentials = secretsmanager.Secret(self, 'RDSPgDbCredentials',
            secret_name=pgdb_secret_name,
            secret_object_value={
                'username': SecretValue.unsafe_plain_text(os.getenv('rds_username')),
                'database': SecretValue.unsafe_plain_text(os.getenv('rds_database')),
                'password': SecretValue.unsafe_plain_text(os.getenv('rds_password'))
            }
        )

        vpc = ec2.Vpc.from_lookup(self, 'DefaultVPC', is_default=True)
        sg = ec2.SecurityGroup(self, 'RDSSecurityGroup',
            security_group_name='fintrust-pgdb-sg',
            vpc = vpc,
            allow_all_outbound = True
        )
        sg.add_egress_rule(
            ec2.Peer.ipv4(os.getenv('sg_ingress_ip')),
            ec2.Port.tcp(5432),
        )
        # TO DO: add security groups rules
        
        rds_instance = rds.DatabaseInstance(self, 'RDSPostgresInstance',
            instance_identifier='fintrust-db-instance',
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_16
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            credentials=rds.Credentials.from_secret(pgdb_credentials),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            publicly_accessible=True,
            allocated_storage=20,
            multi_az=False,
            backup_retention=None,
            deletion_protection=False,
            removal_policy=RemovalPolicy.DESTROY,
            security_groups=[sg]
        )
