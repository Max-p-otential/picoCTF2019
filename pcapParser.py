import dpkt

def main():
	f = open("capture.pcap", "rb")
	pcap = dpkt.pcap.Reader(f)
	data = ""

	for ts, buf in pcap:
		eth = dpkt.ethernet.Ethernet(buf)
		if isinstance(eth.data, dpkt.ip.IP):
			ip = eth.data
			if isinstance(ip.data, dpkt.udp.UDP):
				udp = ip.data
				if udp.dport == 8888:
					data += udp.data.decode("utf-8")
	
	print(data)
     
if __name__ == "__main__":
    main()