import arcade

WIDTH = 800
HEIGHT = 600
MOVEMENT_SPEED = 8


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GRAY)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        self.player = arcade.Sprite(filename="Pictures/white.png",
                                    center_x=700,
                                    center_y=150,
                                    scale=0.5)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()
        arcade.draw_triangle_filled(0, 0, 0, 600, 300, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_triangle_filled(800, 0, 800, 600, 500, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_rectangle_filled(307, 50, 600, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(307, 150, 500, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(307, 250, 400, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(307, 350, 300, 70, arcade.color.BRONZE)

        arcade.draw_rectangle_filled(400, 550, 400, 300, arcade.color.BLUE_BELL)
        

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.update()

    def on_key_press(self, key, key_modifiers):
        print(key, key_modifiers)
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass\

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
