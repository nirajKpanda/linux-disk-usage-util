# Project Summary

In our production environment, we don’t allow developers to SSH into servers without leadership approval. Therefore, it is critical that our team provide tools to allow developers to debug problems using our monitoring tools.

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

1. Change directory to the new node-shopkart directory (`cd linix-disk-usage-util`)

Congratulations, you now have a local copy of the linix-disk-usage-util project!


### Setup linix-disk-usage-util enviornment
Once you have linix-disk-usage-util cloned, before you start the application, you first need to install all of the dependencies:

```bash
pip install -r requirements.txt
```