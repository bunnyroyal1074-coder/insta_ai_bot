import os
import json

transcript_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\2d651b43-9c73-499d-b2b5-c5db794071c9\.system_generated\logs\transcript.jsonl"

if os.path.exists(transcript_path):
    print("[*] Transcript file found. Searching...")
    keys_found = []
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                step = json.loads(line)
                content = str(step.get("content", ""))
                # Search for typical Gemini key pattern starting with AIzaSy
                if "AIzaSy" in content:
                    keys_found.append(content)
                elif "api" in content.lower() and ("key" in content.lower() or "val" in content.lower()):
                    # check if it looks like a key
                    keys_found.append(content)
            except Exception as e:
                pass
                
    print(f"[+] Found {len(keys_found)} matches:")
    for idx, match in enumerate(keys_found[:10], 1):
        print(f"Match {idx}:\n{match}\n" + "-"*40)
else:
    print("[!] Transcript file not found.")
