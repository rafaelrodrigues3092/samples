## SQL Server AlwaysOn with containers

This code uses two images of SQL Server docker to setup AlwaysOn Read-Scale/Clusterless AlwaysOn.


### How to Use

1. Run the following command in this directory:

```
docker-compose up
```
It will take about 2 min to configure the environemnt

In your terminal, you should see something like this
```
...
db1    | ##      AOAG script execution completed     ##
...
db2    | ##      AOAG script execution completed     ##
...
```

2. Connect to the SQL Server instances using the sa login and the passowrd listed in the docker-compose.yml file

3. When done, clean up the environement by running
```
docker-compose down
```
