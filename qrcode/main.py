import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data("https://youtube.com/@wisecodeteam")
image = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
image.save("qrcode.png")