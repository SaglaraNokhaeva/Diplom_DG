import calendar
import pandas as pd
from collections import Counter
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, partial

kv = 'test.kv'
school_days = []
week_days = []
lessons = ()

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

    # # Get Date
    # def show_date_picker(self, x):
    #     # date_dialog = MDDatePicker(2023,9,1)
    #     date_dialog = MDDatePicker(mode='range')
    #
    #         # self.btn[i].bind(on_release=partial(self.HoldButtonNum,  i))
    #     date_dialog.bind(on_save=partial(self.on_save, x), on_cancel=self.on_cancel)
    #     date_dialog.open()

class WeekdaysWindow(Screen):

    def input_working_days_of_the_week(self):
        global week_days

        week_days = [int(self.ids.monday_count.text), int(self.ids.tuesday_count.text), int(self.ids.wednesday_count.text), int(self.ids.thursday_count.text), int(self.ids.friday_count.text), int(self.ids.saturday_count.text)]
        # print('week_days')
        # print(week_days)
        return week_days



class PublicHolidaysWindow(Screen):
    pass


class ResultWindow(Screen):

    def output_of_results(self):
        global lessons
        global week_days
        global school_days

        # print('school_days')
        # print(school_days)
        print('week_days')
        print(week_days)
        lessons = Counter(week_days)
        print("это Лессонс:")
        print(lessons)

        for single_date in school_days:
            for i in range(len(week_days)):
                if single_date.weekday() == i:
                    for j in range(week_days[i]):
                        print(single_date, calendar.day_name[single_date.weekday()])






        # for single_date in school_days:
        #     for item in lessons.items():
        #         # print(item)
        #         # print(item[0])
        #         # print(item[1])
        #         # print(single_date.weekday())
        #         if single_date.weekday() == item[0]:
        #             for j in range(item[1]):
        #                 print(single_date, calendar.day_name[single_date.weekday()])


class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "BlueGray"
        self.screen = Builder.load_file(kv)
        return self.screen

MainApp().run()
