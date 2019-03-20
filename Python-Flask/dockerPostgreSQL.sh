docker network create flaskapinw
docker run --name flaskapidb --network flaskapinw -e POSTGRES_PASSWORD='Password123!' -e POSTGRES_USER='flaskdbuser' -e POSTGRES_DB='flaskapidb' -p 5432:5432 -d postgres
docker run --name flaskapi --network flaskapinw -p 5000:5000 -d flaskapi:latest