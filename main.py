def read_file(filename):
    f = open(filename, "rb")
    temp = []
    byte = f.read(1)
    while byte:
        temp.append(byte)
        byte = f.read(1)
    print("read")        
    return temp

def main(filename):
    bytes = read_file(filename)
    files = {"0":[]}
    status = False
    jump = 0
    counter = 1
    for a in range(len(bytes)):
        if bytes[a+jump] == b'\x00':
            for b in range(1,90):
                if a+jump+b < len(bytes):
                    if bytes[a+jump+b] == b'\x00':
                        status = True
                    else:
                        status = False
                        break
            if status == True:
                jump += 90
                counter += 1
                status = False
                files[str((counter)-1)] = []
                if files[str((counter)-2)] != [b'\x00']:
                    f = open(f"exportedFromUnalloc/{(counter)-2}", "wb")
                    f.write(b''.join(files[str((counter)-2)]))
                    f.close()
                    print(f"write {(counter)}") 
            else:
                pass
        if a+jump <= len(bytes):
            files[str((counter)-1)].append(bytes[a+jump])
            print(f"join bytes: {a+jump}")
            print(f"Byte: {bytes[a+jump]}")
        else:
            break
        
        
main('Unalloc_4_8073216_660652032')