# Lottery APP

This project consist of a lottery service that every day at midnight will choose a winner from within all the participants for a specific lottery.

In order to have this service up and running, you can execute the command `make up` from within the root directory. This will build and run two services: one regarding the lottery application that will manage the participants, ballots and active lotteries, as well as chose a winner every night; the other will be a PostgreSQL service that will manage the database of the system.

To stop and delete the running containers you can execute `make down`, and to clean the lottery service image you can use `make clean_image`.

By running the command `make test` you will launch and run all the necessary infrastructure to run the tests for this project, as well as the execution of these. After the execution, you can use the previous commands to delete and clean your environment from undesired containers and images.

This project was created using Django REST Framework, so you will be able to access the service data through Django's API by accessing host http://0.0.0.0:8000 once the services are up and running.

## How to use 

You can test this application by requesting the service once is up and running. The following are examples on how to request it:

1. To register as lottery participant:

`curl -d '{"name": “Fabio”, "surname": "Alonso", "national_id_card":"923746183S", "age": 27}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8000/participants/`

2. To submit a ballot for a lottery:

`curl -d '{"number": "11", "lottery_date": "2023-08-07", "participant": "http://0.0.0.0:8000/participants/6/"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8000/ballots/`

3. To check the winning ballot for a specific lottery:

`curl http://0.0.0.0:8000/lotteries/2023-08-07/`

