# Anagrams
Demonstration repository to showcase an anagram generation app using Docker and Kubernetes on AWS.

# Installation (to run webapp locally)
- git clone this repo
- Install python3 and virtualenv
- Setup virtualenv (these remaining steps can be accomplished by running setup.sh)
```shell
    $ virtualenv -p python3.6 _env
    $ source _env/bin/activate
```
- Run pip install for all project dependencies
```shell
    $ pip install -r requirements.txt
```

- set the anagrams application entry file in env variable
```shell
   $ export FLASK_APP=anagrams.py
   $ export LC_ALL=en_US.UTF-8
   $ export LANG=en_US.UTF-8
```
- Start the flask application
```
$ flask run --host=0.0.0.0
```

- Visit http://127.0.0.1:5000/

# Deploying with Docker 

After code changes, in Anagrams repo directory, run:
```shell
    $ docker build -t anagrams .
```
To push to docker, run
```shell
    $ docker login
```
Enter docker id and password.
Push new image to dockerhub.
```shell
    $ docker images (get image id of anagrams/latest)
    # docker tag (image id) dlalonde/anagrams:v1.3
    $ docker push dlalonde/anagrams:v1.3
```
To run the service in a docker image locally:
```shell
docker run -d -it -p 8000:8000 dlalonde/anagrams:v1.3
```
View at 0.0.0.0:8000

# Kubernetes deployment
### Set up local web access
```
kubectl proxy
```
Dashboard available at http://localhost:8001/ui
### Create namespace, deployment and service
```
kubectl create namespace anagrams
kubectl run --namespace anagrams anagrams --image=dlalonde/anagrams --replicas=1 --port=8000
kubectl expose --namespace=anagrams deployment anagrams --type=LoadBalancer --port=80 --target-port=8000 --name=anagrams-public
```
Retrieve URL:
```
kubectl --namespace=anagrams describe service anagrams-public
```
URL example: LoadBalancer Ingress:     a2c1997a7d57d11e7a7fd12166a12f4e-1654783314.us-east-1.elb.amazonaws.com
### Deploy a new image
After creating a new version and pushing to DockerHub, 
edit deployment.yaml and update
```
spec:
      containers:
      - image: dlalonde/anagrams:[new version]
```
Run
```shell
kubectl apply -f deployment.yaml -n anagrams
```
or edit the running deployment:
```shell
kubectl edit deployment anagrams -n anagrams
```

# Maintainer
- Doug Lalonde - <douglalonde@gmail.com>
