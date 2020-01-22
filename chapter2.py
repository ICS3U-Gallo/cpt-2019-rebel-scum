import arcade

import settings


class Chapter2View(arcade.View):
  import arcade

WIDTH = 640
HEIGHT = 480
current_screen = "start"
complete = 0
incorrect = 0

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Star Wars Episode IV: Chapter III")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global complete, incorrect, current_screen
    if incorrect == 4:
        current_screen = "game_over"
    if complete == 3:
        draw_done()

def on_draw():
    arcade.start_render()
    if current_screen == "start":
        draw_start()
    if current_screen == "room_one":
        draw_room_one()
    if current_screen == "part1":
        draw_part1()
    if current_screen == "part2":
        draw_part2()
    if current_screen == "part3":
        draw_part3()
    if current_screen == "part4":
        draw_part4()
    if current_screen == "game_over":
        draw_game_over()
    if current_screen == "part5":
        draw_part5()
    if current_screen == "part6":
        draw_part6()
    if current_screen == "part7":
        draw_part7()
    if current_screen == "part8":
        draw_part8()
    if current_screen == "part9":
        draw_part9()
    if current_screen == "done":
        draw_done()


def draw_start():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("The Millenium Falcon has entered the Death Star", 180, 300, arcade.color.WHITE)
    arcade.draw_text("Luke, Han, C3PO, Chewy, Ben and R2D2 have fled the", 165, 280, arcade.color.WHITE)
    arcade.draw_text("ship and they are now hiding in the security room, your ", 160, 260, arcade.color.WHITE)
    arcade.draw_text("mission is to escape the Death Star and rescue", 185, 240, arcade.color.WHITE)
    arcade.draw_text("Princess Leia Orchana from Vader and the Empire", 178, 220, arcade.color.WHITE)
    arcade.draw_text("Press Enter To Continue", 255, 200, arcade.color.WHITE)

