######## Property of Manthan. All Rights Reserved ########

import psycopg2

class Bootstrapper:
    __connection_string = ""

    def __init__(self, connection_string: str):
        """Member that takes care of the connection to the database

        :param connection_string: Database connection string
        :type connection_string: str
        """
        self.__connection_string = connection_string
    
    def serveConnection(self):
        try:
            connection = psycopg2.connect(self.__connection_string)
            cursor = connection.cursor()
            print("Done")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)