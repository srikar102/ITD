#demo.txt contains:
# https status code 400
# https status code 500
# https status code 504
# https status code 404
# 40445544
# 55444433
# 192.168.10.10
# IP ADDRESS 172.168.10.100
# IP ADDRESS 172.160.10.100 RANGE

To find only the IP addresses in demo.txt, you can use the following grep command:

grep -E '(^| )([0-9]{1,3}\.)([0-9]{1,3}\.){2}([0-9]{1,3})' demo.txt

# This grep command searches for IPv4 addresses in demo.txt
# The regex pattern breaks down as follows:
# (^| )          - Matches start of line OR a space character
# ([0-9]{1,3}\.) - Matches 1-3 digits followed by a literal dot (first octet)
# ([0-9]{1,3}\.){2} - Matches the pattern of 1-3 digits + dot exactly 2 times (second and third octets)
# ([0-9]{1,3})   - Matches 1-3 digits without a trailing dot (fourth octet)
# The -E flag enables extended regular expressions for the pattern to work
# Returns all lines containing valid IPv4 address formats
