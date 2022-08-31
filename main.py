# Klasse Image aus der Bibliothek Pillow(PIL) importiert (auf Python Packages gehen, im Python Package Index nach der Bibliothek image suchen, darin Klasse Image)
from PIL import Image

# Hintergrundbild definieren (Variable "Hintergrund" definieren = das konkrete Bild hinterlegt)
hintergrund = Image.open("Bilder/teller.png")

# Hintergrund rendern (unser Image-objekt anzeigen): Methode "show" durch Schreiben des Punktes aufrufen, das angezeigte Fenster benennen "Mein Gerincht"
#hintergrund.show("Mein Gericht")

Erdbeeren = Image.open("Bilder/Erdbeeren.png")

hintergrund.paste(Erdbeeren, (200,200))

hintergrund.show("Mein Gericht")



