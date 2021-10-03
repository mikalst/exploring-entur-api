def keysofkeys(r, prefix=""):
    if(type(r)==list):
        r = r[0]
    print(prefix, r.keys())
    for k in r.keys():
        try:
            keysofkeys(r[k], prefix + " " + k)
        except AttributeError:
            continue