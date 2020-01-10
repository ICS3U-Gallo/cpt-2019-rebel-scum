import arcade
import settings

starcount = 50
self.star_sprite_list = None


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.star_sprite_list = arcade.SpriteList()

        for i in range(starcount):
            star = arcade.draw_circle_filled(star.center_x, star.center_y, 10,
                                             arcade.color.WHITE)

            star.centre_x = random.randrange(settings.WIDTH)
            star.centre_y = random.randrange(settings.HEIGHT)

            self.star_sprite_list.append(star)

    def update(self):
        star.centre_x += 1

        if star.centre_x > settings.WIDTH:
            star.centre_x = 0

    def on_draw(self):
        arcade.start_render()
        self.star_sprite_list.draw()

        arcade.draw_texture_rectangle(settings.WIDTH/2, settings.HEIGHT/2,
                                      settings.WIDTH-100, settings.HEIGHT-200,
                                      alvares/starwars/Star_Wars_Logo.png)

    def on_key_press(self, key, modifiers):
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
    my_view = MenuView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
