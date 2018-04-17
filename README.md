# Resident Scheduler Website
Web interface to Internal Medicine Resident Scheduler Model

The Internal Medicine Resident Scheduler is the interface for accessing the resident 
scheduling Pyomo model written for RIT's Multidisciplinary Senior Design course.


## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes. See deployment for notes on 
how to deploy the project on a live system.

### Prerequisites

Here's everything you need to get started with this

1. A UNIX-based operating system
    * Tested on the following operating systems
        * Ubuntu 16.04
        * RHEL 6.9
2. Python 3.5+
3. Pip (should come with Python install)
4. GLPK
5. Redis

### Installing

Below is a step-by-step guide on how to install the Resident Scheduler on your system from scratch.

#### Prerequisites

* [GLPK](https://www.gnu.org/software/glpk/) - Follow the instructions to install GLPK on your system.

* [Redis](https://redis.io/) - Install through your package manager of choice

#### Resident Scheduler

1. (optional) - Create a Python virtual environment.
    * ```python3 -m venv YOUR_VENV_NAME```
2. (optional) - Activate your virtual environment.
    * ```source YOUR_VENV_NAME/bin/activate```
3. Clone this repository.
    * ```git clone https://github.com/msd18751/sched-site.git```
4. Checkout submodules.
    * ```cd sched-site/```
    * ```git submodule update --init --recursive```
5. Install Python libraries.
    * ```python3 -m pip install -r requirements.txt```
    * If you see an error about "pkg-resources" edit requirements.txt to remove that line and attempt to install the packages again.
6. Exit the directory and create a dummy Django project. This will create a unique secret key that is necessary to securely operate the site.
    * ```cd ..```
    * ```mkdir dummy```
    * ```cd dummy/```
    * ```django-admin startproject dummy_proj```
    * ```grep SECRET_KEY dummy_proj/dummpy_proj.settings.py > ../sched-site/sched_site/sched_site/secrets.py```
    * ```cd ..```
    * ```rm -r dummy/```
8. Create an admin account
    * ```cd sched-site/sched_site```
    * ```python3 manage.py createsuperuser```
9. (optional) - Deactivate virutal environment.
    * ```deactivate```
10. Reflect on how far you've come.

## Deployment

The following is a step-by-step guide on how to run the Resident Scheduler on your system.

1. (optional)- If installed via Python virtual environment, activate it
    * ```source YOUR_VENV_NAME/bin/activate```
2. (optional) - If you want to accept connections outside of localhost, add the hostnames to the KNOWN_HOSTS list in sched-site/sched_site/sched_site/settings.py
    * ```KNOWN_HOSTS = ["localhost", "mydomain.com"]```
3. Make sure the Redis daemon is running
    * ```sudo service redis start```
4. Navigate to the manage.py location
    * ```cd sched-site/sched_site/```
5. Activate the Celery worker, remember the PID
    * ```celery -A sched_site worker -l info &```
6. Activate the Django server on your desired interface and port, remember the PID. The following example will run the server on all interfaces and listen on port 8000.
    * ```python3 manage.py runserver 0.0.0.0:8000 &```
7. To stop running the site you can use a utility like top or htop to kill the processes or the 'kill' command with the PIDs
    * ```kill -9 PID```

### NOTE
If deploying for production, set the DEBUG flag in settings.py to False.1

## Built With

* [Pyomo](http://www.pyomo.org/) - Optimization modeling language
* [GLPK](https://www.gnu.org/software/glpk/) - Linear solver library

## Contributing

### Style

#### Python
Please follow the PEP8 style guide for all python files, which can be found
[here](http://legacy.python.org/dev/peps/pep-0008/). Please run a PEP8 linter
before you commit any code.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Liam Kalir** - lk8150@rit.edu
* **Taylor Blackwell** - teb5039@rit.edu
* **Daniel Fox** - dcf2981@rit.edu

## License

GPL 3.0

## Acknowledgments
* Thanks to Dr. Ruben Proaño and Akshit Agarwal for their research
