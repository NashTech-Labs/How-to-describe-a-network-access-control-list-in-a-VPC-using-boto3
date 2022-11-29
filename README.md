# How to describe a network access control list (NACL) using boto3


## What is network access control list (NACL)?
### A network access control list (NACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.You can follow this [link](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) to know more.

--------------
### I have define the script to describe the Network access control list[NACL]. You just need to pass the region and tag key:value at the run time and one more thing your aws credential (access and secret key) must be configure in your system then you will get the details of you resource. You need to follow the below commands.

**Files:** 

```
       describe_nacl.py
```
## Apply the script using below commands:

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command:


        python3 <describe_nacl.py>


