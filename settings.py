class Settings():

    def __init__(self):
        self.screen_width = 1800
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        self.bullet_width = 6
        self.bullet_height = 25
        self.bullet_color = 0, 255, 0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 5
        self.fleet_direction = 1

    def increse_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor  *= self.speedup_scale
