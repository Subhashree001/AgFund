import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"<Cloud Service Token.json>"

client = vision.ImageAnnotatorClient()

def cropHint(file_path, aspect_ratios):
    with io.open(file_path, 'rb') as image_file:
            content = image_file.read()

    image = vision.types.Image(content=content)

    # desired ratio
    crop_hints_params = vision.types.CropHintsParams(aspect_ratios=aspect_ratios)
    image_context = vision.types.ImageContext(
        crop_hints_params=crop_hints_params)

    response = client.crop_hints(
        image=image,
        image_context=image_context
        )

    cropHints = response.crop_hints_annotation.crop_hints

    for cropHint in cropHints:
        print('Confidence:', cropHint.confidence)
        print('Importance Fraction:', cropHint.importance_fraction)
        print('Vertices:', cropHint.bounding_poly.vertices)


file_name = '<image file name>'
image_path = f'.\\VisionAPI\\Images\\{file_name}'
cropHint(image_path, [16/9])
