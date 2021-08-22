print(""""
  __                ___               ___
              ,' ,'              |   |              `. `.
            ,' ,'                |===|                `. `.
           / //                  |___|                  \\ \
          / //                   |___|                   \\ \
         ////                    |___|                    \\\\
        /  /                    ||   ||                    \  \
       /  /                     ||   ||                     \  \
      /| |                      ||   ||                      | |\
      || |                     | : o : |                     | ||
     |  \|                     | .===. |                     |/  |
     |  |\                    /| (___) |\                    /|  |
    |__||.\         .-.      // /,_._,\ \\      .-.         /.||__|
    |__||_.\        `-.\    //_ [:(|):] _\\    /.-'        /._||__|
 __/|  ||___`._____ ___\\__/___/_ ||| _\___\__//___ _____.'___||_ |\__
/___//__________/.-/_____________|.-.|_____________\-.\__________\\___\
\___\\__\\\_____\`-\__\\\\__\____|_-_|____/_//_____/-'/__//______//__//
   \|__||__..'         //  \ _ \__|||__/ _ /  \\         `..__||__|/
    |__||_./        .-'/    \\   |(|)|   //    \`-.        \..||__|
    |  || /         `-'      \\   \'/   //      `-'         \ ||  |
     |  |/                    \| :(-): |/                    \|  |
     |  /|                     | : o : |                     |\  |
      || |                     | |___| |                     | ||
      \| |                      ||   ||                      | |/
       \  \                     ||   ||                     /  /
        \  \                    ||___||                    /  /
         \\\\                    |___|                    ////
          \ \\                   |___|                   // /
           \ \\                  |   |                  // /
            `. `.                |===|                ,' ,'
              `._`.              |___|              ,'_,'

""")
print("Bienvenido a la nave Octopus. ")
print("Tu mision es aterrizar en el planeta Nerubis y encontrar el tesoro perdido:") 

camino = input("Tienes que escoger 2 caminos Derecha vas al bosque  o izquierda vas a un volcan").lower()

if camino == "izquierda":
        print("Estas a salvo en el volvan, puedes continuar")
        #escalar o atravesar el volvan
        segundo_camino = input('Prefieres "atravesar" el volcan o "rodearlo" ? ').lower()
        if segundo_camino == "atravesar":
                print("Mueres porque te quemaste vivo")
        elif segundo_camino == "rodearlo":
                print("Llegaste a salvo a la cueva donde esta el tesoro")
                tercer_camino = input('Tienes 3 caminos que llevan al tesoro escoge "serpientes", "arañas", "oso" ?:').lower()
                if tercer_camino == "serpientes":
                        print("Felicidades Encontraste el tesoro. Eres millonario")
                elif tercer_camino == "arañas":
                        print("Te mordio una tarantula, pierdes el juego")
                else :
                        print("Perdiste el juego el oso te mato")

else:
        print("Mueres porque los elfos te capturan y te sacrifican.")
