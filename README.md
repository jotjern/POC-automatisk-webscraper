# Proof-of-concept epost greie

Dette prosjektet sjekker vg.no en gang om dagen og sender ut en e-post med alle overskriftene på forsiden. Ment som en demo for å vise hvordan man kunne implementert noe lignende. Prosjektet funker slik:

## Laste ned nettside og hente informasjon

Det er et python script som heter [main.py](./main.py) som bruker python bibliotekene [requests](https://pypi.org/project/requests/) og [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

`Requests` brukes for å gå på https://vg.no og laste ned HTML-en på forsiden.

`BeautifulSoup` tar HTML-en og leter etter `<article>` tags, og samler inn lenkene og teksten i disse lenkene.
Jeg setter sammen en e-post string som heter `email`.

## Sende ut e-post
For å så sende ut dette som en e-post brukte jeg noe som heter `smtplib`. Man kan bruke et "App password" til å logge inn på gmail.

Du kan lage et her: https://support.google.com/mail/answer/185833?hl=en

Vi har "GMAIL_APP_PASSWORD" som en environment-variabel så vi ikke committer den. 

## Kjøre scriptet en gang om dagen
Github actions kan kjøre kode, og har den har en greie hvor du kan si at den skal kjøre hver dag eller uke eller lignende.

Koden for dette ligger i [workflows.yml](/.github/workflows/workflow.yml), kokte hele greia fra https://medium.com/nerd-for-tech/lets-run-cron-jobs-using-github-actions-df64496ffc4a og https://www.geeksforgeeks.org/run-python-script-in-github-actions/

Vi definerer hvor ofte og når den skal kjøre her:
```
    # Every day at 08:00 London time
    - cron: '0 8 * * *'
```
Dette er en cronjob, veldig scuffed å finne ut hva det betyr, men bare å spørre chat.

Eneste spesielle er at vi må hente GMAIL_APP_PASSWORD fra et sted, la den inn som en "repository secret" (idk hva det er egt) ved å gå på github repositoriet, settings, secrets and variables også actions. Da kan vi bruke den i `workflow.yml` til å sette en env variabel. 

