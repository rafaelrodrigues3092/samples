# SQL Server AlwaysOn with containers

This code uses two images of SQL Server docker to setup AlwaysOn Read-Scale/Clusterless AlwaysOn.


## How To

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

## Connecting to SQL Server

- Connect to the primary replica using SQL Server Management Studio (SSMS) using localhost,2500
- Connect to the secondary replica using SQL Server Management Studio (SSMS) using localhost,2600

## Failover

- Only a forced failover works in this type of setup. To perform a failover, connect to the secondary (localhost,2600) and run the command
ALTER AVAILABILITY GROUP AG1 FORCE_FAILOVER_ALLOW_DATA_LOSS;


## Troubleshooting

- If you get sa login errors, please adjust the INIT_WAIT values in the docker-compose.yml file.
Sometimes, depending on the system, the container startup tasks may take longer and it the start sequence could potentially try to start setting you AlwaysOn before SQL Server is up and running.