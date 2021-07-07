### Exploiting Printers (Kyocera)
This script would assisst in a pentest scenario to abuse a printer feature found in Kyocera printers to gain access to windows credentials. 
Kyocera Printers contain an address book feature; within this feature an administrator can use one of two methods to transmit scanned documents: 
- Configure a send to e-mail
- Configure a windows account to login to the host 

Tested on: 
- Kyocera ECOSYS M2640idw
- Kyocera 4550i

## Setup 
Quite simple really you can compile with the **csc.exe** utility in your dotnet framework. 
- Navigate 
`<path/to/csc.exe> KyoceraAddressBookDecryptor.cs`

an example is below: 
`C:\Windows\Microsoft.NET\Framework64\v3.5\csc.exe KyoceraAddressBookDecryptor.cs`

You also need to download KNetViewer to be able to export the addressbook from the printer. 
Pre-compiled binary for the decryptor provided just incase you're pressed for time. :-P

## usage
- Navigate to the path where you have saved this exe
- run `KyoceraAddressBookDecryptor.exe` 
- paste the encrypted value from the SmbLoginPasswd field in the Address Book XML. 

A sample of the address book is below: 


The decryption process is as easy as below:


###Presumed Flow
                    
```seq
Pentester->KNetViewer: Login 
Note left of KNetViewer: Login could be by:\n default (Admin/Admin);\nor Bruteforce
Printer-->Pentester: Export Address Book
Pentester-->Decryptor: Run Decryptor and \npass encrypted Password
Decryptor->Pentester: Get Plaintext Password
Pentester->>Domain: Gain Foothold or Administration\n\n
Note right of Domain: Privilege Gained Depends on \nrights of the configured user!
```

###End