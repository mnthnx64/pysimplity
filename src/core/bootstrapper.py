######## Property of Manthan. All Rights Reserved ########

import psycopg2
import traceback
import sys
sys.path.append('./src')
from utils.logger import Logger

class Bootstrapper:
    """
    A class used to Connect to a database

    ...

    Methods
    -------
    serveConnection():
        serves a connection to the database and returns the cursor
    """
    __connection: psycopg2.extensions.connection = None
    __connection_string: str = ""
    __cursor: psycopg2.extensions.cursor = None

    def __init__(self, connection_string: str):
        """
        Member that takes care of the connection to the database==

        Args
        ----
        connection_string (str): Database Connection URI 
        """
        self.__connection_string = connection_string
        self.logger = Logger(self)

    
    def serveConnection(self):
        """
        Connect to a database.

        Returns
        -------
        DB Cursor - psycopg2.extenstions.cursor
        """
        try:
            self.logger.info("Trying to connect to " + self.__connection_string)
            self.__connection = psycopg2.connect(self.__connection_string)
            self.__cursor = self.__connection.cursor()
            self.logger.info("Connection Successful !")
            return self.__cursor
        except:
            self.logger.error("Error while connecting to PostgreSQL: " + str(sys.exc_info()[0].__name__))
            self.logger.error(str(traceback.format_exc()))

    def closeConnection(self):
        """
        Closes the connection to the database
        """
        self.logger.info("Closing DB connection")
        self.__cursor.close()
        self.__connection.close()
        self.__connection = None
        self.__cursor = None
        self.logger.warning("DB connection closed")

    def __del__(self):
        if(self.__connection):
            self.logger.warning("DB Connecection not closed Manually, closing now....")
            self.__cursor.close()
            self.__connection.close()
            self.logger.warning("DB connection closed on delete! This should be avoided for safer functionality!")