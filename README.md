# Progetto Orders

Benvenuto al progetto Orders.

Si tratta di un sistema per monitorare e gestire gli ordini giornalieri degli utenti.

## Prerequisiti
- Prima di avviare l'applicazione in locale, assicurati di avere installato Python sul tuo sistema e di essere all'interno della root principale.
- Prima di avviare il docker-compose.yml, assicurarsi di avere installato Docker sul sistema.


## Authors

- [@jsotamba](https://github.com/jsotamba)

## Project Structure
- `orders/`: Directory principale.
- `docs/`: Contiene la documentazione del progetto.
- `orders/settings`: Contiene le configurazioni 
- `apps/`: Contiene le app(`order` e `product`)
- `apps/<app>/api`: Contiene i serializers, views e ulrs
- `apps/<app>/unit_test`: Contiene tutti gli unit test


## Documentazione

Per maggiori dettagli, consulta: 
- [Analisi funzionale](docs/Orders_Analisi Funzionale_v1.docx)
- [Analisi tecnica](docs/Orders_Analisi Tecnica_v1.docx)

## Running Tests

Per eseguire i test unitari, eseguire il seguente comando

```bash
  python manage.py test # all tests
  python manage.py test apps.order # only order app tests
  python manage.py test apps.product # only product app tests
```

## Run project

### Per eseguire questo progetto in locale effetuare le seguenti operazioni:
```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
```
Alla fine di quest'ultimo comando, avviare il server
```bash
   python manage.py runserver 0.0.0.0:8000
```

### Per eseguire il progetto tramite docker-compose.yml:
```bash
  docker-compose up --build
```

## API Reference

#### Swagger

```http
  GET /swagger/
```

#### Docs

```http
  GET /redoc/
```

