import story
import gui
import time
from rich.console import Console
from rich.prompt import Prompt

console = Console()
complicity = 0


def text_anim(text, color):
    open =False
    original_color = color

    for char in text:
        if char == '[':
            open = True
            color = ""
            continue

        if char == ']':
            open = False
            continue

        if open == True:
            if char == '/':
                color = original_color
                continue
            color = color + char
        
        if open == False:
            console.print(char, end='', style=color)

text_anim(story.beginning, 'green')

choice = Prompt.ask("[bold yellow]Acceptez vous de jouer? [/bold yellow]", choices=["o", "n"])
        
if choice == "n":
    text_anim(story.denial_alcohol, "green")

elif choice == "o":
    text_anim(story.accept_alcohol, "green")
    i=0
    for truth in story.truth_list:
        text_anim(f"[bold white]Gardes:[/] {truth}\n", "green")

        aleks_choice = Prompt.ask("[bold yellow]Aleks as t'il bu? [/bold yellow]", choices=["o", "n"])

        kitsune_choice = Prompt.ask("[bold yellow]Kitsune as t'elle bu? [/bold yellow]", choices=["o", "n"])

        if aleks_choice == "o" and kitsune_choice == "o":
            story.both_drinks.append(i)
            i = i + 1
            continue
        
        if aleks_choice == "o":
            story.aleks_drinks.append(i)
        
        if kitsune_choice == "o":
            story.kitsune_drinks.append(i)
        
        i = i + 1
    
    text_anim(story.after_truth, "green")

    choice = Prompt.ask("[bold yellow]Acceptez vous de jouer?[/bold yellow]", choices=["o", "n"])

    if choice == "n":
        text_anim(story.denial_shots, "green")

    elif choice == "o":
        guards_shots = 0
        prisonners_shots = 0
        text_anim(story.accept_shots, "green")
        for i in range(len(story.truth_list)):
            if i in story.both_drinks:
                text_anim(story.truth_list[i]+"\n", "green")
                aleks_choice = Prompt.ask("[bold yellow]Aleks a t'il donné des détails?[/bold yellow]", choices=["o", "n"])

                if aleks_choice == "o":
                    text_anim("Les gardes boivent!\n", "green")
                    guards_shots += 1
                    if guards_shots == 4:
                        text_anim("Les gardes commencent à tanguer\n", "green")

                    elif guards_shots == 6:
                        text_anim("Les gardes ont du mal à tenir debout\n", "green")
            
                    elif guards_shots == 8:
                        text_anim("Les gardes ont du s'assoir\n", "green")

                else:
                    text_anim("Vous buvez!\n", "green")
                    prisonners_shots += 1

                kitsune_choice = Prompt.ask("[bold yellow]Kitsune a t'elle donné des détails?[/bold yellow]", choices=["o", "n"])

                if kitsune_choice == "o":
                    text_anim("Les gardes boivent!\n", "green")
                    guards_shots += 1
                    if guards_shots == 4:
                        text_anim("Les gardes commencent à tanguer\n", "green")

                    elif guards_shots == 6:
                        text_anim("Les gardes ont du mal à tenir debout\n", "green")
            
                    elif guards_shots == 8:
                        text_anim("Les gardes ont du s'assoir\n", "green")
                else:
                    text_anim("Vous buvez!\n", "green")
                    prisonners_shots += 1 

            elif i in story.aleks_drinks:
                text_anim(story.truth_list[i] + "\n", "green")
                aleks_choice = Prompt.ask("[bold yellow]Aleks a t'il donné des détails? [/bold yellow]", choices=["o", "n"])

                if aleks_choice == "o":
                    text_anim("Les gardes boivent!\n", "green")
                    guards_shots += 1
                    if guards_shots == 4:
                        text_anim("Les gardes commencent à tanguer\n", "green")

                    elif guards_shots == 6:
                        text_anim("Les gardes ont du mal à tenir debout\n", "green")
            
                    elif guards_shots == 8:
                        text_anim("Les gardes ont du s'assoir\n", "green")
                else:
                    text_anim("Vous buvez!\n", "green")
                    prisonners_shots += 1

            elif i in story.kitsune_drinks:
                text_anim(story.truth_list[i] + "\n", "green")
                kitsune_choice = Prompt.ask("[bold yellow]Kitsune a t'elle donné des détails? [/bold yellow]", choices=["o", "n"])

                if kitsune_choice == "o":
                    text_anim("Les gardes boivent!\n", "green")
                    guards_shots += 1
                    if guards_shots == 4:
                        text_anim("Les gardes commencent à tanguer\n", "green")

                    elif guards_shots == 6:
                        text_anim("Les gardes ont du mal à tenir debout\n", "green")
            
                    elif guards_shots == 8:
                        text_anim("Les gardes ont du s'assoir\n", "green")
                else:
                    text_anim("Vous buvez!\n", "green")
                    prisonners_shots += 1
        
        if guards_shots < 8:
            text_anim(story.not_drunk, "green")
        
        elif guards_shots >= 8:
            text_anim(story.drunk, "green")
            map = gui.App(gui.Map)
            time.sleep(0.01)
            map.root.create_image("images/Map.png")
            map.root.create_players()
            aleks = map.root.aleks
            kitsune = map.root.kitsune
            text_anim(story.room1, "green")
            while aleks.x < 560:
                aleks.move_right()
                kitsune.move_right()
                time.sleep(0.016)

            text_anim(story.choice1, "green")

            choice1 = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["1", "2", "3"])
            
            if choice1 == "1":
                text_anim(story.choice1_1, "green")
                avance = 10
            
            elif choice1 == "2":
                text_anim(story.choice1_2, "green")
                avance = 60
                complicity += 5
                text_anim(f"Votre complicité a augmenté de 5 points, elle est maintenant de {complicity}\n", "green")
            elif choice1 == "3":
                text_anim(story.choice1_3, "green")
                avance = 180
                complicity += 10
                text_anim("Votre complicité a augmenté de 10 points, elle est maintenant de {complicity}\n", "green")
            

            text_anim(story.choice2_aleks, "green")

            while kitsune.x < 660:
                kitsune.move_right()
                aleks.move_right()
                time.sleep(0.016)

            while kitsune.y > 505:
                kitsune.move_up()
                if aleks.x == kitsune.x:
                    aleks.move_up()
                elif aleks.x < kitsune.x:
                    aleks.move_right()
                time.sleep(0.016)

            while kitsune.x > 580:
                kitsune.move_left()
                if aleks.y == kitsune.y:
                    aleks.move_left()
                elif aleks.y > kitsune.y:
                    aleks.move_up()
                time.sleep(0.016)

            while kitsune.y > 420:
                kitsune.move_up()
                if aleks.x == kitsune.x:
                    aleks.move_up()
                elif aleks.x > kitsune.x:
                    aleks.move_left()
                time.sleep(0.016)

            sex_size_aleks = Prompt.ask("[bold yellow]Aleks, écrit ta réponse en chiffre uniquement[/bold yellow]", password=True)
            text_anim(story.choice2_kitsune, "green")
            sex_size_kitsune = Prompt.ask("[bold yellow]Kitsune, écrit ta réponse en chiffre uniquement[/bold yellow]", password=True)
            if sex_size_aleks != sex_size_kitsune:
                text_anim(story.choice2_fail, "green")
            elif sex_size_kitsune == sex_size_aleks:
                text_anim(f"{story.choice2_success} {complicity}. {story.choice2_success_bis}", "green")
                text_anim(f"Attention à la prochaine étape un chronomètre va s'ouvrir et il faudra vous même vous diriger à l'aide des touches directionnelles\n", "bold red")
                input("Appuyer sur entrée pour continuer...")
                timer = gui.App(gui.Timer, avance)
                map.root.activateMove = True
                while map.root.activateMove == True:
                    pass

                text_anim(map.root.secret, "green")

                while kitsune.y < 550:
                    kitsune.move_down()
                    if aleks.x == kitsune.x:
                        aleks.move_down()
                    elif aleks.x < kitsune.x:
                        aleks.move_right()
                    elif aleks.x > kitsune.x:
                        aleks.move_left()
                    time.sleep(0.016)

                while kitsune.x < 500:
                    kitsune.move_right()
                    if aleks.y == kitsune.y:
                        aleks.move_right()
                    elif aleks.y < kitsune.y:
                        aleks.move_down()
                    time.sleep(0.016)

                text_anim(f"{story.bathroom} {complicity}", "green")
                text_anim(story.bathroom_bis, "green")

                choice1 = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["1", "2", "3"])
                
                if choice1 == "1":
                    complicity += 5
                    text_anim(f"Votre complicité a augmenté de 5 points, elle est maintenant de {complicity}\n", "green")
                elif choice1 == "2":
    
                    complicity += 10
                    text_anim(f"Votre complicité a augmenté de 10 points, elle est maintenant de {complicity}\n", "green")
                elif choice1 == "3":
                    complicity += 30
                    text_anim(f"Votre complicité a augmenté de 30 points, elle est maintenant de {complicity}\n", "green")
                
                text_anim(story.choice_bath, "green")
                timer = gui.App(gui.Timer, 300)
                time.sleep(0.1)

                while timer.root.alive == True:
                    pass

                text_anim(story.oral_sex, "green")
                choice = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["o", "n"])
                if choice == "o":
                    text_anim(story.oral_sex_accept, "green")
                
                elif choice == "n":
                    text_anim(story.oral_sex_denial, "green")
                    while aleks.x > 400:
                        aleks.move_left()
                        kitsune.move_left()
                        time.sleep(0.016)

                    while aleks.y > 400:
                        aleks.move_up()
                        if kitsune.x == aleks.x:
                            kitsune.move_up()
                        elif kitsune.x > aleks.x:
                            kitsune.move_left()
                        time.sleep(0.016)

                    while aleks.x < 450:
                        aleks.move_right()
                        if kitsune.y == aleks.y:
                            kitsune.move_right()
                        elif kitsune.y > aleks.y:
                            kitsune.move_up()
                        time.sleep(0.016)

                    while aleks.y > 230:
                        aleks.move_up()
                        if kitsune.x == aleks.x:
                            kitsune.move_up()
                        elif kitsune.x < aleks.x:
                            kitsune.move_right()
                        time.sleep(0.016)
                
                    choice = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["0", "1", "2", "3"])

                    if choice == "0":
                        text_anim(f"Votre complicité a augmenté de 0 points, elle est maintenant de {complicity}\n", "green")

                    elif choice == "1":
                        complicity += 10
                        text_anim(f"Votre complicité a augmenté de 10 points, elle est maintenant de {complicity}\n", "green")

                    elif choice == "2":
                        complicity += 20
                        text_anim(f"Votre complicité a augmenté de 20 points, elle est maintenant de {complicity}\n", "green")

                    elif choice == "3":
                        complicity += 30
                        text_anim(f"Votre complicité a augmenté de 30 points, elle est maintenant de {complicity}\n", "green")
                    
                    text_anim(story.sas_2, "green")

                    while aleks.x < 630:
                        aleks.move_right()
                        if kitsune.y == aleks.y:
                            kitsune.move_right()
                        elif kitsune.y > aleks.y:
                            kitsune.move_up()
                        time.sleep(0.016)

                    while aleks.y > 85:
                        aleks.move_up()
                        if kitsune.x == aleks.x:
                            kitsune.move_up()
                        elif kitsune.x < aleks.x:
                            kitsune.move_right()
                        time.sleep(0.016)

                    choice = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["0", "1", "2", "3"])

                    if choice == "0":
                        text_anim(story.sas_2_fail, "green")
                        quit()

                    elif choice == "1":
                        complicity += 20
                        text_anim(f"Votre complicité a augmenté de 20 points, elle est maintenant de {complicity}\n", "green")

                    elif choice == "2":
                        complicity += 30
                        text_anim(f"Votre complicité a augmenté de 30 points, elle est maintenant de {complicity}\n", "green")

                    elif choice == "3":
                        complicity += 40
                        text_anim(f"Votre complicité a augmenté de 40 points, elle est maintenant de {complicity}\n", "green")
                    
                    text_anim(story.sas_2_succes, "green")

                    while aleks.x > 490:
                        aleks.move_left()
                        if kitsune.y == aleks.y:
                            kitsune.move_left()
                        elif kitsune.y > aleks.y:
                            kitsune.move_up()
                        time.sleep(0.016)

                    while aleks.y > 55:
                        aleks.move_up()
                        if kitsune.x == aleks.x:
                            kitsune.move_up()
                        elif kitsune.x > aleks.x:
                            kitsune.move_left()
                        time.sleep(0.016)

                    while aleks.x > 215:
                        aleks.move_left()
                        if kitsune.y == aleks.y:
                            kitsune.move_left()
                        elif kitsune.y > aleks.y:
                            kitsune.move_up()
                        time.sleep(0.016)

                    while aleks.y < 270:
                        aleks.move_down()
                        if kitsune.x == aleks.x:
                            kitsune.move_down()
                        elif kitsune.x > aleks.x:
                            kitsune.move_left()
                        time.sleep(0.016)

                    choice = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["o", "n"])
                    if choice == "n":
                        text_anim(story.Humiliation_choice_0, "green")
                    
                    elif choice == "o":
                        text_anim(story.Humiliation_choice, "green")

                        choice = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["0", "1", "2", "3"])

                        if choice == "0":
                            text_anim(story.Humiliation_choice_0, "green")
                            quit()
                        
                        elif choice == "1":
                            text_anim("Kitsune prend 0€", "red")

                        elif choice == "2":
                            text_anim("Kitsune prend 1500€, screen pour que je te fasse un virement", "red")

                        elif choice == "3":
                            text_anim("Kitsune prend 3000€, screen pour que je te fasse un virement", "red")
                        
                        text_anim(story.Humiliation_choice_success, "green")

                        while aleks.x > 110:
                            aleks.move_left()
                            if kitsune.y == aleks.y:
                                kitsune.move_left()
                            elif kitsune.y < aleks.y:
                                kitsune.move_down()
                            time.sleep(0.016)

                        while aleks.y < 410:
                            aleks.move_down()
                            if kitsune.x == aleks.x:
                                kitsune.move_down()
                            elif kitsune.x > aleks.x:
                                kitsune.move_left()
                            time.sleep(0.016)

                        while aleks.x > 55:
                            aleks.move_left()
                            if kitsune.y == aleks.y:
                                kitsune.move_left()
                            elif kitsune.y < aleks.y:
                                kitsune.move_down()
                            time.sleep(0.016)

                        while aleks.y > 300:
                            aleks.move_up()
                            if kitsune.x == aleks.x:
                                kitsune.move_up()
                            elif kitsune.x > aleks.x:
                                kitsune.move_left()
                            time.sleep(0.016)

                        choice = Prompt.ask("[bold yellow]Que choisissez vous?[/bold yellow]", choices=["0", "1", "2", "3"])

                        if choice == "0":
                            text_anim(story.sas_2_fail, "green")
                            quit()

                        elif choice == "1":
                            complicity += 30
                            text_anim(f"Votre complicité a augmenté de 30 points, elle est maintenant de {complicity}\n", "green")
                            
                        elif choice == "2":
                            complicity += 40
                            text_anim(f"Votre complicité a augmenté de 40 points, elle est maintenant de {complicity}\n", "green")

                        elif choice == "3":
                            complicity += 100
                            text_anim(f"Votre complicité a augmenté de 100 points, elle est maintenant de {complicity}\n", "green")
                        
                        if complicity >= 100:
                            argent = complicity * 50
                            text_anim("Vous êtes libre!! Personne ne c'est rendu compte de votre évasion, vous foncez à la gare la plus proche pour vous éloignez un maximum de cet enfer!! Vous ne savez toujours pas ce qu'il c'est passé finalement...", "green")
                            text_anim(f"Félicitation, je n'étais vraiment pas sure que vous réussiriez le jeu! Vous gagnez donc deux voeux de votre choix dont le cumul ne peux pas dépasser {argent}€. Screenez la fin du jeu avec vos deux souhaits et je m'en occuperai dès que possible!", "red")
                        
                        elif complicity < 100:
                            text_anim("Malgrès vos efforts votre complicité est trop basse, le sas reste fermé, les supérieurs arrivent et vous reconnaissent, vous finissez pendu\nFin.", "green")
