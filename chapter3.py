import arcade
import random
import settings
import math

LASER_SPEED = 4

class Chapter2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

        self.frame_count = 0

        self.enemy_list = None
        self.laser_list = None
        self.player_list = None
        self.player = None
        self.score = 0
        self.setup()

    def setup(self):
        self.drone_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.score = 0

        self.player = arcade.Sprite("images/luke.png", 1)
        self.player_list.append(self.player)

        
        enemy = arcade.Sprite("images/drone.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = settings_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

        
        enemy = arcade.Sprite("images/drone.png", 0.5)
        enemy.center_x = settings_WIDTH - 120
        enemy.center_y = settings_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.enemy_list.draw()
        self.laser_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):

        self.frame_count += 1

        for enemy in self.enemy_list:
            start_x = enemy.center_x
            start_y = enemy.center_y

            dest_x = self.player.center_x
            dest_y = self.player.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            enemy.angle = math.degrees(angle) - 90


            if self.frame_count % 60 == 0:
                laser = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                laser.center_x = start_x
                laser.center_y = start_y


                laser.angle = math.degrees(angle)


                laser.change_x = math.cos(angle) * LASER_SPEED
                laser.change_y = math.sin(angle) * LASER_SPEED

                self.laser_list.append(laser)

        
        for laser in self.laser_list:
            if laser.top < 0:
                laser.remove_from_sprite_lists()

        self.laser_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.laser_list)
        for laser in hit_list:
            laser.remove_from_sprite_lists()
            self.score += 1

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        
        self.player.center_x = x
        self.player.center_y = y


def on_mouse_motion(self, x, y, delta_x, delta_y):
    
    self.player.center_x = x
    self.player.center_y = y

    def on_key_press(self, key, modifiers):
        if self.score == 5:
            self.director.next_view()


if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.
    You can ignore this whole section. Keep it at the bottom
    of your code.
    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter2View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
