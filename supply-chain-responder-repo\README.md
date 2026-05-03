# 🚀 Autonomous Supply Chain Disruption Responder

An AI-powered real-time supply chain disruption detection and autonomous response system that proactively identifies and mitigates supply chain risks before they impact business operations.

## 🎯 Overview

This system leverages IBM watsonx AI and IBM Bob to autonomously detect supply chain disruptions (weather events, supplier delays, carrier issues, geopolitical tensions) and automatically execute mitigation strategies, reducing response time from hours to seconds.

## 🎥 Demo Video

[Link to demo video will be added here]

## ✨ Key Features

- **Real-time Disruption Detection**: Monitors multiple data sources for supply chain risks
- **Autonomous Response**: Automatically executes mitigation strategies without human intervention
- **Interactive Dashboard**: Visual interface showing active disruptions, suppliers, and orders
- **Impact Analysis**: Calculates financial and timeline impacts of disruptions
- **Resolution Options**: Provides multiple mitigation strategies with cost-benefit analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser

### Installation

```bash
# Clone the repository
git clone [repository-url]
cd supply-chain-responder-repo

# Install dependencies
pip install -r src/requirements.txt

# Run the demo server
cd src
python demo_server.py
```

### Access the Dashboard

Open your browser and navigate to:
```
http://localhost:8000/dashboard
```

## 📁 Project Structure

```
supply-chain-responder-repo/
├── README.md
├── docs/
│   ├── 01-Problem-Solution.md
│   ├── 02-Bob-Usage.md
│   └── 03-Exported-Bob-Report/
├── src/
│   ├── demo_server.py
│   ├── dashboard.html
│   ├── data/
│   └── requirements.txt
├── assets/
│   ├── screenshots/
│   └── bob_sessions/
├── .gitignore
└── LICENSE
```

## 🛠️ Technology Stack

- **Backend**: Python 3.8+
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/ML**: IBM watsonx, IBM Bob
- **Data**: JSON-based data storage

## 📊 Features Demonstrated

1. **Active Disruption Monitoring**: Tracks 3 active disruptions in real-time
2. **Supplier Management**: Monitors 6 global suppliers across multiple regions
3. **Order Tracking**: Manages 6 active orders with impact status
4. **Geopolitical Risk**: Prioritizes critical events like Middle East shipping disruptions
5. **Collapsible UI**: Interactive dashboard with expandable/collapsible sections

## 🤝 Contributing

This project was developed for the IBM watsonx Challenge. For questions or contributions, please refer to the documentation in the `docs/` folder.

## 📄 License

[License type to be specified]

## 👥 Team

[Team information to be added]

## 🙏 Acknowledgments

- IBM watsonx AI Platform
- IBM Bob AI Assistant
- IBM watsonx Challenge organizers