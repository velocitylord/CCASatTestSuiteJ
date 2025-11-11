import os
import matplotlib.pyplot as plt

filepath="/home/clivet268/Downloads/KernelLearnel/CCASatTestSuite/testlogs/2025-11-11_307677302/2025-11-11_307677302_1.log"

csvheader="now_us,bytes_acked,mss,rtt_us,tp_deliver_rate,tp_interval,tp_delivered,lost_pkt,total_retrans_pkt,app_limited,snd_nxt,sk_pacing_rate"

outputfilepath="framework.csv"


try:
    print(root in os.walk("/home/clivet268/Downloads/KernelLearnel/CCASatTestSuite/testlogs/",topdown=True));
    for (root,dirs,files) in os.walk("/home/clivet268/Downloads/KernelLearnel/CCASatTestSuite/testlogs/",topdown=True):
        print("Directory path: %s"%root)
        print("Directory Names: %s"%dirs)
        print("Files Names: %s"%files) 
    with open(outputfilepath, "x") as outputfile:
        outputfile.write(csvheader + "\n")
        print(f"Writing to {outputfilepath}\n")
    
        outputlines=[]
    
        with open(filepath, "r") as inputfile:
            for line in inputfile:
                line = line[:-2]
                line = line[3:]
                pieces = line.split('] [')
                #print(line)
                #print(pieces)
                #try:
                if pieces[1] == "CCRG":
                    flows = {}
                    #print("CCRG line found"+"\n")
                    #print("greijg" + pieces[2]+"\n")
                    if pieces[2] == "FP":
                        #print("gurt fureeekle")
                        flows.setdefault(f"{pieces[3]}", []).append((pieces[4], pieces[5].split(',')))
                        #flows[f"{pieces[3]}"].append((pieces[4], pieces[5]))
                        #print("gurt furkle" + pieces[3]+"\n")
                        if pieces[4] == "FRAMEWORK":
                            #print(pieces[5]+"\n")
                            outputfile.write(pieces[5]+"\n")
                        #print("flow pointer found")
                #except:
                #    print("above line skipped")
                    
except FileExistsError:
    print(f"{outputfilepath} already exists")
except FileNotFoundError:
    print("Cannot find file" + filepath)
