from PIL import Image, ImageFilter

img = Image.open('Pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')

charm = Image.open('Charmander.jpg')
filtered_charm = charm.filter(ImageFilter.BLUR)
filtered_charm.save("CharmanderBlur.png", 'png')

bulbas = Image.open('Bulbasaur.jpg')
filtered_bulbas = bulbas.filter(ImageFilter.SHARPEN)
filtered_bulbas.save("BulbasaurSharp.png", 'png')

squirt = Image.open('Squirtle.jpg')
# filtered_squirt = squirt.convert('L') #greyscale L
crooked = squirt.rotate(180)
crooked.save("Squirtleupsidedown.png", 'png')


Eevee = Image.open('Eevee.jpg')
resize = Eevee.resize((408, 443))
resize.save("Eeveebig.png", 'png')
EB = Image.open('Eeveebig.png')
EB = EB.filter(ImageFilter.SHARPEN)
EB.show()