# DNSHistory

Visit us at (https://redmoonsecurity.com)

**A python script purely for discovering historic IP addresses for a domain that could point to the origin server and allow you to bypass WAF**

View a demo on YouTube here: (https://youtu.be/ROYRyhHbOJE)

![screen of DNShistory](https://user-images.githubusercontent.com/62467907/80868367-62e13500-8c9a-11ea-9131-af622acd7254.png)

## *Usage*

./DNShistory

The script will run and prompt you for a domain to discover historical IP addresses for.

## *Historical IP Addresses and WAF*

A normal visitor connects to a Website. The initial request is a DNS request to ask the IP of the website, so the browser of the client knows where to send the HTTP request to. For sites behind cloudflare or some other public WAF, the reply contains an IP address of the WAF itself. Your HTTP traffic flows basically through the WAF to the origin web server. The WAF blocks malicious requests and protects against (D)DoS attacks. However, if an attacker knows the IP of the origin webserver and the origin webserver accepts HTTP traffic from the entire internet, the attacker can perform a WAF bypass: let the HTTP traffic go directly to the origin webserver instead of passing through the WAF.

This script discovers and lists all historic IP addresses where one or more could point to the origin server, allowing you to bypass the WAF.


