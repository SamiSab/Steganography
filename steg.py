def decode_image(file_location="images/encoded_sample.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
 
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
 
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
 
    for i in range(x_size):
        for j in range(y_size):
            pass #TODO: Fill in decoding functionality
 
    decoded_image.save("images/decoded_image.png")
