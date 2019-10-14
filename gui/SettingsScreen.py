from functools import partial

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class SettingsScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

    @staticmethod
    def add_empty_space(layout, len):
        for i in range(len):
            label = Label(text="")
            layout.add_widget(label)

    @staticmethod
    def draw(label, side, resources_configurations, *args):
        if (side == 'left'):
            with label.canvas.before:
                Color(1, 1, 1)
                print(label.pos)
                Rectangle(size=(2, 40), pos=(Window.width - 100, Window.height - 40))
        elif side == 'right':
            with label.canvas.before:
                Color(1, 1, 1)
                print(label.pos)
                Rectangle(size=(2, 40), pos=(label.x + 100, Window.height - 40))

    @staticmethod
    def create_after_init(self, *args):

        white = (1, 1, 1, 1)
        yellow = (1, 1, 0, 1)
        custom_color = white

        layout = GridLayout(cols=len(self.results.resources_configurations[0].sections) + 2,
                            row_default_height=40, row_force_default=True)

        self.results_screen.add_widget(layout)

        label = Label(text='[b]dlugosc[/b]', size_hint_x=None, width=100, markup=True, color=(1, 0, 0, 1))
        layout.add_widget(label)

        # SettingsScreen.draw(label, 'right', self.results.resources_configurations)

        for j in range(len(self.results.resources_configurations[0].sections)):
            label = Label(text='[b]' + str(j) + '[/b]', markup=True, color=(1, 0, 0, 1))
            layout.add_widget(label)

        label = Label(text='[b]ilosc[/b]', size_hint_x=None, width=100, markup=True, color=(1, 0, 0, 1))
        layout.add_widget(label)

        # SettingsScreen.draw(label, 'left', self.results.resources_configurations)

        print(self.results)

        for i in range(len(self.results.resources_configurations)):

            label = Label(text=str(self.results.resources_configurations[i].resource.length))
            layout.add_widget(label)

            color_index = 0
            custom_color = white
            for j in range(len(self.results.resources_configurations[i].sections)):
                if self.results.resources_configurations_starts_at and j == \
                        self.results.resources_configurations_starts_at[color_index]:
                    if custom_color == white:
                        custom_color = yellow
                    else:
                        custom_color = white
                    if color_index != len(self.results.resources_configurations_starts_at) - 1:
                        color_index += 1

                label = Label(text=str(self.results.resources_configurations[i].sections[j]), color=custom_color)
                layout.add_widget(label)

            label = Label(text=str(self.results.resources_configurations[i].resource.amount))
            layout.add_widget(label)

        label = Label(text="Odpad (m)", color=(1, 0, 0, 1))
        layout.add_widget(label)

        color_index = 0
        custom_color = white
        for j in range(len(self.results.resources_waste.waste)):

            if self.results.resources_configurations_starts_at and j == self.results.resources_configurations_starts_at[
                color_index]:
                if custom_color == white:
                    custom_color = yellow
                else:
                    custom_color = white
                if color_index != len(self.results.resources_configurations_starts_at) - 1:
                    color_index += 1

            label = Label(text=str(self.results.resources_waste.waste[j]), color=custom_color)
            layout.add_widget(label)

        SettingsScreen.add_empty_space(layout, 1)

        label = Label(text="Odpad (zl)", color=(1, 0, 0, 1))
        layout.add_widget(label)

        color_index = 0
        custom_color = white
        for j in range(len(self.results.resources_waste.price)):

            if self.results.resources_configurations_starts_at and j == self.results.resources_configurations_starts_at[
                color_index]:
                if custom_color == white:
                    custom_color = yellow
                else:
                    custom_color = white
                if color_index != len(self.results.resources_configurations_starts_at) - 1:
                    color_index += 1

            label = Label(text=str(self.results.resources_waste.price[j]), color=custom_color)
            layout.add_widget(label)

        for j in range(2 * len(self.results.resources_configurations[0].sections) + 5):
            label = Label(text="")
            layout.add_widget(label)

        label = Label(text="Warianty ciecia", color=(1, 0, 0, 1))
        layout.add_widget(label)

        color_index = 0
        custom_color = white
        for j in range(len(self.results.resources_configurations[0].sections)):

            if self.results.resources_configurations_starts_at and j == self.results.resources_configurations_starts_at[color_index]:
                if custom_color == white:
                    custom_color = yellow
                else:
                    custom_color = white
                if color_index != len(self.results.resources_configurations_starts_at) - 1:
                    color_index += 1

            label = Label(text=str(j), color=custom_color)
            layout.add_widget(label)

        SettingsScreen.add_empty_space(layout, 2)

        color_index = 0
        custom_color = white
        for j in range(len(self.results.x)):

            if self.results.resources_configurations_starts_at and j == self.results.resources_configurations_starts_at[color_index]:
                if custom_color == white:
                    custom_color = yellow
                else:
                    custom_color = white
                if color_index != len(self.results.resources_configurations_starts_at) - 1:
                    color_index += 1

            label = Label(text=str(self.results.x[j]), color=custom_color)
            layout.add_widget(label)

        SettingsScreen.add_empty_space(layout, len(self.results.resources_configurations[0].sections) + 3)

        label = Label(text='Function', color=(1, 0, 0, 1))
        layout.add_widget(label)

        label = Label(text=str(self.results.fun))
        layout.add_widget(label)

        SettingsScreen.add_empty_space(layout, len(self.results.resources_configurations[0].sections))

        label = Label(text='Total waste', color=(1, 0, 0, 1))
        layout.add_widget(label)

        label = Label(text=str(self.results.total_waste))
        layout.add_widget(label)
        SettingsScreen.add_empty_space(layout, len(self.results.resources_configurations[0].sections))

        label = Label(text='Total price of waste', color=(1, 0, 0, 1))
        layout.add_widget(label)

        label = Label(text=str(self.results.total_price))
        layout.add_widget(label)

        SettingsScreen.add_empty_space(layout, len(self.results.resources_configurations[0].sections) + 2)

        # button = Button(text="Back", on_press=SettingsScreen.go_back)
        # layout.add_widget(button)

    def create(self, results):

        self.results = results

        self.results_screen = Screen(name='settings')
        self.manager.switch_to(self.results_screen, direction='left')

        Clock.schedule_once(partial(SettingsScreen.create_after_init, self))
