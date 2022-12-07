import urllib.request
import json
from pprint import pprint
import requests as s
import random


# Importing API KEY from different file 
from config import headers

url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch'


def query_string(dish, cuisine=None, diet=None, allergies=None, time=None, info = 'true', instructions = 'true'):
    """
    Ask for dietary inputs from users and add a them to the core search dict
    """
    querystring = {}
    querystring = {"query": dish, "cuisine": cuisine, "diet": diet, "intolerances": allergies,"readyInMinutes":time, "instructionsRequrired": instructions, "addRecipeInformation": info}
    response= s.request("GET", url, headers = headers, params= querystring)
    rep = response.text
    response_data = json.loads(rep)
    return response_data

def output(dish, cuisine=None, diet=None, allergies=None, time=None, info = 'true', instructions = 'true'):
    recipe = []
    response = query_string(dish, cuisine, diet, allergies,time)
    while True:
        recipe_number = random.randint(0,len((response['results']))-1)
        # print(recipe_number)
        if 'title' in response['results'][recipe_number]:
            title = response["results"][recipe_number]["title"]
        else:
            break
        if 'summary' in response['results'][recipe_number]:
            description = response['results'][recipe_number]['summary']
        else:
            break
        if "analyzedInstructions" in response['results'][recipe_number] and len(response['results'][recipe_number]['analyzedInstructions']) != 0:
            step_list = []
            step_list.append(response['results'][recipe_number]['analyzedInstructions'][0]['steps'])
            for i in range(len(step_list[0])):
                numbered = step_list[0][i]['step']
                recipe.append(f'{i+1}. {numbered}')
            else:
                break
    return title, description, recipe
