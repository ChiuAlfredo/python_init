import os
import platform
import subprocess


    
def initial_venv():    
    system = platform.system()
    venv_name = ".venv"  # 自定義虛擬環境名稱
    venv_dir = os.path.join(os.getcwd(), venv_name)

    # 啟用虛擬環境
    activate_script = "Scripts" if system == "Windows" else "bin"
    if system == ['Darwin', 'Linux']:
        activate_path = os.path.join(venv_dir, activate_script, "activate")
        activate_cmd =  f"source {activate_path}"
    else:
        activate_path = os.path.join(venv_dir, activate_script, "Activate")
        activate_cmd =  '& '+activate_path+'.ps1'
    
    print("啟用虛擬環境...")
    subprocess.call(activate_cmd, shell=True)

    # 安裝必要的套件（這裡可以根據你的需求自行增減）
    print("安裝poetry")
    subprocess.call([ "pip", "install", "poetry"])
    
    print("啟動poetry")
    subprocess.call([ "poetry", "init", "-n"])
    
    


if __name__ == "__main__":
    initial_venv()