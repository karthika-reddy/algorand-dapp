# 🔷 Algorand Project

A blockchain development project built on the **Algorand** network, exploring smart contracts, ASAs (Algorand Standard Assets), and decentralized applications (dApps).

---

## 📌 Project Overview

This repository contains my work throughout the Algorand development course. The goal is to build and deploy a functional decentralized application on the Algorand blockchain using modern tools like AlgoKit, the Python SDK, and Pera Wallet integration.

---

## 🚀 Features (Planned)

- 📝 Smart contract development using **Algorand Python / TEALScript**
- 🪙 Creation and management of **Algorand Standard Assets (ASAs)**
- 🔗 dApp integration via **WalletConnect** and **Pera Wallet**
- 🧪 Local testing using **AlgoKit LocalNet**
- 🌐 Deployment to **TestNet** and eventually **MainNet**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [AlgoKit](https://github.com/algorandfoundation/algokit-cli) | Project scaffolding & local development |
| [Algorand Python SDK](https://github.com/algorand/py-algorand-sdk) | Blockchain interaction |
| [Pera Wallet](https://perawallet.app/) | Wallet integration |
| [AlgoKit LocalNet](https://developer.algorand.org/) | Local testing environment |
| Python 3.8+ | Primary development language |

---

## 📁 Project Structure

```
algorand-dapp/
├── contracts/        # Smart contract source files
├── src/              # Application source code
├── tests/            # Unit and integration tests
├── scripts/          # Deployment and utility scripts
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8 or above
- [AlgoKit](https://github.com/algorandfoundation/algokit-cli) installed
- [Docker](https://www.docker.com/) (for LocalNet)

### Installation

```bash
# Clone the repository
git clone https://github.com/karthika-reddy/algorand-dapp.git
cd algorand-dapp

# Install dependencies
pip install -r requirements.txt

# Start AlgoKit LocalNet
algokit localnet start
```

---

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/
```

---

## 🌐 Network Configuration

| Network | Purpose |
|---------|---------|
| **LocalNet** | Local development & testing |
| **TestNet** | Pre-deployment testing (free TestNet ALGO) |
| **MainNet** | Production deployment |

---

## 📚 Resources

- [Algorand Developer Docs](https://developer.algorand.org/)
- [AlgoKit Documentation](https://github.com/algorandfoundation/algokit-cli)
- [Pera Wallet](https://perawallet.app/)
- [Algorand Stack Exchange](https://stackoverflow.com/questions/tagged/algorand)
- [Algorand Discord](https://discord.gg/algorand)

---

## 📄 License

This project is licensed under the MIT License.

---

> Built with ❤️ on the Algorand blockchain.
