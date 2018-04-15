from Tkinter import*
import MySQLdb
import time
from threading import Timer
from tkFont import*
import thread


from tkMessageBox import *

root = Tk()
root.title("Exam Interface")
root.configure(bg = "#D3D3D3")


scrw=root.winfo_screenwidth()
scrh=root.winfo_screenheight()

scrndimn=str(scrw)+'x'+str(scrh)

root.geometry(scrndimn)
#root.geometry("1024x768")

answers=0


counter=0

answer={}
questions=[] #lists of questions and following are lists of first options, second options so on
opt1=[]
opt2=[]
opt3=[]
opt4=[]
qId=[]
optVal=IntVar()
NoOfQuestions=0
timeMin=60 # variable for taking minutes from database
TimerMinutes=59
TimerSeconds=60

def submitouterframe():
	global e1f1
	global root
	global e2f1
	global e3f1
	#questions=["What is your name?","Who are you?","What am I?","Who's your daddy?"]

	if(e1f1.get()!="" and e2f1.get()!="" and e3f1.get()!=""):
		quesPaper=0
		ipAddress=e1f1.get()
		qPaperName=e2f1.get()
		rollNo=e3f1.get()
		def fetchPaper():
			global quesPaper
			global questions
			global opt1
			global opt2
			global opt3
			global opt4
			global qId
			global answer
			global NoOfQuestions
			global timeMin
			try:
				db=MySQLdb.connect(ipAddress,"root","root","pythondb2",3306)
				cursor=db.cursor()

				FetchPaperSQL="SELECT * FROM `"+qPaperName+"` WHERE 1 ORDER BY RAND()"
				print FetchPaperSQL
				cursor.execute(FetchPaperSQL)
				quesPaper=cursor.fetchall()
				NoOfQuestions=cursor.rowcount
				print "done"
				for q in quesPaper:
					answer[q[0]]=-1
					qId.append(q[0])
					print q[1]
					questions.append(q[1])
					opt1.append(q[2])
					opt2.append(q[3])
					opt3.append(q[4])
					opt4.append(q[5])
				try:
					FetchTimerSQL="SELECT timeMin FROM `qPaperList` WHERE papername='"+qPaperName+"'"
					print FetchTimerSQL
					cursor.execute(FetchTimerSQL)
					res=cursor.fetchone()
					timeMin=int(res[0])
				except Exception, e:
					raise e
					showerror("Error !","Please try Again later or Inform the administrator")
					return 0
			except Exception, e:
				raise e
				showerror("Invalid Entries","Please Check Your Entries")
				return 0
			return 1
			

		if(fetchPaper()==1):
			outerFrame.place_forget()
			global optVal
			optVal.set(-1)
			
			def next():
				global counter
				print qId[counter]
				print optVal.get()
				answer[qId[counter]]=optVal.get()
				counter+=1
				optVal.set(-1)
				if(counter>0):
					BackButton.config(state=ACTIVE)
				if(counter==NoOfQuestions-1):
					NextButton.config(state=DISABLED)

				questionlabel["text"]=questions[counter]
				questionlabel.update()
				ans1rb["text"]=opt1[counter]
				ans2rb["text"]=opt2[counter]
				ans3rb["text"]=opt3[counter]
				ans4rb["text"]=opt4[counter]
				ans1rb.update()
				ans2rb.update()
				ans3rb.update()
				ans4rb.update()
				if(answer[qId[counter]]==1):
					ans1rb.select()
					ans2rb.deselect()
					ans3rb.deselect()
					ans4rb.deselect()
				elif(answer[qId[counter]]==2):
					ans1rb.deselect()
					ans2rb.select()
					ans3rb.deselect()
					ans4rb.deselect()
				elif(answer[qId[counter]]==3):
					ans1rb.deselect()
					ans2rb.deselect()
					ans3rb.select()
					ans4rb.deselect()
				elif(answer[qId[counter]]==4):
					ans1rb.deselect()
					ans2rb.deselect()
					ans3rb.deselect()
					ans4rb.select()
				else:
					ans1rb.deselect()
					ans2rb.deselect()
					ans3rb.deselect()
					ans4rb.deselect()


			def back():
				global counter
				answer[qId[counter]]=optVal.get()
				counter-=1
				if(counter<NoOfQuestions-1):
					NextButton.config(state=ACTIVE)

				if(counter==0):
					BackButton.config(state=DISABLED)
				
				optVal.set(-1)
				questionlabel["text"]=questions[counter]
				questionlabel.update()
				ans1rb["text"]=opt1[counter]
				ans2rb["text"]=opt2[counter]
				ans3rb["text"]=opt3[counter]
				ans4rb["text"]=opt4[counter]
				ans1rb.update()
				ans2rb.update()
				ans3rb.update()
				ans4rb.update()
				if(answer[qId[counter]]==1):
					ans1rb.select()
					ans2rb.deselect()
					ans3rb.deselect()
					ans4rb.deselect()
				elif(answer[qId[counter]]==2):
					ans1rb.deselect()
					ans2rb.select()
					ans3rb.deselect()
					ans4rb.deselect()
				elif(answer[qId[counter]]==3):
					ans1rb.deselect()
					ans2rb.deselect()
					ans3rb.select()
					ans4rb.deselect()
				elif(answer[qId[counter]]==4):
					ans1rb.deselect()
					ans2rb.deselect()
					ans3rb.deselect()
					ans4rb.select()
				else:
					ans1rb.deselect()
					ans2rb.deselect()
					ans3rb.deselect()
					ans4rb.deselect()

			def Timer():
				global TimerMinutes
				global TimerSeconds
				TimerMinutes=timeMin-1
				TimerSeconds=60
				#print ThreadName
				while(TimerMinutes>0 or TimerSeconds>0):
					TimerSeconds-=1
					if(TimerSeconds==-1):
						TimerMinutes-=1
						TimerSeconds=59
					MinutesLabel.config(text=TimerMinutes)
					SecondsLabel.config(text=TimerSeconds)
					MinutesLabel.update()
					SecondsLabel.update()
					time.sleep(1)
				print "submitted"
				#delete everything code
				submit()

			def forceClose():
				#submit()
				root.destroy()
				

			def submit():
				answer[qId[counter]]=optVal.get()
				answersKeys=answer.keys()
				answerString=""
				keyCount=0
				for keyVal in answersKeys:
					if(keyCount==0):
						answerString=answerString+str(keyVal)+","+str(answer[keyVal])
					else:
						answerString=answerString+";"+str(keyVal)+","+str(answer[keyVal])
					keyCount+=1
				db=MySQLdb.connect("127.0.0.1","root","root","pythonanswers",3306)
				cursor=db.cursor()
				try:
					CreateTableSQL="CREATE TABLE IF NOT EXISTS `"+qPaperName+"` (user varchar(9),selection text, PRIMARY KEY(user))"
					cursor.execute(CreateTableSQL)
					InsertAnswerStringSQL="INSERT INTO `"+qPaperName+"` (user,selection) VALUES('"+rollNo+"','"+answerString+"')"
					cursor.execute(InsertAnswerStringSQL)
					db.commit()
					labelframe5.destroy()
					labelframe1.destroy()
					labelframe2.destroy()
					labelframe4.destroy()

					finalframe1=LabelFrame(root,bg="LightGrey",text="Completed :" , font=ubuntuSmall)
					finalframe1.place(relx=0.125 , rely=0.125 , relheight = 0.5 , relwidth=0.75)
					finallabel=Label(finalframe1,bg="LightGrey",text="Your Answers have been submitted.",font=ubuntuNormal)
					finallabel.place(relx=0.315,rely=0.37)



				except Exception, e:
					raise e
					showerror("Error","Please Try Again!")
					db.rollback()
				NextButton.config(state=DISABLED)
				BackButton.config(state=DISABLED)

				db.close()

			
			ubuntuLarge=Font(family="Ubuntu", size=40)
			ubuntuNormal=Font(family="Ubuntu",size=15)
			ubuntuAnswer=Font(family="Ubuntu",size=13)
			ubuntuSmall=Font(family="Ubuntu",size=11)


			labelframe4=LabelFrame(root,bg="LightGrey",text="Timer :" , font=ubuntuSmall)
			labelframe4.place(relx=0.5,rely=0.035,relheight=0.08 , relwidth=0.375)
			warningLabel = Label(root,text="Your answers will be automatically submitted when the timer runs out!",font=ubuntuSmall,fg="Red",bg="LightGrey")
			warningLabel.place(relx=0.5 , rely=0.01)
			minLabel=Label(labelframe4,bg="LightGrey", text="Minutes : ", font=ubuntuSmall)
			minLabel.place(relx=0.24 , rely=0.23)
			MinutesLabel=Label(labelframe4,bg="LightGrey", text=str(TimerMinutes), font=ubuntuSmall)
			MinutesLabel.place(relx=0.38,rely=0.25,relheight=0.5,relwidth=0.1)
			secLabel=Label(labelframe4,bg="LightGrey", text="Seconds : ", font=ubuntuSmall)
			secLabel.place(relx=0.46 , rely=0.23)
			SecondsLabel=Label(labelframe4,bg="LightGrey", text=str(TimerSeconds), font=ubuntuSmall)
			SecondsLabel.place(relx=0.60,rely=0.25,relheight=0.5,relwidth=0.1)


			labelframe3=LabelFrame(root,bg="LightGrey",text="Student Details :" , font=ubuntuSmall)
			labelframe3.place(relx=0.125,rely=0.035,relheight=0.08 , relwidth=0.37)

			l1f3=Label(labelframe3,bg="LightGrey",text="Roll Number ->",font=ubuntuSmall)
			l1f3.place(relx=0.14,rely=0.07)

			rollnoentry=Label(labelframe3,bg="LightGrey", text=rollNo, font=ubuntuSmall)
			rollnoentry.place(relx=0.46,rely=0.07)

			labelframe1=LabelFrame(root,bg="LightGrey",text="Answer Questions here :" , font=ubuntuSmall)
			labelframe1.place(relx=0.125 , rely=0.125 , relheight = 0.5 , relwidth=0.75)

			questionvar=questions[counter]

			questionlabel = Label(labelframe1 , text = questionvar , bg="LightGrey" , font=ubuntuNormal)
			questionlabel.place(relx=0.1,rely=0.050)

			ans1rb =  Radiobutton(labelframe1 ,width=30,height=5, text = opt1[counter] , bg="LightGrey" , font=ubuntuAnswer , variable=optVal , value=1 , indicatoron=0 , wraplength=200 )
			ans1rb.place(relx=0.15,rely=0.20)

			ans2rb =  Radiobutton(labelframe1 ,width=30,height=5, text =  opt2[counter] , bg="LightGrey" , font=ubuntuAnswer , variable=optVal , value=2 , indicatoron=0 )
			ans2rb.place(relx=0.535,rely=0.20)

			ans3rb =  Radiobutton(labelframe1 ,width=30,height=5, text =  opt3[counter] , bg="LightGrey" , font=ubuntuAnswer , variable=optVal , value=3 , indicatoron=0 )
			ans3rb.place(relx=0.15,rely=0.55)

			ans4rb =  Radiobutton(labelframe1 ,width=30,height=5, text =  opt4[counter] , bg="LightGrey" , font=ubuntuAnswer , variable=optVal , value=4 , indicatoron=0 )
			ans4rb.place(relx=0.535,rely=0.55)

			labelframe2=LabelFrame(root,bg="LightGrey",text="Navigation :", font=ubuntuSmall)
			labelframe2.place(relx=0.125,rely=0.65,relheight=0.2,relwidth=0.75)

			NextButton = Button(labelframe2 , compound = RIGHT ,text = "Next" , command = next ,font=ubuntuLarge)
			#NextButton.place(relx=0.5 , rely=0.09 , width=200,height=100)

			#photo=PhotoImage(file="64right2.png")
			NextButton.config(width="5",height="5")
			NextButton.place(relx=0.5 , rely=0.09 , width=200,height=100)

			BackButton = Button(labelframe2 , text = "Back" , command = back , font=ubuntuLarge, state=DISABLED)
			BackButton.place(relx=0.5 , rely=0.09 , width=200,height=100 , anchor=NE)

			labelframe5=LabelFrame(root,bg="LightGrey",text="Click Submit after you have answered all questions", font=ubuntuSmall)
			labelframe5.place(relx=0.125,rely=0.85,relheight=0.1,relwidth=0.75)

			SubmitButton = Button(labelframe5 , text="Submit" , font=ubuntuNormal , command=submit)
			SubmitButton.place(relx=0.45,rely=0.1)
			#label1=Label(labelframe1 , text=counter)
			#label1.grid(row=1 , column=1)
			#labelframe1.update()

			# while 1:
			# 	sleep(2)
			# 	counter=counter+1
			# 	label1["text"]=counter
			# 	labelframe1.update()

			thread.start_new_thread( Timer,() )
			root.protocol("WM_DELETE_WINDOW",forceClose)
		else:
			pass

	else:
		showerror("Error", "Please Fill the empty fields")


	


