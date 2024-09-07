import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Частота кадров
FPS = 10
clock = pygame.time.Clock()

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 36)

# Функция для отображения текста на экране
def draw_text(screen, text, position, color):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, position)

# Определение координат еды
def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        food_position = (x, y)
        if food_position not in snake:  # Еда не должна появляться на теле змейки
            return food_position

# Функция для отрисовки змейки
def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Основная функция игры
def main():
    # Инициализация змейки
    snake = [(100, 100), (80, 100), (60, 100)]  # Начальная длина змейки
    direction = (CELL_SIZE, 0)  # Направление движения вправо
    food = generate_food(snake)  # Изначальное местоположение еды
    score = 0

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # Обновление позиции змейки
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Проверка на столкновение с границами
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            break  # Конец игры, если змейка вышла за пределы поля

        # Проверка на самопересечение
        if new_head in snake:
            break  # Конец игры при самопересечении

        snake.insert(0, new_head)  # Добавление новой головы змейки

        # Проверка на съедение еды
        if new_head == food:
            food = generate_food(snake)  # Генерация новой еды
            score += 1
        else:
            snake.pop()  # Удаление последнего сегмента, если еда не съедена

        # Отрисовка всего на экране
        screen.fill(BLACK)
        draw_snake(screen, snake)
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

        # Отображение счета
        draw_text(screen, f'Score: {score}', (10, 10), WHITE)

        # Обновление экрана
        pygame.display.flip()

        # Контроль скорости змейки
        clock.tick(FPS)

    # Конечный экран
    screen.fill(BLACK)
    draw_text(screen, f'Game Over! Your score: {score}', (WIDTH // 4, HEIGHT // 2), WHITE)
    pygame.display.flip()
    pygame.time.wait(3000)  # Ожидание перед закрытием

if __name__ == '__main__':
    main()
