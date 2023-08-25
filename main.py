import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QVBoxLayout, QWidget, QLabel, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Video Player")

        # Create a central widget and set its layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a list widget
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.list_widget.itemClicked.connect(self.play_video)

        # Create a video widget
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        # Create a media player
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)

        # Create a button
        self.open_button = QPushButton("Open Video")
        self.open_button.clicked.connect(self.open_video)
        layout.addWidget(self.open_button)

    def open_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi *.mkv)", options=options)

        if file_name:
            self.list_widget.addItem(file_name)

    def play_video(self, item):
        file_name = item.text()
        media_content = QMediaContent(QUrl.fromLocalFile(file_name))
        self.media_player.setMedia(media_content)
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
