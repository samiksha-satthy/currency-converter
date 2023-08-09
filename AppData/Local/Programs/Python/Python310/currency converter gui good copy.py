 #Samiksha Satthy and Evana Mahmud
#ICS 208
#Date: November 24, 2021
#Description:
#           Input: Ask the user to choose a radio button (which currency they want to convert) that represents a currency conversion method and amount in that currency
#           Processing: Calculating the amount of one currency to another
#           Output: Display the converted amount, error messages and feedback.

#IMPORTANT: WHEN RUNNING THE CODE, MAKE SURE TO MOVE THE WINDOWS APART TO PREVENT THEM FROM OVERLAPPING!!!!!


# We are importing the tkinter and tkinter messagebox
import tkinter
import tkinter.messagebox


 #make a class      

class MyGUI:
    def __init__(self):

        #making the first main window that displays the different currency methods 
        self.main_window = tkinter.Tk()
        #Naming the window
        self.main_window.title('Currency Converter')
        #default size of the window
        self.main_window.geometry("700x200")
        
        
        #making the frames 
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        

        #making a variable and setting it to 1 (using the same variable because it is radio buttons)
        self.radio_var1 = tkinter.IntVar()


        self.radio_var1.set(1)

        #Adding a label on top to prevent repetition 
        self.info_label = tkinter.Label(self.mid_frame, \
                                        text='Convert from: ')

        #making radio buttons based on the variable made above for the user to choose which currency conversion method they would like 
        self.rb1 = tkinter.Radiobutton(self.top_frame, \
                                       text='CAD to USD or USD to CAD', variable=self.radio_var1, \
                                       value=1)

        self.rb2 = tkinter.Radiobutton(self.top_frame, \
                                       text='CAD to Rupees or Rupees to CAD', variable=self.radio_var1, \
                                       value=2)

        self.rb3 = tkinter.Radiobutton(self.top_frame, \
                                       text='CAD to Euros or Euros to CAD', variable=self.radio_var1, \
                                       value=3)

        self.rb4 = tkinter.Radiobutton(self.top_frame, \
                                       text='CAD to Taka or Taka to CAD', variable=self.radio_var1, \
                                       value=4)

        self.rb5 = tkinter.Radiobutton(self.top_frame, \
                                       text='CAD to Pesos or Pesos to CAD', variable=self.radio_var1, \
                                       value=5)

        tkinter.messagebox.showinfo('Description', 'Hello and Welcome to our conveinent currency converter! Pick a conversion method to get started! ')

        # packing all the radio buttons, buttons, frames and going into a main loop
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()

        self.info_label.pack(side='left')

        self.ok_button = tkinter.Button(self.bottom_frame, \
                                        text='OK', command=self.show_choice)

        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.mid_frame.pack()
        self.mid_frame2.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop


    #function for when the ok_button is pressed 
    def show_choice(self):

        

        # creating if statements to distinguish which radio button the user were to choose
        
        # if the 1st radio button were to be pressed, the following statements will execute below
        if int(self.radio_var1.get()) == 1:

                # creating new window for the radio buttton chosen
                class newwindowGUI:
                    def __init__(hi):

                        #this new window asks the user to specify which currency conversion they want
                        hi.main_window2 = tkinter.Tk()
                        #naming the window
                        hi.main_window2.title('Conversion Method')
                        #default size
                        hi.main_window2.geometry("700x200")
                        
                        #making frames for the new window
                        hi.top_frame2 = tkinter.Frame(hi.main_window2)
                        hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                        hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                        #asking the user to choose a conversion method based on the two currencies picked
                        hi.label_1 = tkinter.Label(hi.top_frame2, \
                                                   text='Choose a conversion method: ')

                        #if the cad to usd or usd to cad radio button was chosen, we ask the user to further clarify their answer with buttons 
                        hi.cad_to_usd = tkinter.Button(hi.bottom_frame2, \
                                                       text='CAD to USD',\
                                                       command=hi.cad_to_usd)
                        
                        hi.usd_to_cad = tkinter.Button(hi.bottom_frame2, \
                                                       text='USD to CAD', \
                                                       command=hi.usd_to_cad)
                        
                        hi.quit = tkinter.Button(hi.bottom_frame3, \
                                                 text='Quit', \
                                                 command=hi.main_window2.destroy)
                                                 

                        
                        #pack labels and frames and buttons and going into the mainloop
                        hi.label_1.pack()
                        hi.cad_to_usd.pack(side='left')
                        hi.usd_to_cad.pack(side='left')
                        hi.quit.pack()
                        

                        hi.top_frame2.pack()
                        hi.bottom_frame2.pack()
                        hi.bottom_frame3.pack()


                        tkinter.mainloop

                    #if cad to usd button was picked, the below statements are to execute 
                    def cad_to_usd(hi):

                            #creating new class and window for this 
                            class newwindow2GUI:
                            
                                def __init__(hi):
                                    
                                    #making a new window to ask the user to enter the amount in CAD so we can convert it into USD 
                                    hi.main_window2 = tkinter.Tk()
                                    #naming the window
                                    hi.main_window2.geometry("700x200")
                                    #default size
                                    hi.main_window2.title('CAD to USD')

                                    #making the frames 
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    
                                    # Ask the user to input an amount in CAD
                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter CAD: ')
                            
                                    hi.entry_cad = tkinter.Entry(hi.top_frame2, \
                                                         width=10)

                                    # Make the convert, quit and finished button that is used after the program has converted the inserted amount
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey)

                                    
                                    # Pack everything and call the mainloop
                                    hi.prompt_label.pack()
                                    hi.entry_cad.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()
                            

                                    hi.top_frame2.pack()
                         
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop

                                    
                            # when convert button is pressed, the below statements will execute 
                                def convert(hi):
                                    
                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_cad.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')


                                    # If there is no error, go ahead with conversion 
                                    else:

                                        cad = float(hi.entry_cad.get())
                 
                                        usd = cad * 0.79

                                        tkinter.messagebox.showinfo('Conversion', message='In USD: $' +
                                                                str(format(usd, ',.2f')))
                                        

                            # when the 'Have you finished' button is pressed, the below statements will execute 
                                def survey(box):

                                        #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var1 = tkinter.IntVar()
                                                box.check_var2 = tkinter.IntVar()
                                                box.check_var3 = tkinter.IntVar()
                                                box.check_var4 = tkinter.IntVar()

                                                #setting the check box variables to 0
                                                box.check_var1.set(0)
                                                box.check_var2.set(0)
                                                box.check_var3.set(0)
                                                box.check_var4.set(0)

                                                # Making a label to thank the user for trying our program and asking a few questions
                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var1)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var2)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var3)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var4)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into/calling the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next(box):

                                                
                                                box.message2 = 'Thank you for the feedback!'


                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response', box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()


                                
                             
                                    
                            #making an instance of the class 
                            new_windoww = newwindow2GUI ()
                            
                     # If the usd_to_cad button was chosen, the statements below will execute       
                    def usd_to_cad(hi):
                        
                        
                        class newwindow2GUI:
                            
                                def __init__(hi):
                                    #new window, name and size is created 
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('USD to CAD')

                                    #making frames 
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    # Ask the user to input an amount in USD
                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter USD: ')
                            
                                    hi.entry_usd = tkinter.Entry(hi.top_frame2, \
                                                         width=10)

                                   
                                    # Make convert, quit and done buttons
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey2)

                                    # Pack everything
                                    hi.prompt_label.pack()
                                    hi.entry_usd.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()
                                    

                                
                            

                                    hi.top_frame2.pack()
                          
                                    hi.bottom_frame2.pack()

                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop


                            
                                def convert(hi):


                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_usd.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                        

                                        

                                       # If there is no error, go ahead with conversion  
                                    else:
                                        usd = float(hi.entry_usd.get())
                                
                                        cad = usd * 1.27

                                        tkinter.messagebox.showinfo('Conversion', message='In CAD: $' +
                                                            str(format(cad, ',.2f')))

                                def survey2(box):

                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var5 = tkinter.IntVar()
                                                box.check_var6 = tkinter.IntVar()
                                                box.check_var7 = tkinter.IntVar()
                                                box.check_var8 = tkinter.IntVar()

                                                #setting the new variables to 0
                                                box.check_var5.set(0)
                                                box.check_var6.set(0)
                                                box.check_var7.set(0)
                                                box.check_var8.set(0)

                                                # As seen in a above comment, repeating the step for each conversion method.
                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var5)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var6)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var7)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var8)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next2)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next2(box):

                                            
                                                box.message2 = 'Thank you for the feedback!'

                                                

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response', box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()

                                
                               
                        # making an instance of the class 
                        new = newwindow2GUI ()
                             
                #making an instance of the class 
                new_window = newwindowGUI ()


        # The above if statment is very similar to the elif statments below. They share the same logic but may have different variables 
                

        # if the 2nd radio button were to be pressed, the following statements will execute below
        elif int(self.radio_var1.get()) == 2:
            # Make a new window for if the user chooses a different button
            class newwindowGUI:
                def __init__(hi):
                    #this new window asks the user to specify which currency conversion they want
                    hi.main_window2 = tkinter.Tk()
                    #naming the window
                    hi.main_window2.geometry("700x200")
                    #deafult size 
                    hi.main_window2.title('Conversion Method')

                    
                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                    #asking the user to choose a conversion method based on the two currencies picked
                    hi.label_1 = tkinter.Label(hi.top_frame2, \
                                               text='Choose a conversion method: ')

                    #if the cad to rupee or rupee to cad radio button was chosen, we ask the user to further clarify their answer
                    hi.cad_to_rupee = tkinter.Button(hi.bottom_frame2, \
                                                   text='CAD to Rupees',\
                                                   command=hi.cad_to_rupee)
                    hi.rupee_to_cad = tkinter.Button(hi.bottom_frame2, \
                                                   text='Rupees to CAD', \
                                                   command=hi.rupee_to_cad)
                    hi.quit = tkinter.Button(hi.bottom_frame3, \
                                             text='Quit', \
                                             command=hi.main_window2.destroy)

                    
                    # Pack everything and going into a main loop
                    hi.label_1.pack()
                    hi.cad_to_rupee.pack(side='left')
                    hi.rupee_to_cad.pack(side='left')
                    hi.quit.pack(side='left')

                    hi.top_frame2.pack()
                    hi.bottom_frame2.pack()
                    hi.bottom_frame3.pack()


                    tkinter.mainloop

                    # Making a seperate function for cad to rupee
                    # If the cad to rupee button was chosen, the statements below will execute 
                def cad_to_rupee(hi):

                        class newwindow2GUI:
                        
                        # Creating a new window, title, frames and setting size
                            def __init__(hi):       
                                hi.main_window2 = tkinter.Tk()
                                hi.main_window2.geometry("700x200")
                                hi.main_window2.title('CAD to Rupee')
                                hi.top_frame2 = tkinter.Frame(hi.main_window2)
          
                                hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                # Ask the user to input an amount in CAD
                                hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                 text='Enter CAD: ')
                        
                                hi.entry_cad = tkinter.Entry(hi.top_frame2, \
                                                     width=10)

                                # Make convert, quit and done buttons
                                hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                           text='Convert', command=hi.convert)

                                hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                        text='Quit', command=hi.main_window2.destroy)
                                
                                hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey3)
                                
                                # Pack everything and calling the mainloop.
                                hi.prompt_label.pack()
                                hi.entry_cad.pack(side='left')
                                hi.convert_button.pack(side='left')
                                hi.quit_button.pack(side='left')
                                hi.done.pack()
                        

                                hi.top_frame2.pack()
            
                                hi.bottom_frame2.pack()

                                hi.bottom_frame3.pack()
                        

                                tkinter.mainloop
                        
                            def convert(hi):

                                # Display an error message if a number below 0 is inputed. 
                                if int(hi.entry_cad.get()) < 0:
                                    tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                    
                                #if no error is detected, continue with the program 
                                else:
                                    cad = float(hi.entry_cad.get())
        
                                    rupee = cad * 58.73

                                    tkinter.messagebox.showinfo('Conversion', message='In Rupee: ' +
                                                        str(format(rupee, ',.2f')))

                            def survey3(box):


                                     #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var9 = tkinter.IntVar()
                                                box.check_var10 = tkinter.IntVar()
                                                box.check_var11 = tkinter.IntVar()
                                                box.check_var12 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var9.set(0)
                                                box.check_var10.set(0)
                                                box.check_var11.set(0)
                                                box.check_var12.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var9)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var10)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var11)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var12)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next3)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything ad going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next3(box):

                                               
                                                box.message2 = 'Thank you for the feedback!'

                                        

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response',  box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()


                            
                        new_windoww = newwindow2GUI ()
                                
                    
                        

                        # If the rupee to cad button was chosen, the statements below will execute
                def rupee_to_cad(hi):
                    
                    
                    class newwindow2GUI:
                        
                            def __init__(hi):       
                                hi.main_window2 = tkinter.Tk()
                                hi.main_window2.geometry("700x200")
                                hi.main_window2.title('Rupee to CAD')
                                hi.top_frame2 = tkinter.Frame(hi.main_window2)
        
                                hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                
                                # Ask the user to input an amount in Rupee
                                hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                 text='Enter Rupee: ')
                        
                                hi.entry_rupee = tkinter.Entry(hi.top_frame2, \
                                                     width=10)


                                # Make convert, quit and done buttons
                                hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                           text='Convert', command=hi.convert4)

                                hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                        text='Quit', command=hi.main_window2.destroy)

                                hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey)

                                hi.prompt_label.pack()
                                hi.entry_rupee.pack(side='left')
                                hi.convert_button.pack(side='left')
                                hi.quit_button.pack(side='left')
                                hi.done.pack()

                            
                        

                                hi.top_frame2.pack()
                      
                                hi.bottom_frame2.pack()

                                hi.bottom_frame3.pack()
                        

                                tkinter.mainloop
                        
                            def convert4(hi):

                                
                                # Display an error message if a number below 0 is inputed.
                                if int(hi.entry_rupee.get()) < 0:
                                    tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                    
                                # otherwise, continue with the program 
                                else:
                                    rupee = float(hi.entry_rupee.get())
                            
                                    cad = rupee * 0.017

                                    tkinter.messagebox.showinfo('Conversion', message='In CAD: $' +
                                                            str(format(cad, ',.2f')))

                            def survey(box):


                                     #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var13 = tkinter.IntVar()
                                                box.check_var14 = tkinter.IntVar()
                                                box.check_var15 = tkinter.IntVar()
                                                box.check_var16 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var13.set(0)
                                                box.check_var14.set(0)
                                                box.check_var15.set(0)
                                                box.check_var16.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var13)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var14)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var15)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var16)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next4)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next4(box):

                                            
                                                box.message2 = 'Thank you for the feedback!'
 

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response', box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()

                           

                    new = newwindow2GUI ()



            new = newwindowGUI ()
                         

                    
                             

    
                            
        # if the 3rd radio button were to be pressed, the following statements will execute below        
        elif self.radio_var1.get() == 3:
            class newwindowGUI:
                    def __init__(hi):       
                        hi.main_window2 = tkinter.Tk()
                        hi.main_window2.geometry("700x200")
                        hi.main_window2.title('Conversion Method')
                        hi.top_frame2 = tkinter.Frame(hi.main_window2)
                       
                        hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                        hi.bottom_frame3 = tkinter.Frame(hi.main_window2)
                        
                        #asking the user to choose a conversion method based on the two currencies picked
                        hi.label_1 = tkinter.Label(hi.top_frame2, \
                                                   text='Choose a conversion method: ')

                        #if the cad to usd or usd to cad radio button was chosen, we ask the user to further clarify their answer
                        hi.cad_to_euro = tkinter.Button(hi.bottom_frame2, \
                                                       text='CAD to Euros',\
                                                       command=hi.cad_to_euro)
                        hi.euro_to_cad = tkinter.Button(hi.bottom_frame2, \
                                                       text='Euros to CAD', \
                                                       command=hi.euro_to_cad)
                        hi.quit = tkinter.Button(hi.bottom_frame3, \
                                                 text='Quit', \
                                                 command=hi.main_window2.destroy)

                        hi.label_1.pack()
                        hi.cad_to_euro.pack(side='left')
                        hi.euro_to_cad.pack(side='left')
                        hi.quit.pack(side='left')

                        hi.top_frame2.pack()
                        hi.bottom_frame2.pack()
                        hi.bottom_frame3.pack()


                        tkinter.mainloop


                        # If the cad to euro button was chosen, the statements below will execute
                        
                    def cad_to_euro(hi):

                            class newwindow2GUI:
                            
                                def __init__(hi):
                                    #making new window, title, frames and setting size of the window 
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('CAD to Euro')
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
                            
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    # Ask the user to input an amount in CAD
                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter CAD: ')
                            
                                    hi.entry_cad = tkinter.Entry(hi.top_frame2, \
                                                         width=10)


                                    # Make convert, quit and done buttons
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey5)

                                    hi.prompt_label.pack()
                                    hi.entry_cad.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()

                        
                            

                                    hi.top_frame2.pack()
                     
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop
                            
                                def convert(hi):

                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_cad.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                        
                                    # otherwise, continue with the program 
                                    else:
                                        cad = float(hi.entry_cad.get())
                      
                                        euro = cad * 0.70

                                        tkinter.messagebox.showinfo('Conversion', message='In Euro: ' +
                                                                str(format(euro, ',.2f')))

                                def survey5(box):


                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var17 = tkinter.IntVar()
                                                box.check_var18 = tkinter.IntVar()
                                                box.check_var19 = tkinter.IntVar()
                                                box.check_var20 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var17.set(0)
                                                box.check_var18.set(0)
                                                box.check_var19.set(0)
                                                box.check_var20.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var17)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var18)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var19)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var20)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next5)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything ad going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next5(box):

                                              
                                                box.message2 = 'Thank you for the feedback!'

                                            

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response',  box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()


                                
                        
                                    
                            new_windoww = newwindow2GUI ()


                     # If the euro to cad button was chosen, the statements below will execute
                            
                    def euro_to_cad(hi):
                        
                        
                        class newwindow2GUI:
                            
                                def __init__(hi):

                                    #create new window, frames, title and setting size of window
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('Euro to CAD')
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
            
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    # Ask the user to input an amount in Euro

                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter Euro: ')
                            
                                    hi.entry_euro = tkinter.Entry(hi.top_frame2, \
                                                         width=10)


                                    # Make convert, quit and done buttons
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey6)

                                    #packing everything so it would display and calling the mainloop
                                    hi.prompt_label.pack()
                                    hi.entry_euro.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()

                                
                            

                                    hi.top_frame2.pack()
                          
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop
                            
                                def convert(hi):

                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_euro.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                        
                                    # otherwise, continue with the program 
                                    else:
                                        euro = float(hi.entry_euro.get())
                                
                                        cad = euro * 1.42

                                        tkinter.messagebox.showinfo('Conversion', message='In CAD: $' +
                                                                str(format(cad, ',.2f')))

                                def survey6(box):


                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var21 = tkinter.IntVar()
                                                box.check_var22 = tkinter.IntVar()
                                                box.check_var23 = tkinter.IntVar()
                                                box.check_var24 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var21.set(0)
                                                box.check_var22.set(0)
                                                box.check_var23.set(0)
                                                box.check_var24.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var21)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var22)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var23)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var24)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next6)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next6(box):

                                            
                                                box.message2 = 'Thank you for the feedback!'
                                                

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response', message=box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()
                               

                        new = newwindow2GUI ()
                             

            new_window = newwindowGUI ()
                            
                
        # if the 4th radio button were to be pressed, the following statements will execute below            
        elif self.radio_var1.get() == 4:
            class newwindowGUI:
                    def __init__(hi):

                        #creating the window, frames, title and setting the size 
                        hi.main_window2 = tkinter.Tk()
                        hi.main_window2.geometry("700x200")                        
                        hi.main_window2.title('Conversion Method')
                        hi.top_frame2 = tkinter.Frame(hi.main_window2)
        
                        hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                        hi.bottom_frame3 = tkinter.Frame(hi.main_window2)
                        
                        #asking the user to choose a conversion method based on the two currencies picked
                        hi.label_1 = tkinter.Label(hi.top_frame2, \
                                                   text='Choose a conversion method: ')

                        #if the cad to taka or taka to cad radio button was chosen, we ask the user to further clarify their answer

                        hi.cad_to_taka = tkinter.Button(hi.bottom_frame2, \
                                                       text='CAD to Taka',\
                                                       command=hi.cad_to_taka)
                        hi.taka_to_cad = tkinter.Button(hi.bottom_frame2, \
                                                       text='Taka to CAD', \
                                                       command=hi.taka_to_cad)
                        
                        hi.quit = tkinter.Button(hi.bottom_frame3, \
                                                 text='Quit', \
                                                 command=hi.main_window2.destroy)

                        # pack everything and call the mainloop
                        hi.label_1.pack()
                        hi.cad_to_taka.pack(side='left')
                        hi.taka_to_cad.pack(side='left')
                        hi.quit.pack(side='left')

                        hi.top_frame2.pack()
                        hi.bottom_frame2.pack()
                        hi.bottom_frame3.pack()


                        tkinter.mainloop

                    # If the cad to taka button was chosen, the statements below will execute
                        
                    def cad_to_taka(hi):

                            class newwindow2GUI:
                            
                                def __init__(hi):       
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('CAD to Taka')
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
                           
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)
                                    
                                    # Ask the user to input an amount in CAD
                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter CAD: ')
                            
                                    hi.entry_cad = tkinter.Entry(hi.top_frame2, \
                                                         width=10)


                                    # Make convert, quit and done buttons
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey7)


                                    #packing everything and entering the mainloop
                                    hi.prompt_label.pack()
                                    hi.entry_cad.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()

                
                            

                                    hi.top_frame2.pack()
                        
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop
                            
                                def convert(hi):

                                    # Display an error message if a number below 0 is inputed.  

                                    if int(hi.entry_cad.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                        
                                    #otherwise continue with the program
                                    else:
                                        cad = float(hi.entry_cad.get())
                               
                                        taka = cad * 67.63

                                        tkinter.messagebox.showinfo('Conversion', message='In Taka: ' +
                                                                str(format(taka, ',.2f')))
                                        
                                def survey7(box):


                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var25 = tkinter.IntVar()
                                                box.check_var26 = tkinter.IntVar()
                                                box.check_var27 = tkinter.IntVar()
                                                box.check_var28 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var25.set(0)
                                                box.check_var26.set(0)
                                                box.check_var27.set(0)
                                                box.check_var28.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var25)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var26)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var27)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var28)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next7)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next7(box):

                                                
                                                box.message2 = 'Thank you for the feedback!'
 

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response', box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()



                                
                        
                                    
                            new_windoww = newwindow2GUI ()

                            # If the taka to cad button was chosen, the statements below will execute
                            
                    def taka_to_cad(hi):
                        
                        
                        class newwindow2GUI:
                            
                                def __init__(hi):

                                    #creating new window, frames and title and setting the size of the window
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('Taka to CAD')
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
            
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    # Ask the user to input an amount in Taka

                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter Taka: ')
                            
                                    hi.entry_taka = tkinter.Entry(hi.top_frame2, \
                                                         width=10)


                                    # Make convert, quit and done buttons
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey8)

                                    #packing everything and calling the mainloop
                                    hi.prompt_label.pack()
                                    hi.entry_taka.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()

                                
                            

                                    hi.top_frame2.pack()
                          
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop
                            
                                def convert(hi):

                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_taka.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                        
                                    # otherwise continue with the program 
                                    else:
                                        taka = float(hi.entry_taka.get())
                                
                                        cad = taka * 0.015

                                        tkinter.messagebox.showinfo('Conversion', message='In CAD: $' +
                                                                str(format(cad, ',.2f')))

                                def survey8(box):

                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var29 = tkinter.IntVar()
                                                box.check_var30 = tkinter.IntVar()
                                                box.check_var31 = tkinter.IntVar()
                                                box.check_var32 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var29.set(0)
                                                box.check_var30.set(0)
                                                box.check_var31.set(0)
                                                box.check_var32.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var29)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var30)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var31)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var32)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next8)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next8(box):

                                            
                                                box.message2 = 'Thank you for the feedback!'

                                               

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response',  box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()

                                
                               

                        new = newwindow2GUI ()
                             

            new_window = newwindowGUI ()
                            
                
                
        # if the 5th radio button were to be pressed, the following statements will execute below
        elif int(self.radio_var1.get()) == 5:
            class newwindowGUI:
                    def __init__(hi):
                        #creating new window, frames, title and setting the size of the window
                        hi.main_window2 = tkinter.Tk()
                        hi.main_window2.geometry("700x200")
                        hi.main_window2.title('Conversion Method')
                        hi.top_frame2 = tkinter.Frame(hi.main_window2)
                
                        hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                        hi.bottom_frame3 = tkinter.Frame(hi.main_window2)
                        
                        #asking the user to choose a conversion method based on the two currencies picked
                        hi.label_1 = tkinter.Label(hi.top_frame2, \
                                                   text='Choose a conversion method: ')

                        #if the cad to peso or peso to cad radio button was chosen, we ask the user to further clarify their answer

                        hi.cad_to_peso = tkinter.Button(hi.bottom_frame2, \
                                                       text='CAD to Pesos',\
                                                       command=hi.cad_to_peso)
                        hi.peso_to_cad = tkinter.Button(hi.bottom_frame2, \
                                                       text='Pesos to CAD', \
                                                       command=hi.peso_to_cad)

                        hi.quit = tkinter.Button(hi.bottom_frame3, \
                                                 text='Quit', \
                                                 command=hi.main_window2.destroy)


                        #packing everything so it will display and calling the mainloop

                        hi.label_1.pack()
                        hi.cad_to_peso.pack(side='left')
                        hi.peso_to_cad.pack(side='left')
                        hi.quit.pack(side='left')

                        hi.top_frame2.pack()
                        hi.bottom_frame2.pack()
                        hi.bottom_frame3.pack()


                        tkinter.mainloop

                        # If the cad to peso button was chosen, the statements below will execute
                        
                    def cad_to_peso(hi):

                            class newwindow2GUI:
                            
                                def __init__(hi):

                                    #making a new window, frames and title and setting the size of the window 
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('CAD to Peso')
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
                            
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    # Ask the user to input an amount in CAD

                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter CAD: ')
                            
                                    hi.entry_cad = tkinter.Entry(hi.top_frame2, \
                                                         width=10)


                                    # Make convert, quit and done buttons
                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey9)

                                    #pack everything and calling the mainloop

                                    hi.prompt_label.pack()
                                    hi.entry_cad.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()
                                

                            

                                    hi.top_frame2.pack()
                       
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop

                                    
                            #if convert is pressed, the below will execute  
                                def convert(hi):

                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_cad.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')


                                   #Otherwise continue with the program      

                                    else:
                                        cad = float(hi.entry_cad.get())
                      
                                        peso = cad * 16.94

                                        tkinter.messagebox.showinfo('Conversion', message='In Peso: ' +
                                                                str(format(peso, ',.2f')))


                                # if the done button is pressed, the below statements will execute 
                                def survey9(box):

                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var33 = tkinter.IntVar()
                                                box.check_var34 = tkinter.IntVar()
                                                box.check_var35 = tkinter.IntVar()
                                                box.check_var36 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var33.set(0)
                                                box.check_var34.set(0)
                                                box.check_var35.set(0)
                                                box.check_var36.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var33)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var34)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var35)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var36)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next9)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next9(box):

                                                
                                                box.message2 = 'Thank you for the feedback!'

                                            

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response',  box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()


                                
                        
                                    
                            new_windoww = newwindow2GUI ()


                            # If the peso to cad button was chosen, the statements below will execute
                            
                    def peso_to_cad(hi):
                        
                        
                        class newwindow2GUI:
                            #making a window, frames, title and setting the size 
                            
                                def __init__(hi):       
                                    hi.main_window2 = tkinter.Tk()
                                    hi.main_window2.geometry("700x200")
                                    hi.main_window2.title('Peso to CAD')
                                    hi.top_frame2 = tkinter.Frame(hi.main_window2)
            
                                    hi.bottom_frame2 = tkinter.Frame(hi.main_window2)
                                    hi.bottom_frame3 = tkinter.Frame(hi.main_window2)

                                    # Ask the user to input an amount in CAD

                                    hi.prompt_label = tkinter.Label(hi.top_frame2, \
                                                     text='Enter Peso: ')
                            
                                    hi.entry_peso = tkinter.Entry(hi.top_frame2, \
                                                         width=10)

                                    # Make convert, quit and done buttons

                                    hi.convert_button = tkinter.Button(hi.bottom_frame2, \
                                                               text='Convert', command=hi.convert)

                                    hi.quit_button = tkinter.Button(hi.bottom_frame2, \
                                                            text='Quit', command=hi.main_window2.destroy)

                                    hi.done = tkinter.Button(hi.bottom_frame3, \
                                                              text='Click after conversion is complete ', command=hi.survey10)


                                    #packing everything and calling the mainloop

                                    hi.prompt_label.pack()
                                    hi.entry_peso.pack(side='left')
                                    hi.convert_button.pack(side='left')
                                    hi.quit_button.pack(side='left')
                                    hi.done.pack()


                                
                                
                            

                                    hi.top_frame2.pack()
                          
                                    hi.bottom_frame2.pack()
                                    hi.bottom_frame3.pack()
                            

                                    tkinter.mainloop

                                    #if convert is picked, the below will display
                            
                                def convert(hi):


                                    # Display an error message if a number below 0 is inputed.
                                    if int(hi.entry_peso.get()) < 0:
                                        tkinter.messagebox.showerror('Error!', message='you entered a negative number. To start from the beginning, press "OK" or the x')

                                        
                                    #Otherwise continue with the program


                                    else:
                                        peso = float(hi.entry_peso.get())
                                
                                        cad = peso * 0.059
                                        
                                        tkinter.messagebox.showinfo('Conversion', message='In CAD: $' +
                                                                str(format(cad, ',.2f')))

                                # if the done button is clicked the below statements will execute 

                                def survey10(box):

                                         #creating a new class
                                        class helloGUI:
                                            def __init__(box):

                                                #creating a new window to display check buttons and get input on the user's content of our program 
                                                box.main_window = tkinter.Tk()
                                                #creating the name 
                                                box.main_window.title('Previous Converters')
                                                #default size 
                                                box.main_window.geometry("700x400")

                                                #making the frames 
                                                box.top_frame = tkinter.Frame(box.main_window)
                                                box.mid_frame = tkinter.Frame(box.main_window)
                                                box.bottom_frame = tkinter.Frame(box.main_window)

                                                #making new variables for each of the check buttons
                                                box.check_var37 = tkinter.IntVar()
                                                box.check_var38 = tkinter.IntVar()
                                                box.check_var39 = tkinter.IntVar()
                                                box.check_var40 = tkinter.IntVar()

                                                #setting them to 0
                                                box.check_var37.set(0)
                                                box.check_var38.set(0)
                                                box.check_var39.set(0)
                                                box.check_var40.set(0)


                                                box.info_label = tkinter.Label(box.top_frame, \
                                                                               text='Thank you for trying our program! Was our currency converter convenient? If so, was it convenient over the following programs?  ')

                                                #making the check buttons 
                                                box.cb1 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Google', variable=box.check_var37)

                                                box.cb2 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Bank', variable=box.check_var38)

                                                box.cb3 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='ATM', variable=box.check_var39)

                                                box.cb4 = tkinter.Checkbutton(box.mid_frame, \
                                                                              text='Other', variable=box.check_var40)

                                                box.next = tkinter.Button(box.bottom_frame, \
                                                                          text='Next', command=box.next10)

                                                box.cancel = tkinter.Button(box.bottom_frame, \
                                                                            text='Cancel', command=box.main_window.destroy)


                                                #packing everything and going into the mainloop
                                                box.info_label.pack()
                                                box.cb1.pack()
                                                box.cb2.pack()
                                                box.cb3.pack()
                                                box.cb4.pack()
                                                box.next.pack()
                                                box.cancel.pack()

                                                box.top_frame.pack()
                                                box.mid_frame.pack()
                                                box.bottom_frame.pack()
                                               

                                                tkinter.mainloop

                                                
                                            #if next button is pressed, the below statements will execute 
                                            def next10(box):

                                                
                                                box.message2 = 'Thank you for the feedback!'

                                             

                                                #message will be displayed to the user
                                                tkinter.messagebox.showinfo('Feedback Response', message=box.message2)

                                        #making an instance of the class    
                                        hi = helloGUI ()

                                
                               
                        #making an instance of each class 
                        new = newwindow2GUI ()
                             

            new_window = newwindowGUI ()
                            

            
my_gui = MyGUI ()
                    


