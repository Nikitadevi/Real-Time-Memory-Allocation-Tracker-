# Real-Time-Memory-Allocation-Tracker-Visulization

This project implements a real-time memory monitoring and visualization system that simulates memory allocation strategies (Paging and Segmentation) while dynamically tracking system memory usage. It is designed as a web-based application using Flask, which serves live memory data collected from the system and displays it interactively.

The core features include:

1. Real-Time Monitoring: A background service continuously collects system memory statistics using the psutil library, logging data such as used, free, total, and swap memory every second.

2. Memory Stress Simulation: A Python script artificially creates memory load using NumPy arrays to test how memory usage fluctuates under high demand.

3. Memory Allocation Simulation: Two classic memory management strategies—Paging and Segmentation—are simulated, showing how processes/pages or segments are managed in limited memory environments.

4. Data Visualization: A dynamic pie chart generated using Matplotlib reflects live memory usage (used vs. free memory), giving users an intuitive understanding of system resource utilization.

5. Web Interface: Users can access the application through a web browser, which provides an endpoint to view the current memory status in JSON format and a front-end to host the visual insights.

# How to Run the Project:-
# Create a Virtual Environment 
cd "repo-name"
python -m venv venv
# On Windows:
venv\Scripts\activate
# Install Required Dependencies
pip install flask psutil matplotlib numpy
#  Run the Flask App
python app.py
-->Then there will a link generated, Click on that link then Project will open

# Project Structure
├── app.py                 # Main Flask web server
├── memory_monitor.py      # Collects and logs real-time memory data
├── memory_test.py         # Generates stress test with memory allocations
├── visualizer.py          # Displays pie chart of current memory usage
├── simulator/
│   ├── paging.py          # Paging algorithm simulator
│   └── segmentation.py    # Segmentation algorithm simulator
├── reports/logs/          # Stores memory_data.json for live updates
└── templates/index.html   # Web interface template

# Requirements
Flask
psutil
matplotlib
numpy

