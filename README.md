# NetsoulFuel

## Overview
NetsoulFuel is a comprehensive security toolset designed for the Fuel Network Attackathon. It covers reconnaissance, vulnerability scanning, and exploit development.

## Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/jeytuan/NetsoulFuel.git
    cd NetsoulFuel
    ```

2. Set up the virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    pip install -r requirements.txt
    ```

3. Update environment variables in `.env`:
    ```plaintext
    GITHUB_TOKEN=<your_github_token>
    SHODAN_API_KEY=<your_shodan_api_key>
    ```

## Usage
1. Run Initial Setup:
    ```sh
    bash scripts/setup_env.sh
    ```

2. Start Scanning and Exploit Development:
    ```sh
    bash scripts/run_scans.sh
    ```

## Tools
- **fuelup**: Toolchain manager for Fuel.
- **forc**: Fuel command-line tool.
- **rustup**: Rust toolchain installer.
- **Sway**: Smart contract language for Fuel.
- **Slither**: Static analysis tool for Solidity.
- **Mythril**: Security analysis tool for Ethereum smart contracts.
- **Echidna**: Smart contract fuzzer for Ethereum.
- **Foundry**: Ethereum application development toolkit.
- **Hardhat**: Development environment for Ethereum software.

## Contributing
If you wish to contribute, please fork the repository and submit a pull request.

## Contact
For more information, contact:
- Justin Nguyen ([@jeytuan](mailto:justin@net-soul.com))
- Louis DeGuzman ([@louis](mailto:louis@net-soul.com))
