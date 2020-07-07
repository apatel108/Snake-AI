import arcade

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 380
SCREEN_TITLE = "Snake Game"
MOVEMENT_SPEED = 10
BODY_SIZE = 15
BODY_COLOR = arcade.color.WHITE

class Cell:

    def __init__(self, x, y, prevPos):
        self.x = x
        self.y = y
        self.prevPos = prevPos

class Snake:
    body = []

    def __init__(self):
        self.direction = [0, 0]
        self.head = Cell(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, [0,0])
        self.body += [self.head]

    def draw(self):
        for i, cell in enumerate(self.body):
            arcade.draw_rectangle_filled(cell.x, cell.y, BODY_SIZE, BODY_SIZE, BODY_COLOR)

    def update(self):

        for i, cell in enumerate(self.body):
            if i == 0:
                cell.prevPos = [cell.x, cell.y]
                self.head.x += self.direction[0] * MOVEMENT_SPEED
                self.head.y += self.direction[1] * MOVEMENT_SPEED
                continue
            cell.prevPos = [cell.x, cell.y]
            cell.x = self.body[i - 1].prevPos[0] - BODY_SIZE * self.direction[0]
            cell.y = self.body[i - 1].prevPos[1] - BODY_SIZE * self.direction[1]

        if self.head.x < BODY_SIZE:
            self.head.x = BODY_SIZE

        if self.head.x > SCREEN_WIDTH - BODY_SIZE:
            self.head.x = SCREEN_WIDTH - BODY_SIZE

        if self.head.y < BODY_SIZE:
            self.head.y = BODY_SIZE

        if self.head.y > SCREEN_HEIGHT - BODY_SIZE:
            self.head.y = SCREEN_HEIGHT - BODY_SIZE


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        self.snake = Snake()

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()

    def update(self, delta_time):
        self.snake.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and self.snake.direction != [1, 0]:
            self.snake.direction = [-1, 0]
        elif key == arcade.key.RIGHT and self.snake.direction != [-1, 0]:
            self.snake.direction = [1, 0]
        elif key == arcade.key.UP and self.snake.direction != [0, -1]:
            self.snake.direction = [0, 1]
        elif key == arcade.key.DOWN and self.snake.direction != [0, 1]:
            self.snake.direction = [0, -1]
        elif key == arcade.key.SPACE:
            self.snake.body += [Cell(self.snake.head.prevPos[0],self.snake.head.prevPos[1], [0,0])]


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()