from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import partial

kv = 'date_generator.kv'
school_days = []
week_days = []
result_school_days = []


class StudyPeriodsWindow(Screen):
    def input_study_period(self, x):
        date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=partial(self.on_save, x), on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, x, instance, value, date_range):
        global school_days

        match x:
            case 'btn0':
                self.ids.date1.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                school_days = date_range
            case 'btn1':
                self.ids.date2.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                school_days = [x for x in school_days if x not in date_range]
            case 'btn2':
                self.ids.date3.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                school_days = [x for x in school_days if x not in date_range]
            case 'btn3':
                self.ids.date4.text = f'{str(date_range[0])} - {str(date_range[-1])}'
                school_days = [x for x in school_days if x not in date_range]

    def on_cancel(self, x, instance):
        pass

class WeekdaysWindow(Screen):
    def input_working_days_of_the_week(self):
        global week_days

        week_days = [int(self.ids.monday_count.text), int(self.ids.tuesday_count.text),
                     int(self.ids.wednesday_count.text), int(self.ids.thursday_count.text),
                     int(self.ids.friday_count.text), int(self.ids.saturday_count.text)]
        return week_days


class PublicHolidaysWindow(Screen):

    def input_public_holidays(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        global school_days

        self.ids.dates.text = self.ids.dates.text + f"\n{str(value)}"
        school_days = [x for x in school_days if x not in [value]]

    def on_cancel(self, instance, value):
        pass

class ResultWindow(Screen):
    def output_of_results(self):
        global week_days
        global school_days
        global result_school_days

        for single_date in school_days:
            for i in range(len(week_days)):
                if single_date.weekday() == i:
                    for j in range(week_days[i]):
                        self.ids.dates.text = self.ids.dates.text + f"\n{single_date.strftime('%Y-%m-%d')}"
                        result_school_days.append(single_date)


    def save_to_file(self):
        global result_school_days

        MyFile = open('dates.txt', 'w')
        for element in result_school_days:
            MyFile.write(str(element))
            MyFile.write('\n')
        MyFile.close()

    def close_application(self):
        App.get_running_app().stop()
        Window.close()

class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.screen = Builder.load_file(kv)
        return self.screen

MainApp().run()
