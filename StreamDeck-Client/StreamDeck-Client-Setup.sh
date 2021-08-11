echo '  ____  _                            ____            _    '
echo ' / ___|| |_ _ __ ___  __ _ _ __ ___ |  _ \  ___  ___| | __'
echo " \___ \| __| '__/ _ \/ _` | '_ ` _ \| | | |/ _ \/ __| |/ /"
echo "  ___) | |_| | |  __/ (_| | | | | | | |_| |  __/ (__|   < "
echo " |____/ \__|_|  \___|\__,_|_| |_| |_|____/ \___|\___|_|\_\"
                                                          
# Installing StreamClient-Client ZIP and move to 
wget https://github.com/philliphqs/StreamDeck/archive/refs/tags/0.0.2-alpha.zip -O ~/etc/StreamDeck-0.0.2-alpha.zip

# Unzip File
cd ~/etc/
unzip StreamDeck-0.0.2-alpha.zip

# Add to startup
crontab -l > file; echo "@reboot ~/etc/StreamDeck-0.0.2-alpha/StreamDeck-Client/start.sh >> file; crontab file; rm file;

cd ~/etc/StreamDeck-0.0.2-alpha/StreamDeck-Client/
chmod +x start.sh
chmod +x command.sh

echo 'Finished installation of StreamDeck'
./start.sh