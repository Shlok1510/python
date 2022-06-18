
import qrcode

import image

s = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"

s.add_data(data)
s.make(fit=True)
img = s.make_image(fill="black", back_color="white")
img.save("test.png")

# Typecasting
a2 = "4444"
print(type(a2))
