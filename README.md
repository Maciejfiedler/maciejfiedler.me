
# maciejfiedler.me

My website, that represents me and my interests. You can use this repository to setup your own personal website.

![enter image description here](https://github.com/Maciejfiedler/maciejfiedler.me/raw/main/Assets/Screenshot.png)

## Setup
The server runs in four Docker containers (webserver, frontend, backend and database).
You have to have Docker on your system installed.

Clone the project into your directory of choice and go into the maciejfiedler.me folder.

    git clone https://github.com/Maciejfiedler/maciejfiedler.me.git
    cd maciejfiedler.me

You have to setup some files, before you can run the server.

 - backend/data.json
 - database/redis.conf

Creates these files in there their directory.

*backend/data.json:* 

  	{ 
	    "users": {
		"admin": {"password": "ADMINPASSWORD"}
	    },
	    "database": {
		"redis_password": "REDISPASSWORD"
	    }
	}
*database/redis.conf*

    requirepass REDISPASSWORD
**Important**
Change REDISPASSWORD and ADMINPASSWORD to your password in production. Or else the website is vulnerable to attackers.

If you want it to have it easy to start, change and stop the Docker containers there are scripts. 

If you're on Linux, MacOS or other Unix based systems you have to give those scrips permission to run them

    chmod +x dev.sh prod_start.sh prod_changes.sh prod_stop.sh 

### Starting the Server
You can run the server with the `dev.sh` or `prod_start.sh` script. Use the `dev.sh` script for testing and developing and the `prod_start.sh` script for production (but I encourage to also test the production script before deploying to production).

In Windows:

    bash dev.sh
In Linux, MacOS and other Unix based systems:

    ./dev.sh

The Docker containers should now start.
After starting the Docker containers go to `172.26.0.101` in you're browser.
The browser that you're using will give you an error or a warning, because the website has a self-signed certificate, that browser don't trust (and you shouldn't on open website to). In production the warning will disappear, because the certificate is then signed by Let's Encrypt, a well known SSL/TLS  certificate signer.

If you want to bypass that warning or error you have to use Firefox because, the will just give a warning and the option to proceed to the website.

# Feedback
**Issues**
If you find an error or have a problem, you can create an Issue on the Issues page. You can also send me an email at  [maciek.fiedler@gmail.com](mailto:maciek.fiedler@gmail.com) and i will try to help you out.

**Contribute**
If you see a bug or want to contribute to the project, you can fork the repository and create a pull request.

