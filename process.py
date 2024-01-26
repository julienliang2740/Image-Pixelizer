from PIL import Image
import cv2
import json

def background_fix(image):
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, mask=image)
    new_image.convert("RGB")
    return new_image

def pixelate(image, n):
    
    new_image = image.resize((n,n), resample=Image.Resampling.BILINEAR)
    result = new_image.resize(image.size, Image.Resampling.NEAREST)
    return result

def resize(image, enlargement_factor):
    pass

def threshold(image_path, threshold_value):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # All pixels with values above threshold_value (whiter) are changed to black
    ret, thresh = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh

if __name__ == '__main__':
    f = open('input.json')
    data = json.load(f)

    imagetype = data['imagetype']
    input_name = data['filename']
    output_name = input_name.split('.')[0] + "_output" + "." + imagetype
    thresholded_output_name = input_name.split('.')[0] + "_thresold" + "." + imagetype
    desired_n = data['desired_n']
    enlargement_factor = data['enlargement_factor']
    threshold_value = data['threshold_value']

    print(f"Input name: {input_name}")
    print(f"Output name: {output_name}")
    print(f"Image type: {imagetype}")
    print(f"Pixel dimensions: {desired_n}")
    print(f"Enlargement factor (deprecated parameter): {enlargement_factor}")
    print(f"Threshold value: {threshold_value}")
    print(type(desired_n))
    f.close()   

    #--------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------------

    image = Image.open(input_name).convert("RGBA")
    image_fixed_background = background_fix(image)
    image_pixelated = pixelate(image_fixed_background, desired_n)
    image_pixelated.save(output_name)

    # Thresholding uses opencv
    image_thresholded = threshold(output_name, threshold_value)
    cv2.imwrite(thresholded_output_name, image_thresholded)
