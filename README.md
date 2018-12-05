# Replication of mongoengine issue #1964

https://github.com/MongoEngine/mongoengine/issues/1964

## Description

If mongoengine connects to a replicaset specifying SECONDARY read preference,
then upsert_one() will sometimes not return an object, even if the read preference
is set to primary for that one call.

Reproduced initially on:

- macOS 10.14.1
- Python 3.5.6
- mongoengine==0.16.2
- pymongo==3.7.2

## Steps to run the example

1. `docker-compose -f docker-compose.yml up`
2. pip install -r requirements.txt
2. python setup.py

## docker-compose.yml

Docker compose file adapted from: https://github.com/yeasy/docker-compose-files/tree/ab71081372f551aab55f61861782f68694899425/mongo_cluster
