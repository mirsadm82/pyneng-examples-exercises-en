import ipaddress


def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False


if __name__ == "__main__":
    ip1 = "10.1.1.1"
    ip2 = "10.1.1"

if __name__ == '__main__':

    print("IP check...")
    print(ip1, check_ip(ip1))
    print(ip2, check_ip(ip2))
