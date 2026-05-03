# Assets Directory

This directory contains screenshots, UI mockups, and other visual assets for the Autonomous Supply Chain Disruption Responder project.

## Directory Structure

```
assets/
├── screenshots/
│   ├── dashboard-overview.png
│   ├── disruption-events.png
│   ├── impact-analysis.png
│   ├── suppliers-view.png
│   ├── active-orders.png
│   └── collapse-expand-demo.png
│
└── bob_sessions/
    ├── bob-conversation-screenshots/
    ├── data-loading-fix.png
    ├── prioritization-implementation.png
    ├── collapse-functionality.png
    └── repository-preparation.png
```

## Screenshots to Include

### Dashboard Screenshots

1. **dashboard-overview.png** - Full dashboard view showing all sections
2. **disruption-events.png** - Disruption Events section with Middle East scenario on top
3. **impact-analysis.png** - Side panel showing impact & resolution analysis
4. **suppliers-view.png** - Suppliers table with impact status
5. **active-orders.png** - Active Orders table with delivery information
6. **collapse-expand-demo.png** - Demonstration of collapsible sections

### Bob Session Screenshots

1. **bob-conversation-screenshots/** - Folder containing key conversation screenshots
2. **data-loading-fix.png** - Bob helping resolve data loading issues
3. **prioritization-implementation.png** - Implementing Middle East scenario prioritization
4. **collapse-functionality.png** - Adding collapse/expand to all sections
5. **repository-preparation.png** - Preparing the project for Git submission

## How to Capture Screenshots

### Dashboard Screenshots:
1. Run the demo server: `python src/demo_server.py`
2. Open browser to `http://localhost:8000/dashboard`
3. Use browser screenshot tools or Snipping Tool (Windows) / Screenshot (Mac)
4. Save with descriptive names in the `screenshots/` folder

### Bob Session Screenshots:
1. Open IBM Bob interface
2. Navigate to relevant conversations
3. Capture screenshots of key interactions
4. Save in the `bob_sessions/` folder

## Image Guidelines

- **Format**: PNG preferred for screenshots (lossless)
- **Resolution**: Minimum 1920x1080 for dashboard screenshots
- **File Size**: Keep under 2MB per image (compress if needed)
- **Naming**: Use lowercase with hyphens (e.g., `dashboard-overview.png`)

## Notes

These assets are essential for:
- Project documentation
- Demo presentations
- GitHub repository README
- IBM watsonx Challenge submission
- Showcasing Bob's contribution to development