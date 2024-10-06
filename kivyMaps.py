# pip install kivy-garden
# garden install mapview

from kivy.garden.mapview import MapView
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDBoxLayout:
    MapView:
        lat: 37.7749
        lon: -122.4194
        zoom: 10
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MainApp().run()