from loc import *
clock = pygame.time.Clock()
running = True
ball1 = ball((random.randint(0,255),random.randint(0,255),random.randint(0,255)), (250,150), (random.random(),random.random()))
BALLS = [ball1]
one_ball_out_side = False
while running:
    ball_append = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                random_color_ball = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                BALLS.append(ball(random_color_ball, (250,150), (random.randrange(-1,1), random.randrange(-1,1))))
    START_ANGLE += SPINNING_SPEED
    END_ANGLE += SPINNING_SPEED
    for balls in BALLS:
        balls.free_fall()
        if balls.ball_in_arc(CENTER_CIRCLE, START_ANGLE, END_ANGLE) and balls.is_outside() == True:
            one_ball_out_side = True
            balls.is_in = False
        if balls.is_in == True:
            balls.bouncing()
    SCREEN.fill("BLACK")
    pygame.draw.circle(SCREEN,COLOR_CIRCLE,CENTER_CIRCLE,RADIUS ,CIRCLE_THICKNESS)
    draw_arc(SCREEN, CENTER_CIRCLE, RADIUS_NEW,START_ANGLE, END_ANGLE)
    for balls in BALLS:
        balls.draw()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()