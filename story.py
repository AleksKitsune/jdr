beginning = "Vous vous reveillez tout les deux dans un endrois complètement inconnu[bold blue] habillés uniquement d'un caleçon et d'une culotte[/], vous êtes allongés sur une banquette. Autour de vous une pièce vide fermé par des barreaux et deux gardes devant, un homme et une femme.\n"\
            "Vous réalisez rapidement que vous êtes enfermé dans une cellule mais n'avez ni l'un ni l'autre aucune idée de comment vous avez attéris là\n\n[bold white]Garde homme:[/] Vous emmergez enfin, j'ai bien cru que je n'aurai pas le plaisir de vous voir pendu\n"\
            "[bold white]Garde femme:[/] Cela aurait été vraiment dommage hahahaha\n\n"\
            "Estomaqué par ce qu'il venait de dire vous commencez à paniquer et à demander pourquoi vous êtes enfermé dans cette cellule et pourquoi parle il de pendaison, malheureusement seul le son de leur rire vient apporter de bien maigres réponses...\n\n"\
            "Après plusieurs jours d'angoisse, vous n'avez pas réussi à en apprendre beaucoups plus, tout ce que vous avez appris est que vous étiez dans une grande prison ou un donjon et que régulièrement de nouveaux gardes, toujours un couple d'homme et femme, venaient prendre la relève, probablement pour ne pas prendre risque de trop s'attacher à vous... "\
            "Chose dont vous doutiez fortement, vu l'amabilité que chacun d'eux avait pour vous deux...\n\n"\
            "Au bout de ce qui vous a semblé être une semaine la nouvelle est tombé, demain matin aux premières lueur du jour vous finirez la corde au cou, sans avoir la moindre idée de ce que vous avez fait pour mériter ça.\n"\
            "Sans trop d'espoir vous demandez en guise de dernière requête de l'alcool pour noyer votre incompréhension ensemble et passer un dernier 'bon moment' l'un avec l'autre\n"\
            "A votre grande surprise les deux gardes acceptent, mais le sourire vicieux sur leurs lèvres ne vous inspire pas vraiment confiance...\n"\
            "[bold white]Garde femme:[/] Il y aura juste une condition pour que vous buviez, nous allons jouer à un petit jeu tout les quatres...\n\n"\
            "Le garde homme vous fait passer une bouteille en plastique rempli de vin ainsi que deux verres eux même en plastique\n\n"\
            "[bold white]Garde homme:[/] Vous connaissez le jeu 'je n'ai jamais'? Nous allons faire des affirmations par exemple 'Je n'ai jamais bu d'alcool' et à chaques fois que l'un de vous avez fait l'affirmation en question [bold blue]vous buvez une gorgée de vin sans expliquer quoi que ce soit ou donner de contexte[/]\n\n"\

denial_alcohol = "Vous êtes tout les deux des personnes fières, vous refusez de leur donner la satisfaction de vous manipuler comme ils le veulent malgré votre fin imminente! Vous passez la nuit sobre et êtes pendu aux premières lueurs du jour comme prévu...\n"\
                "Fin"

accept_alcohol = "Vous mettez votre fièreté de côté et acceptez de jouer, à quoi bon être fier alors que la mort vous tend les bras... Avec un peu de chance vous finirez suffisement bourré pour ne pas sentir la corde. Avant de commencez vous vous [bold blue]promettez sur votre amitié de ne rien ommetre et boire à chaques fois que necessaire[/]\n\n"\
                "[bold white]Garde homme:[/] Commençons:\n"

truth_list = [
    "Je n'ai jamais trompé quelqu'un",
    "Je n'ai jamais vomis à cause de l'alcool",
    "Je n'ai jamais utilisé de fausse carte d'identité",
    "Je n'ai jamais embrassé plus d'une personne en 24 heures",
    "Je n'ai jamais eu d'aventure d'un soir",
    "Je n'ai jamais volé",
    "Je n'ai jamais ri au point de faire pipi dans mon pantalon en tant qu'adulte",
    "Je n'ai jamais envoyé de sexto",
    "Je n'ai jamais envoyé de nude",
    "Je ne me suis jamais endormi pendant un rapport sexuel",
    "Je n'ai jamais donné/reçu un lap dance",
    "Je ne me suis jamais masturbé dans un lieu public/en plein air",
    "Je n'ai jamais pris de drogue douce",
    "Je n'ai jamais pris de drogue dure",
    "Je n'ai jamais léché les pieds de quelqu'un",
    "Je n'ai jamais fait l'amour dans une voiture",
    "je n'ai jamais pratiqué la sodomie",
    "Je n'ai jamais donnée/reçu de golden shower",
    "je n'ai jamais eu de relation sexuelle avec une personne du même sexe",
    "Je n'ai jamais fait de plan à trois"
]

