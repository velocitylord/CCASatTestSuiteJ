import iperf3

GEO = ("GEO", "ccasatpi.dyn.wpi.edu")
LEO = ("LEO", "ccasatpi.dyn.wpi.edu")
WL4GLTE = ("4G/LTE", "ccasatpi.dyn.wpi.edu")
WL5G = ("5G", "ccasatpi.dyn.wpi.edu")
WiFi = ("WiFi", "ccasatpi.dyn.wpi.edu")
Ethernet = ("Ethernet", "ccasatpi.dyn.wpi.edu")

platforms = [GEO, LEO, WL4GLTE, WL5G, WiFi, Ethernet]
ccas = ["CUBIC", "HyStart", "HyStart++", "BBR", "SEARCH"]


def default(platform):
	client = iperf3.Client()
	client.duration = 10  #Seconds
	client.server_hostname = platform[1]
	client.port = 5201 #50268

	result = client.run()

	# Process the results
	if result.error:
		print(f"Error: {result.error}")
	else:
		print("Test completed successfully.")
		print(f"Bandwidth: {result.sent_Mbps} Mbps (sent), {result.received_Mbps} Mbps (received)")
		print(f"Retransmits: {result.retransmits}")
condtions = [default]

for platform in platforms:
	default(platform)
