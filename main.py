import tkinter as tk
from tkinter import ttk
from _tkinter import TclError
from ttkthemes import ThemedTk
from Linards_datu_struktura import generate_game_tree, print_nodes


class Player:

    def __init__(self, playern, score, rocks, statlabel=None) -> None:
        self.playern = playern
        self.name = None
        self.score = score
        self.rocks = rocks
        self.statlabel = statlabel


class GameState:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.players = [player1, player2]
        self.turn = None
        self.totalrocks = None
        self.status = None
        self.gamestatelabel = None
        self.text_pastmoves = None
        self.game_tree = None
        self.past_moves = []


def run_game_ui(game_state) -> None:

    def start_game() -> None:
        if has_errors() is True:
            return
        game_state.game_tree = generate_game_tree(game_state.totalrocks.get())
        # print_nodes(game_state.game_tree)  # Testēšanai
        game_state.players[0].name = value_p1choice.get()
        game_state.players[1].name = value_p2choice.get()
        for i in range(2):
            game_state.players[i].statlabel.set(f"{i + 1}. Spēlētāja\n"
                                                f"Punktu skaits: {game_state.players[i].score}\n"
                                                f"Akmentiņu skaits: {game_state.players[i].rocks}\n"
                                                f"Spēlētājs: {game_state.players[i].name}")
        game_state.turn.set(0)
        update_gamestatelabel()

        f1.grid_remove()
        f2.grid(sticky='nwe')

    def reset_game() -> None:  # TODO izveidot funkcionalitāti
        ...
        # f2.grid_remove()
        # f1.grid()
        #
        # # Reset variables
        #
        # game_state.totalrocks.set(60)
        #
        # game_state.status.set("Rezultāts: Progresā")

    def has_errors() -> bool:
        has_error = False

        if not value_p1choice.get():
            f1_label_p1error.config(text="Jāatzīmē spēlētājs")
            has_error = True
        else:
            f1_label_p1error.config(text="")

        if not value_p2choice.get():
            f1_label_p2error.config(text="Jāatzīmē spēlētājs")
            has_error = True
        else:
            f1_label_p2error.config(text="")

        try:
            n = game_state.totalrocks.get()
            if not 50 <= n <= 70:
                # # # Atkomentēt lai automātiski ieliktu robežās # # #
                # if n < 50:
                #     value_totalrocks.set(50)
                # elif n > 70:
                #     value_totalrocks.set(70)
                # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                f1_label_totalrockserror.config(text="Skaitlim jābūt norādītajā intervālā")
                has_error = True
            else:
                f1_label_totalrockserror.config(text="")
        except TclError:
            f1_label_totalrockserror.config(text="Jāievada skaitlis")
            has_error = True

        return has_error

    def update_value_totalrocks(value) -> None:
        rounded_value = int(float(value))
        game_state.totalrocks.set(rounded_value)

    def update_gamestatelabel() -> None:
        game_state.gamestatelabel.set(f"Pašreizējais akmentiņu skaits: {game_state.totalrocks.get()}\n"
                                      f"{(game_state.turn.get() % 2)+1}.spēlētāja gājiens!")

    def update_statlabel() -> None:
        current_player = game_state.players[1-(game_state.turn.get() % 2)]
        current_player.statlabel.set(f"{current_player.playern}. Spēlētāja\n"
                                     f"Punktu skaits: {current_player.score}\n"
                                     f"Akmentiņu skaits: {current_player.rocks}\n"
                                     f"Spēlētājs: {current_player.name}")

    def update_pastmovelabel() -> None:
        newtext = "Veikto gājienu saraksts:\n"
        for move in game_state.past_moves[-10:]:  # Parāda pēdējos 10 gājienus
            newtext += f"{move[0]}- {move[1] + 1}.spēlētājs, {move[2]} akmentiņi\n"
        game_state.text_pastmoves.set(newtext)

    def confirm_move(rocks_taken) -> None:
        if rocks_taken == 0 or game_state.totalrocks.get() - rocks_taken < 0:
            return
        game_state.totalrocks.set(game_state.totalrocks.get() - rocks_taken)
        turn = game_state.turn.get()
        game_state.players[turn % 2].rocks += rocks_taken

        # Pievienot gājienu vēsturei
        game_state.past_moves.append((turn+1,
                                      turn % 2,
                                      rocks_taken))
        # Nomainīt gājienu
        game_state.turn.set(turn + 1)

        # Atjaunot uzrakstus
        update_pastmovelabel()
        update_statlabel()
        update_gamestatelabel()

        # Atiestatīt pogas izvēli
        rocks_chosen.set(0)

    # --- Spēles loga izveide un uzstādīšana
    root = ThemedTk(theme="arc")  # Izkomentēt šo un atkomentēt apakšējo, lai strādātu bez papilbibliotēkām
    # root = tk.Tk()

    root.configure(bg='#f5f6f7')
    root.columnconfigure(0, weight=1, minsize=800)  # Centrēt galveno konteineri, paplašināt horizontāli līdz ar logu
    root.rowconfigure(0, weight=0, minsize=550)  # Centrēt, bet nemainīt vertikāli

    # --- Definēšana:
    # - Stili
    ...

    # - Konteineri (Frames)
    f1 = ttk.Frame(root,    # Sākuma lapas konteineris
                   padding=30,
                   width=800,
                   height=550)

    f2 = ttk.Frame(root,    # Galvenais spēles Konteineris (2.lapa)
                   padding=30,
                   width=800,
                   height=550)

    f2.columnconfigure(1, weight=1)  # Centrēt spēles konteineri, paplašināt horizontāli līdz ar logu

    # - Sākuma lapas elemeti
    f1_label_title = ttk.Label(f1, text="29-KOMANDAS PROJEKTS!")

    f1_label_p1choice = ttk.Label(f1, text="Izvēlies pirmo spēlētāju:", anchor="w", justify="left")
    value_p1choice = tk.StringVar(root)
    f1_radio_p1 = ttk.Frame(f1)
    f1_radio_p1_0 = ttk.Radiobutton(f1_radio_p1, text="Cilvēks", variable=value_p1choice, value="Cilvēks")
    f1_radio_p1_1 = ttk.Radiobutton(f1_radio_p1, text="Min-max algoritms", variable=value_p1choice, value="Min-max algoritms")
    f1_radio_p1_2 = ttk.Radiobutton(f1_radio_p1, text="Alfa-beta algoritms", variable=value_p1choice, value="Alfa-beta algoritms")
    f1_label_p1error = ttk.Label(f1, text=" ", style='red.TLabel')

    f1_label_p2choice = ttk.Label(f1, text="Izvēlies otro spēlētāju:")
    value_p2choice = tk.StringVar(root)
    f1_radio_p2 = ttk.Frame(f1)
    f1_radio_p2_0 = ttk.Radiobutton(f1_radio_p2, text="Cilvēks", variable=value_p2choice, value="Cilvēks",
                                    state="disabled")
    f1_radio_p2_1 = ttk.Radiobutton(f1_radio_p2, text="Min-max algoritms", variable=value_p2choice,
                                    value="Min-max algoritms")
    f1_radio_p2_2 = ttk.Radiobutton(f1_radio_p2, text="Alfa-beta algoritms", variable=value_p2choice,
                                    value="Alfa-beta algoritms")
    f1_label_p2error = ttk.Label(f1, text=" ", style='red.TLabel')

    f1_span_totalrocks = ttk.Frame(f1)
    f1_label_totalrocks = ttk.Label(f1_span_totalrocks, text="Ieraksti akmentiņu skaitu (no 50 līdz 70):")
    game_state.totalrocks = tk.IntVar(root, 60)
    f1_input_totalrocks = ttk.Spinbox(f1_span_totalrocks, from_=50, to=70, width=3, textvariable=game_state.totalrocks)
    f1_slider_totalrocks = ttk.Scale(f1_span_totalrocks, from_=50, to=70, length=150, variable=game_state.totalrocks,
                                     command=update_value_totalrocks)

    f1_label_totalrockserror = ttk.Label(f1, text=" ", style='red.TLabel')

    # TODO Nomainīt pogu uz ttk tipa ar pareizu stilu
    # f1_button_start = ttk.Button(f1, text="Spēlēt →", command=start_game)
    game_state.turn = tk.IntVar(value=0)
    f1_button_start = tk.Button(f1,
                                bg='#000000',
                                fg='#f8f8f8',
                                relief='flat',
                                text="Spēlēt →",
                                command=start_game)

    # - Galvenā spēles loga elementi

    # TODO Nomainīt pogu uz ttk tipa ar pareizu stilu
    # f2_button_newgame = ttk.Button(f2,text="← Jauna spēle",command=lambda: reset_game())
    f2_button_newgame = tk.Button(f2,
                                  bg='#000000',
                                  fg='#f8f8f8',
                                  relief='flat',
                                  text="← Jauna spēle",
                                  command=lambda: reset_game())
    f2_label_title = ttk.Label(f2, text="29-KOMANDAS PROJEKTS!")
    game_state.status = tk.StringVar(value="Rezultāts: Progresā")
    f2_label_status = ttk.Label(f2, textvariable=game_state.status)
    game_state.players[0].statlabel = tk.StringVar(value="Vēl nav inicializēts\n")
    f2_label_stats_p1 = ttk.Label(f2, textvariable=game_state.players[0].statlabel)
    game_state.players[1].statlabel = tk.StringVar(value="Vēl nav inicializēts\n")
    f2_label_stats_p2 = ttk.Label(f2, textvariable=game_state.players[1].statlabel)
    f2_midframe = ttk.Frame(f2)
    game_state.gamestatelabel = tk.StringVar(value="...")
    f2_midframe_label_totalrocks = ttk.Label(f2_midframe, textvariable=game_state.gamestatelabel, justify="center")

    # TODO Nomainīt pogas uz ttk tipa ar stilu
    rocks_chosen = tk.IntVar()
    f2_midframe_button_left = tk.Button(f2_midframe,
                                        bg='#000000',
                                        fg='#f8f8f8',
                                        relief='flat',
                                        text="2 akmentiņi",
                                        command=lambda: rocks_chosen.set(2))
    f2_midframe_button_right = tk.Button(f2_midframe,
                                         bg='#000000',
                                         fg='#f8f8f8',
                                         relief='flat',
                                         text="3 akmentiņi",
                                         command=lambda: rocks_chosen.set(3))
    f2_midframe_button_confirm = tk.Button(f2_midframe,
                                           bg='#000000',
                                           fg='#f8f8f8',
                                           relief='flat',
                                           text="Apstiprināt gājienu →",
                                           command=lambda: confirm_move(rocks_chosen.get()))

    game_state.text_pastmoves = tk.StringVar(value="Veikto gājienu saraksts:")
    f2_midframe_label_pastmoves = ttk.Label(f2_midframe, textvariable=game_state.text_pastmoves, justify='center')

    # -- Izvietošana (Layout):
    # - f1 elementi
    f1_label_title.grid(row=0, column=0, sticky='n')

    f1_label_p1choice.grid(row=1, column=0, sticky='w')
    f1_radio_p1.grid(row=2, column=0, columnspan=3, sticky='w')
    f1_radio_p1_0.pack(side="left")
    f1_radio_p1_1.pack(side="left")
    f1_radio_p1_2.pack(side="left")
    f1_label_p1error.grid(row=3, column=0, sticky='w')

    f1_label_p2choice.grid(row=4, column=0, sticky='w')
    f1_radio_p2.grid(row=5, column=0, columnspan=3, sticky='w')
    f1_radio_p2_0.pack(side="left")
    f1_radio_p2_1.pack(side="left")
    f1_radio_p2_2.pack(side="left")
    f1_label_p2error.grid(row=6, column=0, sticky='w')

    f1_span_totalrocks.grid(row=7, sticky='w')
    f1_label_totalrocks.pack(side="left")
    f1_input_totalrocks.pack(side="left")
    f1_slider_totalrocks.pack(side="left")
    f1_label_totalrockserror.grid(row=8, column=0, sticky='w')
    f1_button_start.grid(row=9, column=0)

    # - f2 elementi
    f2_button_newgame.grid(row=0, column=0, sticky='nw')
    f2_label_title.grid(row=0, column=1, sticky='n')
    f2_label_status.grid(row=0, column=2, sticky='ne')
    f2_label_stats_p1.grid(row=1, column=0, sticky='nw')
    f2_midframe.grid(row=1, column=1)
    f2_label_stats_p2.grid(row=1, column=2, sticky='ne')

    f2_midframe_label_totalrocks.grid(row=0, column=1)
    f2_midframe_button_left.grid(row=1, column=0)
    ttk.Label(f2_midframe, text="Vai").grid(row=1, column=1)
    f2_midframe_button_right.grid(row=1, column=2)
    f2_midframe_button_confirm.grid(row=2, column=1)
    f2_midframe_label_pastmoves.grid(row=3, column=1)

    # ## UI startup
    f1.grid(row=0, column=0, sticky='n')  # Loga pirmreizēja parādīšana
    root.geometry("800x550")  # Loga izmēri (Platums x Augstums)
    root.minsize(width=800, height=550)
    root.title("29.komandas projekts")
    root.mainloop()


def main():
    p1 = Player(playern=1, score=0, rocks=0)
    p2 = Player(playern=2, score=0, rocks=0)
    game_state = GameState(player1=p1, player2=p2)
    run_game_ui(game_state)


if __name__ == '__main__':
    main()
