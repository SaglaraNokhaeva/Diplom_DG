from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, partial

kv = 'test.kv'

class StudyPeriodsWindow(Screen):

    date_label1 = ObjectProperty(None)
    date_label2 = ObjectProperty(None)
    date_label3 = ObjectProperty(None)
    date_label4 = ObjectProperty(None)


    def on_save(self, instance, value, date_range):

        # print(instance, value, date_range)
        # self.ids.date_label1.text = str(value)
        # self.buttonsid = []
        # for x in range(3):
            # self.buttonsid = [self.ids.btn0, self.ids.btn1, self.ids.btn2, self.ids.btn3]
            # print(self.ids.btn())
            # self.buttonsid.append(self.ids.btn(x))
            # print(self.ids.btn())
        self.buttonsid.bind(on_release=partial(self.HoldButtonNum, x))
        # print(instance.ids)
        # match instance.ids:
        #     case 'btn0':
        #         self.ids.date_label1.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        #     case 'btn1':
        #         self.ids.date_label2.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        #     case 'btn2':
        #         self.ids.date_label3.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        #     case 'btn3':
        #         self.ids.date_label4.text = f'{str(date_range[0])} - {str(date_range[-1])}'

        # for x in range(3):
        #     self.buttonsid[x].bind(on_release=partial(self.HoldButtonNum, x))

        #
        # if self.MDRaisedButton.text == 'Выберите даты начала и окончания учебного года':

        self.ids.date_label2.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.ids.date_label3.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.ids.date_label4.text = f'{str(date_range[0])} - {str(date_range[-1])}'

    def HoldButtonNum(self, x, instance):
        print('Button instance:', instance)
        print('Button index in list:', x)

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
