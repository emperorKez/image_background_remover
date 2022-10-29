from rembg import remove
from PIL import Image
import easygui as eg

input_path = eg.fileopenbox(title ='Select image')
output_path = eg.filesavebox(title='save file to')
input = Image.open(input_path)
output = remove(input)
output.save(output_path)