def draw_room_one():
    arcade.set_background_color(arcade.color.DARK_GRAY)
    # Side Control Panel
    arcade.draw_rectangle_filled(20, 240, 40, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(20, 20, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 40, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 60, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 80, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 100, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 120, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 140, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 160, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 180, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 200, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 220, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 240, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 260, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 280, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 300, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 320, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 340, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 360, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 380, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 400, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 420, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 440, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 460, 20, 10, arcade.color.RED)
    # Desk w Computer & Monitor
    arcade.draw_rectangle_filled(220, 60, 360, 120, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 120, 20, 40, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 180, 180, 100, arcade.color.WHITE)
    arcade.draw_rectangle_outline(220, 180, 180, 100, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 360, 300, 200, arcade.color.WHITE)
    arcade.draw_rectangle_outline(220, 360, 300, 200, arcade.color.BLACK)
    # Right Side Gray Panel & Outlet
    arcade.draw_rectangle_filled(560, 240, 160, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(460, 240, 40, 480, arcade.color.GREEN)
    arcade.draw_rectangle_filled(440, 240, 10, 480, arcade.color.BLACK)
    arcade.draw_rectangle_filled(560, 140, 20, 20, arcade.color.RED)
    # Key Prompt
    arcade.draw_text("Press P to plug into the monitor", 490, 160, arcade.color.BLACK, font_size=9)

def draw_part1():
    arcade.set_background_color(arcade.color.DARK_GRAY)
    # Side Control Panel
    arcade.draw_rectangle_filled(20, 240, 40, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(20, 20, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 40, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 60, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 80, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 100, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 120, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 140, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 160, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 180, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 200, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 220, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 240, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 260, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 280, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 300, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 320, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 340, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 360, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 380, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 400, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 420, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 440, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 460, 20, 10, arcade.color.RED)
    # Desk w Computer & Monitor
    arcade.draw_rectangle_filled(220, 60, 360, 120, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 120, 20, 40, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 180, 180, 100, arcade.color.WHITE)
    arcade.draw_rectangle_outline(220, 180, 180, 100, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 360, 300, 200, arcade.color.WHITE)
    arcade.draw_rectangle_outline(220, 360, 300, 200, arcade.color.BLACK)
    # Right Side Gray Panel & Outlet
    arcade.draw_rectangle_filled(560, 240, 160, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(460, 240, 40, 480, arcade.color.GREEN)
    arcade.draw_rectangle_filled(440, 240, 10, 480, arcade.color.BLACK)
    arcade.draw_rectangle_filled(560, 140, 20, 20, arcade.color.RED)
    # Monitor Message
    arcade.draw_text("The tractor beam is coupled to the main reactor", 100, 380, arcade.color.GO_GREEN, font_size=10)
    arcade.draw_text("in 7 locations. A power loss at one of them", 120, 360, arcade.color.GO_GREEN, font_size=10)
    arcade.draw_text("will allow the ship to leave the terminals", 128, 340, arcade.color.GO_GREEN, font_size=10)
    arcade.draw_text("Press enter to view objective", 148, 320, arcade.color.GO_GREEN, font_size=10)

def draw_part2():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Your plan is to pose Chewy as a prisoner to get past", 160, 260, arcade.color.WHITE)
    arcade.draw_text("security, from here you will be brought to the holding", 155, 240, arcade.color.WHITE)
    arcade.draw_text("centre where you will locate and rescue Leia...", 180, 220, arcade.color.WHITE)
    arcade.draw_text("Press the escape key to return", 225, 200, arcade.color.WHITE)

def draw_part3():
    arcade.set_background_color(arcade.color.DARK_GRAY)
    # Side Control Panel
    arcade.draw_rectangle_filled(20, 240, 40, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(20, 20, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 40, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 60, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 80, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 100, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 120, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 140, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 160, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 180, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 200, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 220, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 240, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 260, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 280, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 300, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 320, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 340, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 360, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 380, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 400, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 420, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 440, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 460, 20, 10, arcade.color.RED)
    # Desk w Computer & Monitor
    arcade.draw_rectangle_filled(220, 60, 360, 120, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 120, 20, 40, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 180, 180, 100, arcade.color.WHITE)
    arcade.draw_rectangle_outline(220, 180, 180, 100, arcade.color.BLACK)
    arcade.draw_rectangle_filled(220, 360, 300, 200, arcade.color.WHITE)
    arcade.draw_rectangle_outline(220, 360, 300, 200, arcade.color.BLACK)
    # Right Side Gray Panel & Outlet
    arcade.draw_rectangle_filled(560, 240, 160, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(460, 240, 40, 480, arcade.color.GREEN)
    arcade.draw_rectangle_filled(440, 240, 10, 480, arcade.color.BLACK)
    arcade.draw_rectangle_filled(560, 140, 20, 20, arcade.color.RED)
    # Monitor Message & Computer Message
    arcade.draw_text("The tractor beam is coupled to the main reactor", 100, 380, arcade.color.GO_GREEN, font_size=10)
    arcade.draw_text("in 7 locations. A power loss at one of them", 120, 360, arcade.color.GO_GREEN, font_size=10)
    arcade.draw_text("will allow the ship to leave the terminals", 128, 340, arcade.color.GO_GREEN, font_size=10)
    arcade.draw_text("Press indicated keys", 170, 175, arcade.color.GO_GREEN, font_size=10)
    # Binders/Handcuffs
    arcade.draw_circle_outline(350, 130, 10, arcade.color.GOLD)
    arcade.draw_circle_outline(336, 130, 10, arcade.color.GOLD)
    arcade.draw_text("S", 365, 140, arcade.color.RED, font_size=10)

def draw_part4():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Select the key to the correct answer", 5, 460, arcade.color.WHITE)
    arcade.draw_text("Answer this movie trivia to obtain the binders: How does", 150, 280, arcade.color.WHITE)
    arcade.draw_text("Luke convince Han to join the rescue mission to save Leia?", 150, 260, arcade.color.WHITE)
    arcade.draw_text("A) Money      B) A New Ship      C) A Droid     D) An R2 Unit", 150, 220, arcade.color.WHITE)
    arcade.draw_text(f"Parts Complete: {complete}", 520, 460, arcade.color.WHITE)
    arcade.draw_text(f"Incorrect Ans: {incorrect}", 520, 440, arcade.color.WHITE)

def draw_game_over():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("GAME OVER", 235, 240, arcade.color.WHITE, font_size=28)
    arcade.draw_text("Press esc to return to start", 256, 220, arcade.color.WHITE, font_size=10)

def draw_part5():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text(f"Parts Complete: {complete}", 520, 460, arcade.color.WHITE)
    arcade.draw_text(f"Incorrect Ans: {incorrect}", 520, 440, arcade.color.WHITE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("You have made it past the first wave of security.", 180, 300, arcade.color.WHITE)
    arcade.draw_text("However, in order to get to the prison cell, you've", 170, 280, arcade.color.WHITE)
    arcade.draw_text("had to shoot down the guards. Consequently, there ", 165, 260, arcade.color.WHITE)
    arcade.draw_text("is now a backup team of Empire Troops storming ", 180, 240, arcade.color.WHITE)
    arcade.draw_text("After you. You must rescue Leia and escape", 185, 220, arcade.color.WHITE)
    arcade.draw_text("Press Enter To Continue", 250, 200, arcade.color.WHITE)

def draw_part6():
    # Counters
    arcade.draw_text(f"Parts Complete: {complete}", 520, 460, arcade.color.WHITE)
    arcade.draw_text(f"Incorrect Ans: {incorrect}", 520, 440, arcade.color.WHITE)
    # Bars
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(160, 240, 30, 480, arcade.color.BLACK)
    arcade.draw_rectangle_filled(320, 240, 30, 480, arcade.color.BLACK)
    arcade.draw_rectangle_filled(480, 240, 30, 480, arcade.color.BLACK)
    # Control Panel
    arcade.draw_rectangle_filled(20, 240, 40, 480, arcade.color.GRAY)
    arcade.draw_rectangle_filled(20, 20, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 40, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 60, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 80, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 100, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 120, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 140, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 160, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 180, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 200, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 220, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 240, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 260, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 280, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 300, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 320, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 340, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 360, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 380, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 400, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 420, 20, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(20, 440, 20, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(20, 460, 20, 10, arcade.color.RED)
    # Side Lines
    arcade.draw_line(40, 240, 640, 240, arcade.color.BLACK)
    # Cell Numbers
    arcade.draw_text("2187", 80, 250, arcade.color.RED, font_size=10)
    arcade.draw_text("A", 85, 270, arcade.color.RED, font_size=10)
    arcade.draw_text("2189", 228, 250, arcade.color.RED, font_size=10)
    arcade.draw_text("B", 233, 270, arcade.color.RED, font_size=10)
    arcade.draw_text("2190", 388, 250, arcade.color.RED, font_size=10)
    arcade.draw_text("C", 393, 270, arcade.color.RED, font_size=10)
    arcade.draw_text("2191", 555, 250, arcade.color.RED, font_size=10)
    arcade.draw_text("D", 558, 270, arcade.color.RED, font_size=10)

def draw_part7():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text(f"Parts Complete: {complete}", 520, 460, arcade.color.WHITE)
    arcade.draw_text(f"Incorrect Ans: {incorrect}", 520, 440, arcade.color.WHITE)
    arcade.draw_text("Good job! You've chosen the correct cell and saved Leia.", 160, 280, arcade.color.WHITE)
    arcade.draw_text("Now all you must do is escape the Death Star. Click the ", 165, 260, arcade.color.WHITE)
    arcade.draw_text("key labelling the correct route of escape, or risk Game Over  ", 150, 240, arcade.color.WHITE)
    arcade.draw_text("Press Enter To Continue", 250, 220, arcade.color.WHITE)

def draw_part8():
    arcade.set_background_color(arcade.color.GRAY)
    # Text
    arcade.draw_text("Garbage Chute", 10, 460, arcade.color.BLACK)
    # Thin Lines
    arcade.draw_line(230, 100, 270, 200, arcade.color.BLACK, line_width=5)
    arcade.draw_line(360, 100, 400, 200, arcade.color.BLACK, line_width=5)
    arcade.draw_line(245, 280, 270, 200, arcade.color.BLACK, line_width=5)
    arcade.draw_line(375, 280, 400, 200, arcade.color.BLACK, line_width=5)
    arcade.draw_line(228, 100, 362, 100, arcade.color.BLACK, line_width=5)
    arcade.draw_line(242, 280, 377, 280, arcade.color.BLACK, line_width=5)
    # Thick Lines
    arcade.draw_line(160, 480, 240, 200, arcade.color.BLACK, line_width=10)
    arcade.draw_line(360, 480, 440, 200, arcade.color.BLACK, line_width=10)
    arcade.draw_line(160, 0, 240, 200, arcade.color.BLACK, line_width=10)
    arcade.draw_line(360, 0, 440, 200, arcade.color.BLACK, line_width=10)
    arcade.draw_line(0, 200, 640, 200, arcade.color.BLACK, line_width=10)
    arcade.draw_line(200, 100, 240, 200, arcade.color.BLACK, line_width=10)
    arcade.draw_line(200, 100, 240, 200, arcade.color.BLACK, line_width=5)
    arcade.draw_line(0, 360, 640, 360, arcade.color.BLACK)
    arcade.draw_line(0, 80, 640, 80, arcade.color.BLACK)
    arcade.draw_circle_filled(440, 110, 10, arcade.color.RED)
    arcade.draw_circle_outline(440, 110, 10, arcade.color.BLACK)
    arcade.draw_text("Press P to press", 460, 120, arcade.color.BLACK)

def draw_part9():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text(f"Parts Complete: {complete}", 520, 460, arcade.color.WHITE)
    arcade.draw_text(f"Incorrect Ans: {incorrect}", 520, 440, arcade.color.WHITE)
    arcade.draw_text("Select the key to the correct answer", 5, 460, arcade.color.WHITE)
    arcade.draw_text("After the garbage chute leads the team into a deadly ", 150, 280, arcade.color.WHITE)
    arcade.draw_text("trash compactor, who saves them from their demise?", 150, 260, arcade.color.WHITE)
    arcade.draw_text("A) Qui-Gon      B) Vader      C) C3PO     D) R2D2", 168, 220, arcade.color.WHITE)

def draw_done():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("GOOD JOB!", 260, 240, arcade.color.WHITE, font_size=20)
    arcade.draw_text("you've completed the chapter", 245, 220, arcade.color.WHITE, font_size=10)

def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "start":
        start_keybinds(key, modifiers)
    if current_screen == "room_one":
        room_one_keybinds(key, modifiers)
    if current_screen == "part1":
        part1_keybinds(key, modifiers)
    if current_screen == "part2":
        part2_keybinds(key, modifiers)
    if current_screen == "part3":
        part3_keybinds(key, modifiers)
    if current_screen == "part4":
        part4_keybinds(key, modifiers)
    if current_screen == "game_over":
        game_over_keybinds(key, modifiers)
    if current_screen == "part5":
        part5_keybinds(key, modifiers)
    if current_screen == "part6":
        part6_keybinds(key, modifiers)
    if current_screen == "part7":
        part7_keybinds(key, modifiers)
    if current_screen == "part8":
        part8_keybinds(key, modifiers)
    if current_screen == "part9":
        part9_keybinds(key, modifiers)

def start_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "room_one"

def room_one_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen == "start"
    if key == arcade.key.P:
        current_screen = "part1"

def part1_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "part2"

def part2_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "part3"

def part3_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.S:
        current_screen = "part4"

def part4_keybinds(key, modifiers):
    global current_screen, complete, incorrect
    if key == arcade.key.A:
        complete += 1
        current_screen = "part5"
    elif key == arcade.key.B:
        incorrect += 1
    elif key == arcade.key.C:
        incorrect += 1
    elif key == arcade.key.D:
        incorrect += 1
    else:
        pass

def game_over_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "start"

def part5_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "part6"

def part6_keybinds(key, modifiers):
    global current_screen, complete, incorrect
    if key == arcade.key.A:
        complete += 1
        current_screen = "part7"
    elif key == arcade.key.B:
        incorrect += 1
    elif key == arcade.key.C:
        incorrect += 1
    elif key == arcade.key.D:
        incorrect += 1
    else:
        pass

def part7_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "part8"

def part8_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.P:
        current_screen = "part9"

def part9_keybinds(key, modifiers):
    global current_screen, complete, incorrect
    if key == arcade.key.A:
        incorrect += 1
    elif key == arcade.key.B:
        incorrect += 1
    elif key == arcade.key.C:
        incorrect += 1
    elif key == arcade.key.D:
        current_screen = "done"
    else:
        pass

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()


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
