import os

# for every png file, if there is not a webp file, call convert on it, then move the source. to be .pold

processed_count = 0
ignored_count = 0

for file in os.listdir("."):
    if not file.endswith(".png"):
        ignored_count += 1
        continue
    webp = file + ".webp"
    if os.path.exists(webp):
        ignored_count += 1
        continue
    os.system(f"convert {file} {webp}")
    os.system(f"mv {file} {file}.old")
    os.system(f"git add {webp}")
    processed_count += 1
    print("done")

print(f"Processed files: {processed_count}, Ignored files: {ignored_count}")
