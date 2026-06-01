#!/usr/bin/env python3
"""
Build script for Code Stats
Located in build_scripts/ folder
"""

import os
import shutil

def main():
    print("=" * 60)
    print("  Code Stats - Build Tool")
    print("=" * 60)
    
    # Get project root directory (parent of build_scripts)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    os.chdir(project_root)
    
    print("\nCleaning old files...")
    
    # Clean old files
    old_files = ["CodeStats.exe", "build", "dist", "CodeStats.spec"]
    for item in old_files:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.rmtree(item, ignore_errors=True)
            else:
                os.remove(item)
    
    # Create launch script
    print("Creating launch script...")
    with open("CodeStats.bat", "w") as f:
        f.write("""@echo off
chcp 936 >nul
cd /d "%~dp0"
python codestats_no_pathlib.py %*
""")
    
    print("\n" + "=" * 60)
    print("  SETUP COMPLETE!")
    print("=" * 60)
    print("\nGenerated files:")
    print("   CodeStats.bat - Launch script")
    print("   codestats_no_pathlib.py - Main script")
    print("\nUsage:")
    print("   Double-click CodeStats.bat to run")
    print("   Or: python codestats_no_pathlib.py [path]")
    print("\nNote: Python 3.8+ required")

if __name__ == "__main__":
    main()