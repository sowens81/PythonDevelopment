docker run --name flaskapidb -e POSTGRES_PASSWORD='Password123!' -e POSTGRES_USER='flaskdbuser' -e POSTGRES_DB='flaskapidb' -p 5432:5432 -d postgres
