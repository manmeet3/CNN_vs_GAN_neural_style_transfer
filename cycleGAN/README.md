This folder contains the various notebooks and python files used to train the cycleGAN for style transfer.

```
The file organization of this foler is as follows:
logs/monet2photo        -   contain the tensorboard training logs
saved_models/05102020   -   contain the saved models 
tensorboard_metrics     -   contains the tensorboard loss graphs' images
CycleGAN_tf_v2.ipynb    -   Primary notebook containing the training loop for the cycleGAN
Infer_cycleGAN.ipynb    -   Infer (do style transfer) based on saved models
tfx_cycleGAN.ipynb      -   Incomplete code on implementing a full tfx pipeline to load, transform data and train the model
References.txt          -   Code references that helped guide this project 
models.py               -   cycleGAN keras model implementation
utils.py                -   Contains an optimizer and Image Pool implementation. Borrowed as-is. See References at the top of file
```
