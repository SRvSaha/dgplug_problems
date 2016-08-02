#
#   @author      : SRvSaha
#   Filename     : irc_nick_count.py
#   Timestamp    : 18:59 26-July-2016 (Thursday)
#   Description  : This code is used to find out the mapping of the nick to
#   the number of times it messaged in the IRC. It's a dictionary based
#   key-value type output.
#

# ''' Take the 4 logs from the top of https://dgplug.org/irclogs/2016/  and then try to find for each nick ever present in
# those files, who spoke with whom highest number of times.

#  Like: kushal spoke to avik 35 times
#     avik spoke to gkadam 55 times

#  and like that, for all the nicks. '''

# log1 contains the content of log https://www.dgplug.org/irclogs/2016/Logs-2016-06-19-15-00-introduction.txt
# log2 contains the content of log https://www.dgplug.org/irclogs/2016/Logs-2016-06-20-15-00-second_session.txt
# log3 contains the content of log https://www.dgplug.org/irclogs/2016/Logs-2016-06-20-15-00-session4.txt
# log4 contains the content of log https://www.dgplug.org/irclogs/2016/Logs-2016-06-20-15-00-session5.txt

with open("input.txt") as f:
    lines = f.read()

result = {}

for line in lines.splitlines():
    if line[11] == '<':
        key = line[12:].split('>')[0]
        if key not in result.keys():
            result[key] = {}

key = result.keys()

for line in lines.splitlines():
    if line[11] == '<':
        name = line[12:].split('>')[0]
        msg = line[12:].split('>')[1]
        for f in key:
            if f in msg and f != name:
                result[name][f] = result[name].get(f, 0) + 1

for key in sorted(result.keys()):
    # Condition to avoid all the empty dict values
    if len(result[key].items()) != 0:
        # lamba expression takes input the tuple and return the
        # tuple
        who,time = sorted(result[key].items(), key=lambda x: x[1], reverse=True)[0]
        print(key,"spoke to",who,time,"times")

