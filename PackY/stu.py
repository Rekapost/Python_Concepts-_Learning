class student:
    def __init__(self,stuid,stuname):
        self.stuid=stuid
        self.stuname=stuname


    def displaystu(self):
       print("student id={} student name={}".format(self.stuid, self.stuname))
        # or  print("employee id= %d name=%s employee salary=%g" %(self.eid,self.ename,self.esal))