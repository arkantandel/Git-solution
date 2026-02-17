import os
import time

print("🚀 DevOps Automation Script Starting...\n")

time.sleep(1)

# Git add
print("📦 Adding files to git...")
os.system("git add .")

time.sleep(1)

# Commit
commit_msg = input("Enter commit message: ")
os.system(f'git commit -m "{commit_msg}"')

time.sleep(1)

# Push
print("⬆️ Pushing to GitHub...")
os.system("git push")

time.sleep(1)

# Docker check
print("\n🐳 Checking Docker containers...\n")
os.system("docker ps")

print("\n✅ Done! All tasks completed.")
