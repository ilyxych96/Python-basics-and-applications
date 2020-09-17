import os
import os.path


answer_dirs = []

for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if file[-3:] == '.py':
            answer_dirs.append(current_dir)
            print(current_dir)
            break

print(answer_dirs)