aleks_drinks = []
kitsune_drinks = []
both_drinks = [] 

after_truth = "[bold white]Garde femme:[/] C'était marrant mais ça manque trop de détails à mon gout...\n\n"\
            "La garde part et reviens avec 4 verres à shot en plastique et une bouteille avec un alcool inconnu, vraisemblablement quelque chose de fort...\n\n"\
            "[bold white]Garde femme:[/] Sur chaques 'je n'ai jamais' où vous avez bu, vous devez donner le maximum de détails sur ce qu'il c'est passé (si c'est arrivé plusieur fois, parlez de la plus marquante), si l'un de vous ne répond pas vous devez tout les deux boire un shot, a chaque fois que vous répondez nous devrons boire\n"

denial_shots = "Vous refusez par fièreté mais à force d'en discuter tout au long de la nuit vous vous rendez compte que vous venez peut être de laisser passer une opportunité de vous échapper... Vous finissez pendu le coeur plein de regret..."\
                "Fin"

accept_shots = "Vous acceptez et comptez bien les faire boire autant que possible, les chances vous parraissent maigre mais l'ombre d'un plan pour s'échapper se forme...\n"

not_drunk = "Les gardes ne sont pas assez bourré, vous avez fait ce vous avez pu mais n'avez malheureusement pas réussi à profiter de la situation... Vous finissez pendu comme prévu au petit matin.\n"\
            "Fin"

drunk = "Les gardes se sont endormis!! Vous arrivez à voler le trousseau de clef de l'un d'eux et à ouvrir la cage. Vous en profitez pour voler leur vêtement, tout vous va à peut près sauf le soutiens-gorge de la garde que kitsune ne peut pas mettre, [bold blue]vous vous habillez[/]\n"\
        "En les déshabillant vous trouvez deux mattraques et une carte de la prison!\n"\
        "Au dos de la carte vous voyez une inscription étrange:\n"\
        "Carte des gardes en chefs: après le premier sas votre havre de paix se trouve en (0, 6), cette carte est la seule clef pour y accéder\n"\
        "Vous n'y prétez pas attention pour le moment et foncez avant d'être repéré!\n"

room1 = "Vous avancez dans le couloir étrois jusqu'à atteindre une porte,vous rentrez dans la pièce.\n"\
        "Vous êtes dans ce qu'il semble être une salle de repos\n"

choice1 = "Vous avez à peine le temps de jeter un oeil à la salle vous entendez du bruit au niveau de la porte au fond du couloir à la sortie, des gardes sont sur le point de rentrer...\n"\
        "[bold white]Garde Femme:[/] J'ai bien faillis me faire avoir par la nouvelle question du sas, la taille de ta bite en érection sérieusement!\n"\
        "[bold white]Garde Homme:[/] Heureusement qu'on en a parlé il n'y a pas si longtemps! Certains ne vont pas avoir la même réponse, ça va être drole d'aller les chercher la dedans\n"\
        "Les gardes viennent d'ouvrir la porte vous devez vite prendre une décision\n"\
            "1. Faites vous passer pour des gardes pour tenter de quitter la pièce sans encombre (+0)\n"\
            "2. Vous repérez un petit placard vide et vous vous précipitez dedans, vous êtes tellement à l'étrois que vous êtes obligé de vous serrer dans les bras. Vous êtes bien caché mais il ne faudrait quand même pas qu'ils s'éternise dans la pièce trop longtemps... (+5)\n"\
            "3. Vous vous mettez rapidement en sous-vetêment et vous collez l'un à l'autre quand les gardes arrivents +(10)\n"

