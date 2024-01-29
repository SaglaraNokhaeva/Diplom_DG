from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "BlueGray"
        self.screen = Builder.load_file('test.kv')
        return self.screen

        # Click OK
    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        # self.root.ids.date_label.text = str(value)
        self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'


        # Click Cancel
    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = "Clicked Cancel"

    # Get Date
    def show_date_picker(self):
        # date_dialog = MDDatePicker(2023,9,1)
        date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()



MainApp().run()
