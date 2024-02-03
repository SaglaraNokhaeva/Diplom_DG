from collections import Counter

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, partial

kv = 'test.kv'
school_days = []

class StudyPeriodsWindow(Screen):

    def input_study_period(self, x):
        date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=partial(self.on_save, x), on_cancel=self.on_cancel)
        # print(x)
        date_dialog.open()

    def on_save(self, x, instance, value, date_range):
        global school_days

        match x:
            case 'btn0':
                self.ids.date1.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                school_days = date_range
                print(school_days)
            case 'btn1':
                self.ids.date2.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                # print(date_range)
                school_days = [x for x in school_days if x not in date_range]
                print(school_days)
            case 'btn2':
                self.ids.date3.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                # print(date_range)
                school_days = [x for x in school_days if x not in date_range]
                print(school_days)
            case 'btn3':
                self.ids.date4.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                # print(date_range)
                school_days = [x for x in school_days if x not in date_range]
                print(school_days)

    def on_cancel(self, x, instance):
        match x:
            case 'btn0':
                self.ids.date1.text = "Clicked Cancel"
            case 'btn1':
                self.ids.date2.text = "Clicked Cancel"
            case 'btn2':
                self.ids.date3.text = "Clicked Cancel"
            case 'btn3':
                self.ids.date4.text = "Clicked Cancel"


    # btn = ObjectProperty(None)
    #
    # date1 = ObjectProperty(None)
    # date2 = ObjectProperty(None)
    # date3 = ObjectProperty(None)
    # date4 = ObjectProperty(None)
    #
    #
    # def on_save(self, x,instance, value, date_range):
    #     print(x)
    #     print(instance)
    #     print(self.ids.write.ids.x.id)
    #     match x:
    #         case 'btn0':
    #             self.ids.date1.text = f'{str(date_range[0])} - {str(date_range[-1])}'
    #         case 'btn1':
    #             self.ids.date2.text = f'{str(date_range[0])} - {str(date_range[-1])}'
    #         case 'btn2':
    #             self.ids.date3.text = f'{str(date_range[0])} - {str(date_range[-1])}'
    #         case 'btn3':
    #             self.ids.date4.text = f'{str(date_range[0])} - {str(date_range[-1])}'
    #
    #
    #
    #     # Click Cancel
    #
    # def on_cancel(self, instance, value):
    #     self.root.ids.date_label1.text = "Clicked Cancel"
    #     self.root.ids.date_label2.text = "Clicked Cancel"
    #     self.root.ids.date_label3.text = "Clicked Cancel"
    #     self.root.ids.date_label4.text = "Clicked Cancel"
    #
    # # Get Date
    # def show_date_picker(self, x):
    #     # date_dialog = MDDatePicker(2023,9,1)
    #     date_dialog = MDDatePicker(mode='range')
    #
    #         # self.btn[i].bind(on_release=partial(self.HoldButtonNum,  i))
    #     date_dialog.bind(on_save=partial(self.on_save, x), on_cancel=self.on_cancel)
    #     date_dialog.open()

class WeekdaysWindow(Screen):
    week_days =
    def input_working_days_of_the_week(self):
        less = []
        week_days = ['monday_count', 'tuesday_count', 'wednesday_count', 'thursday_count', 'friday_count', 'saturday_count']
        for i in range(len(week_days)):
            surname = self.week_days[i].text

            print(surname)
            less = list(map(int, self.get_root_window().ids.week_days[i].text))


        lessons = Counter(less)
        print(lessons)


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
