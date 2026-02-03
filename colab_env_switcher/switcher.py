"""
Python environment switcher for Google Colab
"""

import subprocess


def _is_colab() -> bool:
    """Check if running in Google Colab environment."""
    try:
        import google.colab
        return True
    except ImportError:
        return False


def _restart_runtime() -> None:
    """Restart the Colab runtime to apply Python version changes."""
    if _is_colab():
        print("\n🔄 Restarting runtime to apply changes...")
        print("   After restart, run: import sys; print(sys.version)")
        from google.colab import runtime
        runtime.unassign()
    else:
        print("\n⚠️  Not running in Colab. Please restart your Python environment manually.")


def switch_python_version(version: str, install_uv: bool = False, auto_restart: bool = True) -> None:
    """
    Switch Python version in Google Colab environment.
    
    Args:
        version (str): Python version to switch to (e.g., "3.9", "3.10", "3.11", "3.12", "3.13", "3.14")
        install_uv (bool): Whether to install uv package manager after switching (default: False)
        auto_restart (bool): Whether to automatically restart runtime after switching (default: True)
                            Set to False if you want to install packages before restart.
    
    Example:
        >>> from colab_env_switcher import switch_python_version
        >>> switch_python_version("3.11")  # Will auto restart
        >>> switch_python_version("3.14", install_uv=True)
        >>> switch_python_version("3.12", auto_restart=False)  # Manual restart later
    """
    print(f"🚀 Starting Python environment switch to version: {version}...")
    
    try:
        # Step 1: Update package sources and add deadsnakes PPA
        print("\n📦 Step 1/5: Updating package sources...")
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "software-properties-common", "-y"], check=True)
        subprocess.run(["sudo", "add-apt-repository", "ppa:deadsnakes/ppa", "-y"], check=True)
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)
        
        # Step 2: Install specified Python version and core modules
        print(f"\n📥 Step 2/5: Installing Python {version}...")
        
        # Optional packages that might not be available for newer versions
        optional_packages = [
            f"python{version}-distutils",
            f"python{version}-dev",
            f"python{version}-venv"
        ]
        
        # Try to install base Python first
        subprocess.run(["sudo", "apt-get", "install", f"python{version}", "-y"], check=True)
        
        # Try to install optional packages individually
        for package in optional_packages:
            try:
                print(f"   Installing {package}...")
                subprocess.run(["sudo", "apt-get", "install", package, "-y"], check=True)
            except subprocess.CalledProcessError:
                print(f"   ⚠️  {package} not available, skipping...")
        
        # Step 3: Set update-alternatives to switch system default Python
        print(f"\n🔄 Step 3/5: Setting Python {version} as default...")
        
        # Register this Python version as an alternative (safe to run multiple times)
        subprocess.run([
            "sudo", "update-alternatives", "--install",
            "/usr/bin/python3", "python3",
            f"/usr/bin/python{version}", "100"
        ], check=True, capture_output=True)
        
        # Force switch to this version (critical for multiple switches)
        subprocess.run([
            "sudo", "update-alternatives", "--set",
            "python3", f"/usr/bin/python{version}"
        ], check=True)
        
        # Step 4: Download and install pip for the new Python version
        print("\n📦 Step 4/5: Installing pip...")
        subprocess.run(["wget", "https://bootstrap.pypa.io/get-pip.py", "-O", "get-pip.py"], check=True)
        subprocess.run(["python3", "get-pip.py", "--force-reinstall"], check=True)
        
        # Step 5: Verify installation
        print("\n✅ Step 5/5: Verifying installation...")
        result_python = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        result_pip = subprocess.run(["pip", "--version"], capture_output=True, text=True)
        
        print("\n" + "="*50)
        print("✅ Switch completed! Current environment:")
        print("="*50)
        print(result_python.stdout.strip())
        print(result_pip.stdout.strip())
        print("="*50)
        
        # Optional: Install uv package manager
        if install_uv:
            print("\n📦 Installing uv package manager...")
            subprocess.run(["pip", "install", "uv"], check=True)
            print("✅ uv installed successfully!")
        
        print("\n⚠️  Note: Environment has been reset.")
        print("    Please reinstall required packages using '!pip install ...'")
        print("    (e.g., numpy, pandas, etc.)")
        
        # Auto restart runtime to apply changes
        if auto_restart:
            _restart_runtime()
        else:
            print("\n💡 Tip: Run the following to restart manually:")
            print("    from google.colab import runtime; runtime.unassign()")
            print("    Or use: Runtime > Restart runtime")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error occurred during installation: {e}")
        print(f"\n💡 Tip: Python {version} might not be fully available yet.")
        print(f"    Try a stable version like 3.11 or 3.12 instead.")
        raise
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise
