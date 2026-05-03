"""
Standalone Demo Server for Autonomous Supply Chain Disruption Responder
Runs without external dependencies for demonstration purposes
"""
import json
import http.server
import socketserver
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import webbrowser
import threading
import os

PORT = 8000

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class DemoHandler(http.server.SimpleHTTPRequestHandler):
    """Demo HTTP request handler"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_home_page().encode())
            
        elif parsed_path.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "healthy",
                "timestamp": datetime.utcnow().isoformat(),
                "version": "1.0.0",
                "active_disruptions": 0
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
        
        elif parsed_path.path == '/api/dashboard':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            dashboard_data = self.get_dashboard_data()
            self.wfile.write(json.dumps(dashboard_data, indent=2).encode())
        
        elif parsed_path.path == '/api/suppliers':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            suppliers_data = self.get_suppliers_data()
            self.wfile.write(json.dumps(suppliers_data, indent=2).encode())
        
        elif parsed_path.path == '/api/orders':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            orders_data = self.get_orders_data()
            self.wfile.write(json.dumps(orders_data, indent=2).encode())
        
        elif parsed_path.path == '/api/scenarios':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            scenarios_data = self.get_scenarios_data()
            self.wfile.write(json.dumps(scenarios_data, indent=2).encode())
        
        elif parsed_path.path == '/dashboard':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                dashboard_path = os.path.join(SCRIPT_DIR, 'dashboard.html')
                with open(dashboard_path, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode())
            except FileNotFoundError:
                self.wfile.write(b'<h1>Dashboard not found</h1><p>dashboard.html file is missing</p>')
            
        elif parsed_path.path == '/docs':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_docs_page().encode())
            
        elif parsed_path.path == '/demo':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_demo_page().encode())
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/events':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                event_data = json.loads(post_data.decode())
                response = self.process_event(event_data)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response, indent=2).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_response = {"error": str(e)}
                self.wfile.write(json.dumps(error_response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def process_event(self, event_data):
        """Simulate event processing"""
        event_type = event_data.get('type', 'unknown')
        
        # Simulate disruption detection
        disruption_detected = event_type in ['weather', 'supplier', 'carrier', 'port']
        
        if not disruption_detected:
            return {
                "status": "no_disruption",
                "processing_time_seconds": 0.1
            }
        
        # Simulate full response
        return {
            "status": "success",
            "disruption_id": f"disruption-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            "severity": "high",
            "impacted_orders": 15,
            "actions_taken": 3,
            "requires_approval": False,
            "processing_time_seconds": 0.5,
            "response": {
                "mode": "autonomous",
                "actions_executed": 3,
                "actions_failed": 0,
                "customers_notified": 8,
                "execution_details": {
                    "total_actions": 3,
                    "successful": 3,
                    "failed": 0,
                    "actions": [
                        {
                            "action_id": "action-001",
                            "action_type": "reroute_supplier",
                            "success": True,
                            "message": "Supplier reroute completed successfully"
                        },
                        {
                            "action_id": "action-002",
                            "action_type": "expedite_shipment",
                            "success": True,
                            "message": "Shipment expedite completed successfully"
                        },
                        {
                            "action_id": "action-003",
                            "action_type": "reallocate_inventory",
                            "success": True,
                            "message": "Inventory reallocation completed successfully"
                        }
                    ]
                }
            }
        }
    
    def get_dashboard_data(self):
        """Load dashboard data from test_data.json and demo_scenarios.json"""
        try:
            # Load test data
            test_data_path = os.path.join(SCRIPT_DIR, 'data', 'test_data.json')
            with open(test_data_path, 'r') as f:
                test_data = json.load(f)
            
            # Load scenarios
            scenarios_path = os.path.join(SCRIPT_DIR, 'data', 'demo_scenarios.json')
            with open(scenarios_path, 'r') as f:
                scenarios_data = json.load(f)
            
            # Get active orders count
            active_orders = [o for o in test_data.get('orders', []) if o['status'] in ['in_transit', 'processing']]
            
            # Count active disruptions (scenarios with status='active')
            active_disruptions = len([s for s in scenarios_data.get('scenarios', []) if s.get('status') == 'active'])
            
            return {
                "status": "operational",
                "timestamp": datetime.utcnow().isoformat(),
                "metrics": {
                    "active_disruptions": active_disruptions,
                    "total_suppliers": len(test_data.get('suppliers', [])),
                    "active_orders": len(active_orders),
                    "total_orders": len(test_data.get('orders', [])),
                    "available_scenarios": len(scenarios_data.get('scenarios', []))
                },
                "recent_activity": []
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "metrics": {
                    "active_disruptions": 0,
                    "total_suppliers": 0,
                    "active_orders": 0,
                    "total_orders": 0,
                    "available_scenarios": 0
                }
            }
    
    def get_suppliers_data(self):
        """Load suppliers from test_data.json"""
        try:
            test_data_path = os.path.join(SCRIPT_DIR, 'data', 'test_data.json')
            with open(test_data_path, 'r') as f:
                test_data = json.load(f)
            return {
                "total": len(test_data.get('suppliers', [])),
                "suppliers": test_data.get('suppliers', [])
            }
        except Exception as e:
            return {"error": str(e), "suppliers": []}
    
    def get_orders_data(self):
        """Load orders from test_data.json"""
        try:
            test_data_path = os.path.join(SCRIPT_DIR, 'data', 'test_data.json')
            with open(test_data_path, 'r') as f:
                test_data = json.load(f)
            orders = test_data.get('orders', [])
            active_orders = [o for o in orders if o['status'] in ['in_transit', 'processing']]
            return {
                "total": len(orders),
                "active": len(active_orders),
                "orders": orders
            }
        except Exception as e:
            return {"error": str(e), "orders": []}
    
    def get_scenarios_data(self):
        """Load scenarios from demo_scenarios.json"""
        try:
            scenarios_path = os.path.join(SCRIPT_DIR, 'data', 'demo_scenarios.json')
            with open(scenarios_path, 'r') as f:
                scenarios_data = json.load(f)
            return {
                "total": len(scenarios_data.get('scenarios', [])),
                "scenarios": scenarios_data.get('scenarios', []),
                "demo_sequence": scenarios_data.get('demo_sequence', [])
            }
        except Exception as e:
            return {"error": str(e), "scenarios": []}
    
    def get_home_page(self):
        """Generate home page HTML"""
        return """
