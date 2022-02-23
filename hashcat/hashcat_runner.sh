#!/bin/bash
# @author Munir Njiru <munir@alien-within.com>
# @url www.alien-within.com
# @file hashcat_runner.sh
# @brief A file that tries to solve looping of hashcat cracking
# @description This project seeks to sort wordlists and rules by size and efficiently mix and match them to efficiently crack fast.

#House Keeping Variables
#Configure these and you are good to go
RuleFolder=""#e.g."/usr/share/hashcat/rules"
HashesFile=""#e.g."/home/hacker/project/filewithhashes"
WordlistsFolder=""#e.g."/usr/share/wordlists/"
HashType=""#e.g. "1000"
OutputFolder=""#e.g."/home/hacker/project/cracked_pass/"
#EndHouse Keeping

function ProfileLarge(){
    for RULE in "$RuleFolder"/*; 
    do 
        FILESIZE=$(stat -c%s "$FILE")
        if [ "$FILESIZE" -le "10240" ]
        then
        rulefile=$(basename "$RULE" | sed 's/\(.*\)\..*/\1/')
        wordlist=$(basename "$currentWordlist" | sed 's/\(.*\)\..*/\1/')
        suffix="_large.cracked"
        seperator="_"
        cracked_file= $OutputFolder$wordlist$seperator$rulefile$suffix
        hashcat -m "$HashType" -w 3 --remove "$HashesFile" "$currentWordlist" -r "$RULE" -o "$cracked_file" -O
        fi
    done
}
function ProfileMedium(){
    
    for RULE in "$RuleFolder"/*; 
    do 
        FILESIZE=$(stat -c%s "$RULE")
        if [ "$FILESIZE" -le "122880" ]
        then
        rulefile=$(basename "$RULE" | sed 's/\(.*\)\..*/\1/')
        wordlist=$(basename "$currentWordlist" | sed 's/\(.*\)\..*/\1/')
        suffix="_medium.cracked"
        seperator="_"
        cracked_file= $OutputFolder$wordlist$seperator$rulefile$suffix
        hashcat -m "$HashType" -w 3 --remove "$HashesFile" "$currentWordlist" -r "$RULE" -o "$cracked_file" -O
        fi
    done
}
function ProfileSmall(){
    for RULE in "$RuleFolder"/*; 
    do  
        rulefile=$(basename "$RULE" | sed 's/\(.*\)\..*/\1/')
        wordlist=$(basename "$currentWordlist" | sed 's/\(.*\)\..*/\1/')
        suffix="_small.cracked"
        seperator="_"
        cracked_file= $OutputFolder$wordlist$seperator$rulefile$suffix
        hashcat -m "$HashType" -w 3 --remove "$HashesFile" "$currentWordlist" -r "$RULE" -o "$cracked_file"-O
    done
}

for currentWordlist in "$WordlistsFolder"/*;
do
    $currentWordlist=$(realpath "$currentWordlist")
    FILESIZE=$(stat -c%s "$currentWordlist")
    if [[ "$FILESIZE" -gt "0" && "$FILESIZE" -le "3145728" ]];
    then
        wordlist=$(basename "$currentWordlist" | sed 's/\(.*\)\..*/\1/')
        suffix="_small_straight.cracked"
        seperator="_"
        cracked_file=$OutputFolder$wordlist$suffix
        hashcat -m "$HashType" -w 3 --remove "$HashesFile" "$currentWordlist" -r "$RULE" -o "$cracked_file" -O
        ProfileSmall
    elif [[ "$FILESIZE" -gt "3145728" && "$FILESIZE" -le "314572800" ]];
    then
        wordlist=$(basename "$currentWordlist" | sed 's/\(.*\)\..*/\1/')
        suffix="_medium_straight.cracked"
        seperator="_"
        cracked_file=$OutputFolder$wordlist$suffix
        hashcat -m "$HashType" -w 3 --remove "$HashesFile" "$currentWordlist" -r "$RULE" -o "$cracked_file" -O
        ProfileMedium
    elif [[ "$FILESIZE" -gt "314572800" && "$FILESIZE" -le "3145728000" ]];
    then
        wordlist=$(basename "$currentWordlist" | sed 's/\(.*\)\..*/\1/')
        suffix="_large_straight.cracked"
        seperator="_"
        cracked_file=$OutputFolder$wordlist$suffix
        hashcat -m "$HashType" -w 3 --remove "$HashesFile" "$currentWordlist" -r "$RULE" -o "$cracked_file" -O
        ProfileLarge
    else
        echo "Seems $currentWordlist is too large"
    fi
done