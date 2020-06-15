import dpkt
import sys

def main():
	arguments=sys.argv[1:]
	argc = len(arguments)
	f =''
	if(len(arguments)==0):
		f = open("capture.pcap", "rb")
	if(len(arguments)>=1):
		f = open(arguments[argc-1], "rb")
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