import subprocess


result = subprocess.run(['pip', 'install', "opencv-python", "numpy", "mediapipe", "tkinter", "pillow"], stdout=subprocess.PIPE)

print(result.stdout.decode('utf-8'))

