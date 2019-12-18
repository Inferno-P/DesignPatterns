from abc import ABCMeta, abstractmethod
import time
# Useful to replicate instances of function objects across multiple objects.

class Platform(metaclass=ABCMeta):
    @abstractmethod
    def stop_systems(self):
        raise NotImplementedError('Please implement the method!')
    
    @abstractmethod
    def start_systems(self):
        raise NotImplementedError('Please implement the method <>!')
    
    @abstractmethod
    def health_check_systems(self):
        raise NotImplementedError('Please implement the method <>!')
    

class WebServer(Platform):
    __nodes = ['web_node_a','web_node_b', 'web_node_c']
    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping system : {}".format(system))
            time.sleep(0.5)
    
    def start_systems(self):
        for system in self.__nodes:
            print("Starting system : {}".format(system))
            time.sleep(0.5)
    
    def health_check_systems(self):
        for system in self.__nodes:
            print("Checking health of the system : {}".format(system))
            time.sleep(0.5)

class Firewall(Platform):
    __nodes = ['fw_node_a','fw_node_b', 'fw_node_c']
    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping system : {}".format(system))
            time.sleep(0.5)
    
    def start_systems(self):
        for system in self.__nodes:
            print("Starting system : {}".format(system))
            time.sleep(0.5)
    
    def health_check_systems(self):
        for system in self.__nodes:
            print("Checking health of the system : {}".format(system))
            time.sleep(0.5)

class AppServer(Platform):
    __nodes = ['app_node_a','app_node_b', 'app_node_c']
    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping system : {}".format(system))
            time.sleep(0.5)
    
    def start_systems(self):
        for system in self.__nodes:
            print("Starting system : {}".format(system))
            time.sleep(0.5)
    
    def health_check_systems(self):
        for system in self.__nodes:
            print("Checking health of the system : {}".format(system))
            time.sleep(0.5)


class PatchingFactory(object):
    def stop_all(self, platform_object):
        return eval(platform_object)().stop_systems()
    
    def start_all(self, platform_object):
        return eval(platform_object)().start_systems()

    def hc_all(self, platform_object):
        return eval(platform_object)().health_check_systems()
    
    def make_magic_happen(self, platform_object):
        self.hc_all(platform_object)
        self.stop_all(platform_object)
        self.start_all(platform_object)
        self.hc_all(platform_object)


PF = PatchingFactory()
platform_to_stop = input("Which platform to stop? ")
PF.stop_all(platform_to_stop)
PF.hc_all(platform_to_stop)
PF.start_all(platform_to_stop)
PF.stop_all(platform_to_stop)
PF.hc_all(platform_to_stop)
