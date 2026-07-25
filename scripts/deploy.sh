#!/bin/bash
cd /home/ubuntu/my-portfolio

echo "==> Pulling latest code from GitHub"
git pull origin main

echo "==> Activating virtual environment"
source venv/bin/activate

echo "==> Installing dependencies"
pip install -r requirements.txt

echo "==> Running sanity check"
python -c "import application; print('App imports fine')"

echo "==> Restarting the app service"
sudo systemctl restart portflip

echo "==> Deployment finished successfully"
