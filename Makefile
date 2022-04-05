.DEFAULT_GOAL := help 
.PHONY: test 

help: 
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

create_venv: ## Create venv 
	python3 -m venv venv 
activate: ## Activate venv 
	source venv/bin/activate 

uninstall: ## Uninstall the package
	pip uninstall flitton-fib-py