# Rasa_Chatbot_Multilingual

Telco Chatbot est un assistant virtuel multilingue (français/anglais) pour les opérateurs téléphoniques tunisiens. Ce bot répondra à vos questions et fournira des recommandations sur les offres, promotions, etc. disponibles auprès des opérateurs sélectionnés. 
Telco Bot est développé par le framework RASA. Ce chatbot peut être utilisé comme point de départ pour créer un assistant de service client.

Voici un exemple de conversation que vous pouvez avoir avec ce bot :

![exp1](https://user-images.githubusercontent.com/47745783/185938094-1fc73719-7ac4-4d95-aeb4-44309554be24.PNG)    

![exp2](https://user-images.githubusercontent.com/47745783/185938179-6e0253be-590c-4ef0-8ca1-aff8c4850b3c.PNG)


# Installer 

## Installer les dépendances

Dans un environnement virtuel Python3, exécutez :

> pip install -r requirements.txt
    
# Exécution du bot 

### Entrainer les modéles: 
```
rasa train --config config_fr.yml 
rasa train --config config_en.yml

```

### Pour éxecuter le projet : 

configurez d'abord votre serveur d'action dans une fenêtre de terminal :

rasa run actions 

Ensuite, pour parler au bot, exécutez :

rasa shell --debug

# Déploiement 

Pour que le déploiement fonctionne, exécutez la commande :

rasa run --enable-api --cors "*" 

Dans une autre une fenêtre de terminal :

python app.py 

Dans une autre une 3éme fenêtre de terminal :

rasa run actions --cors "*"
