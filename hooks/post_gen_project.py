import subprocess

print('Almost done!')
print('Initialinzing a git repository.....')
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
print('Intalling requirements.txt......')
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
