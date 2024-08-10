
run:
	sudo docker-compose up
build:
	sudo docker-compose up --build
migrate:
	sudo docker-compose exec joker-server python3 manage.py migrate
mkmigrate:
	sudo docker-compose exec joker-server python3 manage.py makemigrations
shell:
	sudo docker-compose exec joker-server python3 manage.py shell
cadmin:
	sudo docker-compose exec joker-server python3 manage.py createsuperuser
