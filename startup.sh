# This file is optional and uses screen to create a terminal in a seperate window for this service
screen -dmS maciejfiedler.me-website
screen -S maciejfiedler.me-website -X stuff $'cd /home/maciejfieler/maciejfiedler.me/ \n'
screen -S maciejfiedler.me-website -X stuff $'./prod_start.sh \n'
