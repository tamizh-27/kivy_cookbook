from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (300,500)

helper = """
Screen:
    BoxLayout:
        orientation:"vertical"
        MDTopAppBar:
            title:"Demo"
            anchor_title:"left"
            left_action_items:[["menu",lambda x:x]]
            right_action_items:[["clock",lambda x:x]]
            elevation:3
        MDBottomNavigation:
            panel_color : "orange"
            MDBottomNavigationItem:
                icon : "chevron-left"     
            MDBottomNavigationItem:
                icon : "circle"
            MDBottomNavigationItem:
                icon : "square"  
"""

helper2 = """
Screen:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Demo"
            anchor_title: "left"
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["clock", lambda x: x]]
            elevation: 3
        MDLabel:
            text: "Hello World"
            halign: "center"
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: '48sp'
                pos_hint: {'center_x': 0.2, 'y': 0}
                theme_text_color: "Custom"
                text_color: 160/255, 160/255, 163/255, 1
            MDIconButton:
                icon: "circle-outline"
                user_font_size: '48sp'
                pos_hint: {'center_x': 0.5, 'y': 0}
                theme_text_color: "Custom"
                text_color: 160/255, 160/255, 163/255, 1
            MDIconButton:
                icon: "square-outline"
                user_font_size: '48sp'
                pos_hint: {'center_x': 0.8, 'y': 0}
                theme_text_color: "Custom"
                text_color: 160/255, 160/255, 163/255, 1
"""


class SampleApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper2)
        return screen
    
SampleApp().run()