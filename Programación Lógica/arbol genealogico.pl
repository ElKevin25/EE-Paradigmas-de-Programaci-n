hombre(arturo).
hombre(kevin).
hombre(luis).
hombre(terrence).
hombre(perceo).
hombre(jorge).
hombre(alfredo).
hombre(harry).
hombre(james).
hombre(albus).
hombre(ron).
hombre(hugo).

mujer(molly).
mujer(flor).
mujer(victoria).
mujer(domitila).
mujer(audrey).
mujer(lucy).
mujer(molly).
mujer(angelina).
mujer(roxanne).
mujer(ginny).
mujer(lily).
mujer(hermione).
mujer(rose).

madre(molly,bill).
madre(molly,percy).
madre(molly,george).
madre(molly,ginny).
madre(molly,ron).
madre(fleur,victoire).
madre(fleur,dominique).
madre(fleur,louis).
madre(audrey,lucy).
madre(audrey,molly).
madre(angelina,fred).
madre(angelina,roxanne).
madre(ginny,james).
madre(ginny,lily).
madre(ginny,albus).
madre(hermione,hugo).
madre(hermione,rose).

padre(arturo,bill).
padre(arturo,percy).
padre(arturo,george).
padre(arturo,ginny).
padre(arturo,ron).
padre(terrence,victoire).
padre(terrence,dominique).
padre(terrence,louis).
padre(perceo,lucy).
padre(perceo,molly).
padre(jorje,fred).
padre(jorje,roxanne).
padre(harry,james).
padre(harry,lily).
padre(harry,albus).
padre(ron,hugo).
padre(ron,rose).

progenitor(Padre, Hijo) :- padre(Padre,Hijo).

progenitor(Madre, Hijo) :- madre(Madre, Hijo).

hermano(Hermano1, Hermano2) :- hombre(Hermano1),
        ((madre(_,Hermano1), madre(_,Hermano2));(padre(_,Hermano1),padre(_,Hermano2))).

hermana(Hermana1, Hermano2) :- mujer(Hermana1),
    ((madre(_,Hermana1), madre(_,Hermano2));(padre(_,Hermana1),padre(_,Hermano2))).

abuelo(Nieto, Abuelo) :- padre(Padre,Nieto), padre(Abuelo, Padre).

abuelo(Nieto, Abuelo) :- madre(Madre,Nieto), madre(Abuelo, Madre).

hermanos(Hermano1, Hermano2) :- padre(Progenitor, Hermano1) ; padre(Progenitor, Hermano2) ;
        (madre(Progenitor, Hermano1); madre(Progenitor, Hermano2)).
