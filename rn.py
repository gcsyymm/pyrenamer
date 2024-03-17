import os
suffix = ".mp4"
updater = {f" ({i})" + suffix: f"{i}".zfill(2) + suffix for i in range(1, 12)}
for old in updater:
    os.rename(old, updater[old])
