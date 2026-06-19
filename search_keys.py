import os
import json

transcript_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\2d651b43-9c73-499d-b2b5-c5db794071c9\.system_generated\logs\transcript.jsonl"
output_path = r"c:\Users\ADMIN\OneDrive\Desktop\insta_ai_bot\keys_found.txt"

if os.path.exists(transcript_path):
    print("[*] Transcript file found. Extracting...")
    matches = []
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                step = json.loads(line)
                content = str(step.get("content", ""))
                # Check for typical API Key patterns
                # Gemini API keys usually start with AIzaSy
                if "AIzaSy" in content:
                    matches.append(content)
                elif "api" in content.lower() and "key" in content.lower():
                    matches.append(content)
            except Exception:
                pass
                
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(f"Total matches found: {len(matches)}\n\n")
        for idx, m in enumerate(matches, 1):
            out.write(f"Match {idx}:\n{m}\n" + "="*50 + "\n\n")
    print(f"[+] Output written to {output_path}")
else:
    print("[!] Transcript not found.")
