from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import NumericProperty

Window.size = (375, 667)

KV = '''
#: import NoTransition kivy.uix.screenmanager.NoTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import CardTransition kivy.uix.screenmanager.CardTransition
#: import SwapTransition kivy.uix.screenmanager.SwapTransition
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import WipeTransition kivy.uix.screenmanager.WipeTransition
#: import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition

<NotificationPanel@MDCard>:
    size_hint_x: 1
    size_hint_y: None
    height: 150
    pos_hint: {"center_x": 0.5}
    orientation: "vertical"
    md_bg_color: 0.1, 0.1, 0.1, 1
    radius: [0, 0, 20, 20]
    padding: 10
    spacing: 10

    MDLabel:
        text: "Notification Panel"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

    GridLayout:
        cols: 3
        size_hint_y: None
        height: self.minimum_height
        spacing: 10

        MDRectangleFlatButton:
            text: "Button 1"
            size_hint_y: None
            height: 40
            size_hint_x: 0.3
            on_release: app.switch_screen('mainscreen')

        MDRectangleFlatButton:
            text: "Button 2"
            size_hint_y: None
            height: 40
            size_hint_x: 0.3
            on_release: app.switch_screen('screen1')

        MDRectangleFlatButton:
            text: "Button 3"
            size_hint_y: None
            height: 40
            size_hint_x: 0.3
            on_release: app.switch_screen('screen2')

<BottomBar@FloatLayout>:
    size_hint_y: None
    height: 50
    pos_hint: {"bottom": 1}

    MDIconButton:
        icon: "icons/back_icon_black.png"    #"arrow-left"
        icon_size: "22sp"
        pos_hint: {"center_x": 0.2, "center_y": 0.5}
        
    MDIconButton:
        icon: "square-rounded-outline"
        on_release: app.switch_screen('mainscreen')
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDIconButton:
        icon: "view-headline"
        text: "Show Notification"
        on_release: app.show_notification()
        pos_hint: {"center_x": 0.8, "center_y": 0.5}

FloatLayout:
    ScreenManager:
        id: screen_manager
        transition: NoTransition()  

        MDScreen:
            name: 'mainscreen'
            FloatLayout:
                orientation: 'vertical'

                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: 100, 140  # Adjust the height to include spacing
                    pos_hint: {"center_x": 0.2, "center_y": 0.9}  # Center the BoxLayout

                    MDCard:
                        size_hint: None, None
                        size: 100, 100  # Width and Height of the box
                        radius: [15, 15, 15, 15]  # Corner radius (top-left, top-right, bottom-right, bottom-left)
                        md_bg_color: 15/255,159/255,0/255,1

                        AnchorLayout:
                            anchor_x: "center"
                            anchor_y: "center"

                            MDIconButton:
                                icon: "phone"
                                icon_size: "50sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint: None, None
                                size: "60sp", "60sp"  # Size of the icon button

                    Widget:
                        size_hint_y: None
                        height: 10  # Adjust this value to increase or decrease spacing

                    MDLabel:
                        text: "Phone"
                        size_hint: None, None
                        width: 100  # Adjust the width to ensure horizontal alignment
                        halign: "center"
                        valign: "middle"
                        height: self.texture_size[1]

                
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: 100, 140  # Adjust the height to include spacing
                    pos_hint: {"center_x": 0.5, "center_y": 0.9}  # Center the BoxLayout

                    MDCard:
                        size_hint: None, None
                        size: 100, 100  # Width and Height of the box
                        radius: [15, 15, 15, 15]  # Corner radius (top-left, top-right, bottom-right, bottom-left)
                        md_bg_color: 15/255,159/255,0/255,1

                        AnchorLayout:
                            anchor_x: "center"
                            anchor_y: "center"

                            MDIconButton:
                                icon: "chat"
                                icon_size: "50sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint: None, None
                                size: "60sp", "60sp"  # Size of the icon button

                    Widget:
                        size_hint_y: None
                        height: 10  # Adjust this value to increase or decrease spacing

                    MDLabel:
                        text: "Messages"
                        size_hint: None, None
                        width: 100  # Adjust the width to ensure horizontal alignment
                        halign: "center"
                        valign: "middle"
                        height: self.texture_size[1]

                
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: 100, 140  # Adjust the height to include spacing
                    pos_hint: {"center_x": 0.8, "center_y": 0.9}  # Center the BoxLayout

                    MDCard:
                        size_hint: None, None
                        size: 100, 100  # Width and Height of the box
                        radius: [15, 15, 15, 15]  # Corner radius (top-left, top-right, bottom-right, bottom-left)
                        md_bg_color: 15/255,159/255,0/255,1

                        AnchorLayout:
                            anchor_x: "center"
                            anchor_y: "center"

                            MDIconButton:
                                icon: "contacts"
                                icon_size: "50sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint: None, None
                                size: "60sp", "60sp"  # Size of the icon button

                    Widget:
                        size_hint_y: None
                        height: 10  # Adjust this value to increase or decrease spacing

                    MDLabel:
                        text: "Contacts"
                        size_hint: None, None
                        width: 100  # Adjust the width to ensure horizontal alignment
                        halign: "center"
                        valign: "middle"
                        height: self.texture_size[1]


                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: 100, 140  # Adjust the height to include spacing
                    pos_hint: {"center_x": 0.2, "center_y": 0.7}  # Center the BoxLayout

                    MDCard:
                        size_hint: None, None
                        size: 100, 100  # Width and Height of the box
                        radius: [15, 15, 15, 15]  # Corner radius (top-left, top-right, bottom-right, bottom-left)
                        md_bg_color: 15/255,159/255,0/255,1

                        AnchorLayout:
                            anchor_x: "center"
                            anchor_y: "center"

                            MDIconButton:
                                icon: "liquid-spot"
                                icon_size: "50sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint: None, None
                                size: "60sp", "60sp"  # Size of the icon button

                    Widget:
                        size_hint_y: None
                        height: 10  # Adjust this value to increase or decrease spacing

                    MDLabel:
                        text: "Dirt"
                        size_hint: None, None
                        width: 100  # Adjust the width to ensure horizontal alignment
                        halign: "center"
                        valign: "middle"
                        height: self.texture_size[1]

                
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: 100, 140  # Adjust the height to include spacing
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}  # Center the BoxLayout

                    MDCard:
                        size_hint: None, None
                        size: 100, 100  # Width and Height of the box
                        radius: [15, 15, 15, 15]  # Corner radius (top-left, top-right, bottom-right, bottom-left)
                        md_bg_color: 15/255,159/255,0/255,1

                        AnchorLayout:
                            anchor_x: "center"
                            anchor_y: "center"

                            MDIconButton:
                                icon: "newspaper"
                                icon_size: "50sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint: None, None
                                size: "60sp", "60sp"  # Size of the icon button
                                _no_ripple_effect: True

                    Widget:
                        size_hint_y: None
                        height: 10  # Adjust this value to increase or decrease spacing

                    MDLabel:
                        text: "News"
                        size_hint: None, None
                        width: 100  # Adjust the width to ensure horizontal alignment
                        halign: "center"
                        valign: "middle"
                        height: self.texture_size[1]

                    
        MDScreen:
            name: 'screen1'
            MDLabel:
                text: 'This is Screen 1'
                halign: 'center'
        
        MDScreen:
            name: 'screen2'
            MDLabel:
                text: 'This is Screen 2'
                halign: 'center'

    BottomBar:
        id: bottom_bar

    NotificationPanel:
        id: notification_panel
        pos_hint: {"center_x": 0.5}
        size_hint_y: None
        height: 150
        y: app.notification_panel_y  # This property will be managed by the app
'''

class NotificationApp(MDApp):
    notification_panel_y = NumericProperty(Window.height)

    def build(self):
        self.title = "Text-RPG App"
        #self.icon = ""
        #self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Light"
        screen = Builder.load_string(KV)
        self.notification_panel = screen.ids.notification_panel
        self.screen_manager = screen.ids.screen_manager
        self.panel_visible = False
        # Bind to window size changes
        Window.bind(on_resize=self.update_panel_position)
        return screen

    def show_notification(self):
        if not self.panel_visible:
            # Animate panel sliding down from the top
            Animation(y=Window.height - self.notification_panel.height, d=0.3).start(self.notification_panel)
            self.notification_panel_y = Window.height - self.notification_panel.height
        else:
            # Animate panel sliding up to hide it at the top
            Animation(y=Window.height, d=0.3).start(self.notification_panel)
            self.notification_panel_y = Window.height
        self.panel_visible = not self.panel_visible

    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name

    def update_panel_position(self, *args):
        if self.panel_visible:
            self.notification_panel_y = Window.height - self.notification_panel.height
        else:
            self.notification_panel_y = Window.height

if __name__ == '__main__':
    NotificationApp().run()
