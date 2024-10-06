from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.graphics import Color, Rectangle

KV = '''
MDScreen:
    MDLabel:
        text: "Welcome to Fullscreen Mode!"
        halign: "center"
        font_style: "H4"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
'''

class FullScreenMDApp(MDApp):
    def build(self):
        # Set fullscreen and remove window controls
        Window.size = (1920, 1080)
        Window.fullscreen = 'auto'  # Use 'auto' to fill the screen
        Window.borderless = True  # Remove window borders (minimize, maximize, close buttons)

        # Create the main screen
        screen = MDScreen()
        
        # Load and return the layout from the KV string
        return Builder.load_string(KV)

if __name__ == "__main__":
    FullScreenMDApp().run()