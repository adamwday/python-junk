## Purpose:
This script is executed on the EC2 "host" for your ECS cluster. Once executed, it begins to collect docker container stats to a local file, parse the metric data, and "put" the data to AWS/CloudWatch. From there you can pull them into Grafana or some other visualiation tool.

## How To Contribute to this file

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push -u origin my-new-feature`
5. Submit a pull request - enjoy!

----------

Additional Credit: (Co-worker at Dice) Mark Hayford
