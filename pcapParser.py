import dpkt
import sys

def main():
	arguments=sys.argv[1:]
	argc = len(arguments)
	f =''
	if(len(arguments)==0):
		f = open("capture.pcap", "rb")
	if(len(arguments)>=1):
		f = open(arguments[1], "rb")
  
	# open a dpkt reader to our pcap file
	pcap = dpkt.pcap.Reader(f)
	data = ""

	# iterate through all entries (ts = timestamp, buf = packet)
	for ts, buf in pcap:
		# create an Ethernet instance and check if our packet is an IP packet
		eth = dpkt.ethernet.Ethernet(buf)
		if isinstance(eth.data, dpkt.ip.IP):
			ip = eth.data
			# check for UDP
			if isinstance(ip.data, dpkt.udp.UDP):
				udp = ip.data
				# filter for destination port
				if udp.dport == 8888:
					data += udp.data.decode("utf-8")
	
	print(data)
     
if __name__ == "__main__":
    main()