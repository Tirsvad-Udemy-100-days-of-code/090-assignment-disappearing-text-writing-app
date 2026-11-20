[English](Reflection) · **Dansk** · [Bahasa Malaysia](Reflection-ms)

# Refleksion

## Sådan blev projektet grebet an

Arbejdet fulgte plan-først-processen: først en business case, en interessentanalyse, en projektplan og fire milepæle. Derefter blev én use case designet (domænemodel, sekvensdiagrammer, klassediagram), før der blev skrevet kode. Hver milepæl var én gren og én pull request. Reglen, der sletter teksten, blev først skrevet som en almindelig Python-klasse med tests, og Flask kom ovenpå.

## Hvad der var svært

- At beslutte, hvor timeren bor. En timer i JavaScript er hurtig, men kan ikke testes med pytest. Når den bor på serveren, kan reglen testes, og browseren bliver en enkel visning.
- Et kapløb mellem skrivning og polling: et gammelt pollsvar kunne melde, at teksten var slettet, lige efter skribenten havde skrevet et nyt bogstav. Scriptet ignorerer nu svar, der startede før det seneste tastetryk.
- At holde dokumenter, diagrammer og kode i takt, da designet ændrede sig (weblaget blev først designet, efter kernen var færdig).

## Hvad der var let

- Selve reglen: én klasse med tre små metoder.
- Test med falsk ur: ingen test venter i fem sekunder.
- Flask: en app-fabrik, ét blueprint og to ruter var nok.

## Hvad der skal forbedres næste gang

- Test browser-scriptet automatisk. I dag viser kun skærmbillederne fra en container, at det virker.
- Tegn wireframen først og gennemgå den med en læser før designet.
- Start værktøjet til skærmbilleder tidligere, så hvert trin fanges, mens det bygges.

## Den største læring

Hold reglen uden for frameworket. Når reglen er almindelig kode, der får tiden som en værdi, er den let at teste, og weblaget kan blive tyndt.

## Hvad jeg ville gøre anderledes

Tilføje en lille end-to-end-test i containeren, der skriver, venter og tjekker siden, så skærmbillederne bliver et biprodukt af en test og ikke et separat script.
