""" 
Description: 
Makes a new PasteBin paste with a list of a Pokemon's skills in it.
Usage:
  python pokemon_paste.py poke_name
Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_data = poke_api.get_pokemon_info(poke_name)
    if poke_data is not None:
        paste_title, paste_body = get_paste_data(poke_data)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        print(paste_url)

def get_pokemon_name():
    """Obtains the Pokemon name that was sent in as a command line argument.
    Script execution is aborted if no command line parameter is supplied.

    Returns:
        str: Pokemon name
    """
    # TODO: function body
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print(f"Error: Missing parameters.")
        return

def get_paste_data(pokemon_data):
    """Builds the title and body text 
    Args:
        pokemon_info (dict): Dictionary of Pokemon information
    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # TODO: Build the Title and paste body text
    pokemon_name = pokemon_data['name']
    title= f"{pokemon_name.capitalize()}'s Abilities"
    abilities_list = []

    for each_ability in pokemon_data['abilities']:
        abilities_list.append(each_ability['ability']['name'])
    body = '- ' + '\n- '.join(abilities_list)
    print(body)
    return (title,body)

if __name__ == '__main__':
    main()