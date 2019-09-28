"""
Write a simple python function to make an api call to infoblox.
This function should be able to take in as input the hostname and subnet,
and make the correct calls to infoblox to create the A record in the subnet
specified on the next available IP address
"""

import requests


def create_host_record_next_ip(hostname, subnet):
    # base_url = "http://172.16.15.254"
    # endpoint = "wapi/v1.2/record:host"
    base_url = "http://httpbin.org"
    endpoint = "/post"
    url = base_url + endpoint
    header_dict = {"Content-Type": "application/json"}
    func = "func:nextavailableip:{}".format(subnet)
    data = {"name": hostname, "ipv4addrs": [{"ipv4addr": func}]}

    reply = requests.post(url, headers=header_dict, json=data)
    return reply


if __name__ == "__main__":
    output = create_host_record_next_ip("my_new_host", "192.168.100.0/24")
    for section in output:
        print(section)
