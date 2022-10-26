import sys
from PIL import Image
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('F:/Projects/Repo/Python/RGBTexturePacker/main_window.ui', self)
        self.show()

        self.red_path = self.findChild(QtWidgets.QLineEdit, 'redLineEdit')
        self.red_invert = self.findChild(QtWidgets.QCheckBox, "redInvertCheckBox")
        self.red_fill = self.findChild(QtWidgets.QCheckBox, "redFillCheckBox")
        self.red_browse = self.findChild(QtWidgets.QPushButton, 'redBrowseButton')
        self.red_browse.clicked.connect(self.red_browse_clicked)

        self.green_path = self.findChild(QtWidgets.QLineEdit, 'greenLineEdit')
        self.green_invert = self.findChild(QtWidgets.QCheckBox, "greenInvertCheckBox")
        self.green_fill = self.findChild(QtWidgets.QCheckBox, "greenFillCheckBox")
        self.green_browse = self.findChild(QtWidgets.QPushButton, 'greenBrowseButton')
        self.green_browse.clicked.connect(self.green_browse_clicked)

        self.blue_path = self.findChild(QtWidgets.QLineEdit, 'blueLineEdit')
        self.blue_invert = self.findChild(QtWidgets.QCheckBox, "blueInvertCheckBox")
        self.blue_fill = self.findChild(QtWidgets.QCheckBox, "blueFillCheckBox")
        self.blue_browse = self.findChild(QtWidgets.QPushButton, 'blueBrowseButton')
        self.blue_browse.clicked.connect(self.blue_browse_clicked)

        self.alpha_path = self.findChild(QtWidgets.QLineEdit, 'alphaLineEdit')
        self.use_alpha = self.findChild(QtWidgets.QCheckBox, "useAlphaCheckBox")
        self.alpha_invert = self.findChild(QtWidgets.QCheckBox, "alphaInvertCheckBox")
        self.alpha_fill = self.findChild(QtWidgets.QCheckBox, "alphaFillCheckBox")
        self.alpha_browse = self.findChild(QtWidgets.QPushButton, 'alphaBrowseButton')
        self.alpha_browse.clicked.connect(self.alpha_browse_clicked)

        self.pack_textures = self.findChild(QtWidgets.QPushButton, 'packTexturesButton')
        self.pack_textures.clicked.connect(self.pack_textures_clicked)

        self.preview = self.findChild(QtWidgets.QLabel, "previewLabel")

        self.save_texture = self.findChild(QtWidgets.QPushButton, 'saveButton')
        self.save_texture.clicked.connect(self.save_texture_clicked)

    def red_browse_clicked(self):
        self.red_path.setText('Invert: {}, Fill: {}, Clicked'.format(self.red_invert.isChecked(), self.red_fill.isChecked()))

    def green_browse_clicked(self):
        self.green_path.setText('Invert: {}, Fill: {}, Clicked'.format(self.green_invert.isChecked(), self.green_fill.isChecked()))

    def blue_browse_clicked(self):
        self.blue_path.setText('Invert: {}, Fill: {}, Clicked'.format(self.blue_invert.isChecked(), self.blue_fill.isChecked()))

    def alpha_browse_clicked(self):
        self.alpha_path.setText('Use Alpha: {}, Invert: {}, Fill: {}, Clicked'.format(self.use_alpha.isChecked(), self.alpha_invert.isChecked(), self.alpha_fill.isChecked()))

    def pack_textures_clicked(self):
        print("Packed Textures")

    def save_texture_clicked(self):
        print("Saved Texture")


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
