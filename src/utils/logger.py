class Logger:
    """A custom logger class for ease of message passing.
    """
    __logging_class = None

    __HEADER = '\033[95m'
    __OKBLUE = '\033[94m'
    __OKCYAN = '\033[96m'
    __OKGREEN = '\033[92m'
    __WARNING = '\033[93m'
    __FAIL = '\033[91m'
    __ENDC = '\033[0m'
    __BOLD = '\033[1m'
    __UNDERLINE = '\033[4m'


    def __init__(self, logging_class: object):
        self.__logging_class = type(logging_class).__name__

    def info(self,message:str):
        """Prints the given message as info

        :param message: Message to be printed
        :type message: str
        """
        print(self.__OKGREEN + self.__BOLD + "[ INFO ]" + self.__ENDC + " " + self.__logging_class + " - " + message)

    def warning(self,message:str):
        """Prints the given message as warning

        :param message: Message to be printed
        :type message: str
        """
        print(self.__WARNING + self.__BOLD + "[ WARINING ]" + self.__ENDC + " " + self.__logging_class + " - " + message)

    def error(self,message:str):
        """Prints the given message as error

        :param message: Message to be printed
        :type message: str
        """
        print(self.__FAIL + self.__BOLD + "[ ERROR ]" + self.__ENDC + " " + self.__logging_class + " - " + message)

    def debug(self,message:str):
        """Prints the given message as debug

        :param message: Message to be printed
        :type message: str
        """
        print(self.__OKBLUE + self.__BOLD + "[ DEBUG ]" + self.__ENDC + " " + self.__logging_class + " - " + message)
