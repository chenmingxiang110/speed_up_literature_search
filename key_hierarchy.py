f = open("FieldOfStudyHierarchy.txt", 'r')
line = f.readline()
key_map = {}
count = 0

def is_root(id):
    if not key_map.has_key(id): return False
    if key_map[id].has_key(id) and key_map[id][id] == 1:
        return True
    return False

def get_root(id):
    res = {}
    def get_root_helper(id, conf):
        parents = key_map[id]
        for key in parents:
            if is_root(key):
                if res.has_key(key):
                    res[key] = res[key] + 1 * conf
                else:
                    res[key] = 1 * conf
            else:
                new_conf = conf * parents[key]
                get_root_helper(key, new_conf)
    get_root_helper(id, 1)
    return res

while(line):
    array = line.split('\t')
    key = array[0]
    parent = array[2]
    conf = array[4]
    if key_map.has_key(key):
        key_map[key][parent] = float(conf)
    else:
        key_map[key] = {}
        key_map[key][parent] = float(conf)
    if array[3] == 'L0':
        if not key_map.has_key(parent):
            key_map[parent] = {}
            key_map[parent][parent] = 1.0;
            count = count + 1
    line = f.readline()

res = get_root("01E7DD16")
print res
print count
