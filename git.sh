#!/bin/bash

# Prompt user for commit message
read -p "Enter commit message: " commit_msg

# Check if commit message is empty
if [ -z "$commit_msg" ]; then
  echo "Error: Commit message cannot be empty."
  exit 1
fi

# Run git commands
git add .
git commit -m "$commit_msg"
git push

# Confirmation
echo "✅ Changes pushed with commit message: '$commit_msg'"
