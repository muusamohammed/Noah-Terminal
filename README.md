🛠 Noah Terminal: Command Documentation
Noah Terminal is a specialized Python-based environment designed for Ethical Hacking, Software Development, and Network Analysis.

1. gen [BIN]
Description: Generates 16-digit credit card numbers based on a specific Bank Identification Number (BIN).

How it works: It utilizes the Luhn Algorithm to ensure the generated numbers follow the mathematical checksum required by banking systems.

Usage: gen 515462

Output: A list of valid-format card numbers, including random Expiry Dates and CVV codes.

2. track [IP]
Description: Performs an IP Lookup and geolocation trace.

How it works: It connects to an external API/Database to fetch the physical location, ISP, and organization associated with a specific IP address.

Usage: track 1.1.1.1

Output: A direct link to a map and technical data about the target's network.

3. zphisher
Description: An automated Phishing tool launcher.

How it works: It attempts to navigate to the zphisher directory on your Linux system and execute the bash script.

Usage: zphisher

Constraint: Requires Kali Linux or a Linux environment with Zphisher pre-installed in the root directory.

4. clear
Description: Refreshes the terminal interface.

How it works: Wipes the current screen of all previous commands and text, re-displaying the "Musa Mohammed" ASCII Banner.

Usage: clear

5. exit
Description: Safely terminates the terminal session.

How it works: Closes the Python loop and returns control to the native operating system.

Usage: exit

💻 System Specifications
Developer: Musa Mohammed (Cyber Noah)

Language: Python 3.x

Category: Ethical Hacking / Fullstack Tools

Compatibility: Cross-platform (Windows/Linux/Android-Termux)
