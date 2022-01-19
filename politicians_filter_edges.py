folder = '.'
input_file_name = 'C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\TEST_etoimo dataset_clustering\\2021-11-14-twitter\\2021-11-14-twitter\\user-hub.edges'
output_file_name = 'C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\TEST_etoimo dataset_clustering\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges'

# ground truth
# load parties
parties_id = {}
noi_set = set()
with open(folder + '\\' + 'mp-of-all-parties.txt', 'r') as f:
    for i,line in enumerate(f):
        tokens = line.split()
        noi = tokens[0].strip()
        noi_set.add(noi)
        parties_id[noi] = int(tokens[2].strip())
f.close()

output_file = open(output_file_name, "w")

with open(input_file_name, 'r') as input_file:
    for i,line in enumerate(input_file):
        tokens = line.split(',')
        user = tokens[0].strip()
        noi = tokens[1].strip()
        if noi in noi_set:
            output_file.write(line)
input_file.close()
output_file.close()