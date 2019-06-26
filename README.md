# Remediar

`remediar` is an issue and vulnerability tracker framework. It helps you to 
check on the state of findings and to document their rectification.

During a penetration test or a security check assignment one will collect 
details about configuration mistakes, vulnerabilities, deviations from
given standards, security implications and various other information about
the targets. To confirm that after a mitigation all relevant issues were
addressed, often one will need to spend the same amount of time on the 
assessment as in the first place. This includes comparing the results from
the tools used and to remove the noise. 

`remediar` allows to check for specific issues like an open TCP port, an
available SSH cipher or an entry in the HTTP headers and will give you in a
quick way the foundation to say that vulnerabilities or issues were closed 
on the systems.


## Installation

One requirements is that you have Python 3 installed. Clone the Git repository
and change to the checkout. 

```bash
$ git clone https://github.com/fabaff/remediar.git
$ ce remediar
$ pip3 install -r requirements.txt
$ pip3 install setup.py
```

## Usage

### Command-line interface

You should be able to use `remediar` ight after the installation from the 
command-line.

```bash
$ remediar --help
usage: remediar [-h] [-d] [-q] [-v] {run} ...

Remediar is an issue and vulnerability tracker framework

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    full application debug mode
  -q, --quiet    suppress all console output
  -v, --version  show program's version number and exit

sub-commands:
  {run}
    run          run tasks
```

The task file has to be written in YAML. It can contain multiple hosts and 
need the required checks including the necessary details 

```yaml
# Remediar Sample Tasks file
---
name: 'This is the campaign name'
description: 'More details...'
hosts:
  - ip_address: 192.168.122.164
    name: demo1.lab.network.area
    ssh:
      checks:
        - is_hmac_used
    smb:
      checks:
        - are_shares_present
  - ip_address: 192.168.122.165
    name: This is demo 2
    http:
      port: 80
      checks:
        - is_server_present
```

### Docker

Included is a basic `Dockerfile` for building and distributing `Remediar`,
and can be built with the included `make` helper:

```basgh
$ make docker
$ docker run -it remediar --help
```

This requires that you have `docker` or `podman` installed.

## Documentation

At the current state there is no documentation beside the README.md available.

## License

`remediar` is licensed under the Apache Software License 2.0.