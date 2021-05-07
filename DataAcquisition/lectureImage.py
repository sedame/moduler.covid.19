#modules a importer
import pytesseract 
from PIL import Image
#modules deja diaponibles
import os

#lister les elements du dossier
contenu=os.listdir('images/')
os.chdir('images')
 
#parcours de chaque element du dossier
for elemement in contenu:
    nom = str(elemement)
    #extraction des ecritures
    text = pytesseract.image_to_string(Image.open(nom))
    print (text)
    
