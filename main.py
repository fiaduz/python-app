
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('main.kv')

class GameScreen(Screen):
    manager = None



    def reset(self):
        # time.sleep(2)
        self.flag = False
        # self.ids.my_label.text = " "
        self.ids.my_label.markup = True  # Enable markup for formatting
        self.ids.my_label.font_size = '72sp'  # Set the font size (use 'sp' for scalable pixels)
        self.p = 0
        # time.sleep(2)
        self.ids.my_button1.text = ''
        self.ids.my_button2.text = ''
        self.ids.my_button3.text = ''
        self.ids.my_button4.text = ''
        self.ids.my_button5.text = ''
        self.ids.my_button6.text = ''
        self.ids.my_button7.text = ''
        self.ids.my_button8.text = ''
        self.ids.my_button9.text = ''
    
        self.c = 0    
        self.p = 0
        self.p1 = 'a'
        self.p2 = 'a'
        self.p3 = 'a'
        self.p6 = 'a'
        self.p5 = 'a'
        self.p4 = 'a'
        self.p7 = 'a'
        self.p8 = 'a'
        self.p9 = 'a'
    def reset_btn(self):
        self.flag = False
        self.ids.my_label.text = " "
        self.ids.my_label.markup = True  # Enable markup for formatting
        self.ids.my_label.font_size = '72sp'  # Set the font size (use 'sp' for scalable pixels)
        self.p = 0
        self.ids.my_button1.text = ''
        self.ids.my_button2.text = ''
        self.ids.my_button3.text = ''
        self.ids.my_button4.text = ''
        self.ids.my_button5.text = ''
        self.ids.my_button6.text = ''
        self.ids.my_button7.text = ''
        self.ids.my_button8.text = ''
        self.ids.my_button9.text = ''
    
        self.c = 0    
        self.p1 = 'a'
        self.p2 = 'a'
        self.p3 = 'a'
        self.p6 = 'a'
        self.p5 = 'a'
        self.p4 = 'a'
        self.p7 = 'a'
        self.p8 = 'a'
        self.p9 = 'a'
    flag = False
    c = 0    
    p = 0
    p1 = 'a'
    p2 = 'a'
    p3 = 'a'
    p6 = 'a'
    p5 = 'a'
    p4 = 'a'
    p7 = 'a'
    p8 = 'a'
    p9 = 'a'
    def my_button1_press(self):
        if self.flag == False: 
            if self.p1 == 'a':
                self.p += 1
            self.c += 1
            if self.p1 == 'X':
                self.ids.my_button1.text = 'X'
                # speak("x given")
                
            elif self.p1 == 'O':
                self.ids.my_button1.text = 'O'
                # speak("O given")
            
            elif self.p % 2 == 1:
                self.ids.my_button1.text = 'X'
                self.p1 = 'X'
                # speak("x given")
            else:
                self.ids.my_button1.text = 'O'
                self.p1 = 'O'
            
            # if self.flag == True:
            #     self.p1 = ''
            self.result()
            
            self.game_over()
        elif self.ids.my_button1.text == '':
            self.ids.my_button1.text = ''
        else:
            pass
    def my_button2_press(self):
        if self.flag == False:
            if self.p2 == 'a':
                self.p += 1
            self.c += 1
                
            if self.p2 == 'X':
                self.ids.my_button2.text = 'X'

                
            elif self.p2 == 'O':
                self.ids.my_button2.text = 'O'
            elif self.p % 2 == 1:
                self.ids.my_button2.text = 'X'
                self.p2 = 'X'
            else:
                self.ids.my_button2.text = 'O'
                self.p2 = 'O'
            # if self.flag == True:
            #     self.p2 = ''
            self.result()
            self.game_over()
        elif self.ids.my_button2.text == '':
            self.ids.my_button2.text = ''
        else:
            pass
        
    def my_button3_press(self):
            
        if self.flag == False:
            if self.p3 == 'a':
                self.p += 1
            self.c += 1
            if self.p3 == 'X':
                self.ids.my_button3.text = 'X'

                
            elif self.p3 == 'O':
                self.ids.my_button3.text = 'O'
            elif self.p % 2 ==1:
                self.ids.my_button3.text = 'X'
                self.p3 = 'X'
            else:
                self.ids.my_button3.text = 'O'
                self.p3 = 'O'
            # if self.flag == True:
            #     self.p3 = ''
            self.result() 
            self.game_over()
        elif self.ids.my_button3.text == '':
            self.ids.my_button3.text = ''
        else:
            pass
    def my_button4_press(self):
        if self.flag == False:
            if self.p4 == 'a':
                self.p += 1
            self.c += 1
            if self.p4 == 'X':
                self.ids.my_button4.text = ''

                
            elif self.p4 == 'O':
                self.ids.my_button4.text = 'O'
            elif self.p % 2 ==1:
                self.ids.my_button4.text = 'X'
                self.p4 = 'X'
            else:
                self.ids.my_button4.text = 'O'
                self.p4 = 'O'
            # if self.flag == True:
            #     self.p4 = ''
            self.result() 
            self.game_over()
        elif self.ids.my_button4.text == '':
            self.ids.my_button4.text = ''
        else:
            pass
        
    
    def my_button5_press(self):
        if self.flag == False:
            if self.p5 == 'a':
                self.p += 1
            self.c += 1
            if self.p5 == 'X':
                self.ids.my_button5.text = 'X'

                
            elif self.p5 == 'O':
                self.ids.my_button5.text = 'O'
            elif self.p % 2 == 1:
                self.ids.my_button5.text = 'X'
                self.p5 = 'X'
            else:
                self.ids.my_button5.text = 'O'
                self.p5 = 'O'
            # if self.flag == True:
            #     self.p5 = ''
            self.result()
            self.game_over()
        elif             self.ids.my_button5.text == '':
            self.ids.my_button5.text = ''
        else:
            pass
    def my_button6_press(self):
        if self.flag == False:
            if self.p6 == 'a':
                self.p += 1
            self.c += 1
            if self.p6 == 'X':
                self.ids.my_button6.text = 'X'

                
            elif self.p6 == 'O':
                self.ids.my_button6.text = 'O'
            elif self.p % 2 ==1:
                self.ids.my_button6.text = 'X'
                self.p6 = 'X'
            else:
                self.ids.my_button6.text = 'O'
                self.p6 = 'O'
            # if self.flag == True:
            #     self.p6 = ''
            self.result()    
            self.game_over()
        elif self.ids.my_button6.text == '':
            self.ids.my_button6.text = ''
        else:
            pass
        
    def my_button7_press(self):
        if self.flag == False:
            if self.p7 == 'a':

                self.p+= 1
            self.c += 1
            if self.p7 == 'X':
                self.ids.my_button7.text = 'X'

                
            elif self.p7 == 'O':
                self.ids.my_button7.text = 'O'
            elif self.p % 2 ==1:
                self.ids.my_button7.text = 'X'
                self.p7 = 'X'
            else:
                self.ids.my_button7.text = 'O'
                self.p7 = 'O'
            # if self.flag == True:
            #     self.p7 = ''
            self.result()  
            self.game_over()
        elif self.ids.my_button7.text == '':
            self.ids.my_button7.text = '' 
        else:
            pass    
    
    def my_button8_press(self):
        if self.flag == False:
            if self.p8 == 'a':
    
                self.p += 1
            self.c += 1
            if self.p8 == 'X':
                self.ids.my_button8.text = 'X'

                
            elif self.p8 == 'O':
                self.ids.my_button8.text = 'O'
            elif self.p % 2 == 1:
                self.ids.my_button8.text = 'X'
                self.p8 = 'X'
            else:
                self.ids.my_button8.text = 'O'
                self.p8 = 'O'
            # if self.flag == True:
            #     self.p8 = ''
            self.result()
            self.game_over()
        elif self.ids.my_button8.text == '':
            self.ids.my_button8.text = ''
        else:
            pass
    def my_button9_press(self):
        if self.flag == False:
            if self.p9 == 'a':
                self.p += 1
            self.c += 1     
            if self.p9 == 'X':
                self.ids.my_button9.text = 'X'

                
            elif self.p9 == 'O':
                self.ids.my_button9.text = 'O'
            elif self.p % 2 ==1:
                self.ids.my_button9.text = 'X'
                self.p9 = 'X'
                
            else:
                self.ids.my_button9.text = 'O'
                self.p9 = 'O'
            # if self.flag == True:
            #     self.p9 = ''
            self.result()
            self.game_over()
        elif self.ids.my_button4.text == '':
            self.ids.my_button9.text = ''
        else:
            pass

    def game_over(self):
        if self.flag == True:
            self.result()
            
            # self.reset()
            
        
        elif self.p%9 == 0:
            
            # Assuming you have an id named 'my_label' for your Label widget
            self.ids.my_label.text = "[b]Game Over!!![/b]"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'  # Set the font size (use 'sp' for scalable pixels)
        else:
            pass

            
    

    def result(self):
        
    
        if (self.ids.my_button1.text == 'X' and self.ids.my_button2.text == 'X' and self.ids.my_button3.text == 'X') or \
        (self.ids.my_button4.text == 'X' and self.ids.my_button5.text == 'X' and self.ids.my_button6.text == 'X') or \
        (self.ids.my_button7.text == 'X' and self.ids.my_button8.text == 'X' and self.ids.my_button9.text == 'X'):
            self.flag = True
            self.ids.my_label.text = "X Won!"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'
            print("Congratulation player X won the match")

        elif (self.ids.my_button1.text == 'O' and self.ids.my_button2.text == 'O' and self.ids.my_button3.text == 'O') or \
        (self.ids.my_button4.text == 'O' and self.ids.my_button5.text == 'O' and self.ids.my_button6.text == 'O') or \
        (self.ids.my_button7.text == 'O' and self.ids.my_button8.text == 'O' and self.ids.my_button9.text == 'O'):
            self.flag = True
            self.ids.my_label.text = "O Won!"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'
            print("Congratulation player O won the match")
        
        elif (self.ids.my_button1.text == 'O' and self.ids.my_button4.text == 'O' and self.ids.my_button7.text == 'O') or \
        (self.ids.my_button2.text == 'O' and self.ids.my_button5.text == 'O' and self.ids.my_button8.text == 'O') or \
        (self.ids.my_button3.text == 'O' and self.ids.my_button6.text == 'O' and self.ids.my_button9.text == 'O'):
            self.flag = True
            self.ids.my_label.text = "O Won!"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'
            print("Congratulation player O won the match")
        
        elif (self.ids.my_button1.text == 'X' and self.ids.my_button4.text == 'X' and self.ids.my_button7.text == 'X') or \
        (self.ids.my_button2.text == 'X' and self.ids.my_button5.text == 'X' and self.ids.my_button8.text == 'X') or \
        (self.ids.my_button3.text == 'X' and self.ids.my_button6.text == 'X' and self.ids.my_button9.text == 'X'):
            self.flag = True
            self.ids.my_label.text = "X Won!"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'
            print("Congratulation player X won the match")

        elif (self.ids.my_button1.text == 'O' and self.ids.my_button5.text == 'O' and self.ids.my_button9.text == 'O') or \
        (self.ids.my_button3.text == 'O' and self.ids.my_button5.text == 'O' and self.ids.my_button7.text == 'O'):
            self.flag = True
            self.ids.my_label.text = "O Won!"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'
            print("Congratulation player O won the match")

        elif (self.ids.my_button1.text == 'X' and self.ids.my_button5.text == 'X' and self.ids.my_button9.text == 'X') or \
        (self.ids.my_button3.text == 'X' and self.ids.my_button5.text == 'X' and self.ids.my_button7.text == 'X'):
            self.flag = True
            self.ids.my_label.text = "X Won!"
            self.ids.my_label.markup = True  # Enable markup for formatting
            self.ids.my_label.font_size = '72sp'
            print("Congratulation player X won the match")
           
        else:
            pass
    # def switch_to_detail(self):
    #     self.manager.current = 'detail_screen'

# class DetailScreen(Screen):
#     manager = None
#     def switch_to_game(self):
#         self.manager.current = 'game_screen'  

class MyScreenManager(ScreenManager):
    pass
class tita(App):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    tita().run()
