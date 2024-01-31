# Akraya-Backend
AI model optimized for CPU usage.

Powered by [ctransformers](https://github.com/marella/ctransformers/).

**Tested on Systems with Minimal Requirements**
- Intel Core i5-750
- 8GB DDR3 RAM
- 150GB HDD (for OS)
- 1.7TB (Fusion Drive SSD + HDD RAID-0)
- Ubuntu 22.04 Desktop
**Demonstrated System Specifications + The Recomended Ones (Hetzner Cloud VPS, €32/month)**
- 16 Cores (AMPER-ARM)
- 32GB RAM
- 350GB SSD 
- Ubuntu 22.04 (The available one)


Installation
Add SWAP Ram (64G insted of 1G in the tutorial) - Just Recomended [Digital Ocean Docs](https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04)

Copy and Paste *ONE-BY-ONE* the commands

apt update -y   
apt install python3-pip -y   
apt install git -y
git clone https://github.com/marella/ctransformers
cd ctransformers
CMAKE_ARGS="-DCT_CUBLAS=ON -DCT_INSTRUCTIONS=avx" pip install .
cd
git clone https://github.com/akraya-club/akraya-backned.git
cd akraya-backned


python3 main.py
