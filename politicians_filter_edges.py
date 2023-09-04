folder = '.'
input_file_name = 'C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-hub.edges'
output_file_name = 'C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges'

# ground truth
# load parties
parties_id = {}
noi_set = set()
with open(folder + '\\' + 'mp-of-all-parties.txt', 'r') as f:   # mp,party_name,party_id kai mazeuw
    for i, line in enumerate(f):
        tokens = line.split()
        noi = tokens[0].strip()                                 #sto noi_set=mp dld token[0]
        noi_set.add(noi)
        parties_id[noi] = int(tokens[2].strip())                #sto parties_id=ta ids dld tokens[2] gia kathe noi

f.close()

print(noi_set)
print(parties_id)

output_file = open(output_file_name, "w")         # 'W' = write

with open(input_file_name, 'r') as input_file:    # anoigw to file me ta ids kai ta mme ,  'R' = read
    for i,line in enumerate(input_file):
        tokens = line.split(',')                  # [ id, mme_name ]
        user = tokens[0].strip()                  # o user = to id dld token[0]    MALLON USER=FOLLOWER?
        noi = tokens[1].strip()                   # kai o noi= to mme_name dld token[1]

        if noi in noi_set:
            output_file.write(line)
input_file.close()
output_file.close()