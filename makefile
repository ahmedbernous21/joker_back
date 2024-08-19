
run:
	python3 manage.py runserver
docker:
	sudo docker-compose up
migrate:
	python3 manage.py runserver
mkmigrate:
	python3 manage.py makemigrations
shell:
	python3 manage.py shell
cadmin:
	python3 manage.py createsuperuser
 