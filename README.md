# SQLAuthDecrypt
Simple script to decrypt password used in SQL Server authentication.

This simple script can "decrypt" a password caught on the wire when SQL Server authentication is used.
SQL Server authentication simply performs few actions such as swapping high and low nibbles and 
XOR-ing the values with 0xA5.

This has been reversed many years ago (see https://nvd.nist.gov/vuln/detail/CVE-2002-1872) but since
a lot of applications need backward compatibility, this can easily be found in up-to-date applications.

Now, these days the authentication over TDS will be additionally encrypted in transit, so it should
not be possible to get the obfuscated password, unless an attacker can inject into a client process and
collect this information before it's being encrypted (but still obfuscated as the SQL Server 
authentication protocol requires).

If such an obfuscated password is acquired, it can be deobfuscated with this script:

```
$ SQLAuthDecrypt.py 
Enter encrypted password: A2A5B3A592A592A5D2A553A582A5E3A5
Decrypted password: password
```
