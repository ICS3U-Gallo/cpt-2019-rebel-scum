import arcade
import settings


class Chapter4View(arcade.View):

player_scaling = 0.15
player_bolt_scaling = 0.1
enemy_scaling = 0.1
enemy_bolt_scaling = 0.05

screen_width = 640
screen_height = 480
screen_title = "Millennium Falcon Escape"

player_movement_speed = 8
bolt_speed = 5


class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0

        if self.right > screen_width - 1:
            self.right = screen_height - 1

        if self.bottom < 0:
            self.bottom = 0

        if self.top > screen_height - 1:
            self.top = screen_height - 1

def on_show(self):

    self.player_list = None
    self.player_bolt_list = None
    self.enemy_list = None
    self.enemy_bolt_list = None

    self.frame_count = 0

    self.player_sprite = None
    self.player = None
    self.player_score = 0
    self.player_status = 0

    self.a_pressed = False
    self.d_pressed = False
    self.w_pressed = False
    self.s_pressed = False

    arcade.set_background_color(arcade.color.BLACK)
    self.setup()

def setup(self):

    self.player_list = arcade.SpriteList()
    self.player_bolt_list = arcade.SpriteList()
    self.enemy_list = arcade.SpriteList()
    self.enemy_bolt_list = arcade.SpriteList()

    self.player_sprite = Player("millennium_falcon.png", player_scaling)
    self.player_sprite.center_x = screen_width/2
    self.player_sprite.center_y = screen_height/2
    self.player_list.append(self.player_sprite)

    enemy = arcade.Sprite("tie_fighter.png", enemy_scaling)
    enemy.center_x = 70
    enemy.center_y = screen_height - enemy.height
    enemy.angle = 180
    self.enemy_list.append(enemy)

    enemy = arcade.Sprite("tie_fighter.png", enemy_scaling)
    enemy.center_x = 140
    enemy.center_y = screen_height - enemy.height
    enemy.angle = 180
    self.enemy_list.append(enemy)

    enemy = arcade.Sprite("tie_fighter.png", enemy_scaling)
    enemy.center_x = screen_width - 70
    enemy.center_y = screen_height - enemy.height
    enemy.angle = 180
    self.enemy_list.append(enemy)

    enemy = arcade.Sprite("tie_fighter.png", enemy_scaling)
    enemy.center_x = screen_width - 140
    enemy.center_y = screen_height - enemy.height
    enemy.angle = 180
    self.enemy_list.append(enemy)

def on_draw(self):

    arcade.start_render()

    self.player_list.draw()
    self.player_bolt_list.draw()
    self.enemy_list.draw()
    self.enemy_bolt_list.draw()

    arcade.draw_text(f"Objective: Destroy 4/{self.player_score} TIE fighters.", 10, 20, arcade.color.WHITE, 10)

    if self.player_score == 4:
        arcade.draw_text("SUCCESS", (screen_width / 2) - 70, (screen_height / 2) - 10, arcade.color.WHITE, 30)

    if self.player_status == 1:
        arcade.draw_text("DESTROYED", (screen_width / 2) - 90, (screen_height / 2) - 10, arcade.color.WHITE, 30)

def on_update(self, delta_time):

    self.frame_count += 1

    self.player_sprite.change_x = 0
    self.player_sprite.change_y = 0

    if self.w_pressed and not self.s_pressed:
        self.player_sprite.change_y = player_movement_speed
    elif self.s_pressed and not self.w_pressed:
        self.player_sprite.change_y = -player_movement_speed
    if self.a_pressed and not self.d_pressed:
        self.player_sprite.change_x = -player_movement_speed
    elif self.d_pressed and not self.a_pressed:
        self.player_sprite.change_x = player_movement_speed

    self.player_list.update()
    self.player_bolt_list.update()

    for enemy in self.enemy_list:

        start_x = enemy.center_x
        start_y = enemy.center_y

        dest_x = self.player_sprite.center_x
        dest_y = self.player_sprite.center_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        enemy.angle = math.degrees(angle) - 90

        if self.frame_count % 20 == 0:
            enemy_bolt = arcade.Sprite("empire_blaster_bolt.png", enemy_bolt_scaling)
            enemy_bolt.center_x = start_x
            enemy_bolt.center_y = start_y

            enemy_bolt.angle = math.degrees(angle) - 90

            enemy_bolt.change_x = math.cos(angle) * bolt_speed
            enemy_bolt.change_y = math.sin(angle) * bolt_speed

            self.enemy_bolt_list.append(enemy_bolt)

    for enemy_bolt in self.enemy_bolt_list:
        if enemy_bolt.bottom < 0:
            enemy_bolt.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(enemy_bolt, self.player_list)
        if len(hit_list) > 0:
            enemy_bolt.remove_from_sprite_lists()
            self.player_sprite.remove_from_sprite_lists()
            self.player_status = 1

    self.enemy_bolt_list.update()

    for player in self.player_list:

        if self.frame_count % 6 == 0:
            player_bolt = arcade.Sprite("rebel_blast_bolt.png", player_bolt_scaling)
            player_bolt.center_x = player.center_x
            player_bolt.angle = 0
            player_bolt.top = player.bottom
            player_bolt.change_y = bolt_speed
            self.player_bolt_list.append(player_bolt)

    for player_bolt in self.player_bolt_list:
        if player_bolt.top < 0:
            player_bolt.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(player_bolt, self.enemy_list)
        for enemy in hit_list:
            player_bolt.remove_from_sprite_lists()
            enemy.remove_from_sprite_lists()
            self.player_score += 1
        if self.player_score == 2:
            arcade.draw_text("SUCCESS", (screen_width / 2), (screen_height / 2), arcade.color.WHITE, 30)

    self.player_bolt_list.update()

def on_key_press(self, key, modifiers):

    if key == arcade.key.W:
        self.w_pressed = True
    elif key == arcade.key.S:
        self.s_pressed = True
    elif key == arcade.key.A:
        self.a_pressed = True
    elif key == arcade.key.D:
        self.d_pressed = True

def on_key_release(self, key, modifiers):

    if key == arcade.key.W:
        self.w_pressed = False
    elif key == arcade.key.S:
        self.s_pressed = False
    elif key == arcade.key.A:
        self.a_pressed = False
    elif key == arcade.key.D:
        self.d_pressed = False



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
    my_view = Chapter4View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
