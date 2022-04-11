from msilib.schema import Class
from operator import index
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QUrl, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView

__version__ = 'v1.1'
__author__ = 'Emma'


class YoutubePlayer(QWidget):
    def __init__(self, video_id, parent=None):
        super().__init__()
        self.parent = parent
        self.video_id = video_id

        defaultSettings = QWebEngineSettings.globalSettings()
        defaultSettings.setFontSize(QWebEngineSettings.MinimumFontSize, 25)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        topLayout = QHBoxLayout()
        self.layout.addLayout(topLayout)

        label = QLabel('Enter YouTube URL: ')
        self.input = QLineEdit()
        self.input.installEventFilter(self)
        self.input.setText(self.video_id)

        topLayout.addWidget(label, 1)
        topLayout.addWidget(self.input, 9)

        self.addWebView(self.input.text())

        buttonLayout = QHBoxLayout()
        self.layout.addLayout(buttonLayout)

        buttonUpdate = QPushButton('Update', clicked=self.updateVideo)
        buttonRemove = QPushButton('Delete', clicked=self.removePlayer)
        buttonLayout.addWidget(buttonUpdate)
        buttonLayout.addWidget(buttonRemove)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.updateVideo()
        return super().eventFilter(source, event)

    def addWebView(self, video_id):
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl('https://www.youtube.com/embed/{self.video_id}?rel=0'))
        self.layout.addWidget(self.webview)
    def updateVideo(self):
        video_Id = self.input.text()
        self.webview.setUrl(QUrl('https://www.youtube.com/embed/{video_Id}?rel=0'))
    def removePlayer(self):
        widget = self.sender().parent()
        widget.setParent(None)
        widget.deleteLater()

        self.organizeLayout()

    def organizeLayout(self):
        playerCount = self.parent.videoGrid.count()
        players = []

        for i in reversed(range(playerCount)):
            player = self.parent.videoGrid.itemAt(i).widget()
            player.append(player)

            for indx, player in enumerate(players[::-1]):
                self.parent.videoGrid.addWidget(player, indx % 3, indx // 3)
    



    


class YoutubeWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Youtube Video Player')
            self.setWindowIcon(QIcon('glep.webp'))

            self.setMinimumSize(1000, 500)
            self.players = []

            self.layout = QVBoxLayout()
            self.setLayout(self.layout)

            buttonAddPlayer = QPushButton('&AddPlayer', clicked=self.addPlayer)
            self.layout.addWidget(buttonAddPlayer)

            self.videoGrid = QGridLayout()
            self.layout.addLayout(self.videoGrid)

            self.player = YoutubePlayer('RTWhvp_OD6s&list=RDRTWhvp_OD6s&start_radio=1', parent=self)
            self.videoGrid.addWidget(self.player, 0, 0)

            self.layout.addWidget(QLabel(__version__ + ' by ' + __author__), alignment=Qt.AlignBottom | Qt.AlignRight)

            self.setStyleSheet("""
                QPushButton{
                    font-size: 20px;
                    height: 40px;
                    width: 40px;
                    background-color: #EFE9E7;
                    color: black;
                }

                * {
                    background-color: #F2FDFF;
                    
                }
                
                QLineEdit {
                    background-color: #F2FDFF;
                    font-size: 15px;
                }
            
            
            """)

        def addPlayer(self):
            playerCount = self.videoGrid.count()
            row = playerCount % 3
            col = playerCount // 3

            self.player = YoutubePlayer('', parent=self)
            self.videoGrid.addWidget(self.player, row, col)







if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = YoutubeWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
            print('Player Window Closed')














# # importing pyglet module
# import pyglet
 
# # width of window
# width = 500
   
# # height of window
# height = 500
   
# # caption i.e title of the window
# title = "Geeksforgeeks"
   
# # creating a window
# window = pyglet.window.Window(width, height, title)
 
 
# # video path
# vidPath ="videoplayback.mp4"
 
# # creating a media player object
# player = pyglet.media.Player()
 
# # creating a source object
# source = pyglet.media.StreamingSource()
 
# # load the media from the source
# MediaLoad = pyglet.media.load(vidPath)
 
# # add this media in the queue
# player.queue(MediaLoad)
 
# # play the video
# player.play()
 
# # on draw event
# @window.event
# def on_draw():
     
#     # clea the window
#     window.clear()
     
#     # if player source exist
#     # and video format exist
#     if player.source and player.source.video_format:
         
#         # get the texture of video and
#         # make surface to display on the screen
#         player.get_texture().blit(0, 0)
         
         
# # key press event    
# @window.event
# def on_key_press(symbol, modifier):
   
#     # key "p" get press
#     if symbol == pyglet.window.key.P:
         
#         # printing the message
#         print("Key : P is pressed")
         
#         # pause the video
#         player.pause()
         
#         # printing message
#         print("Video is paused")
         
         
#     # key "r" get press
#     if symbol == pyglet.window.key.R:
         
#         # printing the message
#         print("Key : R is pressed")
         
#         # resume the video
#         player.play()
         
#         # printing message
#         print("Video is resumed")
 
# # run the pyglet application
# # pyglet.app.run()