outerFrame=LabelFrame(root,text="Enter Details :" ,highlightbackground="#1E90FF",bg="#D3D3D3")
outerFrame.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)

l1f1=Label(outerFrame ,bg="#D3D3D3", text="Enter the server IP address :")
l1f1.place(relx=0.125,rely=0.125)

e1f1=Entry(outerFrame ,highlightbackground="#1E90FF", width = 40)
e1f1.place(rely=0.125,relx=0.41)

l2f1=Label(outerFrame ,bg="#D3D3D3", text="Enter the name of the Question Paper :")
l2f1.place(relx=0.125,rely=0.2)

e2f1=Entry(outerFrame ,highlightbackground="#1E90FF", width = 40)
e2f1.place(rely=0.2,relx=0.41)

l3f1=Label(outerFrame,bg="#D3D3D3",text="Enter Your Roll Number" )
l3f1.place(relx=0.125,rely=0.275)

e3f1=Entry(outerFrame ,highlightbackground="#1E90FF", width = 40)
e3f1.place(relx=0.41,rely=0.275)

outerframeSubmitButton=Button(outerFrame,text="SUBMIT",command=submitouterframe,bd=3)
outerframeSubmitButton.place(relx=0.41,rely=0.35)



#root.protocol("WM_DELETE_WINDOW",submit)
root.mainloop()


