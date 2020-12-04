#! /bin/bash

ssh swarm-master << EOF

cd QA-Practical-Project
git pull
docker stack deploy --compose-file docker-compose.yaml project

EOF