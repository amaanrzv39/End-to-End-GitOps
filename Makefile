.PHONY: process train deploy

# Data processing
process:
	python src/data_processing.py


# Model training
train:
	python src/model_training.py
	
# run app
deploy:
	python app.py

# run training pipeline
run:
	make process
	make train

# git push
push:
	git add .
	git commit -m "deploying"
	git push -u origin main