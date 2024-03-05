import frappe
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
import base64

@frappe.whitelist(allow_guest=True)
def barcode_generator(param):
    data = param

    # Generate a Code 128 barcode
    code128 = barcode.get_barcode_class('code128')

    # Create the barcode instance
    barcode_instance = code128(data, writer=ImageWriter())

    # Create an in-memory stream to hold the image data
    image_stream = BytesIO()

    # Write the barcode image data to the in-memory stream
    barcode_instance.write(image_stream)

    # Seek to the beginning of the stream
    image_stream.seek(0)

    # Encode the image data as base64
    base64_image = base64.b64encode(image_stream.getvalue()).decode()

    # Create a data URL for the image
    data_url = f'data:image/png;base64,{base64_image}'

    # Return the data URL
    return data_url