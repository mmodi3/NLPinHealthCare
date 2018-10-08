import xml.etree.ElementTree as ET
import requests
import sys
import json
import errno


prescriptions = ['Diphenhydramine', 'Ibuprofen', 'Codeine methylbromide']

def setup():
    tree = ET.parse('full_database.xml')
    root = tree.getroot()
    gens = []
    brands = []
    with open('generic-names.txt','r') as generics:
        for genline in generics:
                gens = genline.split(',')
    with open('brands.txt','r') as brands:
        for brandline in brands:
            brands = brandline.split(',')
    print(root.tag)
    return root
#root, gens, brands = setup()

def DB_id_from_name(drugname, treeroot):
    for child in treeroot:
        if child.find('name').text == drugname:
            return child.find('drugbank-id').text
    return 'ERROR: DRUG NOT FOUND'

def name_from_brand(brandname, treeroot):
    for child in treeroot:
        products = child.find('products').findall('product')
        prods=[]
        for product in products:
            prods.append(product.find('name').text)
        if brandname in prods:
            return child.find('name').text
    return 'ERROR: DRUG NOT FOUND'

def element_from_id(dbid, treeroot):
    for child in treeroot:
        DBID = child.find('drugbank-id').text
        if DBID == dbid:
            return child
    return None

def bdi(brandname, drugname, treeroot):
    nombre = name_from_brand(brandname, treeroot)
    check = DB_id_from_name(nombre,treeroot)
    checkagainst = DB_id_from_name(drugname,treeroot)
    canode = element_from_id(checkagainst, treeroot)
    interactions = canode.find('drug-interactions')
    for interaction in interactions:
        if interaction.find('drugbank-id').text == check:
            return interaction.find('description').text
    return ''

def dbi(drugname, brandname, treeroot):
    nombre = name_from_brand(brandname, treeroot)
    check = DB_id_from_name(nombre,treeroot)
    checkagainst = DB_id_from_name(drugname,treeroot)
    canode = element_from_id(checkagainst, treeroot)
    interactions = canode.find('drug-interactions')
    for interaction in interactions:
        if interaction.find('drugbank-id').text == check:
            return interaction.find('description').text
    return ''

def bbi(brandname1, brandname2, treeroot):
    nombre1 = name_from_brand(brandname1, treeroot)
    nombre2 = name_from_brand(brandname2, treeroot)
    check = DB_id_from_name(nombre1,treeroot)
    checkagainst = DB_id_from_name(nombre2,treeroot)
    canode = element_from_id(checkagainst, treeroot)
    interactions = canode.find('drug-interactions')
    for interaction in interactions:
        if interaction.find('drugbank-id').text == check:
            return interaction.find('description').text
    return ''

def ddi(drugname1, drugname2, treeroot):
    check = DB_id_from_name(drugname1,treeroot)
    checkagainst = DB_id_from_name(drugname2,treeroot)
    canode = element_from_id(checkagainst, treeroot)
    interactions = canode.find('drug-interactions')
    for interaction in interactions:
        if interaction.find('drugbank-id').text == check:
            return interaction.find('description').text
    return ''

def interactions(name1, name2, treeroot):
    with open('generic-names.txt','r') as generics:
        for genline in generics:
                gens = genline.split(',')
    with open('brands.txt','r') as brands:
        for brandline in brands:
            brands = brandline.split(',')
    if name1 in brands:
        if name2 in brands:
            return bbi(name1,name2,treeroot)
        elif name2 in gens:
            return bdi(name1, name2, treeroot)
        else:
            return 'ERROR {generic} NOT FOUND'.format(generic = name2)
    elif name1 in gens:
        if name2 in brands:
            return dbi(name1,name2,treeroot)
        elif name2 in gens:
            return ddi(name1, name2, treeroot)
        else:
            return 'ERROR {generic} NOT FOUND'.format(generic = name2)
    else:
        return 'ERROR {generic} NOT FOUND'.format(generic=name1)

def process_input(msg):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'e74ec3d437c84103b0cda324cef1473e',
    }
    params ={
        # Query parameter
        'q': msg,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }
    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/a7985484-8966-4125-969a-e13be956d301',headers=headers, params=params)
        print(r.json())
        return r.json()

    except Exception as e:
        print("WERROR")
def input_handler(msg, root):
    luis_out = process_input(msg)
    output_str = ''
    if luis_out['topScoringIntent']['intent'] == 'drugInteraction':
        if len(luis_out['entities'])==2:
            a = luis_out['entities'][0]['entity'].title()
            b = luis_out['entities'][1]['entity'].title()
            output_str = interactions(a,b, root)
            return output_str
        if len(luis_out['entities'])==1:
            for drug in prescriptions:
                a = luis_out['entities'][0]['entity'].title()
                output_str+=interactions(a,drug, root)+"\n"
            return output_str
        else:
            return 'Sorry, I cannot do that yet! Try a different question.'
    elif luis_out['topScoringIntent']['intent'] == 'None':
        return luis_out
    else:
        return luis_out
