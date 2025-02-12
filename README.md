---
title: 'Setting up a Node: Lodestar and Geth'

---

1. Create a Docker Container

   ```bash 
   docker run -dit --name node_four --privileged --cgroupns=host --restart unless-stopped --network host   ubuntu:jammy
   ```

   ```bash
   docker exec -it node_four bash
   ```

2. Update the system and install dependencies

    ``` bash 
    apt-get update && apt-get upgrade -y
    ```

    ```bash
     apt install -y \
     curl \
     wget \
     git \
     jq \
     nano \
     sudo \
     unzip \
     software-properties-common \
     ca-certificates \
     ufw \
     gnupg
    ```
    
    
    ```bash
    apt-get install -y curl git build-essential python3 python3-pip cmake libssl-dev pkg-config openssl
    ```
    
3. Install NodeJS

   ```bash
   
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash export NVM_DIR="$HOME/.nvm" [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   ```

   ```bash 
    nvm install 22 && nvm use 22 
    ```
    
   ```bash 
   npm install -g yarn
   ```
   
   
4. Install Go Lang for Geth

    ```bash
    curl -LO https://go.dev/dl/go1.21.1.linux-amd64.tar.gz tar -C /usr/local -xzf go1.21.1.linux-amd64.tar.gz echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc source ~/.bashrc```


5. Create JWT

     ```bash
     mkdir -p /jwt
     ```
     
     ```bash
     openssl rand -hex 32 > /jwt/jwt.hex  # Generates       a 64-character hex secret
     ```
     
6. Install Geth
    ```bash
    git clone https://github.com/ethereum/go-ethereum.git
    cd go-ethereum
   make geth
   cp build/bin/geth /usr/local/bin/
   cd ..
    ```
    
    
    make geth error fix
    ```bash
    sudo apt remove golang-go  # For Debian/Ubuntu-based systems
    wget https://go.dev/dl/go1.22.4.linux-arm64.tar.gz
    sudo rm -rf /usr/local/go  # Remove old installation (if any)
    sudo tar -C /usr/local -xzf go1.22.4.linux-arm64.tar.gz
    #Add the following line to your shell profile (e.g., ~/.bashrc or ~/.zshrc): export PATH="$PATH:/usr/local/go/bin"
    source ~/.bashrc  # or source ~/.zshrc
    make geth
    
7. Install and build Lodestar

   ```bash
   git clone https://github.com/ChainSafe/lodestar.git
   cd lodestar
   yarn install --ignore-optional
   yarn build
   npm link
   cd ..
   ```
8. Create the start script

   ```bash
   #!/bin/bash

    # Start Lodestar with JWT authentication
    lodestar beacon \
      --network goerli \
      --eth1 \
      --execution.urls http://localhost:8551 \
      --jwt-secret /root/jwt/jwt.hex

   # Start Geth with JWT authentication
   geth \
     --http \
     --http.addr 0.0.0.0 \
     --http.api eth,net,web3,engine,admin \
     --authrpc.jwtsecret /root/jwt/jwt.hex \
     --authrpc.port 8551 \
     --authrpc.addr 0.0.0.0 &

   ```
1. Create a Docker Container

   ```bash 
   docker run -dit --name node_four --privileged --cgroupns=host --restart unless-stopped --network host   ubuntu:jammy
   ```

   ```bash
   docker exec -it node_four bash
   ```

2. Update the system and install dependencies

    ``` bash 
    apt-get update && apt-get upgrade -y
    ```

    ```bash
     apt install -y \
     curl \
     wget \
     git \
     jq \
     nano \
     sudo \
     unzip \
     software-properties-common \
     ca-certificates \
     ufw \
     gnupg
    ```
    
    
    ```bash
    apt-get install -y curl git build-essential python3 python3-pip cmake libssl-dev pkg-config openssl
    ```
    
3. Install NodeJS

   ```bash
   
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash export NVM_DIR="$HOME/.nvm" [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   ```

   ```bash 
    nvm install 22 && nvm use 22 
    ```
    
   ```bash 
   npm install -g yarn
   ```
   
   
4. Install Go Lang for Geth

    ```bash
    curl -LO https://go.dev/dl/go1.21.1.linux-amd64.tar.gz tar -C /usr/local -xzf go1.21.1.linux-amd64.tar.gz echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc source ~/.bashrc```


5. Create JWT

     ```bash
     mkdir -p /jwt
     ```
     
     ```bash
     openssl rand -hex 32 > /jwt/jwt.hex  # Generates       a 64-character hex secret
     ```
     
6. Install Geth
    ```bash
    git clone https://github.com/ethereum/go-ethereum.git
    cd go-ethereum
   make geth
   cp build/bin/geth /usr/local/bin/
   cd ..
    ```
    
    
    make geth error fix
    ```bash
    sudo apt remove golang-go  # For Debian/Ubuntu-based systems
    wget https://go.dev/dl/go1.22.4.linux-arm64.tar.gz
    sudo rm -rf /usr/local/go  # Remove old installation (if any)
    sudo tar -C /usr/local -xzf go1.22.4.linux-arm64.tar.gz
    #Add the following line to your shell profile (e.g., ~/.bashrc or ~/.zshrc): export PATH="$PATH:/usr/local/go/bin"
    source ~/.bashrc  # or source ~/.zshrc
    make geth
    
7. Install and build Lodestar

   ```bash
   git clone https://github.com/ChainSafe/lodestar.git
   cd lodestar
   yarn install --ignore-optional
   yarn build
   npm link
   cd ..
   ```
8. 
