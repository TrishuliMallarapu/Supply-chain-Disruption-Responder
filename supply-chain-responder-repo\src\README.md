# Source Code

This directory contains the core implementation of the Autonomous Supply Chain Disruption Responder.

## Files

### Main Application
- **demo_server.py** - Python HTTP server with RESTful API endpoints
- **dashboard.html** - Interactive web dashboard with real-time updates

### Data
- **data/demo_scenarios.json** - Disruption scenarios with impact analysis
- **data/test_data.json** - Sample suppliers, orders, customers, and inventory

### Dependencies
- **requirements.txt** - Python package dependencies

## Running the Application

### Prerequisites
```bash
python --version  # Requires Python 3.8+
```

### Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

### Start the Server
```bash
# Run the demo server
python demo_server.py
```

The server will start on `http://localhost:8000`

### Access the Dashboard
Open your browser and navigate to:
```
http://localhost:8000/dashboard
```

## API Endpoints

### GET /api/dashboard
Returns dashboard metrics including active disruptions, suppliers, and orders.

**Response:**
```json
{
  "status": "operational",
  "metrics": {
    "active_disruptions": 3,
    "total_suppliers": 6,
    "active_orders": 6,
    "available_scenarios": 6
  }
}
```

### GET /api/scenarios
Returns all disruption scenarios with their status and impact data.

**Response:**
```json
{
  "total": 6,
  "scenarios": [...]
}
```

### GET /api/suppliers
Returns all suppliers with their details and reliability scores.

**Response:**
```json
{
  "total": 6,
  "suppliers": [...]
}
```

### GET /api/orders
Returns all orders with their status and delivery information.

**Response:**
```json
{
  "total": 7,
  "active": 6,
  "orders": [...]
}
```

## Data Structure

### Scenarios (demo_scenarios.json)
Each scenario includes:
- ID, name, description
- Severity level (critical, high, medium)
- Status (active, monitoring)
- Event details (type, source, timestamp)
- Expected impact (affected orders, customers, costs, delays)
- Recommended actions (mitigation strategies with cost-benefit analysis)

### Test Data (test_data.json)
Includes:
- **Suppliers**: 6 global suppliers across Asia, North America, Europe, and Middle East
- **Orders**: 7 orders with various statuses and priorities
- **Customers**: 5 customers with SLA requirements
- **SKUs**: 5 product types with pricing and lead times
- **Inventory**: Warehouse stock levels across multiple locations

## Features

### Dashboard
- Real-time metrics display
- Collapsible sections for Disruption Events, Suppliers, and Active Orders
- Status badges (Active/Monitoring, Impacted/Monitoring)
- Refresh buttons for manual data updates
- Auto-refresh every 30 seconds

### Impact Analysis
- Side panel with detailed disruption analysis
- Baseline vs. mitigation cost comparisons
- Time savings calculations
- Multiple resolution options with execution simulation

### Data Management
- JSON-based data storage
- Absolute path resolution for reliable file loading
- Dynamic calculation of active disruptions
- Relationship mapping between entities

## Development

### Code Structure
```
src/
├── demo_server.py          # HTTP server and API logic
├── dashboard.html          # Frontend UI
├── data/
│   ├── demo_scenarios.json # Disruption scenarios
│   └── test_data.json      # Sample data
└── requirements.txt        # Dependencies
```

### Key Functions

**demo_server.py:**
- `get_dashboard_data()` - Aggregates metrics from data files
- `get_suppliers_data()` - Loads and returns supplier information
- `get_orders_data()` - Filters and returns active orders
- `get_scenarios_data()` - Loads disruption scenarios

**dashboard.html:**
- `loadDashboard()` - Fetches and displays dashboard metrics
- `loadScenarios()` - Loads and sorts disruption events
- `loadSuppliers()` - Displays supplier table with impact status
- `loadOrders()` - Shows active orders with delivery information
- `showImpactAnalysis()` - Opens side panel with detailed analysis
- `toggleSection()` - Handles collapse/expand functionality

## Testing

### Verify Data Loading
```bash
python -c "import json; print('Scenarios:', len(json.load(open('data/demo_scenarios.json'))['scenarios'])); print('Suppliers:', len(json.load(open('data/test_data.json'))['suppliers']))"
```

### Test API Endpoints
```bash
# Using curl (if available)
curl http://localhost:8000/api/dashboard
curl http://localhost:8000/api/scenarios
curl http://localhost:8000/api/suppliers
curl http://localhost:8000/api/orders
```

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, modify the `PORT` variable in `demo_server.py`:
```python
PORT = 8080  # Change to any available port
```

### Data Not Loading
Ensure you're running the server from the `src/` directory or that the data files are in the correct relative path.

### Browser Cache Issues
Clear browser cache or use Ctrl+F5 (Windows) / Cmd+Shift+R (Mac) to force refresh.

## Future Enhancements

- Database integration (PostgreSQL, MongoDB)
- Real-time data streaming with WebSockets
- User authentication and authorization
- Multi-tenant support
- Advanced analytics and reporting
- Mobile-responsive design improvements
- Integration with external APIs (weather, news, shipping)