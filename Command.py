from abc import ABCMeta, abstractmethod

#Base Class
class Transaction(metaclass = ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    
#Child Class 1
class SELECT(Transaction):
    def __init__(self, transaction):
        self.trans = transaction
     
    def execute(self):
        self.trans.SELECT()

#Child Class 2        
class INSERT(Transaction):
    def __init__(self, transaction):
        self.trans = transaction
    
    def execute(self):
        self.trans.INSERT()

#Child Class 3
class UPDATE(Transaction):
    def __init__(self, transaction):
        self.trans = transaction
    
    def execute(self):
        self.trans.UPDATE()


class TransactionManager:
    def SELECT(self):
        print("Performing SELECT Operation.")
        
    def INSERT(self):
        print("Performing INSERT Operation.")
    
    def UPDATE(self):
        print("Performing UPDATE Operation.")


class TransactionBroker:
    def __init__(self,):
        self.__transactionQueue = []
        
    def requestTransaction(self, transaction):
        self.__transactionQueue.append(transaction)
        transaction.execute()


if __name__  == '__main__':
    transaction = TransactionManager()
    tr_select = SELECT(transaction)
    tr_insert = INSERT(transaction)
    tr_update = UPDATE(transaction)
    
    broker = TransactionBroker()
    broker.requestTransaction(tr_select)
    broker.requestTransaction(tr_insert)
    broker.requestTransaction(tr_update)
    broker.requestTransaction(tr_select)
    broker.requestTransaction(tr_insert)
    broker.requestTransaction(tr_select)
    broker.requestTransaction(tr_insert)
    broker.requestTransaction(tr_select)
    broker.requestTransaction(tr_insert)
