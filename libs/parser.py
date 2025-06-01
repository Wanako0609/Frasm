from libs.instruction import *
def executer_initialisation(instruc, pointeur, programme):
    if not instruc or instruc[0].strip() == "":
        return pointeur, True  # Ligne vide

    #print("init")
    match instruc[0]:
        case "definir":
            definir(instruc[1:])
        case "charger":
            charger(instruc[1:])
        case "revenir":
            return revenir(), True
        case _:
            error_and_exit("Execution", f"Seul definir et charger sont autorisé pendant l'initialisation : {instruc[0]}")

    return pointeur, True

def executer_instruction(instruc, pointeur, programme):
    if not instruc or instruc[0].strip() == "":
        return pointeur, True  # Ligne vide

    match instruc[0]:
        case "definir":
            definir(instruc[1:])
        case "somme":
            somme(instruc[1:])
        case "soustraire":
            soustraire(instruc[1:])
        case "ecrire":
            ecrire(instruc[1:])
        case "charger":
            charger(instruc[1:])
        case "produit":
            produit(instruc[1:])
        case "quotient":
            quotient(instruc[1:])
        case "aller":
            return aller(instruc[1:], pointeur), True
        case "revenir":
            return revenir(), True
        case "caractere":
            caractere(instruc[1:])
        case "si":
            if si(instruc[1:]):
                # On doit exécuter la prochaine instruction sur la même ligne (type: si a == b aller X)
                if len(instruc) >= 6 and instruc[4] == "aller":
                    # Test si l'instruction apres le si est si non. Si oui on le pointeur le saute
                    if programme[pointeur + 1].strip().split(' ')[0] == "sinon":
                        return aller(instruc[5:], pointeur+2), True
                    return aller(instruc[5:], pointeur), True
                else:
                    error_and_exit("si", "Il manque l'instruction à exécuter après la condition")

            # Gestion de sinon
            else:
                instruc_sinon = programme[pointeur + 1].strip().split(' ') # Permet d'analyser l'instruction de sinon
                if instruc_sinon[0] == "sinon":
                    if len(instruc_sinon) == 3 and instruc_sinon[1] == "aller":
                        return aller(instruc_sinon[2:], pointeur+1), True # +1 pour que le pointeur revienne sur l'instruction de apres le sinon
                    else:
                        error_and_exit("sinon", "Il manque l'instruction à exécuter après la condition")
                else:
                    return pointeur, True

        case "fin":
            return pointeur, False
        case _:
            error_and_exit("Execution", f"Instruction inconnue : {instruc[0]}")

    return pointeur, True
