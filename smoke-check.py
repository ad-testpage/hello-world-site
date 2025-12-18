import sys
import os

# Preveri, ali datoteka index.html obstaja
if not os.path.isfile("index.html"):
    print(f"index.html missing")
    sys.exit(1)
else:
    print(f"index.html obstaja")


# Preveri osnovne HTML tage
try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read().lower()  # pretvori vsebino v male črke

    tags = ["<html", "<head", "<body"]
    all_found = True

    for tag in tags:
        if tag in content:
            print(f"{tag} obstaja")
        else:
            print(f"{tag} ne obstaja")
            all_found = False

except Exception as e:
    print(f"Napaka pri branju datoteke: {e}")
    sys.exit(1)

if all_found:
    print(f"smoke OK: vsi osnovni HTML tagi prisotni")
    sys.exit(0)
else:
    print(f"smoke FAIL: manjkajo nekateri osnovni HTML tagi")
    sys.exit(1)