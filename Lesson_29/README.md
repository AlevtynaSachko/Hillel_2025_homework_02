# Docker + SQLAlchemy + Postgres 

CreateReadUpdateDelete з SQLAlchemy у Docker.

## Запуск без docker-compose
```
docker network create appnet
docker run -d --name pg --network appnet -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=appdb -p 5432:5432 postgres:16
docker build -t pyapp .
docker run --rm --name pyapp --network appnet -e DB_HOST=pg -e DB_PORT=5432 -e DB_USER=postgres -e DB_PASSWORD=postgres -e DB_NAME=appdb pyapp
```
