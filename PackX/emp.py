class employee:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def displayemp(self):
        print("employee id={} employee name={} employee salary={}".format(self.eid, self.ename, self.esal))
        # or  print("employee id= %d name=%s employee salary=%g" %(self.eid,self.ename,self.esal))