choice1_1 = "Vous saluez les gardes à leur entrée et continuez votre chemin vers la sortie...\n"\
            "[bold white]Garde femme:[/] atendez! Vous puez tout les deux! Vous devriez pourtant savoir qu'une des première règle ici est une hygiène impécable!\n"\
            "[bold white]Garde homme:[/] C'est marrant je ne vous ai jamais vu avant...\n"\
            "[bold white]Kitsune:[/] ... Nous sommes nouveau et en fin de patrouille, il fait vraiment chaud ici difficile de ne pas transpirer"\
            "[bold white]Garde homme:[/] C'est étrange quand même...\n"\
            "Soudain des cris sont entendu depuis votre ancienne celulle!!\n"\
            "[bold white]Garde femme:[/] Surveille les je vais voir ce qu'il se passe!\n"\
            "Une fois la garde partie le garde homme vous regarde tout les deux avec suspicion, aleks se voyait déjà la corde au cou lorsque Kitsune fit quelque chose d'innatendu et [bold blue]souleva son haut[/] devant le garde!\n"\
            "[bold blue]Au bout de 5 secondes[/] aleks repris ses esprits et sauta matraque en l'air sur le garde complètement déboussolé par la poitrine de Kitsune.\n"\
            "Une fois le garde maitrisé et attaché vous filez vers la sortie et entendez dans le couloir juste avant la pièce une horde de garde prêt à vous récupérer!\n"\
            "Votre evasion est repéré et avez perdu du temps avec le garde, votre avance est mince\n"

choice1_2 = "Vous restez blotis l'un contre l'autre dans ce placard [bold blue]pendant une bonne minute[/] quand soudain des cris sont entendu depuis votre ancienne celulle!\n"\
            "Les deux gardes se précipitent hors de la pièce pour voir ce qu'il se passe, vous sortez de votre cachette et filez vers la sortie opposé!\n"\
            "Votre évasion est repéré mais vous avez un peu d'avance sur vos assaillants\n"

choice1_3 = "Les gardes vous surprennent en plein calin à moitier nu et s'excusent immédiètement avant de filer vers la sortie en moins de [bold blue]10 secondes[/]\n"\
            "Vous vous rabillez en coups de vent et prennez la sortie opposé sans demander votre reste\n"\
            "Votre évasion va être repéré dans moins d'une minute mais vous avez déjà quitté la pièce, vous avez une avance confortable!\n"

choice2_aleks = "Vous arrivez dans une sorte d'antichambre suivis d'un couloir menant vers une petite pièce carré, vous entrez dans la pièce quand soudains un mur s'érige entre vous deux vous séparant, [bold blue]vous ne pouvez plus communiquer[/]\n"\
        "[bold white]Voix robotique:[/] garde homme, merci de rentrer la taille de votre sexe en érection en centimètre sur l'écran contre le mur, votre partenaire devra rentrer la même valeur sous peine de rester coincés et subir un examen de sécurité par vos supérieurs\n"

choice2_kitsune = "[bold white]Voix robotique:[/] garde femme, merci de rentrer la taille du sexe de votre partenaire en érection en centimètre sur l'écran contre le mur, vous devez rentrer pas la même valeur sous peine de rester coincés et subir un examen de sécurité par vos supérieurs\n"

choice2_fail = "[bold white]Voix robotique:[/] La valeur n'est pas la même, vos supérieurs sont contactés et vont venir vont intéroger sur votre relation, comme vous devez le savoir chaques couple de garde doivent se connaitre intimement!\n"\
                "Des hauts gradés arrivent dans la pièce et comprennent vite qu'ils ont affaire aux prisonniers évadés! Vous finissez pendu\n"\
                "Fin"

choice2_success = "[bold white]Voix robotique:[/] Vous avez la même réponse, vous pouvez continuez, attention cependant votre niveau de complicité n'est que de"
choice2_success_bis = "Vous devez augmenter cette valeur sous peine de ne pas passer les prochains sas...\n"

