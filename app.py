#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_vpn.aws_cdk_vpn_stack import AwsCdkVpnStack
from dotenv import load_dotenv

load_dotenv()

app = cdk.App()
certificate_arn = os.environ['CERTIFICATE_ARN']
client_vpn = AwsCdkVpnStack(app, "AwsCdkVpnStack", certificate_arn)

cdk.Tags.of(client_vpn).add('Name', 'Test_VPN')

app.synth()
