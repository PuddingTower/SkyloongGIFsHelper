import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageSequence

# Configuration file for saving resolution
CONFIG_FILE = 'config.txt'

def load_resolution():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            res = f.read().strip()
            if 'x' in res:
                width, height = res.split('x')
                return width.strip(), height.strip()
    return '320', '240'  # Default resolution

def save_resolution(width, height):
    with open(CONFIG_FILE, 'w') as f:
        f.write(f"{width}x{height}")

class GIFCropperApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIF Cropper")

        # Get screen size, set window size
        screen = QtWidgets.QApplication.primaryScreen()
        size = screen.size()
        self.resize(int(size.width() * 0.8), int(size.height() * 0.8))

        # Load saved resolution
        saved_width, saved_height = load_resolution()
        self.width_var = saved_width
        self.height_var = saved_height
        self.aspect_ratio = float(saved_width) / float(saved_height)

        self.image = None
        self.photo_image = None
        self.crop_box = None
        self.gif_path = None

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        # Resolution input
        res_layout = QtWidgets.QHBoxLayout()
        res_label = QtWidgets.QLabel("Enter resolution (width x height):")
        res_layout.addWidget(res_label)

        self.width_input = QtWidgets.QLineEdit(self.width_var)
        self.width_input.setFixedWidth(50)
        res_layout.addWidget(self.width_input)

        x_label = QtWidgets.QLabel("x")
        res_layout.addWidget(x_label)

        self.height_input = QtWidgets.QLineEdit(self.height_var)
        self.height_input.setFixedWidth(50)
        res_layout.addWidget(self.height_input)

        btn_320x240 = QtWidgets.QPushButton("320x240")
        btn_320x240.clicked.connect(lambda: self.set_resolution('320', '240'))
        res_layout.addWidget(btn_320x240)

        btn_240x135 = QtWidgets.QPushButton("240x135")
        btn_240x135.clicked.connect(lambda: self.set_resolution('240', '135'))
        res_layout.addWidget(btn_240x135)

        res_layout.addStretch()
        layout.addLayout(res_layout)

        # Load GIF buttons
        btn_layout = QtWidgets.QHBoxLayout()
        btn_load_gif = QtWidgets.QPushButton("Select GIF")
        btn_load_gif.clicked.connect(self.load_single_gif)
        btn_layout.addWidget(btn_load_gif)

        btn_load_dir = QtWidgets.QPushButton("Select GIF Directory")
        btn_load_dir.clicked.connect(self.load_gif_directory)
        btn_layout.addWidget(btn_load_dir)

        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Canvas for displaying images
        self.graphics_view = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        layout.addWidget(self.graphics_view)

        # Confirm button
        self.confirm_button = QtWidgets.QPushButton("Confirm Crop and Save")
        self.confirm_button.clicked.connect(self.crop_and_save_gif)
        self.confirm_button.setEnabled(False)
        layout.addWidget(self.confirm_button)

        # High DPI support
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    def set_resolution(self, width, height):
        self.width_var = width
        self.height_var = height
        self.width_input.setText(width)
        self.height_input.setText(height)
        self.aspect_ratio = float(width) / float(height)
        save_resolution(width, height)

    def update_aspect_ratio(self):
        try:
            width = int(self.width_input.text())
            height = int(self.height_input.text())
            self.aspect_ratio = float(width) / float(height)
            save_resolution(str(width), str(height))
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Please enter a valid resolution")

    def load_single_gif(self):
        self.update_aspect_ratio()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select GIF File", "", "GIF Images (*.gif)")
        if file_path:
            self.process_gif(file_path)

    def load_gif_directory(self):
        self.update_aspect_ratio()
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select GIF Directory")
        if dir_path:
            for file_name in os.listdir(dir_path):
                if file_name.lower().endswith(".gif"):
                    file_path = os.path.join(dir_path, file_name)
                    self.process_gif(file_path)
            QtWidgets.QMessageBox.information(self, "Completed", "All GIFs processed successfully")

    def process_gif(self, gif_path):
        try:
            self.gif_path = gif_path
            with Image.open(gif_path) as im:
                self.image = im.convert("RGBA")
                self.display_image()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Cannot load GIF: {e}")

    def display_image(self):
        self.scene.clear()
        img_width, img_height = self.image.size

        # Convert PIL image to QImage
        data = self.image.tobytes("raw", "RGBA")
        qimage = QtGui.QImage(data, img_width, img_height, QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap.fromImage(qimage)

        self.pixmap_item = self.scene.addPixmap(pixmap)
        self.graphics_view.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)

        # Add crop rectangle
        self.crop_rect_item = QtWidgets.QGraphicsRectItem()
        self.crop_rect_item.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        self.scene.addItem(self.crop_rect_item)

        self.is_drawing = False

        # Connect events
        self.scene.mousePressEvent = self.on_mouse_press
        self.scene.mouseMoveEvent = self.on_mouse_move
        self.scene.mouseReleaseEvent = self.on_mouse_release

    def on_mouse_press(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_drawing = True
            self.start_point = event.scenePos()
            self.crop_rect_item.setRect(QtCore.QRectF(self.start_point, self.start_point))
            self.confirm_button.setEnabled(False)

    def on_mouse_move(self, event):
        if self.is_drawing:
            current_point = event.scenePos()
            rect = self.calculate_aspect_ratio_rect(self.start_point, current_point)
            self.crop_rect_item.setRect(rect)

    def on_mouse_release(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.is_drawing:
            self.is_drawing = False
            self.confirm_button.setEnabled(True)
            # Save crop area
            rect = self.crop_rect_item.rect()
            self.crop_box = (int(rect.left()), int(rect.top()), int(rect.right()), int(rect.bottom()))

    def calculate_aspect_ratio_rect(self, start_point, current_point):
        dx = current_point.x() - start_point.x()
        dy = current_point.y() - start_point.y()

        if dx == 0 or dy == 0:
            return QtCore.QRectF(start_point, start_point)

        # Adjust dx and dy according to aspect ratio
        aspect = self.aspect_ratio
        if abs(dx / dy) > aspect:
            dy = dx / aspect if dy != 0 else 0
        else:
            dx = dy * aspect if dx != 0 else 0

        end_point = QtCore.QPointF(start_point.x() + dx, start_point.y() + dy)
        return QtCore.QRectF(start_point, end_point).normalized()

    def crop_and_save_gif(self):
        if not self.crop_box or not self.gif_path:
            return

        try:
            target_width = int(self.width_input.text())
            target_height = int(self.height_input.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Please enter a valid resolution")
            return

        with Image.open(self.gif_path) as im:
            frames = []
            duration = im.info.get('duration', 100)
            loop = im.info.get('loop', 0)

            for frame in ImageSequence.Iterator(im):
                frame = frame.convert('RGBA')
                cropped_frame = frame.crop(self.crop_box)
                resized_frame = cropped_frame.resize((target_width, target_height), Image.LANCZOS)
                frames.append(resized_frame.convert('P', palette=Image.ADAPTIVE))

            base_name, ext = os.path.splitext(self.gif_path)
            new_file_path = f"{base_name}_cropped{ext}"

            frames[0].save(
                new_file_path,
                save_all=True,
                append_images=frames[1:],
                duration=duration,
                loop=loop
            )
            QtWidgets.QMessageBox.information(self, "Completed", f"GIF saved as: {new_file_path}")

        # Reset state
        self.scene.clear()
        self.confirm_button.setEnabled(False)
        self.crop_box = None
        self.gif_path = None

if __name__ == "__main__":
    # High DPI screen adaptation
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    app = QtWidgets.QApplication(sys.argv)
    window = GIFCropperApp()
    window.show()
    sys.exit(app.exec_())