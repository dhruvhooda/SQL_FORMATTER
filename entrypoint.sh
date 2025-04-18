#!/bin/bash

/bin/ollama serve &
pid=$!


sleep 5

echo "🔴 Retrieve LLAMA3 model..."
ollama pull llama3:8b
echo "🟢 Done!"

wait $pid