class Vs:
    def __init__(self,name,Occupation):
     self._name = name    # _ :protected
     self.__Occupation =Occupation # __: private
     
    def data(self):
        print(f"My name is " + self.name+" and I am a " + self.Occupation+ " at the GLA University")
    
s1=Vs("Varun Sharma", "Student")
s2=Vs("Parth Teotia", "Student")
s3=Vs("Anmol Kumar Mishra", "Student")
s4=Vs("Priyanshu Singh", "Student")
s1.data()
s2.data()
s3.data()
s4.data()