bathroom = "Vous récupérez la carte et rentrez dans le passage qui se referme derrière vous, devant vous une petite pièce avec une baignoire et un lit, vous découvrez aussi un trousseau de clef de secours, ça pourrait être utile plus tard\n"\
                "Soudain une voix robotique vous fait sursauter\n"\
                "[bold white]Voix robotique:[/] Bienvenu dans votre pièce de repos, votre complicité est de"

bathroom_bis = "Vu votre odeur vous décidez de vous laver malgrès le manque d'intimité de la pièce, 3 options s'offrent à vous:\n"\
                "1. Vous doucher séparément, mais impossible de se cacher l'un de l'autre vu la configuration de la pièce... (+5)\n"\
                "2. Vous doucher ensemble rapidement (+10)\n"\
                "3. Vous décidez de vous relaxer et de prendre un bain minimum 15 min (+30)\n"\
                "[red]Si jamais vous n'avez pas de baignoire pour un bain l'option 3 devient:[/]\n"\
                "3. Vous doucher ensemble en prenant votre temps et vous faire au moins un gros calin dans la douche (+30)\n"

choice_bath = "Vous êtes maintenant propre et un peu plus relaxé, vous vous installez sur le lit pour vous reposer un peu quand la voix robotique vous interomp\n"\
                "[bold white]Voix robotique:[/] Il existe un passage secret d'ici vers la sortie uniquement ouvert aux gardes en chefs ayant le maximum de complicité, soit 200, dans cinq minutes je vous proposerai un moyens de monter à 200 points directement, en attendant je vous laisse vous reposer et discuter\n"

oral_sex= "[bold white]Voix robotique:[/] Celà fait cinq minutes, pour augmenter en une fois votre complicité d'autant de points il faudra qu'aleks se masturbe devant kitsune\n"

oral_sex_accept = "[bold white]Voix robotique:[/] Votre complicité et maintenant de 200, j'ouvre le passage secret\n"\
                "Devant vous un passage s'ouvre, vous l'empruntez pendant plusieurs minutes jusqu'à atteindre le fond, vous grimpez une échelle, vous sortez au millieu d'un champs, vous refermez la trappe qui se camouffle parfaitement. D'un côté à 500 mètres la prison, de l'autre à moins de 100m le village voisin, vous vous y précipitez et prennez le premier train loins d'ici!! Vous êtes libres\n\n"\
                "[red]Félicitation vous avez gagnez par la meilleure des manière, je ne vous en pensez sincèrement pas capable! Vous gagnez donc deux voeux de votre choix dont le cumul ne peux pas dépasser 10 000€. Screenez la fin du jeu avec vos deux souhaits et je m'en occuperai dès que possible![/]"

oral_sex_denial = "Vous refusez, incapable d'aller aussi loins, vous vous reposez puis resortez de votre havre de paix temporaire après vous être assuré que la voix était libre, maintenant propre et reposé vous ressemblez à deux vrai gardes!\n"\
                "Vous vous dirigez vers la sortie de la pièce vide vers la suivante, elle est fermé à clef, heureusement le trousseau trouvé plus tôt vous permet d'ouvrir. Vous découvrez une grande pièce remplis de tables, ça a tout l'air d'etre un grand réfectoire. Il y a quelques personnes assises à l'intérieur, en tendant un peu l'oreille vous apprenez que tout le monde pensent que vous vous êtes échappés par le passage secret, plus personne ne vous cherche dans la prison!\n"\
                "Vous traversez la pièce direction la sortie quand deux gardes sur un canape devant une TV vous interpellent:\n"\
                "[bold white]Garde femme:[/] Hé vous deux, on cherche des joueurs pour un mario kart ça vous dit?\n"\
                "Vous hésitez à les ignorer mais vous vous dites que ça risquerai d'éveiller les soupçons, et après tout plus c'est gros plus ça passe! Vous acceptez\n"\
                "[bold white]Garde homme:[/] On fait toujours un pari entre ma partenaire et moi pour savoir lequel sera le mieux classé, la le perdant devra se mettre à poil dans le réfectoire, autant vous dire qu'on va se taper dessus! Vous voulez parier quelques chose entre vous?\n"\
                "0. Pas de pari ça ne nous interesse pas (+0)\n"\
                "1. Le perdant raconte à l'autre le truc le plus fou qu'il ait jamais fait sexuellement (+10)\n"\
                "2. Le perdant doit masser le dos du gagnant pendant 10 minutes (+20)\n"\
                "3. Le perdant doit faire un strip tease sexy (avec musique) au gagnant (+30)\n"\
                
