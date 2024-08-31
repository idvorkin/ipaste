#!python3
import os

# for every png file, if there is not a webp file, call convert on it, then move the source. to be .pold

print ("converting")

for file in os.listdir("."):
    if not file.endswith(".png"):
        continue
    webp = file.replace(".png", ".webp")
    if os.path.exists(webp):
        continue
    print(file)
    os.system(f"convert {file} {file.replace('.png', '.webp')}")
    os.system(f"mv {file} {file}.pold")
    os.system(f"git add {file.replace('.png', '.webp')}")
    print("done")
