from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2
)
from constructs import Construct


class AwsCdkVpnStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, certificate_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = aws_ec2.Vpc(
            self,
            "Vpc_CDK",
            cidr="172.31.0.0/16",
            max_azs=1,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    name='Public-Subent',
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                    cidr_mask=20
                ),
            ],
        )

        isubnet = vpc.public_subnets

        client_vpn = aws_ec2.ClientVpnEndpoint(
            scope=self,
            id="Client_VPN",
            vpc=vpc,
            cidr="10.0.0.0/22",
            authorize_all_users_to_vpc_cidr=False,
            split_tunnel=False,
            server_certificate_arn=certificate_arn,
            client_certificate_arn=certificate_arn,
        )

        client_vpn.add_authorization_rule(
            id="auth",
            cidr="0.0.0.0/0",
        )

        for isub in isubnet:
            client_vpn.add_route(
                id="routing",
                cidr='0.0.0.0/0',
                target=aws_ec2.ClientVpnRouteTarget.subnet(subnet=isub)
            )
