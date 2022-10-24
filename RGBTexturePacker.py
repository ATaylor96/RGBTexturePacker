import sys
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('F:/Projects/Repo/Python/RGBTexturePacker/main_window.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()



# from PIL import Image
#
# r = Image.open("Textures\\roughness.tga").convert('RGB')
# g = Image.open("Textures\\metallic.tga").convert('RGB')
# b = Image.open("Textures\\ao.tga").convert('RGB')
# a = Image.open("Textures\\opacity.tga").convert('RGB')
# output_path = "Textures\\result.tga"
#
# print(r.size)
#
# if a != "":
#     result = Image.merge("RGBA", [r.convert("L"), g.convert("L"), b.convert("L"), a.convert("L")])
#
# else:
#     result = Image.merge("RGB", [r.convert("L"), g.convert("L"), b.convert("L")])
#
# result.save(output_path)
