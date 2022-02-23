$Banner = @"
-------------------------------------------
-------------------------------------------
Hashcat Password Cracking Manager
		By
	  Munir Njiru
-------------------------------------------
-------------------------------------------
-------------------------------------------
"@
#Load Wordlists->LoopThrough->Checksize->LoadProfile->RunProfile->Next
#Place script in same folder as hashcat binary
write-Host $Banner
#House Keeping Variabless
$wordlistPath ="" #e.g."D:\usr\share\wordlists"
$hashType=""#e.g."1000"
$OutputPath = ""#e.g. "D:\hacker\project\cracked_pass\"
$HashFile = ""#"e.g. D:\hacker\project\hashes"
$rulePath = ""#e.g. "D:\usr\bin\hashcat\rules"
#End House Keeping 
function Profile-Large {
#Load Rules Less Than 10KB
   $rules = Get-ChildItem -Path $rulePath | Sort-Object Length
    for ($i=0; $i -lt $rules.Count; $i++) {
        $ruleFile= $rules[$i].FullName
        $ruleName= $rules[$i].BaseName
        If ((Get-Item $ruleFile).length -lt 10KB){
            $outputFile =  ($OutputPath + $FinalName.ToString() + "_"  + $ruleName.ToString() + "_large.cracked")
            iex (".\hashcat.exe -m $hashType -w 3 --remove $hashFile $currentWordlist -r $ruleFile -o $outputFile -O")
        }
        
    }
}
function Profile-Medium {
#Load Rules Less Than 120KB 
    $rules = Get-ChildItem -Path $rulePath | Sort-Object Length
    for ($i=0; $i -lt $rules.Count; $i++) {
        $ruleFile= $rules[$i].FullName
        $ruleName= $rules[$i].BaseName
        If ((Get-Item $ruleFile).length -lt 120KB){
            $outputFile =  ($OutputPath + $FinalName.ToString() + "_"  + $ruleName.ToString() + "_medium.cracked")
            iex (".\hashcat.exe -m $hashType -w 3 --remove $hashFile $currentWordlist -r $ruleFile -o $outputFile -O")
        }
        
    }
}
function Profile-Small {
#Load All Rules
    $rules = Get-ChildItem -Path $rulePath | Sort-Object Length
    for ($i=0; $i -lt $rules.Count; $i++) {
        $ruleFile= $rules[$i].FullName
        $ruleName= $rules[$i].BaseName
        $outputFile =  ($OutputPath + $FinalName.ToString() + "_"  + $ruleName.ToString() + "_small.cracked")
        iex (".\hashcat.exe -m $hashType -w 3 --remove $hashFile $currentWordlist -r $ruleFile -o $outputFile -O")
    }

}
$wordlists = Get-ChildItem -Path $wordlistPath -Recurse | Sort-Object Length
for ($i=0; $i -lt $wordlists.Count; $i++) {
    $currentWordlist = $wordlists[$i].FullName
    $FinalName= $wordlists[$i].BaseName
    If ((Get-Item $currentWordlist).length -gt 0KB -And (Get-Item $currentWordlist).length -lt 3MB)
	{
        $straight_crack = ($FinalName + "_small.cracked")
        iex (".\hashcat.exe -m $hashType -w 3 --remove $hashFile $currentWordlist -o $straight_crack -O")
        Profile-Small
    }
    ElseIf((Get-Item $currentWordlist).length -gt 3MB -And (Get-Item $currentWordlist).length -lt 300MB)
    {
      
        $straight_crack = ($FinalName + "_medium.cracked")
        iex (".\hashcat.exe -m $hashType -w 3 --remove $hashFile $currentWordlist -o $straight_crack -O")
         Profile-Medium

    }
    ElseIf((Get-Item $currentWordlist).length -gt 300MB -And (Get-Item $currentWordlist).length -lt 30GB)
    {
        $straight_crack = ($FinalName + "_large.cracked")
        iex (".\hashcat.exe -m $hashType -w 3 --remove $hashFile $currentWordlist -o $straight_crack -O")
         Profile-Large
    }
    Else
    {
         Write-Host $currentWordlist + "has is too large let's skip"
         $i++
    }

}
