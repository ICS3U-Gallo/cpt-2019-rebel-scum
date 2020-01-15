import arcade
import settings


class Star(arcade.sprite):

    def reset_pos(self):
        self.centre_y = random.randrange(settings.HEIGHT)
        self.centre_x = random.randrange(settings.WIDTH - 20)
    
    def update(self):
        self.centre_x += 1

        if self.top < 0:
            self.reset_pos()


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        starcount = 50
        self.star_sprite_list = None
        self.coin_sprite_list = None

        self.coin_sprite = None

    def setup(self):
        self.star_sprite_list = arcade.SpriteList()
        self.coin_sprite_list = arcade.SpriteList()

        self.coin_sprite = arcade.Sprite(":resources:images/items/coinGOLD.png"
                                         , SPRITE_SCALING_COIN)
        self.coin_sprite.center_x = 50
        self.coin_sprite.centre_y = 50
        self.coin_sprite_list.append(self.coin_sprite)

        for i in range(starcount):
            star = arcade.Sprite(star)

            star.centre_x = random.randrange(settings.WIDTH)
            star.centre_y = random.randrange(settings.HEIGHT)

            self.star_sprite_list.append(star)
    
    def on_draw(self):
        arcade.start_render()
        star = arcade.draw_circle_filled(star.center_x, star.center_y, 10,
                                         arcade.color.WHITE)
        self.star_sprite_list.draw()
        self.coin_sprite_list.draw()

        arcade.draw_texture_rectangle(settings.WIDTH/2, settings.HEIGHT/2,
                                      settings.WIDTH-100, settings.HEIGHT-200,
                                      alvares/starwars/Star_Wars_Logo.png)
        
        arcade.draw_texture_rectangle(settings.WIDTH/2, settings.HEIGHT/2, 
                                      settings.WIDTH, settings.HEIGHT - 300)

    def on_mouse_motion(self, x, y, dx, dy):
        self.coin_sprite.centre_x = x
        self.coin_sprite.centre_y = y

    def update(self):
        
        self.star_sprite_list.update()

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
