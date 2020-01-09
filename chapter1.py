import arcade

import settings

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GRAY)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        self.player = arcade.Sprite(filename="Pictures/white.png",
                                    center_x=700,
                                    center_y=200,
                                    scale=0.5)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()
        arcade.draw_rectangle_filled(300, 50, 600, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(300, 200, 600, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(300, 350, 600, 70, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(300, 500, 600, 70, arcade.color.BRONZE)

        

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.update()

    def on_key_press(self, key, key_modifiers):
        print(key, key_modifiers)
        if key == arcade.key.D:
            self.player.change_x = 1

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

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
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter1View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
