init: ## Run package install
	pip install -r requirements.txt

build: ## Run SAM build
	sam build

validate: ## Run validate tempalte
	sam validate --lint

deploy: build ## Run deploy
	sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

deploy-apigateway:
	aws apigateway create-deployment --rest-api-id ${API_GATEWAY_ID} --stage-name ${STAGE_NAME}

get: ## Run GetFunction
	sam local invoke GetFunction --env-vars envs/local.json

post: ## Run PostFunction
	sam local invoke PostFunction --event events/post.json --env-vars envs/local.json

requests: get post ## Run all requests

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: help init build validate deploy get post requests
.DEFAULT_GOAL := help
