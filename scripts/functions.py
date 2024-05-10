from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara

def numbers_to_words (number):
    number2word = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
            '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
    return " ".join(map(lambda i: number2word[i], str(number)))

def invalid_to_valid_name(name):
        return ''.join(e for e in name if e.isalnum())

def configure_zebra(router, words):
        try :
                router.update_file_from_list(
                lines=[
                f"interface {words[1]}",
                f" ip address {words[2]}" 
                ],
                dst_path= "/etc/frr/zebra.conf"
                )
        except Exception:
                pass              