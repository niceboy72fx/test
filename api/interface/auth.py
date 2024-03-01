import abc

class Auth(abc.ABC):
    @abc.abstractmethod
    def get_user(self):
        pass
    
    @abc.abstractmethod
    def create_user(self):
        pass
    
    @abc.abstractmethod
    def update_user(self):
        pass
    
    