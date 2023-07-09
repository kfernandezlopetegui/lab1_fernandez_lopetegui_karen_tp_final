import pygame
from constantes import *
from auxiliar import Auxiliar


class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale=1, interval_time_jump=100) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''
        self.position = pygame.Vector2(x, y)
        self.nombre = "player"
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Idle ({0}).png", 1, 10, flip=False, scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Idle ({0}).png", 1, 10, flip=True, scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Jump ({0}).png", 1, 10, flip=False, scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Jump ({0}).png", 1, 10, flip=True, scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Run ({0}).png", 1, 8, flip=False, scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Run ({0}).png", 1, 8, flip=True, scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Shoot ({0}).png", 1, 4, flip=False, scale=p_scale, repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Shoot ({0}).png", 1, 4, flip=True, scale=p_scale, repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Melee ({0}).png", 1, 8, flip=False, scale=p_scale, repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Melee ({0}).png", 1, 8, flip=True, scale=p_scale, repeat_frame=1)
        self.death_r = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Dead ({0}).png", 1, 10, scale=p_scale)
        self.death_l = Auxiliar.getSurfaceFromSeparateFiles(
            "images/caracters/players/robot/Dead ({0}).png", 1, 10, flip=True, scale=p_scale)

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(
            x+self.rect.width/3, y, self.rect.width/3, self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0  # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.can_shoot = True
        self.last_shoot_time = None
        self.shoot_delay = 300

        self.contador_daño_recibido = 0

        self.platform = None

        self.is_stay = True

        self.is_death = False
        
        self.animacion_muerte_completada = False

    def walk(self, direction):

        if (self.is_jump == False and self.is_fall == False):
            if (self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if (direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def do_death(self):
        if self.direction == DIRECTION_R:
            self.animation = self.death_r
        else:
            self.animation = self.death_l

    def shoot(self, on_off=True):
        self.is_shoot = on_off
        if (on_off == True and self.is_jump == False and self.is_fall == False):

            if (self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if (self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l

    def receive_shoot(self):
        self.receive_damage(7)

    def receive_damage(self, damage):
        self.contador_daño_recibido += damage
        if self.contador_daño_recibido > 20:

            self.lives -= 1
            self.contador_daño_recibido = 0

    def knife(self, on_off=True):
        self.is_knife = on_off
        if (on_off == True and self.is_jump == False and self.is_fall == False):
            if (self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if (self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l

    def jump(self, on_off=True):

        if (on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if (self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if (on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if (self.is_knife or self.is_shoot):
            return

        if (self.animation != self.stay_r and self.animation != self.stay_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            self.is_stay = True

    def change_x(self, delta_x):
        if self.rect.x < 1 and delta_x < 0:
            self.rect.x == 0
        elif self.rect.x > 1123 and delta_x > 0:
            self.rect.x == 1122
        else:

            self.rect.x += delta_x
            self.collition_rect.x += delta_x
            self.ground_collition_rect.x += delta_x

    def change_y(self, delta_y):

        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if (self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            if self.lives < 1:
                self.do_death()

            if (abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if (not self.is_on_plataform(plataform_list)):
                if (self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)

            else:
                if (self.is_jump):
                    self.jump(False)
                self.is_fall = False
                if self.platform is not None and self.is_stay == True and self.platform.move:
                    self.change_x(self.platform.move_x)

    def is_on_plataform(self, plataform_list):
        retorno = False

        if (self.ground_collition_rect.bottom >= GROUND_LEVEL):
            self.platform = None
            retorno = True
        else:
            for plataforma in plataform_list:
                if (self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    self.platform = plataforma
                    retorno = True
                    break
        return retorno

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if self.animation == self.death_l or  self.animation== self.death_r:
                if not self.animacion_muerte_completada:
          
                    self.frame += 1
                    if self.frame >= len(self.animation):
                        self.frame = len(self.animation) - 1  # Muestra el último fotograma
                        self.animacion_muerte_completada = True
                else:
                    
                        self.is_death = True        
            else:
                        
                if (self.frame < len(self.animation) - 1):
                    self.frame += 1
                    # print(self.frame)
                else:
                    
                    self.frame = 0
        self.image = self.animation[self.frame]

    def update(self, delta_ms, plataform_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def draw(self, screen, offset=None):

        if (DEBUG):
            pygame.draw.rect(screen, color=(255, 0, 0),
                             rect=self.collition_rect)
            pygame.draw.rect(screen, color=(255, 255, 0),
                             rect=self.ground_collition_rect)

        x = self.rect.x
        y = self.rect.y
        print("x={}".format(x))

        screen.blit(self.image, (x, y))

    def events(self, delta_ms, keys):
        self.tiempo_transcurrido += delta_ms

        if self.lives > 0:
            if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_L)

            if (not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_R)

            if (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.stay()
            if (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.stay()

            if (keys[pygame.K_SPACE]):
                if ((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                    self.jump(True)
                    self.tiempo_last_jump = self.tiempo_transcurrido

            if (not keys[pygame.K_a]):
                self.shoot(False)

            if (not keys[pygame.K_a]):
                self.knife(False)

            if (keys[pygame.K_s] and not keys[pygame.K_a]):
                self.shoot()

            if (keys[pygame.K_a] and not keys[pygame.K_s]):
                self.knife()
        else:
            self.do_death()
