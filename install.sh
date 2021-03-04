

echo "[+] Install All requirements"
echo "Press any key to install..."
read

pip3 install -r requirements.txt
clear
echo "[+] Requirements successfully installed"
echo "[+] Running main.py"
python3 main.py
