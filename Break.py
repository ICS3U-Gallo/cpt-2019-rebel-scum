import arcade
import os

WIDTH = 800
HEIGHT = 600

current_screen = "menu"
score = 0


def setup():
    global x1, y1
    x1 = 0
    y1 = 425
    arcade.open_window(WIDTH, HEIGHT, "Mateo Tompkins")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1 / 60)

    global x
    x = 505
    global z
    z = 495
    global xx
    xx = 705
    global zz
    zz = 695
    global gunx
    gunx = 400
    global guny
    guny = 300

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global x
    x += 25
    if x == 805:
        x -= 400
    global z
    z -= 25
    if z <= 0:
        z += 400
    global xx
    xx += 25
    if xx == 805:
        xx -= 400
    global zz
    zz -= 25
    if zz <= 0:
        zz += 400


"""
##################################################
def on_key_press(self, key, modifiers):
       Called whenever a key is pressed.
   if key == arcade.key.UP:
       self.player_sprite.change_y = MOVEMENT_SPEED
   elif key == arcade.key.DOWN:
       self.player_sprite.change_y = -MOVEMENT_SPEED
   elif key == arcade.key.LEFT:
       self.player_sprite.change_x = -MOVEMENT_SPEED
   elif key == arcade.key.RIGHT:
       self.player_sprite.change_x = MOVEMENT_SPEED
"""


def on_key_press(key, modifiers):
    global gunx

    if key == arcade.key.D:
        gunx += 100


def on_key_release(key, modifiers):
    global gunx

    if key == arcade.key.D:
        gunx += 0

    # global gunx
    # if key == arcade.key.D:
    #    gunx += 5


def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        draw_game()
    if current_screen == "start":
        draw_start()
    if current_screen == "room_one":
        draw_room_one()
    if current_screen == "room_one_right":
        draw_room_one_right()
    if current_screen == "room_one_left":
        draw_room_one_left()
    if current_screen == "d1_rm1":
        draw_d1_rm1()
    if current_screen == "b1_rm1":
        draw_b1_rm1()


def draw_game():
    global x
    arcade.draw_line(x, 0, x, 800, arcade.color.GRAY, 2)
    global z
    arcade.draw_line(z, 0, z, 800, arcade.color.GRAY, 2)
    global xx
    arcade.draw_line(xx, 0, xx, 800, arcade.color.GRAY, 2)
    global zz
    arcade.draw_line(zz, 0, zz, 800, arcade.color.GRAY, 2)
    # TRENCH
    arcade.draw_line(90, 49, 400, 250, arcade.color.GRAY, 2)
    arcade.draw_line(710, 49, 400, 250, arcade.color.GRAY, 2)
    arcade.draw_line(70, 525, 400, 250, arcade.color.GRAY, 2)
    arcade.draw_line(730, 525, 400, 250, arcade.color.GRAY, 2)

    arcade.draw_triangle_filled(70, 525, 400, 250, 730, 525, arcade.color.BLACK)
    arcade.draw_rectangle_filled(400, 600, 800, 150, arcade.color.BLACK)

    arcade.draw_triangle_filled(90, 49, 710, 49, 400, 250, arcade.color.BLACK)
    arcade.draw_rectangle_filled(400, 0, 800, 100, arcade.color.BLACK)

    global gunx

    global guny
   # arcade.draw_circle_outline(gunx, guny, 15, arcade.color.RED, 5)

    # CIRCLE
    arcade.draw_circle_outline(400, 300, 500, arcade.color.BLACK, 210)

    # TOP LINE HORIZONTAL
    arcade.draw_line(330, 450, 470, 450, arcade.color.DARK_BLUE_GRAY, 5)

    # BOTTOM LINE HORIZONTAL
    arcade.draw_line(330, 150, 470, 150, arcade.color.DARK_BLUE_GRAY, 5)

    # LEFT LINE VERTICAL
    arcade.draw_line(250, 230, 250, 370, arcade.color.DARK_BLUE_GRAY, 5)

    # RIGHT LINE VERTICAL
    arcade.draw_line(550, 230, 550, 370, arcade.color.DARK_BLUE_GRAY, 5)

    # NE DIAGONAL
    arcade.draw_line(470, 450, 550, 370, arcade.color.DARK_BLUE_GRAY, 5)

    # NW DIAGONAL
    arcade.draw_line(330, 450, 250, 370, arcade.color.DARK_BLUE_GRAY, 5)

    # SE DIAGONAL
    arcade.draw_line(330, 150, 250, 230, arcade.color.DARK_BLUE_GRAY, 5)

    # SW DIAGONAL
    arcade.draw_line(470, 150, 550, 230, arcade.color.DARK_BLUE_GRAY, 5)

    # TOP LEFT LINE
    arcade.draw_line(50, 900, 330, 450, arcade.color.DARK_BLUE_GRAY, 5)

    # TOP RIGHT LINE
    arcade.draw_line(750, 900, 470, 450, arcade.color.DARK_BLUE_GRAY, 5)

    # BOTTOM LEFT LINE
    arcade.draw_line(330, 150, 50, -900, arcade.color.DARK_BLUE_GRAY, 5)

    # BOTTOM RIGHT LINE
    arcade.draw_line(750, -900, 470, 150, arcade.color.DARK_BLUE_GRAY, 5)

    # BOTTOM MIDDLE LEFT LINE
    arcade.draw_line(250, 230, 39, 130, arcade.color.DARK_BLUE_GRAY, 5)

    # BOTTOM MIDDLE RIGHT LINE
    arcade.draw_line(550, 230, 761, 130, arcade.color.DARK_BLUE_GRAY, 5)

    # TOP MIDDLE LEFT LINE
    arcade.draw_line(39, 461, 250, 370, arcade.color.DARK_BLUE_GRAY, 5)

    # TOP MIDDLE RIGHT LINE
    arcade.draw_line(550, 370, 761, 461, arcade.color.DARK_BLUE_GRAY, 5)

    # FINAL CIRCLE
    # arcade.draw_circle_outline(400, 295, 400, arcade.color.DARK_GRAY, 5)
    arcade.draw_circle_outline(400, 295, 400, arcade.color.DARK_BLUE_GRAY, 5)

    # WALLS

    # self.player = arcade.sprite(resources/resources/images/spritesheets/explosion.png)
    # self.player.draw

    # self.player = arcade.Sprite(":resources:/images/animated_characters/male_adventurer/maleAdventurer_idle.png")
    # self.player.center_x = 100
    # self.player.center_y = 100

    def on_draw(self):
        arcade.start_render()  # keep as first line
        self.player.draw()


