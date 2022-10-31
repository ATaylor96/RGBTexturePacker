import sys
from PIL import Image, ImageOps
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('main_window.ui', self)
        self.show()

        self.redBrowseButton.clicked.connect(self.red_browse_clicked)
        self.greenBrowseButton.clicked.connect(self.green_browse_clicked)
        self.blueBrowseButton.clicked.connect(self.blue_browse_clicked)
        self.alphaBrowseButton.clicked.connect(self.alpha_browse_clicked)
        self.packTexturesButton.clicked.connect(self.pack_textures_clicked)
        # self.saveButton.clicked.connect(self.save_texture_clicked)

    def red_browse_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open Texture...')
        self.redLineEdit.setText(file_name[0])

    def green_browse_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open Texture...')
        self.greenLineEdit.setText(file_name[0])

    def blue_browse_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open Texture...')
        self.blueLineEdit.setText(file_name[0])

    def alpha_browse_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open Texture...')
        self.alphaLineEdit.setText(file_name[0])

    def pack_textures_clicked(self):
        packed_image = self.pack_images(self.redLineEdit.text(), self.greenLineEdit.text(), self.blueLineEdit.text(), self.alphaLineEdit.text())
        pixmap = QPixmap(packed_image)
        self.previewLabel.setPixmap(pixmap)
        print("Packed Textures")

    def save_texture_clicked(self):
        print("Saved Texture")

    def pack_images(self, red, green, blue, alpha):
        r = Image.open(red).convert('RGB')
        g = Image.open(green).convert('RGB')
        b = Image.open(blue).convert('RGB')

        if self.redInvertCheckBox.isChecked():
            r = ImageOps.invert(r)

        if self.greenInvertCheckBox.isChecked():
            g = ImageOps.invert(g)

        if self.blueInvertCheckBox.isChecked():
            b = ImageOps.invert(b)

        if alpha != "":
            a = Image.open(alpha).convert('RGB')

            if self.alphaInvertCheckBox.isChecked():
                a = ImageOps.invert(a)

        if alpha != "":
            result = Image.merge("RGBA", [r.convert("L"), g.convert("L"), b.convert("L"), a.convert("L")])
        else:
            result = Image.merge("RGB", [r.convert("L"), g.convert("L"), b.convert("L")])

        result.save("Textures\\result.tga")
        return "Textures\\result.tga"


app = QApplication(sys.argv)
window = Ui()
app.exec_()

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
