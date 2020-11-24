up:
	docker-compose up -d

down:
	docker-compose down

check:
	docker-compose ps

stop:
	docker-compose stop

create:
	docker exec -it kafka-broker kafka-topics.sh --create --topic $(topic)

describe:
	docker exec -it kafka-broker kafka-topics.sh --describe --topic $(topic)

produce:
	docker exec -it broker kafka-console-producer.sh --topic $(topic)

consume:
	docker exec -it broker kafka-console-consumer.sh --topic $(topic) --from-beginning