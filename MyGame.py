import arcade

PLAYER_SCALING = 0.5
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = None

    def setup(self):
        self.background = arcade.load_texture("бг.png")
        self.player_sprite = arcade.Sprite("pixil-frame-0.png",
                                           PLAYER_SCALING)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50


    def on_draw(self):
        arcade.start_render()


    def on_key_press(self, key, modifiers):
            MOVEMENT_SPEED = 5

            if key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
                self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.player_sprite.change_x = 0
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT,"Drawing Example")
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()