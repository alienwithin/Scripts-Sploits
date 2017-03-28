# Scripts & Sploits

This repo will contain a collection of scripts that are POC's against various vulnerabilities identified. Currently here in there's: 

**zen_app_mobile_wp_rfu.py**

``` 
This exploit caters for 5 CVE's that can be exploited
* Zen App Mobile Native <=3.0 (CVE-2017-6104)
* Wordpress Plugin webapp-builder v2.0 (CVE-2017-1002002)
* Wordpress Plugin wp2android-turn-wp-site-into-android-app v1.1.4 CVE-2017-1002003)
* Wordpress Plugin mobile-app-builder-by-wappress v1.05 CVE-2017-1002001)
* Wordpress Plugin mobile-friendly-app-builder-by-easytouch v3.0 (CVE-2017-1002000)

```

**wp_ue_api.py**
 ``` 
 This exploit enumerates users on wordpress 4.7 via the JSON API (CVE 2017-5487)
 
 ```
 
**membership-simplified-for-oap-members-only-exploit.py**
 ``` 
 This exploit is a PoC for Wordpress Plugin Membership Simplified v1.58 - Arbitrary File Download and attempts to download the wordpress configuration file or /etc/passwd file from the target system. (CVE-2017-1002008)
 
 ```
  
**mimi_multidump.bat**
 ``` 
 This is a simple batch script that makes it efficient if you have multiple lsass.dmp files to dump the passwords into text files for each. 
 
 ```
