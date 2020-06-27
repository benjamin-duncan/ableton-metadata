import xml.etree.ElementTree as ET
import gzip
import glob
import os
# mytree = ET.parse('simple_xml.xml')
# myroot = mytree.getroot()
# print(myroot)

"""
data='''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
</metadata>
'''
"""
# myroot = ET.fromstring(data)

"""
mytree = ET.parse('simple_xml.xml')
myroot = mytree.getroot()
for x in myroot.findall('food'):
    item = x.find('item').text
    price = x.find('price').text
    print(item,price,x)
"""

"""
mytree = ET.parse('smooth strut.xml')
myroot = mytree.getroot()
for x in myroot.findall('Track'):
    item = x.find('item').text
    price = x.find('price').text
    print(item,price,x)
"""


def unzip_als(directory): # unzip project & 'choose' xml inside it
    with gzip.open(directory) as f:
        return f.read()

def generate_text(directory):
    # filename = os.path.basename(directory) # import project file
    root = ET.fromstring(unzip_als(directory))

    f_text = open(directory.replace('als','txt'),"w+")
    f_text.write(f"Version: {root.attrib['Creator']}")
    #tempo
    # print(root.findtext("./LiveSet/MasterTrack/DeviceChain/Mixer/Tempo"))
    tempo =root.find("./LiveSet/MasterTrack/DeviceChain/Mixer/Tempo/Manual[@Value]").attrib.get('Value')
    f_text.write(f"\nBPM: {tempo}")

    #root.attrib
    #print(root.find("Tempo"))
    # print(f"Tempo: {tempo.} BPM\n")
    #for track in root.findall(".//EffectiveName[@Value]"): # print all tracks in project
        #print(track.attrib)
    # for track in root.findall(".//GroupTrack"): 


    # number of tracks
    tracks= root.findall("./LiveSet/Tracks/*")

    f_text.write(f"\nTracks: {len(tracks)}")



    plugins = set()
    for plugs in root.findall(".//PlugName[@Value]"):
        plugins.add(plugs.attrib.get('Value'))
    f_text.write("\nPlugins used:\n")
    f_text.write("\n".join(sorted(list(plugins))))

def get_als_files():
    return glob.glob("D:\\Software\\Untitled Project\\2020\\Apr\\*.als")

if __name__ == "__main__":
    for i in get_als_files():
        generate_text(i)
    pass

# get some basic information from project

# project file name


# version

# print results