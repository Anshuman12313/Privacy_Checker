import exifread

#writing funciion to extract meta data

def scan_metadata(imagepath):
    with open(imagepath,"rb") as image_file:
        tags = exifread.process_file(image_file)
    
    #print all metadata
    for tag,value in tags.items():
        print(f"{tag}:{value}")
