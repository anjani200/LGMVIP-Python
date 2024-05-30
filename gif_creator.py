from PIL import Image
image_path_list=["/Users/gk/Downloads/1.jpeg","/Users/gk/Downloads/2.jpeg","/Users/gk/Downloads/3.jpeg","/Users/gk/Downloads/4.jpeg","/Users/gk/Downloads/5.jpeg","/Users/gk/Downloads/6.jpeg","/Users/gk/Downloads/7.jpeg","/Users/gk/Downloads/8.jpeg","/Users/gk/Downloads/9.jpeg","/Users/gk/Downloads/10.jpeg"]
image_list=[Image.open(file)for file in image_path_list]
image_list[0].save(
    'animation.gif',
    save_all=True,
    append_images=image_list[1:],
    duration=250,
    loop=0
)
