import argparse
import math
import pdb
import random

MIN = 300
MAX = 800
PI = 3.14


class Map():

    def __init__(self):
        random.seed()
        self.x = random.randint(MIN, MAX)
        self.y = random.randint(MIN, MAX)
        self.area = self.x * self.y


class Lake():

    def __init__(self, maps):
        self.radius = round(min([maps.x, maps.y]) / random.randint(5, 10))
        x_min = self.radius
        y_min = self.radius
        x_max = maps.x - (self.radius * 2)
        y_max = maps.y - (self.radius * 2)
        print(f'x min/max: {x_min} - {x_max}')
        print(f'y min/max: {y_min} - {y_max}')
        self.center_x = round(random.randint(x_min, x_max))
        self.center_y = round(random.randint(y_min, y_max))
        self.area = round(PI * self.radius * self.radius)

    def center(self):
        return self.center_x, self.center_y

    def is_inside(self, x, y):
        diff = pow((x - self.center_x), 2) + pow((y - self.center_y), 2)
        return diff <= pow(self.radius, 2)


def fire(maps):
    x = random.randint(0, maps.x)
    y = random.randint(0, maps.y)
    return x, y


def percentage(part, whole):
    return round(100 * part / whole)


def compute(args, maps):
    print("---------------------------")
    lake = Lake(maps)
    
    fires = []
    touched = 0
    untouched = 0
    for el in range(args.fires):
        x, y = fire(maps)
        strike = lake.is_inside(x, y)
        if strike:
            touched += 1
        else:
            untouched += 1
        fires.append((x, y, strike))
    
    estimated_lake_are = maps.area * touched / args.fires
    print(f"size of the map = {maps.x} x {maps.y}")
    print(f"map area = {maps.area}")
    print(f"lake center position = {lake.center()}")
    print(f"lake radius = {lake.radius}")
    print(f"lake area = {lake.area}")
    print(f"lake area percentage of the map= {percentage(lake.area, maps.area)}%")
    print(f"touched: {touched} - {percentage(touched, args.fires)}%")
    print(f"untouched: {untouched} - {percentage(untouched, args.fires)}%")
    print(f"estimated lake area = {estimated_lake_are}")
    return lake, fires


def render():
    parser = argparse.ArgumentParser()
    parser.add_argument("fires", type=int, help="number of bullets to fire")
    args = parser.parse_args()
    maps = Map()
    lake, fires = compute(args, maps)
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((maps.x, maps.y))
    clock = pygame.time.Clock()
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("green")
        # RENDER YOUR GAME HERE
        pygame.draw.circle(screen, "blue", (lake.center_x, lake.center_y), lake.radius)
        for el in fires:
            color = "black"
            if el[2]:
                color = "red"
            pygame.draw.circle(screen, color, (el[0], el[1]), 2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            lake, fires = compute(args, maps)
        # flip() the display to put you work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


def main():
    render()


if __name__ == "__main__":
    main()
