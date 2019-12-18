# Using Singleton Pattern 
# This class is allwed to have only one instance. No matter how many time we call it, it will always return the same instance of the class.
# Solves issues relatd to persistence like session transfer, database management, etc.

class Singleton_Lazy(object):
    __instance = None
    
    def __init__(self):
        if not Singleton_Lazy.__instance:
            print("I have already got an instance.")
        else:
            print("I do not have an instance yet.")
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_Lazy()
        return cls.__instance
    
class Singleton_Strict(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_Strict, cls).__new__(cls)
        return cls.instance
    
    
sL1 = Singleton_Lazy()
sL2 = Singleton_Lazy()
print("sL1: %s, sL2: %s ",(sL1.getInstance(), sL2.getInstance()) )

sS1 = Singleton_Strict()
sS2 = Singleton_Strict()
print("sS1: %s, sS2: %s ",(sS1, sS2))

