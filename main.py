import qrcode
from PIL import Image
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

logo = Image.open('logo.png')
basewidth = 75
wpercent = (basewidth / float(logo.size[0]))
hsize = int(float(logo.size[1] * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr_big.add_data("https://papadoner.kz")
qr_big.make(fit=True)
img_qr_big = qr_big.make_image(fill_color="black", back_color="white", eye_drawer=RoundedModuleDrawer(radius_ratio=1.2),
                               color_mask=RadialGradiantColorMask(edge_color='255, 0, 0')).convert("RGB")
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)
img_qr_big.save('qr_papadoner.png')
