# VGG19 Architecture for Neural Style Transfer

Neural style treansfer is a technique where there are 3 images. Content image, Style image and input image. We want to retain content of the content image into our input image and we want to retain style of the style image into our input image.

For this we define 2 losses : The principle of neural style transfer is to define two distance functions, one that describes how different the content of two images are , $L_{content}$, and one that describes the difference between two images in terms of their style, $L_{style}$. Then, given three images, a desired style image, a desired content image, and the input image (initialized with the content image), we try to transform the input image to minimize the content distance with the content image and its style distance with the style image.

In summary, we’ll take the base input image, a content image that we want to match, and the style image that we want to match. We’ll transform the base input image by minimizing the content and style distances (losses) with backpropagation, creating an image that matches the content of the content image and the style of the style image.

# Loss Update 
![Loss](https://user-images.githubusercontent.com/20379771/82529525-1007da00-9af0-11ea-99c0-36a70ccf9d3e.png)

