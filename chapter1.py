import arcade
import time
import settings
WIDTH = 800
HEIGHT = 600
title = "cantina"
MOVEMENT_SPEED = 15
holding_glass = False

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x <= 630 and self.center_y == 50:
            self.center_x = 630

        if self.center_x >= 740 and self.center_y == 50:
            self.center_x = 740

        if self.center_x <= 580 and self.center_y == 150:
            self.center_x = 580

        if self.center_x >= 700 and self.center_y == 150:
            self.center_x = 700

        if self.center_x <= 530 and self.center_y == 250:
            self.center_x = 530
        
        if self.center_x >= 650 and self.center_y == 250:
            self.center_x = 650

        if self.center_x <= 480 and self.center_y == 350:
            self.center_x = 480

        if self.center_x >= 630 and self.center_y == 350:
            self.center_x = 630

        if self.center_y <= 50:
            self.center_y = 50
        if self.center_y >= 350:
            self.center_y = 350


class Chapter1View(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_list = None

        arcade.set_background_color(arcade.color.GRAY)
        self.player_list = arcade.SpriteList()
        self.player = Player(filename="images/tend.png",
                             center_x=700,
                             center_y=150,
                             scale=0.35)

    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render() 

        arcade.draw_triangle_filled(0, 0, 0, 600, 300, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_triangle_filled(800, 0, 800, 600, 500, 600, arcade.color.BLUE_SAPPHIRE)

        arcade.draw_rectangle_filled(310, 50, 600, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(310, 150, 500, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(310, 250, 400, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(310, 350, 300, 60, arcade.color.BRONZE)

        arcade.draw_rectangle_filled(400, 550, 400, 300, arcade.color.BLUE_BELL)
        arcade.draw_rectangle_filled(400, 510, 200, 100, arcade.color.BABY_BLUE_EYES)
        self.player.draw()

    def update(self, delta_time):

        self.player.update()

    def on_key_press(self, key, key_modifiers):
        print(key, key_modifiers)
        if key == arcade.key.UP:
            self.player.change_y += 100
        elif key == arcade.key.DOWN:
            self.player.change_y -= 100
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        
        
    def on_key_release(self, key, key_modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


if __name__ == "__main__":    
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter1View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
