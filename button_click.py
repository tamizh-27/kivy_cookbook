from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class MyApp(App):

    def build(self):
        # Load the sound file
        self.click_sound = SoundLoader.load(r'sound/button_sound.mp3')

        layout = BoxLayout(orientation='vertical')

        # Create a button and bind to play the click sound on press
        btn = Button(text="Click Me")
        btn.bind(on_press=self.on_button_click)
        
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        if self.click_sound:
            self.click_sound.play()

if __name__ == "__main__":
    MyApp().run()
