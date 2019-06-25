#!/usr/bin/env python3

import yaml
def main():

    hitchikers = [{"name":"Zapho Bebr", "species":"Betelguese"},{"name":"Arthur", "species": "Human"}]
    print(hitchikers)
    zfile = open("galaxy.yaml","w")
    yamlOut = yaml.dump(hitchikers)
    print(yamlOut)
    zfile.close()
   
def second():
    print("Second part")
    yammyfile = open("/home/student/mycode/nasa02/yamlIntro/yaml2.yml","r")
    pyyammy = yaml.load(yammyfile)
    yammyfile.close()
    print(pyyammy)
    pyyammy[0]['apps'].append('minecraft')
    print(pyyammy)
    
    yammyfile2 = open("/home/student/mycode/nasa02/yamlIntro/yaml2.yml","w")

    yaml.dump(pyyammy,yammyfile2)

    yammyfile2.close()

main()
second()
