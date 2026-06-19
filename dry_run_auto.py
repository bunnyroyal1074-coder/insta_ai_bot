import os
import subprocess
import shutil

def main():
    print("=== Dry-Run Auto Logic ===")
    
    # 1. Back up existing .env
    env_exists = os.path.exists(".env")
    if env_exists:
        shutil.copy(".env", ".env.real")
        
        # Read real env and write dummy username version
        lines = []
        with open(".env", "r") as f:
            for line in f:
                if line.startswith("INSTAGRAM_USERNAME="):
                    lines.append("INSTAGRAM_USERNAME=your_username_here\n")
                else:
                    lines.append(line)
                    
        with open(".env", "w") as f:
            f.writelines(lines)
            
    try:
        # 2. Run the bot in auto mode
        print("\nExecuting: python app.py --mode auto")
        result = subprocess.run(["python", "app.py", "--mode", "auto"], capture_output=True, text=True)
        print("\n=== Bot Output ===")
        print(result.stdout)
        print(result.stderr)
        print("==================")
    finally:
        # 3. Restore real .env
        if env_exists:
            shutil.move(".env.real", ".env")
            print("\n[+] Restored real .env file.")

if __name__ == "__main__":
    main()
