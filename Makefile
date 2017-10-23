run:
	docker build -t docker-devf-knn .
	docker run --name contenedor-knn -i -t -p 8000:8000 docker-devf-knn

clean:

