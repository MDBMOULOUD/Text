from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTextField:
        id: text_input
        hint_text: "Enter text"
        helper_text: " "
        helper_text_mode: "persistent"

    MDRaisedButton:
        text: "Show Text"
        on_release: app.show_text()

    MDLabel:
        id: displayed_text
        text: ""
        halign: 'center'
        theme_text_color: "Secondary"
'''


class TextApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_text(self):
        text = self.root.ids.text_input.text
        self.root.ids.displayed_text.text = text


if __name__ == '__main__':
    TextApp().run()
