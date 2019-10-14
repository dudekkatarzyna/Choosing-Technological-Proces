from kivy.clock import Clock
from kivy.properties import partial, ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from cta import ResourceData, ChoosingTechnologicalProcess
from gui.SettingsScreen import SettingsScreen


class MenuScreen(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.cost = 0
        self.totalLength = []

        self.resources = []
        Clock.schedule_once(self.setup_scrollview, 1)

    def calculate(self):
        result = ChoosingTechnologicalProcess(self.resources, self.totalLength, self.cost).solve()
        print(result)
        SettingsScreen.create(self=self, results=result)

    def setup_scrollview(self, dt):
        if self.container is not None:
            self.container.bind(minimum_height=self.container.setter('height'))

    def on_checkbox_active(self, *args):
        print(args)
        if args[2] != '':
            self.resources[args[0]].exact_amount = args[2]

    def save_value(self, value):

        if value != '':
            self.cost = float(value)

    def save_total_length(self, value):
        if value != '':
            list = value.split(';')
            for item in list:
                self.totalLength.append(float(item.replace(',', '.')))
            print(self.totalLength)

    def save_length(self, *args):

        if args[2] != '':
            self.resources[args[0]].length = float(args[2].replace(',', '.'))
        pass

    def save_amount(self, *args):

        if args[2] != '':
            self.resources[args[0]].amount = int(args[2])
        pass

    def on_enter(self, value=None):

        if not value:
            value = 0
        if self.container is not None:
            self.container.clear_widgets()

        for i in range(int(value)):
            self.resources.append(ResourceData(1, 1, True))

            label = Label(text=str(i + 1) + '.')
            self.container.add_widget(label)

            lengthinput = TextInput(multiline=False, input_type='number')
            lengthinput.bind(text=partial(self.save_length, i))
            self.container.add_widget(lengthinput)

            checkbox = CheckBox(group='sign' + str(i), active=True)
            checkbox.bind(active=partial(self.on_checkbox_active, True))

            checkbox2 = CheckBox(group='sign' + str(i))
            checkbox2.bind(active=partial(self.on_checkbox_active, False))

            self.container.add_widget(checkbox)
            self.container.add_widget(checkbox2)

            amountinput = TextInput(multiline=False, input_type='number')
            amountinput.bind(text=partial(self.save_amount, i))
            self.container.add_widget(amountinput)
