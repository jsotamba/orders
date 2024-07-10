from enum import Enum


class MessageEnum(Enum):
    SUCCESS = "Operazione completata con successo."
    ERROR = "Si è verificato un errore."
    NOT_FOUND = "Risorsa non trovata."
    UNAUTHORIZED = "Accesso non autorizzato."
    FORBIDDEN = "Accesso vietato."
    BAD_REQUEST = "Richiesta non valida."
    SERVER_ERROR = "Errore interno del server."
    CREATED = "Risorsa creata con successo"
    DELETED = "Risorsa eliminata con successo"
    UPDATED = "Risorsa modificata con successo"


def get_message_by_code(enum_member) -> dict:
    return {"message": enum_member.value}
