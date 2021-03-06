# Running an App to be tested, and a rest API testing framework in separate containers on the same host

make is required to run locally and is used to orchestrate the docker commands to make setup and teardown simple 

## Starting the app container
- navigate to the root of the basic-restapi-app directory
- Start the App container by entering make run
- Verify the fastAPI app is running by hitting the url: <http://localhost:8080/docs#/>

## Starting the rest api automation framework container
- Add a secrets.ini file to the project root directory by copying the contents of the secrets_backup.ini file 
- Navigate to the root of the basic-restapi-testfwk directory
- Start the container by entering make dev
- Verify the pytest test suite runs by running pytest in the test api terminal

## sectrets.ini

Secretes.ini is git ignored, and needs to be added and in place for the example make file to add the required environmental variables to the docker container.    
A sample file named *secrets_backup.ini* is included in the framework to make adding the file and demoing easier

To enable a container to access a service on the host, the solutioon is host OS specific. For OSX:
<https://docs.docker.com/desktop/mac/networking/>

> ## I want to connect from a container to a service on the host (OSX instructions)

> - The host has a changing IP address (or none if you have no network access). We recommend that you connect to the special DNS name host.docker.internal which resolves to the internal IP address used by the host. This is for development purpose and will not work in a production environment outside of Docker Desktop for Mac.

> - You can also reach the gateway using gateway.docker.internal.

> - If you have installed Python on your machine, use the following instructions as an example to connect from a container to a service on the host:

> - Run the following command to start a simple HTTP server on port 8000.

> - $ python -m http.server 8000

> If you have installed Python 2.x, run python -m SimpleHTTPServer 8000.

> - Now, run a container, install curl, and try to connect to the host using the following commands:

 - $ docker run --rm -it alpine sh
 - $ apk add curl
 - $ curl <http://host.docker.internal:8000>
 - $ exit

> so on a mac, localhost needs to be changed to host.docker.internal in config.py

## .dockerignore

Once running, create and adjust .dockerignore file to prevent certain things from being copied to the image

**/__pycache__/
*.pyc
venv
.vscode
.idea
.gitignore
.DS_Store
Dockerfile
db*

## .gitignore

!**/__pycache__/
*.pyc
venv
.vscode
.idea
.DS_Store
*.html
.pytest_cache
reports

## update APP_URL to support deployments to different environments

Need to make App globals dynamic and pulled from the environment at deploy time.

Usually as part of cicd, container properties are passed at build time

Create a secrets.ini file in the root of the project directory, and put variables into the file.

APP_URL=<http://host.docker.internal:8080>
ADMIN_USER=admin  
ADMIN_PASSWORD=admin  

replace literal string with os.getenv and empty string as defaults in config.py file

update docker local command to load secrets.ini file

docker run $(LOCAL_OPTS) --name $(NAME) --env-file secrets.ini -it $(IMAGE) /bin/bash
