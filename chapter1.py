import arcade

WIDTH = 800
HEIGHT = 600
MOVEMENT_SPEED = 8
SPRITE_SCALING = 0.5

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > WIDTH - 1:
            self.right = WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > HEIGHT - 1:
            self.top = HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player_list = None
        self.player_sprite = None

        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player = arcade.Sprite(filename="white.png",
                                    center_x=700,
                                    center_y=150,
                                    scale=0.5)


    def on_draw(self):
        arcade.start_render() 

        arcade.draw_triangle_filled(0, 0, 0, 600, 300, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_triangle_filled(800, 0, 800, 600, 500, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_rectangle_filled(307, 50, 600, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(307, 150, 500, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(307, 250, 400, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(307, 350, 300, 70, arcade.color.BRONZE)

        arcade.draw_rectangle_filled(400, 550, 400, 300, arcade.color.BLUE_BELL)
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

    def on_mouse_motion(self, x, y, delta_x, delta_y):

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):

        pass

    def on_mouse_release(self, x, y, button, key_modifiers):

        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