<!DOCTYPE html>
<html>
<head>
    <title>Autonomous Supply Chain Disruption Responder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .status {
            display: inline-block;
            padding: 5px 15px;
            background: #10b981;
            color: white;
            border-radius: 20px;
            font-size: 14px;
        }
        .button {
            display: inline-block;
            padding: 12px 24px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            margin: 10px 10px 10px 0;
        }
        .button:hover {
            background: #5568d3;
        }
        .feature {
            margin: 15px 0;
            padding: 10px;
            border-left: 4px solid #667eea;
        }
        .metric {
            display: inline-block;
            margin: 10px 20px 10px 0;
            padding: 15px;
            background: #f0f9ff;
            border-radius: 6px;
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }
        .metric-label {
            font-size: 12px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Autonomous Supply Chain Disruption Responder</h1>
        <p>AI-powered autonomous system for detecting and resolving supply chain disruptions</p>
        <span class="status">✓ OPERATIONAL</span>
    </div>
    
    <div class="card">
        <h2>System Status</h2>
        <div class="metric">
            <div class="metric-value">0</div>
            <div class="metric-label">Active Disruptions</div>
        </div>
        <div class="metric">
            <div class="metric-value">100%</div>
            <div class="metric-label">System Health</div>
        </div>
        <div class="metric">
            <div class="metric-value"><5min</div>
            <div class="metric-label">Detection Speed</div>
        </div>
        <div class="metric">
            <div class="metric-value">85%+</div>
            <div class="metric-label">Success Rate</div>
        </div>
    </div>
    
    <div class="card">
        <h2>Quick Links</h2>
        <a href="/dashboard" class="button">📊 Dashboard</a>
        <a href="/docs" class="button">📚 API Documentation</a>
        <a href="/demo" class="button">🎮 Interactive Demo</a>
        <a href="/health" class="button">💚 Health Check</a>
    </div>
    
    <div class="card">
        <h2>Key Features</h2>
        <div class="feature">
            <strong>✓ Real-time Detection</strong> - Monitors weather, suppliers, carriers, and ports
        </div>
        <div class="feature">
            <strong>✓ Intelligent Analysis</strong> - Assesses impact on orders, SKUs, and customers
        </div>
        <div class="feature">
            <strong>✓ Autonomous Execution</strong> - 9 mitigation actions with rollback support
        </div>
        <div class="feature">
            <strong>✓ Proactive Communication</strong> - Multi-channel customer notifications
        </div>
        <div class="feature">
            <strong>✓ Continuous Learning</strong> - Tracks outcomes to improve decisions
        </div>
    </div>
    
    <div class="card">
        <h2>API Endpoints</h2>
        <p><code>POST /events</code> - Process disruption events</p>
        <p><code>GET /health</code> - System health check</p>
        <p><code>GET /docs</code> - API documentation</p>
        <p><code>GET /demo</code> - Interactive demo</p>
    </div>
    
    <div class="card">
        <p style="text-align: center; color: #666;">
            Built with ❤️ for autonomous supply chain resilience<br>
            Version 1.0.0 | Running on port """ + str(PORT) + """
        </p>
    </div>
</body>
</html>
        """
    
    def get_docs_page(self):
        """Generate API documentation page"""
        return """
<!DOCTYPE html>
<html>
<head>
    <title>API Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .endpoint { background: #f8f9fa; padding: 15px; margin: 15px 0; border-radius: 6px; }
        .method { display: inline-block; padding: 4px 12px; border-radius: 4px; font-weight: bold; }
        .post { background: #10b981; color: white; }
        .get { background: #3b82f6; color: white; }
        code { background: #e5e7eb; padding: 2px 6px; border-radius: 3px; }
        pre { background: #1f2937; color: #f3f4f6; padding: 15px; border-radius: 6px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>📚 API Documentation</h1>
    <p><a href="/">← Back to Home</a></p>
    
    <div class="endpoint">
        <span class="method post">POST</span> <code>/events</code>
        <p>Process a disruption event and trigger autonomous response</p>
        <pre>{
  "type": "weather",
  "source": "weather_api",
  "data": {
    "event_type": "hurricane",
    "severity": "severe",
    "location": {"region": "Southeast US"},
    "affected_suppliers": ["SUP-001"],
    "duration_hours": 48
  }
}</pre>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span> <code>/health</code>
        <p>Check system health status</p>
        <pre>{
  "status": "healthy",
  "timestamp": "2026-05-01T22:00:00.000Z",
  "version": "1.0.0",
  "active_disruptions": 0
}</pre>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span> <code>/docs</code>
        <p>View this API documentation</p>
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span> <code>/demo</code>
        <p>Access interactive demo interface</p>
    </div>
</body>
</html>
        """
    
    def get_demo_page(self):
        """Generate interactive demo page"""
        return """
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Demo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .demo-section { background: white; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        button { padding: 12px 24px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer; margin: 5px; }
        button:hover { background: #5568d3; }
        #response { background: #1f2937; color: #f3f4f6; padding: 15px; border-radius: 6px; margin-top: 15px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>🎮 Interactive Demo</h1>
    <p><a href="/">← Back to Home</a></p>
    
    <div class="demo-section">
        <h2>Test Disruption Scenarios</h2>
        <p>Click a button to simulate a disruption event:</p>
        <button onclick="testEvent('weather')">🌪️ Weather Disruption</button>
        <button onclick="testEvent('supplier')">🏭 Supplier Delay</button>
        <button onclick="testEvent('carrier')">🚚 Carrier Issue</button>
        <button onclick="testEvent('port')">⚓ Port Congestion</button>
        <div id="response"></div>
    </div>
    
    <script>
        function testEvent(type) {
            const events = {
                weather: {
                    type: 'weather',
                    source: 'demo',
                    data: {
                        event_type: 'hurricane',
                        severity: 'severe',
                        location: {region: 'Southeast US'},
                        affected_suppliers: ['SUP-001'],
                        duration_hours: 48
                    }
                },
                supplier: {
                    type: 'supplier',
                    source: 'demo',
                    data: {
                        supplier_id: 'SUP-001',
                        delay_days: 5,
                        affected_skus: ['SKU-001', 'SKU-002']
                    }
                },
                carrier: {
                    type: 'carrier',
                    source: 'demo',
                    data: {
                        carrier_id: 'CARRIER-001',
                        on_time_percentage: 0.65,
                        affected_routes: ['ROUTE-001']
                    }
                },
                port: {
                    type: 'port',
                    source: 'demo',
                    data: {
                        port_id: 'PORT-001',
                        congestion_level: 0.85
                    }
                }
            };
            
            document.getElementById('response').textContent = 'Processing...';
            
            fetch('/events', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(events[type])
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => {
                document.getElementById('response').textContent = 'Error: ' + error;
            });
        }
    </script>
</body>
</html>
        """

def open_browser():
    """Open browser after short delay"""
    import time
    time.sleep(1.5)
    webbrowser.open(f'http://localhost:{PORT}/dashboard')

if __name__ == '__main__':
    print("=" * 60)
    print("Autonomous Supply Chain Disruption Responder")
    print("=" * 60)
    print(f"\nServer starting on http://localhost:{PORT}")
    print(f"Dashboard: http://localhost:{PORT}/dashboard")
    print(f"API Documentation: http://localhost:{PORT}/docs")
    print(f"Interactive Demo: http://localhost:{PORT}/demo")
    print(f"Health Check: http://localhost:{PORT}/health")
    print("\nDashboard will open automatically in your browser...")
    print("Press Ctrl+C to stop the server\n")
    
    # Open browser in background thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Start server
    with socketserver.TCPServer(("", PORT), DemoHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped")
            print("=" * 60)

# Made with Bob
