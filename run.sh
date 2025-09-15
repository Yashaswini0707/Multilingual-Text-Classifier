#!/bin/bash

echo "🚀 Starting Language Detection Tool..."

# Navigate to the correct directory
cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Start the server
echo "🌐 Starting server on http://localhost:5000"
echo "📱 Opening frontend in browser..."
echo ""
echo "Press Ctrl+C to stop the server"

# Start server and open frontend
python app_simple.py &
sleep 3
open index.html

# Wait for the background process
wait
