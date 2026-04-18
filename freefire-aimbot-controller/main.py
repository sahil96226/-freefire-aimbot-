from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
import random

class AimbotController(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (0.35, 0.5)
        self.pos_hint = {'center_x': 0.85, 'center_y': 0.5}
        self.aimbot_on = False
        self.fov_value = 300
        self.smooth_value = 0.2
        self.targets_locked = 0
        
        # Header
        header = Label(text='🎯 FREE FIRE AIMBOT v2.0', 
                      font_size=28, bold=True, size_hint_y=0.15)
        self.add_widget(header)
        
        # Toggle Button
        self.toggle_btn = Button(text='🚀 ACTIVATE AIMBOT', size_hint_y=0.2,
                               background_color=(0, 0.8, 0, 1), font_size=20)
        self.toggle_btn.bind(on_press=self.toggle_aimbot)
        self.add_widget(self.toggle_btn)
        
        # FOV Slider
        fov_label = Label(text=f'FOV: {self.fov_value}px', size_hint_y=0.1)
        self.fov_label = fov_label
        self.add_widget(fov_label)
        self.fov_slider = Slider(min=100, max=600, value=300, size_hint_y=0.15)
        self.fov_slider.bind(value=self.update_fov)
        self.add_widget(self.fov_slider)
        
        # Smoothness Slider
        smooth_label = Label(text=f'Smooth: {self.smooth_value}', size_hint_y=0.1)
        self.smooth_label = smooth_label
        self.add_widget(smooth_label)
        self.smooth_slider = Slider(min=0.05, max=0.5, value=0.2, size_hint_y=0.15)
        self.smooth_slider.bind(value=self.update_smooth)
        self.add_widget(self.smooth_slider)
        
        # Stats
        self.stats_label = Label(text='Targets: 0\nAccuracy: 98%\nStatus: Ready', 
                               size_hint_y=0.25, halign='center')
        self.add_widget(self.stats_label)
        
        Clock.schedule_interval(self.game_loop, 1/60)
    
    def toggle_aimbot(self, instance):
        self.aimbot_on = not self.aimbot_on
        if self.aimbot_on:
            self.toggle_btn.text = '⏹️ DEACTIVATE'
            self.toggle_btn.background_color = (0.9, 0.1, 0.1, 1)
        else:
            self.toggle_btn.text = '🚀 ACTIVATE AIMBOT'
            self.toggle_btn.background_color = (0, 0.8, 0, 1)
    
    def update_fov(self, instance, value):
        self.fov_value = int(value)
        self.fov_label.text = f'FOV: {self.fov_value}px'
    
    def update_smooth(self, instance, value):
        self.smooth_value = round(value, 2)
        self.smooth_label.text = f'Smooth: {self.smooth_value}'
    
    def simulate_enemy_detection(self, dt):
        # Simulate Free Fire enemy detection
        if random.random() < 0.7:  # 70% detection rate
            self.targets_locked += 1
            return (random.randint(200, 1700), random.randint(100, 800))
        return None
    
    def game_loop(self, dt):
        if self.aimbot_on:
            target = self.simulate_enemy_detection(dt)
            if target:
                self.stats_label.text = f'Targets: {self.targets_locked}\nLocked: ({target[0]},{target[1]})\nStatus: AIMING'
                print(f"🎯 Locked enemy at {target} - HEADSHOT!")
            else:
                self.stats_label.text = f'Targets: {self.targets_locked}\nStatus: Scanning...'
        return True

class FreeFireAimbotApp(App):
    def build(self):
        self.title = 'Free Fire Aimbot Controller v2.0'
        return AimbotController()

if __name__ == '__main__':
    FreeFireAimbotApp().run()