class DBStorage:
    def close(self):
        """
        calls remove() method on the private
        session attribute (self.__session).
        """
        self.__session.close()
