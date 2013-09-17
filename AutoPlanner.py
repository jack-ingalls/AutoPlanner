# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Whitney Jo\.spyder2\.temp.py
"""

import ast
import datetime
import Tkinter

DEFAULT_TASK_TIME = datetime.timedelta(hours=1)  # 1 hour
DEFAULT_TASK_DURATION = datetime.timedelta(days=1)  # 1 hour

def VerboselyPrintTime(myTime):
        print "Year: ", myTime.year
        print "Month: ", myTime.month
        print "Date: ", myTime.day
        print "Hour: ", myTime.hour
        print "Minute: ", myTime.minute
        print "Second: ", myTime.second

def EditDateTime(myTime):
    while True:
        print "Changing: ", myTime
        VerboselyPrintTime(myTime)
        print "Input first letter of what you want to change, or q to exit."
        print "Type at least two letters for month and minute."
        change = raw_input("Change:")
        print
        if len(change) == 0: return myTime
        elif change is 'm' or change is 'M':
            print "I'm confused. Please type more letters."
            
        elif "Year: ".startswith(change):
            newYear = raw_input("Input new year:")
            try:
                myTime.year = int(newYear)
            except:
                print "Not a valid integer."
                
        elif "Month: ".startswith(change):
            newMonth = raw_input("Input new month:")
            try:
                newMonth = int(newMonth)
                if newMonth < 0 or newMonth > 12:
                    print "Invalid value"
                else:
                    myTime.month = newMonth
            except:
                print "Not a valid integer."
                
        elif "Day: ".startswith(change):
            newDay = raw_input("Input new day:")
            print newDay
            try:
                newDay = int(newDay)
                if newDay < 0 or newDay > 31:
                    print "Invalid value"
                else:
                    myTime.day = newDay
            except:
                print "Not a valid integer."
                
        elif "Hour: ".startswith(change):
            newHour = raw_input("Input new hour:")
            try:
                newHour = int(newHour)
                if newHour < 0 or newHour > 24:
                    print "Invalid value"
                else:
                    myTime.hour = newHour
            except:
                print "Not a valid integer."
                
        elif "Minute: ".startswith(change):
            newMinute = raw_input("Input new minute:")
            try:
                newMinute = int(newMinute)
                if newMinute < 0 or newMinute > 60:
                    print "Invalid value"
                else:
                    myTime.minute = newMinute
            except:
                print "Not a valid integer."
                
        elif "Second: ".startswith(change):
            newSecond = raw_input("Input new second:")
            try:
                newSecond = int(newSecond)
                if newSecond < 0 or newSecond > 60:
                    print "Invalid value"
                else:
                    myTime.second = newSecond
            except:
                print "Not a valid integer."
                
        else: return myTime
        
class task:
    def __init__(self, myDict=None, start=None, end=None,
                 total=DEFAULT_TASK_TIME, repeat=None):
        if type(myDict) is dict:
            self.startTime = myDict["Start time"]
            self.startTime = myDict["End time"]
            self.startTime = myDict["Total labor"]
            self.startTime = myDict["Repeat every"]
            return
        if type(start) is datetime.datetime:
            self.startTime = start
        else: 
            self.startTime = datetime.datetime.now()
        if type(end) is datetime.datetime:
            self.endTime = end
        else: 
            self.endTime = self.startTime + DEFAULT_TASK_DURATION
        if type(total) is datetime.timedelta:
            self.totalLabor = total
        else:
            self.totalLabor = DEFAULT_TASK_TIME
        if type(repeat) is datetime.timedelta:
            self.repeatEvery = repeat
        else:
            self.repeatEvery = None
            
    def __str__(self):
        return str({"Start time": self.startTime,
                    "End time": self.endTime,
                    "Total labor": self.totalLabor,
                    "Repeat every": self.repeatEvery})
            
    def PrintTask(self):
        print "Start time: ", self.startTime
        print "End time: ", self.endTime
        print "Total labor: ", self.totalLabor
        print "Repeats every: ", self.repeatEvery

    def InteractiveEditting(self):
        while True:
            self.PrintTask()
            print "Please enter the starting letter for what you want to edit"
            print "Or enter q to exit."
            startingString = raw_input("Change:")
            print
            if len(startingString) == 0: return
            elif "Start time".startswith(startingString):
                self.startTime = EditDateTime(self.startTime)
            elif "End time".startswith(startingString):
                self.endTime = EditDateTime(self.endTime)
            elif "Total labor".startswith(startingString):
                self.totalLabor = EditDateTime(self.totalLabor)
            else: return
            
class ToDoList:
    def __init__(self, listFile = "MyToDos.dat"):
        self.listFile = listFile
        try:
            f = open(listFile, 'r')
            self.dictionaryOfTasks = ast.literal_eval(f.read())
            f.close()
        except:
            self.dictionaryOfTasks = {}
            f.close()
        
    def MainMenu(self):
        while True:
            print "Press 1 to print all tasks."
            print "Press 2 to add a task."
            print "Press 3 to save."
            print "Press 0 to exit and save."
            option = raw_input("Option:")
            print
            if option == '1': self.PrintAllEvents()
            elif option == '2': self.AddTask()
            elif option == '3': self.Save()
            elif option == '0':
                self.Save()
                return
        
    def PrintAllEvents(self):
        for key in self.dictionaryOfTasks:
            print key
            self.dictionaryOfTasks[key].PrintTask()
            doNext = raw_input("Input n for next, p for previous, e to edit,"
                               " q to exit")
            print
            if doNext.startswith('n') or doNext.startswith('N'):
                pass
            elif doNext.startswith('p') or doNext.startswith('P'):
                pass
            elif doNext.startswith('e') or doNext.startswith('E'):
                self.dictionaryOfTasks[key].InteractiveEditting()
            else: return
            
    def Save(self):
        f = open(self.listFile, 'w')
        f.write(str(self.dictionaryOfTasks))
        f.close()
            
    def AddTask(self):
        name = raw_input("Input name of task:")
        print "Sample time: [2000, 12, 31, 23, 59, 59]"
        startDate = raw_input("Input start time:")
        startDate = ast.literal_eval(startDate)
        startDate = startDate + [0] * (6 - len(startDate))
        startDate = datetime.datetime(year=startDate[0],
                                      month=startDate[1],
                                      day=startDate[2],
                                      hour=startDate[3],
                                      minute=startDate[4],
                                      second=startDate[5])
        
        endDate = raw_input("Input end time:")
        endDate = ast.literal_eval(endDate)
        endDate = endDate + [0] * (6 - len(endDate))
        endDate = datetime.datetime(year=endDate[0],
                                    month=endDate[1],
                                    day=endDate[2],
                                    hour=endDate[3],
                                    minute=endDate[4],
                                    second=endDate[5])
        
        print "Sample labor time: [23, 59, 59]"
        labor = raw_input("Input estimated labor time:")
        labor = ast.literal_eval(labor)
        labor = labor + [0] * (3 - len(labor))
        labor = datetime.timedelta(hours=labor[0], minutes=labor[1], 
                                   seconds=labor[2])
        
        newTask = task(start=startDate, end=endDate, total=labor)
        self.dictionaryOfTasks[name] = newTask
        print
        
def MainDisplay(myToDoList):
    root = Tkinter.Tk()
    mainContainer = Tkinter.Frame(root)
    mainContainer.pack()
    
    addButton = Tkinter.Button(mainContainer)
    addButton["text"] = "Add Task"
    addButton.pack()
    
    showButton = Tkinter.Button(mainContainer)
    showButton["text"] = "Show Tasks"
    showButton.pack()
    
    root.mainloop()
    
myToDoList = ToDoList()
MainDisplay(myToDoList)