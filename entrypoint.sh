#!/bin/bash

/bin/ollama serve &
pid=$!


sleep 5

echo "🔴 Do not run localhost yet, pulling The model 🔴"
ollama pull llama3:8b
echo "🟢 Model pulled, you are now allowed to run the localhost 🟢"

wait $pid