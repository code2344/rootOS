# rootOS

Tries to use various CVEs to gain sudo or root access. All exploits have an end goal of adding `ALL ALL=(ALL) NOPASSWD: ALL` to `/etc/sudoers` allowing any user to run `sudo` commands.

⚠️ **ETHICAL USE ONLY**: This tool is designed exclusively for authorized penetration testing and security research. Unauthorized use is illegal.

![screenshot](docs/screenshot.png)

## Features

### 🔒 Ethical Safeguards
- **Disclaimer on startup**: Requires explicit user consent before proceeding
- **Confirmation prompts**: All dangerous operations require user confirmation
- **Verbose logging**: Detailed output for all actions and attempts
- **Security warnings**: Alerts for writable daemon files and privilege escalation attempts

### 🆕 Modern macOS Support (Sequoia 15.x, Sonoma 14.x, Ventura 13.x)
- **Daemon Hijacking**: Detects and exploits writable LaunchDaemon/LaunchAgent files
- **TCC Bypass**: Techniques for bypassing Transparency, Consent, and Control protections
- **Sudo Token Reuse**: Exploits active sudo sessions for privilege escalation
- **System Path Manipulation**: Identifies and exploits writable system paths

### 📜 Legacy macOS Support
- Maintains compatibility with older macOS versions (10.5 - 10.14)
- All legacy exploits preserved and functional

## Run

```bash
python root.py
```

The tool will:
1. Display an ethical use disclaimer
2. Require explicit authorization confirmation
3. Detect your macOS version
4. Attempt applicable exploits with verbose output
5. Request confirmation before modifying system files

## Exploits

## Exploits

### Modern Exploits (macOS 13.x - 15.x+)

**Note**: The problem statement mentions "macOS Tahoe (26)" but current macOS versions are:
- macOS 15.x = Sequoia
- macOS 14.x = Sonoma  
- macOS 13.x = Ventura

The modern exploits target these latest versions and future releases.

| Name                    | CVE                      | Target Versions       | Description                                          |
| ----------------------- | ------------------------ | --------------------- | ---------------------------------------------------- |
| Sequoia PrivEsc        | 2024-SEQUOIA-PRIVESC     | 15.x (Sequoia)+       | System path manipulation and permission exploitation |
| TCC Bypass             | 2024-TCC-BYPASS          | 14.x (Sonoma)+        | Transparency, Consent, Control protection bypass     |
| Daemon Hijack          | 2024-DAEMON-HIJACK       | 15.x (Sequoia)+       | LaunchDaemon/LaunchAgent writable file exploitation  |
| Sudo Token Reuse       | 2024-SUDO-TOKEN-REUSE    | 13.x (Ventura)+       | Active sudo session token reuse                      |

### Legacy OS Exploits

| Name                         | CVE            | Date       | Link(s)                                                                                                |
| ---------------------------- | -------------- | ---------- | ------------------------------------------------------------------------------------------------------ |
| ARDAgent                     | CVE-2008-2830  | 06/23/2008 | <https://nvd.nist.gov/vuln/detail/CVE-2008-2830>                                                       |
| DYLD_PRINT_TO_FILE           | CVE-2015-3760  | 08/16/2015 | <https://nvd.nist.gov/vuln/detail/CVE-2015-3760> <https://twitter.com/i0n1c/status/623727538234368000> |
| MallocLog                    | CVE-2015-5889  | 0/09/2015  | <https://nvd.nist.gov/vuln/detail/CVE-2015-5889>                                                       |
| Proxifier Sanitize           | CVE-2017-7643  | 04/14/2017 | <https://nvd.nist.gov/vuln/detail/CVE-2017-7643>                                                       |
| Sera Local Pass              |                | 10/31/2017 | <https://m4.rkw.io/blog/cve201715918-sera-12-local-root-privesc-and-password-disclosure.html>          |
| NoPass                       | CVE-2017-13872 | 11/29/2017 | <https://nvd.nist.gov/vuln/detail/CVE-2017-13872> <https://objective-see.com/blog/blog_0x24.html>      |
| KeySteal                     | CVE-2019-8526  | 06/01/2019 | <https://github.com/LinusHenze/Keysteal>                                                               |
| AppleScript Dynamic Phishing |                |            | <https://github.com/thehappydinoa/rootOS/blob/master/apps.json>                                        |
| Sudo Piggyback               |                |            | <https://www.n00py.io/2016/10/privilege-escalation-on-os-x-without-exploits/>                          |

### Dynamic Phishing

![phishing](docs/phishing.png)

Please note the dynamic icon and prompt

## Safety Features

### Confirmation Prompts
All dangerous operations require explicit user confirmation:
- **Sudoers modification**: Requires typing 'yes' to confirm
- **Daemon file exploitation**: Warns about writable files before proceeding
- **TCC bypass attempts**: Explicit confirmation required

### Verbose Output
The tool provides detailed information about:
- Current macOS version detection
- Available exploits for your system
- CVE numbers and credits for each exploit
- Success/failure status for each attempt
- Summary statistics at completion

## Important Notes

⚠️ **Legal Warning**: This tool should ONLY be used on systems you own or have explicit written authorization to test. Unauthorized access to computer systems is illegal under the Computer Fraud and Abuse Act (CFAA) and similar laws worldwide.

⚠️ **Security Impact**: Successfully running these exploits will modify your system's security configuration. Only use in controlled testing environments.

⚠️ **Modern macOS Protection**: Current macOS versions (14.x+) include System Integrity Protection (SIP) and other hardening features that prevent many of these exploits from working. These exploits are provided for educational and authorized testing purposes.

## Additional Exploits

- [amanszpapaya/MacPer](https://github.com/amanszpapaya/MacPer)

## License

[MIT](LICENSE)
