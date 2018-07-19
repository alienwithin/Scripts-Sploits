Write-Host "###################################################################################

	Netsparker Multiple Instance Launcher by Munir Njiru (Alien-within)
	
	Purpose: Launch Multiple instances of Netsparker to scan
	each URL in a text file. Please consider your text
	file list based on resources in the machine to avoid choking it.
	
	Website: https://www.alien-within.com
	e-mail: munir@alien-within.com
					
###################################################################################

";

$NetsparkerInstallPath = Read-Host -Prompt 'Input Path to Netsparker Installation e.g. C:\Program Files (x86)\Netsparker\Netsparker.exe' 
$TargetURLs = Read-Host -Prompt 'Input path to text file with URLs e.g. F:\Pentests\scan_targets.txt'
$ReportStorage = Read-Host -Prompt 'Input path to save your reports when done e.g. F:\Pentests\Reports\'
$ReportType = "Detailed Scan Report"
 foreach ($url in get-content $TargetURLs) {
     $domain = ([System.URI]"$url").Host
     $report = $ReportStorage + $domain + "_" + (Get-Date -format "yyyyMMdHm")
     start-process -FilePath "$NetsparkerInstallPath" -ArgumentList "/url ""$url"" /profile ""$domain"" /a /s /r ""$report"" /rt ""$ReportType"""
}