sas_2 = "Vous sortez de la pièce et tombez directement sur un sas, cependant cette fois ci vous n'êtes pas séparé, la voix robotique habituelle retentis:\n"\
        "[bold white]Voix robotique:[/] L'épreuve pour passer ce sas est à choix, les voici:\n"\
        "0. Ne rien faire et attendre les supérieurs\n"\
        "1. Si vous sortez de la en vie vous vous promettez de vous changer, de dormir et de vous laver ensemble autant de temps que possible (+20) [red]Petite précision: Valable sur le weekend entier, que vous finissiez le jeu ou non[/]\n"\
        "2. Vous vous embrassez pendant quelques secondes (+30) [red](Attention je demande pas un french kiss)[/]\n"\
        "3. Vous vous mettez entièrement nu et vous faites un calin pendant 1 minute (+40)\n"\

sas_2_fail = "Des hauts gradés arrivent dans la pièce et comprennent vite qu'ils ont affaire aux prisonniers évadés! Vous finissez pendu\n"\
                "Fin"

sas_2_succes = "Vous sortez du sas, devant vous un long et étrois couloir, vous le traversez sans encombre\n"\
                "Vous rentrez dans la pièce suivante et tombez sur deux gardes femmes, l'accès au sas de sortie est a porté de vu quand une des gardes vous interpelle\n"\
                "[bold white]Garde femme:[/] Je vous reconnais, vous êtes les prisonniers soit disant évadé...\n"\
                "Paniqué vous tentez de fuir vers le dernier sas mais vous vous faite rapidement maitriser par les deux gardes\n"\
                "[bold white]Garde femme:[/] Restez tranquille, on ne compte pas vous dénoncer, nous sommes d'humeur joueuses. Notre grand plaisir est de voir un homme humilié, on va vous proposer 3 humiliations possible pour ton partenaire, [bold blue]il n'a aucun droit de vote, c'est toi qui décide seule![/] suivant ce que tu décides tu pourrais repartir plus riche...\n"\
                "[red]Avant de voir les choix Aleks doit accepter et promettre de faire ce que kitsune décidera. Kitsune devra promettre de ne pas épargner Aleks et prendre la décision la plus avantageuse pour elle! Kitsune l'argent gagné ici sera uniquement pour toi et il sera gagné peut importe que vous finissiez le jeu ou pas[/]\n"

Humiliation_choice= "0. Ne rien faire\n"\
                        "1. Tu prends un verre d'eau, tu malaxes l'eau dans ta bouche puis la recrache dans le verre, tu fais ça 5 fois puis ton partenaire doit boire et avaler tout le verre et apres tu maches un gros morceau de gateau qu'il devra manger (+20)\n"\
                        "2. Ton partenaire se met nu et se branle devant toi sans jouir pendant 5 minutes, il doit bander tout du long sans aide de type film/image (+30)\n"\
                        "3. Tu fais subir une golden shower à ton partenaire et il devra lecher un peu de ta pisse (+60)\n"\
                        
Humiliation_choice_0 = "Les gardes vous dénoncent et vous finissez pendu\n"\
                        "Fin"

Humiliation_choice_success = "Vous passez le test des gardes avec succès et vous dirigez vers le dernier sas. Vous rentrez à l'intérieur et sans surprise la voix robotique habituelle vous parle:\n"\
                                "[bold white]Voix robotique:[/] Il vous faut 100 ou plus de complicité pour quitter le sas, l'épreuve pour passer ce sas est unique, la voici:\n"\
                                "0. Ne rien faire et attendre les supérieurs\n"\
                                "1. Mettez vous entièrement nu et regardez le film porno suivant enssemble (+40)\n"\
                                "[red]https://www.youporn.com/watch/102733121/[/]\n"\
                                "2. L'un de vous doit lécher les deux pieds de l'autre et lui sucer les orteils, 1 min par pied (+50)\n"\
                                "3. Aleks goute un peu de pisse de kitsune (+100)[/]\n"\




