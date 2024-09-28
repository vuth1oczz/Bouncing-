import pygame
import numpy
import random
import math
WIDTH = 500                                                                                      # Kích thước screen
HEIGH = 500
CENTER_CIRCLE = numpy.array([WIDTH/2, HEIGH/2], dtype = numpy.float64)                           # Vị trí Vòng tròn lớn
RADIUS = 120                                                                                     # Bán kính vòng tròn lớn
CIRCLE_THICKNESS = 3                                                                             # Độ dày 
COLOR_CIRCLE = "white"
GRAVITY = 0.2                                                                                    # Gia tốc rơi
RADIUS_NEW = 150                                                                                
SCREEN = pygame.display.set_mode((WIDTH,HEIGH))
START_ANGLE = math.radians(-30)                                                                  # Góc quay
END_ANGLE = math.radians(30)
SPINNING_SPEED = 0.01                                                                            # Tốc độ quay 
def dis(x,y):
    return  math.sqrt((x[0]-y[0])**2 + (x[1] - y[1])**2)
class ball:
    def __init__(self, color,  position, velocity):                                              # Khởi tạo
        self.radius = 5
        self.position = numpy.array(position, dtype = numpy.float64)
        self.velocity = numpy.array(velocity, dtype = numpy.float64)
        self.color = color
        self.is_in = True
        self.cham_tuong = False
    def draw(self):                                                                              # Vẽ bóng trên screen
        pygame.draw.circle(SCREEN, self.color, self.position, self.radius)
    def free_fall(self):                                                                         # Bóng rơi tự do 
            self.velocity[1] += GRAVITY
            self.position += self.velocity
    def bouncing(self):                                                                          # Bóng nẩy, thay đổi hướng
        if dis(self.position, CENTER_CIRCLE) + self.radius > RADIUS:
                d = self.position - CENTER_CIRCLE
                d_unit = d/ math.sqrt(numpy.dot(d,d))
                t = numpy.array([-d[1], d[0]], dtype = numpy.float64)
                proj_v_t = (numpy.dot(self.velocity, t) / numpy.dot(t,t)) *t
                self.velocity = 2 * proj_v_t - self.velocity
                self.position = d_unit *(dis(self.position, CENTER_CIRCLE) - self.radius) + CENTER_CIRCLE
                self.position -= t*SPINNING_SPEED
                return self.velocity
        
    def is_outside(self):                                                                        # Kiểm tra bóng có ở ngoài Vòng tròn lớn hay không
        if dis(self.position, CENTER_CIRCLE) + self.radius > RADIUS :
            return True
        else:
            return False
    def ball_in_arc(self,CENTER_CIRCLE , start_angle, end_angle):
        dx = self.position[0] - CENTER_CIRCLE[0]
        dy = self.position[1] - CENTER_CIRCLE[1]
        anpha = math.atan2(dy,dx)
        start_angle = start_angle %(2* math.pi)
        end_angle = end_angle %(2* math.pi)
        if start_angle > end_angle:
            end_angle += 2* math.pi
        if start_angle <= anpha <= end_angle or(start_angle <= anpha + 2*math.pi <= end_angle):
            return True
        else:
            return False
    def ball_Thusday(self):
         if dis(self.position, CENTER_CIRCLE) + self.radius == RADIUS:
              self.cham_tuong = True
              return self.cham_tuong 
         else:
              return self.cham_tuong
         
def draw_arc(screen, center, radius, start_angle, end_angle):
    p1 = center + radius* numpy.array([math.cos(start_angle), math.sin(start_angle)], dtype = numpy.float64)
    p2 = center + radius* numpy.array([math.cos(end_angle), math.sin(end_angle)], dtype= numpy.float64)
    pygame.draw.polygon(screen, "black", [center, p1,p2], 0)

     





    


