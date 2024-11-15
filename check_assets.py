import os


# each python file has background image and its path starts with :/assets/ chane it to ./
def check_asset_path_and_fix_size():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                # exclude this file
                if file == "check_assets.py":
                    continue
                with open(os.path.join(root, file), "r") as f:
                    lines = f.readlines()
                with open(os.path.join(root, file), "w") as f:
                    for line in lines:
                        if ":/assets/" in line:
                            line = line.replace(":/assets/", "./")
                        if "MainWindow.resize" in line:
                            line = line.replace(
                                "MainWindow.resize", "MainWindow.setFixedSize"
                            )
                        f.write(line)
