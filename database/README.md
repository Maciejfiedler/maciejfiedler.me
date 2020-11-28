After creation of the database set a password

    redis-cli
    AUTH mypassword
    CONFIG SET requirepass "mypassword"
    AUTH "mypassword"
    

