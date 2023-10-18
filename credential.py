class credential:
    """The credential class includes methods that create a username and password and determine 
    the strength of the password.
    """    
    def __init__(self, password: str, username: str):
        """Initializes a credential using the specified password and username.

        Args:
            password (str): specified password
            username (str): specified username

        :ivar __password: password for this credential
        :ivar __username: username for this credential

        Raises:
            ValueError: indicates specified password is None
            ValueError: indicates specified username is None
        """      
        try:
            if(password is None):
                raise ValueError('PASSWORD CANNOT BE NONE')
            if(username is None):
                raise ValueError('USERNAME CANNOT BE NONE')
        finally:
            self._password = password
            self._username = username

    def getPassword(self):  
        """Returns the password for the calling credential.

        Returns:
            str: password
        """
        return self._password
    
    def setPassword(self, password: str):
        """Sets the password in the calling credential to the specified password.

        Args:
            password (str): specified password

        Raises:
            ValueError: indicates specified password is None
        """    
        self._password = password

    def getUsername(self):  
        """Returns the username for the calling credential.

        Returns:
            str: username
        """
        return self._username
    
    def setUsername(self, username: str):
        """Sets the username in the calling credential to the specified username.

        Args:
            username (str): specified username

        Raises:
            ValueError: indicates specified username is None
        """    
        self._username = username

    def __strength(self):
        

        """Determines the strength of the calling credential's password based on its content and length.

        Returns:
            str: "Weak" if the password contains only numbers or only characters or 
            is fewer than 8 characters in length, else "Strong"
        """    
        if len(self.getPassword()) < 8 or self.getPassword().isalnum() or self.getPassword().isdigit():
            return 'Weak'
        else:
            return 'Strong'  
        
    def __str__(self):
        """Returns string representation of the calling credential.

        Returns:
            str: string representation of the calling credential
        """
        return f"Password={self.getPassword()} Username={self.getUsername()} password_strength={self.__strength()}"
    
    def __eq__(self, other):
        """Tests if the calling credential is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling credential is equal to the specified
            object, else False
        """        
        if(isinstance(other, credential)):
            if(self.getPassword() == other.getPassword() and self.getUsername() == other.getUsername()):
                return True
            else:
                return False
        else:
            return False
