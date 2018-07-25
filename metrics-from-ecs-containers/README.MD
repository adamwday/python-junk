## Purpose:
This script is executed on the EC2 "host" for your ECS cluster. Once executed, it begins to collect docker container stats to a local file, parse the metric data, and "put" the data to AWS/CloudWatch. From there you can pull them into Grafana or some other visualiation tool.

## Usage:
One method to deploy this script is to store it in an S3 bucket for retrieval. You can reference this location in your user data script from the 'cluster.template.json' file for your ECS cluster. An example of how this is configured in user data is seen below.
```
"UserData": {
          "Fn::Base64": {
            "Fn::Join": [
              "",
              [
                "#!/bin/bash -xe\n",
                "echo ECS_CLUSTER=",
                {
                  "Ref": "ECSCluster"
                },
                " >> /etc/ecs/ecs.config\n",
                "yum install -y aws-cfn-bootstrap\n",
                "yum install aws-cli -y\n",
                "yum install git -y\n",
                "yum install awslogs -y\n",
                "/opt/aws/bin/cfn-signal -e $? ",
                "         --stack ",
                {
                  "Ref": "AWS::StackName"
                },
                "         --resource ECSAutoScalingGroup ",
                "         --region ",
                {
                  "Ref": "AWS::Region"
                },
                "\n",
                "service awslogs start\n",
                "mkdir -p /opt/dataplatform/metrics/\n",
                "touch /opt/dataplatform/metrics/stats.txt\n",
                "chmod 766 /opt/dataplatform/metrics/stats.txt\n",
                "aws s3 cp s3://dataplatform-userdata-scripts/ECSCloudwatchMetrics/cloudwatchPutECStaskMetrics.py /opt/dataplatform/metrics/cloudwatchPutECStaskMetrics.py\n",
                "echo '*/5 * * * * python /opt/dataplatform/metrics/cloudwatchPutECStaskMetrics.py' > /opt/dataplatform/metrics/stats.txt\n",
                "sudo -u ec2-user bash -c 'crontab stats.txt'\n",
                "python  /opt/dataplatform/metrics/test.py\n"
              ]
            ]
          }
        }
      }
    },
```
As you can see above, we are creating a local directory on the EC2 host, creating a stats file to store them in, copying the script from S3 and then executing the script with crontab. As your containers spin up or down, the metrics will be sent to cloudwatch for you to get.
## How To Contribute to this file

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push -u origin my-new-feature`
5. Submit a pull request - enjoy!

----------

Additional Credit: (Co-worker at Dice) Mark Hayford
