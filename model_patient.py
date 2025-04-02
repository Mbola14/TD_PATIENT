from typing import Annotated
from pydantic import AfterValidator, BaseModel, ValidationError

def verifier_ssr(ssn:str) -> str:
    if not ssn:
        raise ValueError("Le numéro de sécurité sociale est vide")
    if len(ssn) != 15:
        raise ValueError("La longueur doit être exactement 15 caractères")
    if ssn[0] not in ('1', '2'):
        raise ValueError("Le premier chiffre doit être 1 ou 2")
    if not (ssn[3:5].isdigit() and 1 <= int(ssn[3:5]) <= 12):
        raise ValueError("Mois non valide")
    validation = int(ssn[0:13])
    cle = int(ssn[-2:])
    print(validation%97)
    print(cle)
    if validation % 97 != cle:
        raise ValueError("Il y a une erreur dans le numéro de sécurité sociale")
    return ssn

class Patient(BaseModel):
    nom:str
    prenom:str
    ssn: Annotated[str, AfterValidator(verifier_ssr)]

    @property
    def nom(self) -> str:
        return self.nom
    
    @property
    def prenom(self) -> str:
        return self.prenom
    
    @property
    def ssn(self) -> str:
        return self.ssn

