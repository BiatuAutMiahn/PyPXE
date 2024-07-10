from pypxe import dhcp


dhcpd = dhcp.DHCPD(
    ip = "10.0.0.16",
    offer_from = "10.0.0.110",
    offer_to = "10.0.0.115",
    subnet_mask = "255.255.255.0",
    router = "10.0.0.1",
    dns_server = "10.0.0.1",
    broadcast = "10.0.0.255",
    mode_debug = True
)


dhcpd.listen()
