from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPApp:
    def __init__(self):
        #  create db object
        self.dbo = Database()
        self.apio = API()

        #  login kaa gui load hoga
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/science_outofspace_world_galaxy_astronomy_universe_space_solar_system_planet_icon_263086.ico')
        self.root.geometry('500x600')
        self.root.configure(bg='#34495E')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clear()

        heading = Label(self.root,text = "NLPApp",fg = 'white',bg = '#34495E')
        heading.pack(pady = (25,30))
        heading.configure(font = ('poppins'  ,24 , "bold"))

        label1 = Label(self.root,text = 'Enter your email')
        label1.pack()

        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady = (10,10), ipady = 5)

        label2 = Label(self.root,text = 'Enter your password')
        label2.pack()

        self.password_input = Entry(self.root,width = 50,show = '*')
        self.password_input.pack(pady = (10,10), ipady = 5)

        login_btn = Button(self.root,text = 'Login',width = 30,height = 2,command = self.perform_login)
        login_btn.pack(pady = (5,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady = (10,10))

        redirect_btn = Button(self.root, text='Register Now', width=10, height=1,command = self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root,text = "NLPApp",fg = 'white',bg = '#34495E')
        heading.pack(pady = (25,30))
        heading.configure(font = ('poppins'  ,24 , "bold"))

        label1 = Label(self.root,text = 'Enter your name')
        label1.pack()

        self.name_input = Entry(self.root,width = 50)
        self.name_input.pack(pady = (10,10), ipady = 5)

        label2 = Label(self.root,text = 'Enter your email')
        label2.pack()

        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady = (10,10), ipady = 5)

        label3 = Label(self.root,text = 'Enter your password')
        label3.pack()

        self.password_input = Entry(self.root,width = 50,show = '*')
        self.password_input.pack(pady = (10,10), ipady = 5)

        register_btn = Button(self.root,text = 'Register',width = 30,height = 2,command = self.perform_registration)
        register_btn.pack(pady = (5,10))

        label4 = Label(self.root, text='Already a member?')
        label4.pack(pady = (10,10))

        redirect_btn = Button(self.root, text='Login Now', width=10, height=1,command = self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        #          clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
#         fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response =  self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success' , "Successfully registered. You can now login.")
        else:
            messagebox.showerror('Error' , 'Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response =  self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror("Error" , 'Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", fg='white', bg='#34495E')
        heading.pack(pady=(25, 30))
        heading.configure(font=('poppins', 24, "bold"))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.home_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.home_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', width=20, height=2, command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", fg='white', bg='#34495E')
        heading.pack(pady=(25, 30))
        heading.configure(font=('poppins', 24, "bold"))

        heading2 = Label(self.root, text="Sentiment Analysis", fg='white', bg='#34495E')
        heading2.pack(pady=(20, 20))
        heading2.configure(font=('poppins', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(10, 10), ipady=5)

        sentiment_btn = Button(self.root, text='Analyze sentiment', width=20, height=2, command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result1 = Label(self.root, text='' ,bg = '#34495E' , fg = 'white' )
        self.sentiment_result1.pack(pady=(10, 10))
        self.sentiment_result1.configure(font = ('poppins' , 16))

        back_btn = Button(self.root, text='Go Back', width=20, height=2, command=self.home_gui)
        back_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        # print(result)

        l = []
        for i in result['scored_labels']:
            l.append(i['score'])

        index = sorted(list(enumerate(l)), key=lambda x: x[1], reverse=True)[0][0]
        response = result['scored_labels'][index]['label']

        self.sentiment_result1['text'] = response

nlp = NLPApp()