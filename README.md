# Project Summary

In our app environment, we don’t allow developers to SSH into servers without leadership approval. Therefore, it is critical that our team provide tools to allow developers to debug problems using our monitoring tools.

For example, when we get an alert that a disk is getting full, you would want to know what files are using up all of the space.


## Development tools

1. Python
2. Ubuntu (16.x or later) or similar distribution
3. SSH enabled servers

### Prerequisites

| Prerequisite                                | Version |
| ------------------------------------------- | ------- |
| [Python](http://www.mongodb.org/downloads) | `~ ^2.7`  |

> _Updating to the latest releases is recommended_.

If python and ssh is already installed in your machine, run the following commands to validate the versions:

```shell
python -v
ssh -h
```

If your versions are lower than the prerequisite versions, you should update.

#### Cloning Repository

1. Open a Terminal / Command Line / Bash Shell in your projects directory (_i.e.: `/yourprojectdirectory/`_)
2. Clone the linix-disk-usage-util repository

```shell
$ git clone https://github.com/nirajKpanda/linux-disk-usage-util.git
```

This will download the entire linix-disk-usage-util repo to your project directory.

#### Setup Your Upstream

1. Change directory to the new linix-disk-usage-util directory (`cd linix-disk-usage-util`)

Congratulations, you now have a local copy of the linix-disk-usage-util project!


### Setup linix-disk-usage-util enviornment
Once you have linix-disk-usage-util cloned, before you start the application, you first need to install all of the dependencies:

```bash
pip install -r requirements.txt
```

### Script Usage

[niraj@niraj]$python get_diskusage.py --help<br />
usage: get_diskusage.py [-h] [-i HOST] [-u USER] [-p PASSWORD] [-f FILENAME]<br />
                        -m MOUNTPOINT<br />
<br />
optional arguments:<br />
  -h, --help            show this help message and exit<br />
  -i HOST, --host HOST  The hostname or IP address of the server to connect<br />
  -u USER, --user USER  The remote server username preferably a sudo user<br />
  -p PASSWORD, --password PASSWORD<br />
                        The password of the remote server user<br />
  -f FILENAME, --filename FILENAME<br />
                        Load server credentials from configuration file,<br />
                        provide absolute path of the config file<br />
  -m MOUNTPOINT, --mountpoint MOUNTPOINT<br />
                        Mount point of the server directory structure<br />
[niraj@niraj]$<br />

### Run in local server

[niraj@niraj]$python get_diskusage.py -i localhost -m /tmp<br />
INFO:User requested to fetch local server file disk usage.....<br />
Mount point is : /tmp<br />
{<br />
    "/tmp/unity_support_test/tmp0": 0, <br />
    "/tmp/e3546f11-84f5-4c95-90e9a5af-36eeff8e/tmpdmp": 221248, <br />
    "/tmp/config-err-0PdOED": 0, <br />
    "/tmp//tmporg/tmpchromium/tmpChromium/tmpMNLHuI/Skype1_5/tmppng": 652, <br />
    "/tmp/a": 349, <br />
    "/tmp//tmpX0-lock": 11<br />
}<br />
[niraj@niraj]$<br />

### Run in remote server
[niraj@niraj]python get_diskusage.py -i <ip-address> -u <username> -p <password> -m <mountpoint>


### Load server credetnitals from config file
[niraj@nira]$python get_diskusage.py -f server.config -m /tmp