def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "menu":
        menu_keybinds(key, modifiers)

    """
    if current_screen == "start":
        start_keybinds(key, modifiers)
    if current_screen == "room_one":
        room_one_keybinds(key, modifiers)
    if current_screen == "room_one_right":
        room_one_right_keybinds(key, modifiers)
    if current_screen == "room_one_left":
        room_one_left_keybinds(key, modifiers)
    if current_screen == "d1_rm1":
        d1_rm1_keybinds(key, modifiers)
    if current_screen == "b1_rm1":
        b1_rm1_keybinds(key, modifiers)
 """


"""
def menu_keybinds(key, modifiers):
   global current_screen
   if key == arcade.key.ENTER:
       current_screen = "room_one_right"


def start_keybinds(key, modifiers):
   global current_screen
   if key == arcade.key.ESCAPE:
       current_screen = "menu"
   if key == arcade.key.Y:
       current_screen = "room_one"
   if key == arcade.key.N:
       current_screen = "menu"


def room_one_keybinds(key, modifiers):
   global current_screen
   if key == arcade.key.ESCAPE:
       current_screen = "start"
   if key == arcade.key.RIGHT:
       current_screen = "room_one_right"
   if key == arcade.key.LEFT:
       current_screen = "room_one_left"
   if key == arcade.key.W:
       current_screen = "d1_rm1"
   if key == arcade.key.B:
       current_screen = "b1_rm1"


def d1_rm1_keybinds(key, modifiers):
   global current_screen, score
   if key == arcade.key.ESCAPE:
       current_screen = "room_one"
   if key == arcade.key.A:
       score += 1
       current_screen = "room_one"
   else:
       pass
"""
"""
def b1_rm1_keybinds(key, modifiers):
   global current_screen, score
   if key == arcade.key.C:
       score += 1
       current_screen = "room_one"


def room_one_right_keybinds(key, modifiers):
   global current_screen
   if key == arcade.key.LEFT:
       current_screen = "room_one"


def room_one_left_keybinds(key, modifiers):
   global current_screen
   if key == arcade.key.RIGHT:
       current_screen = "room_one"
"""


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()




