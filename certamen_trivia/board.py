import quote
import theme
import visual
import image
import player
import connections
import player_box

import generate_questions

from PIL import Image
import numpy as np
import cv2
import pygame

import random

SCALAR = 1
# WUDTH = 3240
WIDTH = 1512 * SCALAR

# HEIGHT = 1950
HEIGHT = 910 * SCALAR



TOP_LEFT = (round(WIDTH/31.5), round(HEIGHT/8.0531))
# TOP_LEFT = (48, 113)
BOX_HEIGHT = 129 * SCALAR
BOX_WIDTH = 236 * SCALAR



QUOTE_COLS = 2
THEME_COLS = 2
CONNECTIONS_COLS = 1
VISUAL_COLS = 1
OTHER_COLS = 0

class Board:
    def __init__(self):
        pygame.init()
        # pygame.mixer.init()

        self.quote_questions = []
        self.theme_questions = []
        self.connection_questions = []
        self.visual_questions = []

        self.state = "ask"

        self.all_questions = []
        self.locations = []
        self.p1 = player.Player("p1", "blue")
        self.p2 = player.Player("p2", "green")
        self.p3 = player.Player("p3", "red")
        self.previous_questions = []



# quote1 = quote.Quote("q1", "quote", 100, )

    def retrieve_questions(self):
        # UNCOMMENT TO CREATE NEW QUESTIONS
        # generate_questions.doShit()

        file = open("questions.txt", "r")
        while True:
            q1 = file.readline()
            print("\n-----\n")
            if q1 == "":
                print("Exiting!")
                break
            q1 = q1.split(',')
            print(q1[0])

            if q1[0] == "quote":
                print("GOT HERE")
                quote1 = quote.Quote(q1[1], q1[2], int(q1[3]))
                self.quote_questions.append([])
                self.quote_questions[-1].append(quote1)
                self.all_questions.append(quote1)
                for q in range(4):
                    temp_q = file.readline()
                    temp_q = temp_q.split(',')
                    temp_quote = quote.Quote(temp_q[1], temp_q[2], int(temp_q[3]))
                    self.quote_questions[-1].append(temp_quote)
                    self.all_questions.append(temp_quote)


            if q1[0] == "theme":
                print("GOT THeme")

                theme1 = theme.Theme(q1[1], q1[2], int(q1[3]))
                self.theme_questions.append([])
                self.theme_questions[-1].append(theme1)
                self.all_questions.append(theme1)
                for q in range(4):
                    temp_q = file.readline()
                    temp_q = temp_q.split(',')
                    temp_theme = theme.Theme(temp_q[1], temp_q[2], int(temp_q[3]))
                    self.theme_questions[-1].append(temp_theme)
                    self.all_questions.append(temp_theme)


            if q1[0] == "visual":
                print("GOT Visual")

                visual1 = visual.Visual(q1[1], q1[2], int(q1[3]))
                self.visual_questions.append([])
                self.visual_questions[-1].append(visual1)
                self.all_questions.append(visual1)

                for q in range(4):
                    temp_q = file.readline()
                    temp_q = temp_q.split(',')
                    temp_visual = visual.Visual(temp_q[1], temp_q[2], int(temp_q[3]))
                    self.visual_questions[-1].append(temp_visual)
                    self.all_questions.append(temp_visual)

            if q1[0] == "connection":
                print("GOT Connection")

                connection1 = connections.Connection(q1[1], q1[2], q1[3], q1[4], q1[5], int(q1[6]))
                self.connection_questions.append([])
                self.connection_questions[-1].append(connection1)
                self.all_questions.append(connection1)

                for q in range(4):
                    temp_q = file.readline()
                    temp_q = temp_q.split(',')
                    temp_connection = connections.Connection(temp_q[1], temp_q[2], temp_q[3], temp_q[4], temp_q[5], int(temp_q[6]))
                    self.connection_questions[-1].append(temp_connection)
                    self.all_questions.append(temp_connection)

        top_left = (TOP_LEFT[0], TOP_LEFT[1])

        self.all_questions.insert(0, player_box.Player_box(1, "sub"))
        self.all_questions.insert(6, player_box.Player_box(1, "add"))
        self.all_questions.insert(12, player_box.Player_box(2, "sub"))
        self.all_questions.insert(18, player_box.Player_box(2, "add"))
        self.all_questions.insert(24, player_box.Player_box(3, "sub"))
        self.all_questions.insert(30, player_box.Player_box(3, "add"))

        for x in range(6):
            for y in range(6):
                self.locations.append((top_left[0] + BOX_WIDTH * x, top_left[1] + BOX_HEIGHT * y))

        




    def find_hovering_over(self, x, y):
        x_idx = -1
        y_idx = -1
        for i in range(6):
            if self.locations[i*6][0] < x :
                x_idx = i*6

        for i in range(6):
            if self.locations[i][1] < y:
                y_idx = i

        if x > BOX_WIDTH * 6 + TOP_LEFT[0] or  y > BOX_HEIGHT * 6 + TOP_LEFT[1]:
            x_idx = -1
            y_idx = -1

        if x_idx != -1 and y_idx != -1:
            return x_idx + y_idx
        return -1
            
            
    def wait(self, question):
        print("waiting...")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("leaving waiting")
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("leaving waiting")
                        return
                    if event.key == pygame.K_q:
                        print("leaving waiting")
                        return
                    self.handle_score(question, event)


 


    def handle_score(self, question, event):
        # print(type(event))
        if event.key == pygame.K_1:
            self.p1.score += question.value
            pygame.display.flip()
            return True
        if event.key == pygame.K_4:
            self.p1.score -= question.value
            pygame.display.flip()
            return False
        
        if event.key == pygame.K_2:
            self.p2.score += question.value
            pygame.display.flip()
            return True
        if event.key == pygame.K_5:
            self.p2.score -= question.value
            pygame.display.flip()
            return False        
        if event.key == pygame.K_3:
            self.p3.score += question.value
            pygame.display.flip()
            return True
        if event.key == pygame.K_6:
            self.p3.score -= question.value
            pygame.display.flip()
            return False        
        return False

    def display_answer(self, screen, question):
        middle = (round(WIDTH/2), round(HEIGHT/2 - h/2))
        border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-w/32,top_left[1]-h/32, round(w+w/16), round(h+h/16)))

            



    def display_connection(self, screen, top_left, img):
        
        im = Image.open("images_and_themes/" + str(img))
        # im.thumbnail((round(WIDTH/2.55), round(HEIGHT/2.55)))
        # w, h = im.size
      # Calculate the aspect ratio
        aspect_ratio = im.width / im.height

        # Set the new width
        new_width = round(HEIGHT/2.55)
        # Calculate the new height to maintain aspect ratio
        new_height = int(new_width / aspect_ratio)

        if new_height > round(HEIGHT/2.55):
            new_height = round(HEIGHT/2.55)
            new_width = int(new_height * aspect_ratio)


        # Resize the image
        im = im.resize((new_width, new_height))
        w, h = im.size










        border_rect_1 = pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(top_left[0]-w/32,top_left[1]-h/32, round(w+w/16), round(h+h/16)))
        sample_rect_1 = pygame.draw.rect(screen, (90, 90, 90), pygame.Rect(top_left[0],top_left[1], w, h))

        im.save("temp.png")
        this_image = pygame.image.load("temp.png")
        screen.blit(this_image, (top_left[0], top_left[1]))

        pygame.display.flip()





    def play_connections(self, connections, screen):
        im = Image.open("images_and_themes/gandalf.png")
        im.thumbnail((round(WIDTH/2.55), round(HEIGHT/2.55)))
        w, h = im.size
        top_left_1 = (round(WIDTH/4 + WIDTH/150), round(HEIGHT/4 - h/3.75))
        top_left_2 = (round(WIDTH/2)+round(w/32), round(HEIGHT/4 - h/3.75))
        top_left_3 = (round(WIDTH/4 + WIDTH/150), round(HEIGHT/2)+round(w/6))
        top_left_4 = (round(WIDTH/2)+round(w/32), round(HEIGHT/2)+round(w/6))

        top_left_pos = [top_left_1, top_left_2, top_left_3, top_left_4]

        photos = [connections.s1, connections.s2, connections.s3, connections.s4]
        
        # top_left = (round(WIDTH/2 - w/2), round(HEIGHT/2 - h/2))

        # border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-30,top_left[1]-30, round(w+w/16), round(h+h/16)))
        # sample_rect = pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(top_left[0],top_left[1], w, h))

        # im = pygame.image.load("images_and_themes/sound.png").convert()
        # screen.blit(im, top_left)

        
        # music = pygame.mixer.music.load("images_and_themes/" + str(theme.theme))
        # pygame.mixer.music.set_endevent(SONG_END)
        # pygame.mixer.music.play()
        # pygame.mixer.music.pause()

        play = True
        photo_num = 0
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if connections not in self.previous_questions:
                        self.previous_questions.append(connections)
                    return
                if event.type == pygame.KEYDOWN:
                    print(type(event))
                    if event.key == pygame.K_SPACE:
                        if photo_num == 4:
                            if connections not in self.previous_questions:
                                self.previous_questions.append(connections)
                            return
                        self.display_connection(screen, top_left_pos[photo_num], photos[photo_num])
                        photo_num += 1
                    
                    if event.key == pygame.K_q:
                        if connections not in self.previous_questions:
                            self.previous_questions.append(connections)
                        return
                    
                    
                    # if event.key == pygame.K_RIGHT:
                    #     speed *= 2
                    # if event.key == pygame.K_LEFT:
                    #     speed /= 2           


                    self.handle_score(quote, event)
                    self.display_points(screen)


    def play_theme(self, theme, screen):

        pygame.mixer.music.load("images_and_themes/" + theme.theme)
        im = Image.open("images_and_themes/sound.png")
        im.thumbnail((round(WIDTH/3 * 2), round(HEIGHT/3 * 2)))
        w, h = im.size

        top_left = (round(WIDTH/2 - w/2), round(HEIGHT/2 - h/2))
        border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-w/32,top_left[1]-h/32, round(w+w/16), round(h+h/16)))
        sample_rect = pygame.draw.rect(screen, (90, 90, 90), pygame.Rect(top_left[0],top_left[1], w, h))

        im.save("temp.png")

        this_image = pygame.image.load("temp.png")
        screen.blit(this_image, (top_left[0], top_left[1]))

        
        # top_left = (round(WIDTH/2 - w/2), round(HEIGHT/2 - h/2))

        # border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-30,top_left[1]-30, round(w+w/16), round(h+h/16)))
        # sample_rect = pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(top_left[0],top_left[1], w, h))

        # im = pygame.image.load("images_and_themes/sound.png").convert()
        # screen.blit(im, top_left)

        pygame.display.flip()
        self.wait(theme)
        
        # music = pygame.mixer.music.load("images_and_themes/" + str(theme.theme))
        # pygame.mixer.music.set_endevent(SONG_END)
        # pygame.mixer.music.play()
        # pygame.mixer.music.pause()

        play = True
        pygame.mixer.music.play()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if theme not in self.previous_questions:
                        self.previous_questions.append(theme)
                    pygame.mixer.music.pause()
                    return
                if event.type == pygame.KEYDOWN:
                    print(type(event))
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.pause()
                        self.wait(theme)
                        pygame.mixer.music.unpause()

                    
                    if event.key == pygame.K_q:
                        if theme not in self.previous_questions:
                            self.previous_questions.append(theme)
                        pygame.mixer.music.pause()                       
                        return
                    
                    if event.key == pygame.K_r:
                        pygame.mixer.music.rewind()

                    
                    # if event.key == pygame.K_RIGHT:
                    #     speed *= 2
                    # if event.key == pygame.K_LEFT:
                    #     speed /= 2                    
                    self.handle_score(theme, event)
                    self.display_points(screen)
            




       

    def play_quote(self, quote, screen):

        im = Image.open("images_and_themes/gandalf.png")
        im.thumbnail((round(WIDTH/3 * 2), round(HEIGHT/3 * 2)))
        w, h = im.size

        top_left = (round(WIDTH/2 - w/2), round(HEIGHT/2 - h/2))
        border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-w/32,top_left[1]-h/32, round(w+w/16), round(h+h/16)))
        sample_rect = pygame.draw.rect(screen, (90, 90, 90), pygame.Rect(top_left[0],top_left[1], w, h))

        im.save("temp.png")

        this_image = pygame.image.load("temp.png")
        screen.blit(this_image, (top_left[0], top_left[1]))





        
        # top_left = (round(WIDTH/2 - w/2), round(HEIGHT/2 - h/2))

        # border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-30,top_left[1]-30, round(w+w/16), round(h+h/16)))
        # sample_rect = pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(top_left[0],top_left[1], w, h))

        # im = pygame.image.load("images_and_themes/sound.png").convert()
        # screen.blit(im, top_left)

        pygame.display.flip()
        
        # music = pygame.mixer.music.load("images_and_themes/" + str(theme.theme))
        # pygame.mixer.music.set_endevent(SONG_END)
        # pygame.mixer.music.play()
        # pygame.mixer.music.pause()

        play = True
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if quote not in self.previous_questions:
                        self.previous_questions.append(quote)
                    return
                if event.type == pygame.KEYDOWN:
                    print(type(event))
                    if event.key == pygame.K_SPACE:
                        pass
                    
                    if event.key == pygame.K_q:
                        if quote not in self.previous_questions:
                            self.previous_questions.append(quote)
                        return
                    
                    
                    # if event.key == pygame.K_RIGHT:
                    #     speed *= 2
                    # if event.key == pygame.K_LEFT:
                    #     speed /= 2                    
                    self.handle_score(quote, event)
                    self.display_points(screen)

            





    def play_visual(self, visual, screen):
        play = True

        im = Image.open("images_and_themes/" + str(visual.visual))
        # im.thumbnail((round(WIDTH/3 * 2), round(HEIGHT/3 * 2)))
        # w, h = im.size


        # Calculate the aspect ratio
        aspect_ratio = im.width / im.height

        # Set the new width
        new_width = round(HEIGHT/3 * 2)
        # Calculate the new height to maintain aspect ratio
        new_height = int(new_width / aspect_ratio)

        if new_height > round(HEIGHT/3 * 2):
            new_height = round(HEIGHT/3 * 2)
            new_width = int(new_height * aspect_ratio)


        # Resize the image
        im = im.resize((new_width, new_height))
        w, h = im.size


        # arr = np.array([[[0 for u in range(3)] for j in range(w)] for i in range(h)], dtype=np.uint8)

        index_arr = []

        for i in range(w):
            for j in range(h):
                index_arr.append([i, j])

        random.shuffle(index_arr)

        idx = 0

        top_left = (round(WIDTH/2 - w/2), round(HEIGHT/2 - h/2))
        print("width:", w)
        print("height:", h)

        border_rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(top_left[0]-w/32,top_left[1]-h/32, round(w+w/16), round(h+h/16)))
        sample_rect = pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(top_left[0],top_left[1], w, h))
        pygame.display.flip()

        pixels = list(im.getdata())

        # og_img_matrix = cv2.imread(visual.visual, 1)
        # og_img_matrix = og_img_matrix[...,::-1] 
        data = np.asarray(im)
        # data = np.rot90(data)
        # data = np.rot90(data)
        data = np.rot90(data)
        data = np.flipud(data)

        # file = open("error.txt", "w")
        # file.write(str(data))
        # file.close()

        print(len(data))
        print(len(data[0]))

        print(len(index_arr))


        # self.wait()


        speed = 1

        while play:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if visual not in self.previous_questions:
                        self.previous_questions.append(visual)
                    return
                if event.type == pygame.KEYDOWN:
                    print(type(event))
                    if event.key == pygame.K_SPACE:
                        self.wait(visual)
                    
                    if event.key == pygame.K_q:
                        if visual not in self.previous_questions:
                            self.previous_questions.append(visual)
                        return
                    
                    if event.key == pygame.K_RIGHT:
                        speed *= 2
                        speed = min(30000, speed)
                    if event.key == pygame.K_LEFT:
                        speed /= 2                
                        speed = max(speed, 1)    
                    self.handle_score(visual, event)
                    self.display_points(screen)

            # print("idx:", idx)
            # print("index_arr[idx]:", index_arr[idx])


            color = (data[index_arr[idx][0]][index_arr[idx][1]][0], data[index_arr[idx][0]][index_arr[idx][1]][1], data[index_arr[idx][0]][index_arr[idx][1]][2])
            screen.fill(color, ((top_left[0]+index_arr[idx][0], top_left[1]+index_arr[idx][1]), (1, 1)))
            if(idx>len(index_arr)-3):
                if visual not in self.previous_questions:
                    self.previous_questions.append(visual)
                play = False
            idx += 1
                    

            # self.draw_board(screen, background_img, border_img)
            if(idx%round(speed) == 0):
                pygame.display.flip()       


        pygame.display.flip()       
        self.wait(visual)




    def erase_past_boxes(self, screen):
        for i in range(len(self.previous_questions)):
            square_idx = self.all_questions.index(self.previous_questions[i])
            pygame.draw.rect(screen, (20, 0, 80), pygame.Rect(self.locations[square_idx][0], self.locations[square_idx][1], BOX_WIDTH, BOX_HEIGHT))


    def background(self, screen, background_img, border_img):
        blue = (0, 0, 255)
        screen.fill(blue)
        screen.blit(background_img, (0,0))



        self.draw_question_box(screen, "", TOP_LEFT[0], TOP_LEFT[1], False)
        self.erase_past_boxes(screen)
        self.hover(screen)
        self.display_points(screen)
        self.display_catagories(screen)
        screen.blit(border_img, (0,0))
        pygame.display.flip()





    def draw_question_box(self, screen, question, x, y, active):

        # fill to regular blue, when highlighted slowly change color to light blue
        # pygame.draw.rect(screen, (50, 50, 255), pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT), border_radius=6) 
        # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT), 2, 6)

        # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.locations[0][0], self.locations[0][1], BOX_WIDTH, BOX_HEIGHT))
        # pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(self.locations[1][0], self.locations[1][1], BOX_WIDTH, BOX_HEIGHT))
        # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.locations[2][0], self.locations[2][1], BOX_WIDTH, BOX_HEIGHT))
        # pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(self.locations[3][0], self.locations[3][1], BOX_WIDTH, BOX_HEIGHT))
        # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.locations[4][0], self.locations[4][1], BOX_WIDTH, BOX_HEIGHT))
        # pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(self.locations[5][0], self.locations[5][1], BOX_WIDTH, BOX_HEIGHT))



        font_size = 20
        




    def draw_board(self, screen, background_img, border_img):
        self.background(screen, background_img, border_img)
        # self.draw_question_box(screen, "", 200, 200, False)

    def hover(self, screen):
        pos = pygame.mouse.get_pos()

        square_idx = self.find_hovering_over(pos[0], pos[1])
        # print("-----")
        # print("Square idx: ", square_idx)
        # print("final location: ", self.locations[square_idx])

        if square_idx != -1:
            pygame.draw.rect(screen, (102, 178, 255), pygame.Rect(self.locations[square_idx][0], self.locations[square_idx][1], BOX_WIDTH, BOX_HEIGHT))
        
    def display_points(self, screen):
        font = pygame.font.Font('freesansbold.ttf', round(80*SCALAR))

        text = font.render(str(str(self.p1.score) + '  '), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (self.locations[9][0] + round(BOX_WIDTH/6*SCALAR), round(20*SCALAR))
        screen.blit(text, textRect)

        text = font.render(str(str(self.p2.score) + '  '), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (self.locations[20][0] + round(BOX_WIDTH/6*SCALAR), round(20*SCALAR))
        screen.blit(text, textRect)

        text = font.render(str(str(self.p3.score) + '  '), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (self.locations[31][0] + round(BOX_WIDTH/6*SCALAR), round(20*SCALAR))
        screen.blit(text, textRect)

    def display_catagories(self, screen):

        for i in range(6):
            question_type = str(self.all_questions[i*6+1].type_).upper()
            
            font_size = 75 * SCALAR * (5/len(question_type))

            font = pygame.font.Font('impact.ttf', round(font_size))

            text = font.render(question_type, True, (240, 255, 0))
            textRect = text.get_rect()

            text_center = (TOP_LEFT[0] + BOX_WIDTH*i + BOX_WIDTH/2, TOP_LEFT[1] + float(BOX_HEIGHT/2) + round(BOX_WIDTH/40*SCALAR))

            textRect.center = text_center

            screen.blit(text, textRect.topleft)








    def on_click(self, screen):
        pos = pygame.mouse.get_pos()
        square_idx = self.find_hovering_over(pos[0], pos[1])
        # If we r on an actual square
        if square_idx == -1:
            return
        
        question = self.all_questions[square_idx]
        print(question.type_)
        if question.type_ == "player_box":
            if question.player_idx == 1:
                if question.operation == "add":
                    self.p1.score += 100
                else:
                    self.p1.score -= 100
            elif question.player_idx == 2:
                if question.operation == "add":
                    self.p2.score += 100
                else:
                    self.p2.score -= 100
            else:
                if question.operation == "add":
                    self.p3.score += 100
                else:
                    self.p3.score -= 100
        
        if question.type_ == "visual":
            self.play_visual(question, screen)
        
        if question.type_ == "theme":
            self.play_theme(question, screen)
        
        if question.type_ == "quote":
            self.play_quote(question, screen)

        if question.type_ == "connection":
            self.play_connections(question, screen)





    def run(self):
        run = True
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Certamen')
        clock = pygame.time.Clock()

        background_img = pygame.image.load('images_and_themes/jeapordy_board.png')
        background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

        border_img = pygame.image.load('images_and_themes/border.png')
        border_img = pygame.transform.scale(border_img, (WIDTH, HEIGHT))




        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.state = "ask"
                if event.type == pygame.MOUSEBUTTONUP:
                    self.on_click(screen)


            self.draw_board(screen, background_img, border_img)
            pygame.display.flip()
