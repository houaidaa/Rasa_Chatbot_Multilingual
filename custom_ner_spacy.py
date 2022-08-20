import spacy
import random
from spacy.util import minibatch, compounding
from pathlib import Path
from spacy.training.example import Example


nlp = spacy.load("fr_core_news_md")

#print(nlp.pipe_names)

# Getting the pipeline component
ner = nlp.get_pipe("ner")

trainData = [("Puis-je vous emprunter 500 dollars pour acheter des actions Microsoft", {"entities": [(23, 34, "Money")]}),
             ("Tesla va construire un royaume-uni usine pour 6 milliards", {"entities": [(46, 57, "Money")]}),

             ("Comment procéder pour mieux bénéficier de l'offre Darbox.", {"entities": [(50, 56, "OffreBoxOrg")]}),
             ("Pour Darbox quel est la procédure à suivre pour profiter de l'offre", {"entities": [(5, 11, "OffreBoxOrg")]}),
             ("Où je peux trouver les instructions à faire pour profiter de l'offre Darbox, ça se fait en ligne ou sur place ?", {"entities": [(69, 75, "OffreBoxOrg")]}),
             ("Instructions à faire pour Darbox", {"entities": [(26, 32, "OffreBoxOrg")]}),
             ("Je voulais savoir à propos de l'offre Darbox, comment procéder pour en profiter ?", {"entities": [(38, 44, "OffreBoxOrg")]}),
             ("À propos de Darbox quelle instruction faisait pour profiter de cette offre", {"entities": [(12, 18, "OffreBoxOrg")]}),
             ("Je voulais connaître l'offre de Darbox, comment faire pour en bénéficier ?", {"entities": [(32, 38, "OffreBoxOrg")]}),
             ("Je voulais connaître la proposition de Darbox, comment en profiter ?", {"entities": [(39, 45, "OffreBoxOrg")]}),

             ("On commande le flybox postpaye en ligne ?", {"entities": [(15, 30, "OffreBoxOrg")]}),
             ("Est ce que le flybox postpaye est vendu en ligne ?",{"entities":[(14,29,"OffreBoxOrg")]}),
             ("Pour le Flybox postpaye comment on passe la commande ?", {"entities": [(8, 23, "OffreBoxOrg")]}),
             ("Comment effectuer une commande pour le flybox postpaye ?", {"entities": [(39, 54, "OffreBoxOrg")]}),
             ("Comment commander le flybox postpaye, comment faire pour paiement ?",{"entities": [(21, 36, "OffreBoxOrg")]}),
             ("On fait la commande de Flybox postpaye en ligne ?", {"entities": [(23, 38, "OffreBoxOrg")]}),
             ("Comment acheter le flybox postpaye", {"entities": [(19, 34, "OffreBoxOrg")]}),
             ("Je voulais connaître l'offre de flybox postpaye, comment faire pour en bénéficier ?",{"entities":[(32, 47, "OffreBoxOrg")]}),
             ("Je voulais savoir la proposition de flybox postpaye, comment en profiter ?", {"entities": [(36, 51, "OffreBoxOrg")]}),

             ("Comment puis-je profiter de l'offre giga plus", {"entities": [(36, 45, "OffreGigaPlus")]}),
             ("Comment utiliser l'offre giga plus", {"entities": [(25, 34, "OffreGigaPlus")]}),
             ("Pour l'offre Giga plus comment faire pour en profiter", {"entities": [(13, 22, "OffreGigaPlus")]}),
             ("Pour le Giga plus comment en peut on profiter ", {"entities": [(8, 17, "OffreGigaPlus")]}),
             ("Au sujet de l'offre de giga plus, comment puis-je en profiter?", {"entities": [(23, 32, "OffreGigaPlus")]}),

             ("On peut activer le pass Hajj via le téléphone ou on le fait sur le site ?", {"entities": [(24, 28, "OffreHajj")]}),
             ("Nous pouvons activer le pass du Hajj par téléphone ou sur le site .", {"entities": [(32, 36, "OffreHajj")]}),
             ("Pour l'offre du Hajj, comment faire pour profiter d'elle ?", {"entities": [(16, 20, "OffreHajj")]}),
             ("Comment profiter de l'offre du hajj ?", {"entities": [(31, 35, "OffreHajj")]}),
             ("Comment bénéficier de l'offre du hajj ?", {"entities":[(33, 37, "OffreHajj")]}),
             ("Est ce qu'on peut profiter de plus de 250 Mo pour l'offre  du Hajj?", {"entities": [(61, 65, "OffreHajj")]}),
             ("Est-il possible de tirer profit de plus de 250 Mo concernant l'offre Hajj?", {"entities": [(69, 73, "OffreHajj")]}),
             ]

# Adding labels to the `ner`
for _, annotations in trainData:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable pipeline components you dont need to change
pipe_exceptions = ["ner", "tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]


# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes):
    # Training for 30 iterations
    for iteration in range(50):
        random.shuffle(trainData)
        losses = {}
        batches = minibatch(trainData, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)

        example = []
        # Update the model with iterating each text
        for i in range(len(texts)):
            doc = nlp.make_doc(texts[i])
            example.append(Example.from_dict(doc, annotations[i]))
            # Update the model
            nlp.update(example, losses=losses, drop=0.3)
            #print("Losses", losses)

# Testing the model


# Save the  model to directory
output_dir = Path("C:/Model_Spacy/")
nlp.to_disk(output_dir)
print("Saved model to", output_dir)

# Load the saved model and predict
print("Loading from", output_dir)
nlp_updated = spacy.load(output_dir)

doct = nlp_updated("45 milliards existe dans mon compte")
print("Entities", [(ent.text, ent.label_) for ent in doct.ents])

doc1 = nlp_updated("j'habite à paris")
print("Entities", [(ent.text, ent.label_) for ent in doc1.ents])

doccc= nlp_updated("Pour Darbox quels sont les instructions à suivre")
print("Entities", [(ent.text, ent.label_) for ent in doccc.ents])

tt = nlp_updated("Comment acheter le flybox postpaye")
print("Entities", [(ent.text, ent.label_) for ent in tt.ents])

ddd = nlp_updated("Pour l'offre Giga plus comment faire pour en profiter")
print("Entities", [(ent.text, ent.label_) for ent in ddd.ents])
