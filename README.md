### Description
This is a simple scalable app based on python flask and RedisJson. 

### Context
Traditionally, we would set up a DB and use redis as cache. This requires additional processes to load data into cache, and introduces a complex system with multiple components. 

### Setup
Here, we use redis as primary DB and cache. We keep flask app stateless (as API service) and it can be scaled according to load. Redis also can be scaled / sharded accordingly. 

### Benefits
Flask app and Redis are decoupled and can be managed separately for loadbalancing, disaster recovery, cost optimization, etc.


