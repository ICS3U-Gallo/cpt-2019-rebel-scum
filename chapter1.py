import arcade
import time
import settings
import random
import sys
WIDTH = 800
HEIGHT = 600
MOVEMENT_SPEED = 30
frm_count = 0
score = 0


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


class Customer():

    def __init__(self, center_x, center_y, change_x, change_y):
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y

    def game_over(self):
        pass

    def update(self):
        self.center_x += self.change_x
        self.center_y += 0
        if self.center_y == 85 and self.center_x >= 630:
            self.center_x = 630
        if self.center_y == 185 and self.center_x >= 580:
            self.center_x = 580
        if self.center_y == 285 and self.center_x >= 530:
            self.center_x = 530
        if self.center_y == 385 and self.center_x >= 480:
            self.center_x = 480

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 30, 70, arcade.color.BABY_BLUE_EYES)


class Glass():
    def __init__(self, center_x, center_y, change_x, change_y):
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y

    def update(self, x2, y2):

        print(x2, self.center_x, "x2")
        self.center_x += self.change_x
        self.center_y += 0
        if (self.center_x - x2) < 10 and self.center_y == y2:
            return "hit"
        elif self.center_x <= 0:
            return "del"
        else:
            return "miss"

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 50, 50, arcade.color.WHITE)


class Chapter1View(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.GRAY)
        self.player_list = None
        self.player_list = arcade.SpriteList()
        self.player = Player(filename="images/tend.png",
                             center_x=700,
                             center_y=150,
                             scale=0.35)
        self.player_list.append(self.player)
        self.glasses = []
        # self.luke = arcade.Sprite("images/Luke.png")
        # self.customer_list = arcade.SpriteList
        # self.customer_list.append(self, self.luke)
        global customers
        self.holding_glass = False
        customers = []
        self.glass = Glass(600, 90, 5, 0)

        # self.customer = Customer(filename=customer_sprites[random.randrange(5)],
        #                         center_x = -70,
        #                         center_y=random.randrange(85, 386, 100),
        #                         scale=0.35)
    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        global customers
        global frm_count
        arcade.start_render()
        # print(frm_count)
        for customer in customers:
            customer.draw()
        arcade.draw_triangle_filled(0, 0, 0, 600, 300, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_triangle_filled(800, 0, 800, 600, 500, 600, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_rectangle_filled(400, 550, 400, 300, arcade.color.BLUE_BELL)
        arcade.draw_rectangle_filled(400, 510, 200, 100, arcade.color.BABY_BLUE_EYES)
        arcade.draw_rectangle_filled(310, 50, 600, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(310, 150, 500, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(310, 250, 400, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(310, 350, 300, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_filled(780, 50, 70, 60, arcade.color.BROWN_NOSE)
        arcade.draw_rectangle_filled(740, 150, 70, 60, arcade.color.BROWN_NOSE)
        arcade.draw_rectangle_filled(700, 250, 70, 60, arcade.color.BROWN_NOSE)
        arcade.draw_rectangle_filled(650, 350, 70, 60, arcade.color.BROWN_NOSE)
        self.player.draw()
        # self.glass.draw()
        for glass in self.glasses:
            glass.draw()

    def update(self, delta_time):

        global frm_count
        self.player.update()
        if frm_count % 300 == 0:
            pos = [[-70, 70], [-70, 170], [-70, 70], [-70, 370]]
            idx = random.randrange(4)
            customers.append(Customer(pos[idx][0], pos[idx][1], 3, 0))
        for customer in customers:
            customer.update()
        pos = [[-70, 70], [-70, 170], [-70, 270], [-70, 370]]
        frm_count += 1
        for i in range(3):
            idx = random.randrange(3)
        if frm_count % 100 == 0:
            customers.append(Customer(pos[idx][0], pos[idx][1], 3, 4))

        for glass in self.glasses[:]:
            for customer in customers:
                result = glass.update(customer.center_x, customer.center_y)
                if result == "hit":
                    print("hit")
                    customer.change_x *= -1
                    self.glasses.remove(glass)
                    break
                elif result == "del":
                    print("del")
                    self.glasses.remove(glass)

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
        if key == arcade.key.SPACE and self.player.center_x == 740 and self.player.center_y == 50:
            self.holding_glass = True
            print(self.holding_glass)
        elif key == arcade.key.SPACE and self.player.center_x == 700 and self.player.center_y == 150:
            self.holding_glass = True
            print(self.holding_glass)
        elif key == arcade.key.SPACE and self.player.center_x == 650 and self.player.center_y == 250:
            self.holding_glass = True
            print(self.holding_glass)
        elif key == arcade.key.SPACE and self.player.center_x == 630 and self.player.center_y == 350:
            self.holding_glass = True
            print(self.holding_glass)

        if key == arcade.key.SPACE and self.player.center_x == 630 and self.player.center_y == 50:
            if self.holding_glass == True:
                self.holding_glass = False
                self.glasses.append(Glass(630, 70, -5, 0))
        elif key == arcade.key.SPACE and self.player.center_x == 580 and self.player.center_y == 150:
            if self.holding_glass == True:
                self.holding_glass = False
                self.glasses.append(Glass(580, 170, -5, 0))
        elif key == arcade.key.SPACE and self.player.center_x == 530 and self.player.center_y == 250:
            if self.holding_glass == True:
                self.holding_glass = False
                self.glasses.append(Glass(530, 270, -5, 0))
        elif key == arcade.key.SPACE and self.player.center_x == 480 and self.player.center_y == 350:
            if self.holding_glass == True:
                self.holding_glass = False
                self.glasses.append(Glass(480, 370, -5, 0))

# pos = [[-70, 70], [-70, 170], [-70, 70], [-70, 370]]


if __name__ == "__main__":
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter1View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
