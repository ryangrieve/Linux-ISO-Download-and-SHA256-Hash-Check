import json
import subprocess

print(
    """
Linux ISO Download and SHA256 Hash Check

This Python script downloads Linux ISO files and verifies their SHA256 hash
values. Select a distribution and the script downloads the distribution's
ISO and SHA256 hash files. The script will calculate the hash value of the
downloaded ISO and compare it with the hash value stored in the downloaded
hash file. After the comparison, the script states whether the hashes match."""
)

with open("distros.json", "r") as f:
    distros = json.load(f)


# Downloads the .iso and hash file
def download_file(url, filename):
    print(f"\nDownloading {filename}...")
    cmd = [
        "wget",
        url,
        "-O",
        filename,
        "-q",
        "--show-progress",
    ]
    subprocess.run(cmd, check=True)


# Calculates and compares the SHA256 hash
def check_hash(iso_filename, hash_filename):
    iso_hash_output = subprocess.run(
        ["sha256sum", iso_filename], capture_output=True, text=True, check=True
    )
    iso_hash = iso_hash_output.stdout.split()[0]

    with open(hash_filename, "r") as f:
        hash_file_contents = f.read()
        hash_lines = hash_file_contents.split("\n")
        matching_line = None
        for line in hash_lines:
            if iso_hash in line:
                matching_line = line
                break
        if matching_line:
            print(
                f"\nSHA256 hash match confirmed!\n\n"
                f"Downloaded {iso_filename} hash: {iso_hash}\n"
                f"Downloaded {hash_filename} hash: {matching_line}"
            )
        else:
            print(
                f"\nERROR: SHA256 hash does not match!\n\n"
                f"Downloaded {iso_filename} hash: {iso_hash}\n"
                f"Downloaded {hash_filename} hash: {hash_file_contents}"
            )
        quit()


def download_and_check(distro):
    urls = distros[str(distro)]
    iso_filename, hash_filename = [url.split("/")[-1] for url in urls.values()]
    download_file(urls["iso"], iso_filename)
    download_file(urls["hash"], hash_filename)
    check_hash(iso_filename, hash_filename)


def main_menu():
    while True:
        try:
            print("\nDistribution Options:")
            for option, urls in distros.items():
                print(f"{option}) {urls['iso'].split('/')[-1]}")
            print(f"{len(distros)+1}) Quit")
            distro = int(input(f"\nSelect an option (1-{len(distros)+1}): "))
            if distro == len(distros) + 1:
                quit("\nClosing...\n")
            download_and_check(distro)
        except Exception:
            print("\nInvalid choice, please try again.")
            continue


main_menu()
