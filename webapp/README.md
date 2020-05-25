This folder contains the flask based webapp. The architecture is simple: flask webapp with nginx webserver run using gunicorn.

```
Files:
model - contains the DNN prediction code where saved models are loaded and web input is converted and returned
static - static web assets
styles - Contains images of pre-curated Style Transfer choices that are provided while using the webapp
templates - html code
neural_style.py - main flask application code
other files - helpers or environment related
```