#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import skimage    

home = html.H1(children= "Guess who - Whoogle Images", 
                  style= {'margin-left':'10px', 'margin-top':'120px','text-align':'center','font-size':'70px','margin-bottom':'20px'})

lib = dict()
lib['Chicken'] = "The chicken (Gallus gallus domesticus), a subspecies of the red junglefowl, is a type of domesticated fowl. Rooster or cock is a term for an adult male bird. A younger male may be called a cockerel; a male that has been castrated is a capon. The adult female bird is called a hen. Originally raised for cockfighting or for special ceremonies, chickens were not kept for food until the Hellenistic period (4th–2nd centuries BCE).[1][2] Humans now keep chickens primarily as a source of food (consuming both their meat and eggs) and, less commonly, as pets."
lib['Cow'] = "Cattle, or cows (female) and bulls (male), are the most common type of large domesticated ungulates. They are a prominent modern member of the subfamily Bovinae, are the most widespread species of the genus Bos, and are most commonly classified collectively as Bos taurus.\n Cattle are commonly raised as livestock for meat (beef or veal, see beef cattle), for milk (see dairy cattle), and for hides, which are used to make leather. They are used as riding animals and draft animals (oxen or bullocks, which pull carts, plows and other implements). Another product of cattle is their dung, which can be used to create manure or fuel. In some regions, such as parts of India, cattle have significant religious meaning. Cattle, mostly small breeds such as the Miniature Zebu, are also kept as pets."
lib['Deer'] = "Deer or true deer are hoofed ruminant mammals forming the family Cervidae. The two main groups of deer are the Cervinae, including the muntjac, the elk (wapiti), the red deer, the fallow deer, and the chital; and the Capreolinae, including the reindeer (caribou), the roe deer, the mule deer, and the moose. Female reindeer, and male deer of all species except the Chinese water deer, grow and shed new antlers each year. In this they differ from permanently horned antelope, which are part of a different family (Bovidae) within the same order of even-toed ungulates (Artiodactyla)."
lib['Human'] = "Humans (Homo sapiens) are a species of highly intelligent primates. They are the only extant members of the subtribe Hominina and—together with chimpanzees, gorillas, and orangutans—are part of the family Hominidae (the great apes, or hominids). Humans are terrestrial animals, characterized by their erect posture and bipedal locomotion; high manual dexterity and heavy tool use compared to other animals; open-ended and complex language use compared to other animal communications; larger, more complex brains than other primates; and highly advanced and organized societies"
lib['Monkey']= "Monkey is a common name that may refer to groups or species of mammals, in part, the simians of infraorder Simiiformes. The term is applied descriptively to groups of primates, such as families of New World monkeys and Old World monkeys. Many monkey species are tree-dwelling (arboreal), although there are species that live primarily on the ground, such as baboons. Most species are mainly active during the day (diurnal). Monkeys are generally considered to be intelligent, especially the Old World monkeys of Catarrhini."
lib['Pig'] = "A pig is any of the animals in the genus Sus, within the even-toed ungulate family Suidae. Pigs include domestic pigs and their ancestor, the common Eurasian wild boar (Sus scrofa), along with other species. Pigs, like all suids, are native to the Eurasian and African continents, ranging from Europe to the Pacific islands. Suids other than the pig are the babirusa of Indonesia, the pygmy hog of South Asia, the warthog of Africa, and another genus of pigs from Africa. The suids are a sister clade to peccaries."
lib['Rabbit']= "Rabbits are small mammals in the family Leporidae (along with the hare) of the order Lagomorpha (along with the pika). Oryctolagus cuniculus includes the European rabbit species and its descendants, the world's 305 breeds[1] of domestic rabbit. Sylvilagus includes 13 wild rabbit species, among them the seven types of cottontail. The European rabbit, which has been introduced on every continent except Antarctica, is familiar throughout the world as a wild prey animal and as a domesticated form of livestock and pet. With its widespread effect on ecologies and cultures, the rabbit (or bunny) is, in many areas of the world, a part of daily life—as food, clothing, a companion, and a source of artistic inspiration."
lib['Sheep'] ="Sheep (Ovis aries) are quadrupedal, ruminant mammals typically kept as livestock. Like all ruminants, sheep are members of the order Artiodactyla, the even-toed ungulates. Although the name sheep applies to many species in the genus Ovis, in everyday usage it almost always refers to Ovis aries. Numbering a little over one billion, domestic sheep are also the most numerous species of sheep. An adult female is referred to as a ewe, an intact male as a ram, occasionally a tup, a castrated male as a wether, and a young sheep as a lamb."

logo_dossier = 'https://www.icone-png.com/png/54/54079.png'
logo_google = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/1200px-Google_%22G%22_Logo.svg.png'
logo_aide = 'https://image.flaticon.com/icons/png/512/18/18436.png'

# alert = html.Div([
#     dbc.Row([
#         html.P(
#         dbc.Button(
#             # html.Img(src=logo_aide, height="15px",style = {'margin-left':'80px'}),
#             "Click here to read some instructions before start",id = 'read-instructions', color="link"),
#         style = {'margin-left':'60px', 'margin-bottom':'2px','font-style':'italic'})])])

search_bar = html.Div([
    dbc.Navbar([
dbc.Row([
     dbc.Col(
         html.A(
             dbc.Button(
                 html.Img(src=logo_google, height="25px"),id = 'logo_folder', size = 'sm', color="dark"),
             href = 'https://www.google.fr/imghp?hl=fr&authuser=0&ogbl',
             target = '_blank'),
         style = {'margin-left':'1px'}),
     dbc.Col(
         dcc.Upload(
             dbc.Button(
             html.Img(src=logo_dossier, height="30px"),id = 'logo_google', size = 'sm',color="dark"), id= 'upload-image'),
         width=0.2, style = {'margin-right':'2px'}),
     dbc.Col(
         dbc.Input(id= 'input-img', type="url", placeholder="Coller l'URL de l'image ou le chemin d'accès du fichier", size = '500', maxLength=524288), width = 9.85),
     dbc.Col(
            dbc.Button("Guess who", color="primary", className="ml-2", id= 'guess-button'),
            # toast],
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
],
color= 'dark'
)])

modal = html.Div([
    html.P(
        dbc.Button(
            # html.Img(src=logo_aide, height="15px",style = {'margin-left':'80px'}),
            "Click here to read some instructions before start",id = 'read-instructions', color="link"),
        style = {'margin-left':'60px', 'margin-bottom':'2px','font-style':'italic'}),
        dbc.Modal(
            [
                dbc.ModalHeader("Some instructions before start"),
                dbc.ModalBody(dcc.Markdown('''
* You can only test individuals from the following list: pig, cow, rabbit, monkey, human, chicken, deer, sheep.
* You can upload the images from Google Images or directly from your file explorer.
* Favor images with the heads of individuals.
* Favor images with individuals alone.''')),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto")
                ),
            ],
            id="modal",
        ),
    ]
)

