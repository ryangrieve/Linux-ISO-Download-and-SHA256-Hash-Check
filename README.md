# Linux-ISO-Download-and-SHA256-Hash-Check

This is a Python script for downloading Linux ISO files and checking their SHA256 hash values. The script prompts the user to select a distribution and downloads the distribution's ISO file and its SHA256 hash file using 'subprocess' and 'wget'. The script uses 'subprocess' and 'sha256sum' to calculate the hash value of the downloaded ISO file and compares it with the hash value stored in the downloaded hash file. After the comparison, the script states whether the hashes match.

- 'wget' must be installed to use this script.

The script currently supports the following Linux distributions:
1. Debian
2. Xubuntu
3. Fedora
4. Rocky Linux
5. openSUSE Tumbleweed
