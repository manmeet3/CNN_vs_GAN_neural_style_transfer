import os, uuid
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt

print(os.getcwd())
monet2photo=tf.saved_model.load("./model/05102020/a2b_monet_to_photo")
photo2monet=tf.saved_model.load("./model/05102020/b2a_photo_to_monet")
static_path="static/images/"

def read_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    original = tf.image.decode_jpeg(content)
    resized_original = tf.image.resize(original, (256, 256))
    float_original = tf.cast(resized_original, tf.float32)
    inputs = float_original / 127.5 - 1
    inputs = tf.expand_dims(inputs, 0)
    return inputs


def cGAN(content_image_path):
    global static_path
    content_image_path = static_path + content_image_path
    inputs = read_file(content_image_path)
    global monet2photo
    global photo2monet
    photo = monet2photo(inputs)
    monet = photo2monet(inputs)

    print("converting to photo")
    gen_photo = photo[0]
    gen_photo = (gen_photo + 1) * 127.5
    gen_photo = tf.cast(gen_photo, tf.uint8)
    gen_photo = tf.image.resize(gen_photo, (218, 178))
    gen_photo = tf.cast(gen_photo, tf.uint8)
    im = Image.fromarray(gen_photo.numpy())
    myuuid_ph = str(uuid.uuid4()) + ".png"
    im.save(static_path + myuuid_ph)
    print("converting to monet")
    gen_monet = monet[0]
    gen_monet = (gen_monet + 1) * 127.5
    gen_monet = tf.cast(gen_monet, tf.uint8)
    gen_monet = tf.image.resize(gen_monet, (218, 178))
    gen_monet = tf.cast(gen_monet, tf.uint8)
    im = Image.fromarray(gen_photo.numpy())
    myuuid_mon = str(uuid.uuid4()) + ".png"
    im.save(static_path + myuuid_mon)

    return (myuuid_ph, myuuid_mon)

#main("foo.jpg")
