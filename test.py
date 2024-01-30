from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen

kv = 'test.kv'

class StudyPeriodsWindow(Screen):
    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        # self.root.ids.date_label.text = str(value)
        self.root.ids.date_label1.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.root.ids.date_label2.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.root.ids.date_label3.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.root.ids.date_label4.text = f'{str(date_range[0])} - {str(date_range[-1])}'

        # Click Cancel

    def on_cancel(self, instance, value):
        self.root.ids.date_label1.text = "Clicked Cancel"
        self.root.ids.date_label2.text = "Clicked Cancel"
        self.root.ids.date_label3.text = "Clicked Cancel"
        self.root.ids.date_label4.text = "Clicked Cancel"

    # Get Date
    def show_date_picker(self):
        # date_dialog = MDDatePicker(2023,9,1)
        date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

class WeekdaysWindow(Screen):
    pass


class PublicHolidaysWindow(Screen):
    pass

class ResultWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass



class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "BlueGray"
        self.screen = Builder.load_file(kv)
        return self.screen

        # Click OK




MainApp().run()
