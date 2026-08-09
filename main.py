from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class AlgoTraderApp(App):
    def build(self):
        self.title = 'AlgoTrader'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title Label
        title_label = Label(
            text='AlgoTrader Login',
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title_label)

        # Inputs
        self.api_key = TextInput(hint_text='API Key', multiline=False, size_hint_y=None, height=40)
        self.username = TextInput(hint_text='User ID', multiline=False, size_hint_y=None, height=40)
        self.password = TextInput(hint_text='Password', password=True, multiline=False, size_hint_y=None, height=40)
        self.totp_token = TextInput(hint_text='TOTP Key', multiline=False, size_hint_y=None, height=40)

        layout.add_widget(self.api_key)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.totp_token)

        # Login Button
        login_btn = Button(
            text='Connect / Login',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 1, 1)
        )
        login_btn.bind(on_press=self.on_login)
        layout.add_widget(login_btn)

        # Status Label
        self.status_label = Label(text='Status: Ready', size_hint_y=None, height=30)
        layout.add_widget(self.status_label)

        return layout

    def on_login(self, instance):
        self.status_label.text = "Status: Connecting..."

if __name__ == '__main__':
    AlgoTraderApp().run()
