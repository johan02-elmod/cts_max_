debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION = CURRENT_VERSION.replace("\n", "")


import os, sys, random, requests


def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None


def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(filename, "wb") as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")


try:
    from colorama import init, Fore, Back, Style

    init()

    def color(text, fore=None, back=None):
        color_map = {
            (255, 0, 0): Fore.RED,
            (0, 255, 0): Fore.GREEN,
            (0, 0, 255): Fore.BLUE,
            (255, 255, 0): Fore.YELLOW,
            (0, 255, 255): Fore.CYAN,
            (255, 0, 255): Fore.MAGENTA,
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

    local_ip = requests.get("https://api.ipify.org").text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")

    from colorama import init, Fore, Back, Style

    init()

    def color(text, fore=None, back=None):
        color_map = {
            (255, 0, 0): Fore.RED,
            (0, 255, 0): Fore.GREEN,
            (0, 0, 255): Fore.BLUE,
            (255, 255, 0): Fore.YELLOW,
            (0, 255, 255): Fore.CYAN,
            (255, 0, 255): Fore.MAGENTA,
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

# text = """


banner = r"""




  ██████╗████████╗███████╗        ███╗   ███╗ █████╗ ██╗  ██╗        
██╔════╝╚══██╔══╝██╔════╝        ████╗ ████║██╔══██╗╚██╗██╔╝        
██║        ██║   ███████╗        ██╔████╔██║███████║ ╚███╔╝         
██║        ██║   ╚════██║        ██║╚██╔╝██║██╔══██║ ██╔██╗         
╚██████╗   ██║   ███████║███████╗██║ ╚═╝ ██║██║  ██║██╔╝ ██╗███████╗
 ╚═════╝   ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                    
                                                                                  
                           
 
                   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
                   █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
                       
                   𝙲𝙰𝚁 𝙿𝙰𝚁𝙺𝙸𝙽𝙶 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙰𝚈𝙴𝚁
                         𝙿𝚁𝙴𝙲𝙸𝙾𝙽𝙴 𝙴𝙽𝚃𝙴𝚁                                 
"""[
    1:
]



pyAnime.Fade(
    pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True
)


# pyAnime.Fade(pyCenter.Center(text), pyColors.purple_to_red, pyColorate.Vertical, enter=True)
# print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))

pySystem.Clear()

# print("\n"*2    )
# print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
# print("\n"*2)



from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from pystyle import Center
import datetime


from cpmcheats import CPMCheats

__CHANNEL_USERNAME__ = "nuevo_en_script"
__GROUP_USERNAME__ = "max_cpm_shadow"
__BOT_RICK_NAME__ = "@Shadow_cid_bot"
_CHEATS_NAME = "CPMMAX"


def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)


def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != " ":
                color_index = int(
                    (
                        (x / (width - 1 if width > 1 else 1))
                        + (y / (height - 1 if height > 1 else 1))
                    )
                    * 0.5
                    * (len(colors) - 1)
                )
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text


def modificar_todos_los_autos(cpm, hp, hp_interno, nm, torque):
    try:
        response = cpm.modificar_todos_los_autos(hp, hp_interno, nm, torque)
        if response:
            print(
                Colorate.Horizontal(
                    Colors.rainbow, "Todos los autos han sido modificados exitosamente."
                )
            )
        else:
            print(Colorate.Horizontal(Colors.rainbow, "Error al modificar los autos."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.rainbow, f"Error: {e}"))


def banner(console):
    os.system("cls" if os.name == "nt" else "clear")

    brand_name = """
  ██████╗████████╗███████╗        ███╗   ███╗ █████╗ ██╗  ██╗        
██╔════╝╚══██╔══╝██╔════╝        ████╗ ████║██╔══██╗╚██╗██╔╝        
██║        ██║   ███████╗        ██╔████╔██║███████║ ╚███╔╝         
██║        ██║   ╚════██║        ██║╚██╔╝██║██╔══██║ ██╔██╗         
╚██████╗   ██║   ███████║███████╗██║ ╚═╝ ██║██║  ██║██╔╝ ██╗███████╗
 ╚═════╝   ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                    
                                                                            
    """

    colors = [
        "rgb(255,0,0)",  # Vermelho
        "rgb(255,51,0)",  # Vermelho-alaranjado
        "rgb(255,102,0)",  # Laranja
        "rgb(255,153,0)",  # Amarelo-alaranjado
        "rgb(255,204,0)",  # Amarelo
        "rgb(255,255,0)",  # Amarelo claro
    ]

    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter(
                "─════════════════════════════[ 𝖨𝖬𝖯𝖮𝖱𝖳𝖠𝖭𝖳𝖤  ]════════════════════════════─"
            ),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter("𝖢𝖨𝖤𝖱𝖱𝖤 𝖲𝖤𝖲𝖨𝖮𝖭 𝖤𝖭 𝖢𝖯𝖬 𝖠𝖭𝖳𝖤𝖲 𝖣𝖤 𝖴𝖲𝖠𝖱 𝖬𝖨 𝖧𝖤𝖱𝖱𝖠𝖬𝖨𝖤𝖭𝖳𝖠"),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter("𝗡𝗢 𝗦𝗘 𝗣𝗨𝗘𝗗𝗘 𝗖𝗢𝗠𝗣𝗔𝗥𝗧𝗜𝗥 𝗟𝗔 𝗖𝗟𝗔𝗩𝗘 𝗗𝗘 𝗔𝗖𝗖𝗘𝗦𝗢 𝗬 𝗦𝗜 𝗟𝗢 𝗛𝗔𝗖𝗘𝗦 𝗦𝗘𝗥𝗔𝗦 𝗕𝗟𝗢𝗤𝗨𝗘𝗔𝗗𝗢"),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter(
                f" 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}"
            ),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter(
                "─════════════════════════════[ DETALLES DE LA CUENTA ]════════════════════════════─"
            ),
        )
    )


def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get("ok"):
        data = response.get("data")
        if (
            isinstance(data, dict)
            and "floats" in data
            and "localID" in data
            and "money" in data
            and "coin" in data
        ):
            name = data.get("Name", "UNDEFINED")
            local_id = data.get("localID")
            money = data.get("money")
            coin = data.get("coin")
            print(
                Colorate.Horizontal(
                    Colors.green_to_blue,
                    Center.XCenter(
                        f"Nombre: {name} <> ID: {local_id} <> Dinero: {money} <> Monedas: {coin}"
                    ),
                )
            )
        else:
            print(
                Colorate.Horizontal(
                    Colors.green_to_blue,
                    "⚠️Alerta: Las cuentas nuevas deben iniciar sesión en el juego al menos una vez. !",
                )
            )
    else:
        print(
            Colorate.Horizontal(
                Colors.green_to_blue, " ⚠️ALERTA: El inicio de sesión parece no estar configurado correctamente !"
            )
        )


def load_key_data(cpm):

    data = cpm.get_key_data()

    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter(
                "─══════════════════════[ 𝗗𝗘𝗧𝗔𝗟𝗟𝗘𝗦 𝗗𝗘 𝗟𝗔 𝗖𝗟𝗔𝗩𝗘 𝗗𝗘 𝗔𝗖𝗖𝗘𝗦𝗢 ]══════════════════════─"
            ),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter(
                f'Clave de acceso: {data.get("access_key")} <> Telegram ID: {data.get("telegram_id")} <> Balance: {(data.get("coins") if not data.get("is_unlimited") else "Ilimitado")}'
            ),
        )
    )


def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(
                Colorate.Horizontal(
                    Colors.green_to_blue,
                    f"{tag} NO PUEDE ESTAR VACÍO O SOLO ESPACIOS, POR FAVOR INTÉNTALO DE NUEVO",
                )
            )
        else:
            return value


def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter("─═════════════════════[ LOCALIZACIÓN ]═════════════════════─"),
        )
    )
    print(
        Colorate.Horizontal(
            Colors.green_to_blue,
            Center.XCenter(
                f'Pais: {data.get("country")} <> Region: {data.get("regionName")} <> City: {data.get("Cuidad")}'
            ),
        )
    )


def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i : i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i : i + 2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(
        int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb)
    )
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)


def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f"[{interpolated_color}]{char}"
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[?] CORREO ELECTRÓNICO DE LA CUENTA", "Email", password=False)
        acc_password = prompt_valid_value(
            "[?] CONTRASEÑA DE LA CUENTA", "Password", password=False
        )
        acc_access_key = prompt_valid_value(
            "[?] CLAVE DE ACCESO", "Access Key", password=False
        )
        console.print("[%] INTENTANDO INICIAR SESIÓN: ", end=None)
        cpm = CPMCheats(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.green_to_blue, "CORREO ELECTRÓNICO  INCORRECTO"))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.green_to_blue, "CONTRASEÑA INCORRECTA"))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.green_to_blue, "CLAVE DE ACCESO NO VÁLIDA"))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.green_to_blue, "INTENTAR OTRA VEZ"))
                print(
                    Colorate.Horizontal(
                        Colors.green_to_blue,
                        "⚠️ NOTA: ASEGÚRATE DE COMPLETAR LOS CAMPOS",
                    )
                )
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.green_to_blue, "EXITOSO"))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "38",
                "39",
                "40",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "47",
                "48",
                "49",
                "50",
                "51",
                "52",
            ]
            print(
                Colorate.Horizontal(
                    Colors.green_to_blue,
                    Center.XCenter(
                        Box.DoubleCube(
                            "➩ (01) Aumentar el dinero                         1.5K |  ➩ (02) Aumentar monedas                     1.5K\n\n"
                            "➩ (03) Rango de rey                               8K   |  ➩ (04) Cambiar ID                           4.5K\n\n"
                            "➩ (05) Cambiar nombre                             100  |  ➩ (06) Cambiar nombre (Arcoíris)            100\n\n"
                            "➩ (07) Diseños de Placas aleatorias               2K   |  ➩ (08) Eliminar cuenta                      Gratis\n\n"
                            "➩ (09) Crear nueva cuenta                         Free |  ➩ (10) Eliminar amigos                      500\n\n"
                            "➩ (11) Desbloquear Lamborghinis (solo iOS)        5K   |  ➩ (12) Desbloquear todos los carros         6K\n\n"
                            "➩ (13) Desbloquear la sirena en todos los carros  3.5K |  ➩ (14) Desbloquear el motor W16             4K\n\n"
                            "➩ (15) Desbloquea todos los claxon                3K   |  ➩ (16) Desbloquear motor indestructible     3K\n\n"
                            "➩ (17) Desbloquear gasolina infinita              3K   |  ➩ (18) Desbloquear la casa de paga          4K\n\n"
                            "➩ (19) Desbloquear humo                           4K   |  ➩ (20) Desbloquear rines                    4K\n\n"
                            "➩ (21) Desbloquear animaciones                    2K   |  ➩ (22) Desbloquear ropa M                   3K\n\n"
                            "➩ (23) Desbloquear ropa F                         3K   |  ➩ (24) Cambiar carreras ganadas             1K\n\n"
                            "➩ (25) Cambiar carreras perdidas                  1K   |  ➩ (26) Clonar cuenta                        7K\n\n"
                            "➩ (27) HP personalizado                           2.5K |  ➩ (28) Ángulo personalizado                 1.5K\n\n"
                            "➩ (29) Quemador neumáticos personalizado          1.5K |  ➩ (30) Kilometraje de coches personalizados 1.5K\n\n"
                            "➩ (31) Freno del carro personalizado              2K   |  ➩ (32) Quitar el parachoques trasero        2K\n\n"
                            "➩ (33) Quitar el parachoques delantero            2K   |  ➩ (34) Cambiar la contraseña de la cuenta   2K\n\n"
                            "➩ (35) Cambiar el correo electrónico de la cuenta 2K   |  ➩ (36) Alerón personalizado                 10K\n\n"
                            "➩ (37) Body kits personalizado                    10K  |  ➩ (38) Desbloquear rines de paga            4.5K\n\n"
                            "➩ (39) Desbloquear auto del clan                  2K   |  ➩ (40) Desbloquear sombrero de clan (M)     3K\n\n"
                            "➩ (41) Quitarle la cabeza al personaje (M)        3K   |  ➩ (42) Quitarle la cabeza al personaje (F)  3K\n\n"
                            "➩ (43) Desbloquear la ropa top 1 del clan (M)     3K   |  ➩ (44) Desbloquear la ropa top 2 de clan M  3K\n\n"
                            "➩ (45) Desbloquear la ropa top 3 del clan (M)     3K   |  ➩ (46) Desbloquear la ropa top 1 clan (FM)  3K\n\n"
                            "➩ (47) Desbloquear la ropa top 2 del clan (FM)    3K   |  ➩ (48) Desbloquear Mercedes Cls             4K\n\n"
                            "➩ (49) Poner HP a todos los autos                 7.5K |  ➩ (50) Desbloquear los autos de paga        5K\n\n"
                            "➩ (51) Comba de postura                           1k   |  ➩ (52) Copiar el diseño de un auto a otro   2.5k\n\n"
                        )
                    ),
                )
            )

            print(
                Colorate.Horizontal(
                    Colors.green_to_blue, Center.XCenter(Box.DoubleCube(" ➩{0}: Exit"))
                )
            )

            print(
                Colorate.Horizontal(
                    Colors.green_to_blue,
                    "                               ─═══════════════[ ☆ CPMMAX ☆ ]═══════════════─",
                )
            )

            service = IntPrompt.ask(
                f"[bold]                                     [?] SELECCIONE UN SERVICIO[red][1-{choices[-1]} or 0][/red][/bold]",
                choices=choices,
                show_choices=False,
            )

            if service == 0:  # Exit
                console.print("[bold white] Gracias por usar mi herramienta[/negrita blanca]")
            elif service == 1:  # Increase Money
                console.print(
                    "[bold yellow][bold white][?][/bold white] Inserta cuanto dinero deseas[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Cantidad")
                console.print("[%] Guardando sus datos: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]EXITOSO (✔)[/bold green]")
                        console.print(
                            "[bold green]======================================[/bold green]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir? ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO (✘)[/bold red]")
                        console.print(
                            "[bold red]¡Por favor inténtelo de nuevo más tarde! (✘)[/bold red]"
                        )
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO (✘)[/bold red]")
                    console.print("[bold red]¡Por favor utilice valores válidos! (✘)[/bold red]")
                    sleep(2)
                    continue
            elif service == 2:  # Increase Coins
                console.print(
                    "[bold yellow][bold white][?][/bold white] Introduce cuantas monedas quieres[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Cantidad")
                print("[ % ] Guardando sus datos: ", end="")
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]EXITOSO (✔)[/bold green]")
                        console.print(
                            "[bold green]======================================[/bold green]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO[/bold red]")
                        console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] 'Por favor, utilice valores válidos[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 3:  # King Rank
                console.print(
                    "[bold red][!] NOTA:[/bold red]: Si el rango de rey no aparece en el juego, ciérrelo y ábralo varias veces..",
                    end=None,
                )
                console.print(
                    "[bold red][!] NOTA:[/bold red]: Por favor, no hagas King Rank en la misma cuenta dos veces.",
                    end=None,
                )
                sleep(2)
                console.print("[%] Dándote un rango de rey: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                    console.print(
                        "[bold yellow] '======================================[/bold yellow]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir? ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 4:  # Change ID
                console.print("[bold yellow] '[?] Ingrese su nueva iD [/bold yellow]")
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Guardando sus datos: ", end=None)
                if (
                    len(new_id) >= 8
                    and len(new_id)
                    <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                    and (" " in new_id) == False
                ):
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                        console.print(
                            "[bold yellow] '======================================[/bold yellow]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO[/bold red]")
                        console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold yellow] 'Por favor, utilice un ID válida[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5:  # Change Name
                console.print("[bold yellow] '[?] Ingrese su nuevo nombre[/bold yellow]")
                new_name = Prompt.ask("[?] Nombre")
                console.print("[%] Guardando sus datos: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                        console.print(
                            "[bold yellow] '======================================[/bold yellow]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO[/bold red]")
                        console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] 'Por favor, utilice valores válidos[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 6:  # Change Name Rainbow
                console.print(
                    "[bold yellow] '[?] Ingresa tu nuevo nombre arcoíris[/bold yellow]"
                )
                new_name = Prompt.ask("[?] nombre")
                console.print("[%] Guardando sus datos: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                        console.print(
                            "[bold yellow] '======================================[/bold yellow]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO[/bold red]")
                        console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] 'Por favor, utilice valores válidos[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 7:  # Number Plates
                console.print("[%] Dándole una Placa: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 8:  # Account Delete
                console.print(
                    "[bold yellow] '[!] Después de eliminar tu cuenta no hay vuelta atrás !![/bold yellow]"
                )
                answ = Prompt.ask(
                    "[?] ¿Quieres eliminar esta cuenta?",
                    choices=["y", "n"],
                    default="n",
                )
                if answ == "y":
                    cpm.delete()
                    console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                    console.print(
                        "[bold yellow] '======================================[/bold yellow]"
                    )
                    console.print(
                        "[bold yellow] f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram.: @{__CHANNEL_USERNAME__}[/bold yellow]"
                    )
                else:
                    continue
            elif service == 9:  # Account Register
                console.print("[bold yellow] '[!] Registrar una nueva cuenta[/bold yellow]")
                acc2_email = prompt_valid_value(
                    "[?] Correo electrónico de la cuenta", "Email", password=False
                )
                acc2_password = prompt_valid_value(
                    "[?] Contraseña de la cuenta", "Password", password=False
                )
                console.print("[%] Creando una nueva cuenta: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                    console.print(
                        "[bold yellow] '======================================[/bold yellow]"
                    )
                    console.print(
                        "[bold yellow] f'INFO: Para poder modificar esta cuenta con termux[/bold yellow]"
                    )
                    console.print(
                        "[bold yellow] 'Debes iniciar sesión en el juego usando esta cuenta[/bold yellow]"
                    )
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] '¡Este correo electrónico ya existe![/bold yellow]"
                    )
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 10:  # Delete Friends
                console.print("[%] Eliminar a tus amigos: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 11:  # Unlock All Lamborghinis
                console.print(
                    "[!] ⚠️NOTA: Esta función tarda un tiempo en completarse, no la canceles..",
                    end=None,
                )
                console.print("[%] Desbloqueo de todos los Lamborghinis: ", end=None)
                if cpm.unlock_all_lamborghinis():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 12:  # Unlock All Cars
                console.print("[%] Desbloqueo de todos los coches: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 13:  # Unlock All Cars Siren
                console.print("[%] Desbloqueo de la sirena de todos los coches: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 14:  # Unlock w16 Engine
                console.print("[%] Desbloqueo del motor w16: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 15:  # Unlock All Horns
                console.print("[%] Desbloqueando todos los claxon: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 16:  # Disable Engine Damage
                console.print("[%] Desbloqueo de motor indestructibles: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 17:  # Unlimited Fuel
                console.print("[%] Desbloqueo de gasolina infinita: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 18:  # Unlock House 3
                console.print("[%] Desbloqueo de la casa de paga: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 19:  # Unlock Smoke
                console.print("[%] Desbloqueo de humo: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 20:  # Unlock Smoke
                console.print("[%] Desbloqueo de rines: ", end=None)
                if cpm.unlock_wheels():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(8)
                    continue
            elif service == 21:  # Unlock Smoke
                console.print("[%] Desbloqueo de animaciones: ", end=None)
                if cpm.unlock_animations():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 22:  # Unlock Smoke
                console.print("[%] Desbloqueo de equipos masculinos: ", end=None)
                if cpm.unlock_equipments_male():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 23:  # Unlock Smoke
                console.print("[%] Desbloqueo de ropa de mujer: ", end=None)
                if cpm.unlock_equipments_female():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 24:  # Change Races Wins
                console.print(
                    "[bold yellow] '[!] Inserta cuantas carreras ganas[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Cambiar sus datos: ", end=None)
                if (
                    amount > 0
                    and amount
                    <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                ):
                    if cpm.set_player_wins(amount):
                        console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                        console.print(
                            "[bold yellow] '======================================[/bold yellow]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO[/bold red]")
                        console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] '[!] Por favor, utilice valores válidos[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 25:  # Change Races Loses
                console.print(
                    "[bold yellow] '[!] Inserta cuantas carreras perdidas quieres tener[/bold yellow]"
                )
                amount = IntPrompt.ask("[?] Cantidad")
                console.print("[%] Cambiar sus datos: ", end=None)
                if (
                    amount > 0
                    and amount
                    <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                ):
                    if cpm.set_player_loses(amount):
                        console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                        console.print(
                            "[bold yellow] '======================================[/bold yellow]"
                        )
                        answ = Prompt.ask(
                            "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] Gracias por usar mi herramienta[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FALLIDO[/bold red]")
                        console.print(
                            "[bold yellow] '[!] Por favor, utilice valores válidos[/bold yellow]"
                        )
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] '[!] Por favor, utilice valores válidos[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 26:  # Clone Account
                console.print(
                    "[bold yellow] '[!] Por favor ingrese los detalles de la cuenta[/bold yellow]"
                )
                to_email = prompt_valid_value(
                    "[?] Correo electrónico de la cuenta", "Email", password=False
                )
                to_password = prompt_valid_value(
                    "[?] Contraseña de la cuenta", "Password", password=False
                )
                console.print("[%] Clonando tu cuenta: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold yellow] '[!] LA CONTRASEÑA DE GMAIL DE LA CUENTA DEL DESTINATARIO NO ES VÁLIDA O ESA CUENTA NO ESTÁ REGISTRADA[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 27:
                console.print(
                    "[bold yellow][!] Note[/bold yellow]: ¡No se puede restaurar la velocidad original!."
                )
                console.print("[bold yellow][!] Introduzca los detalles del vehículo.[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] ID del carro[/bold]")
                new_hp = IntPrompt.ask("[bold][?]Ingrese al nuevo HP[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?]Ponga el Inner del Hp[/bold]")
                new_nm = IntPrompt.ask("[bold][?]ponga el nuevo NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?]ponga el Torque[/bold]")
                console.print(
                    "[bold yellow][%] Hackeando la velocidad del coche[/bold yellow]:", end=None
                )
                if cpm.hack_car_speed(car_id, new_hp, new_inner_hp, new_nm, new_torque):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print(
                        "[bold yellow] '[!] Por favor, utilice valores válidos[/bold yellow]"
                    )
                    sleep(2)
                    continue
            elif service == 28:  # ANGLE
                console.print("[bold yellow] '[!] INGRESE LOS DETALLES DEL VEHÍCULO[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold yellow] '[!] INTRODUCIR EL ÁNGULO DE DIRECCIÓN[/bold yellow]")
                custom = IntPrompt.ask(
                    "[red][?]﻿INTRODUCE LA CANTIDAD DE ÁNGULO QUE DESEAS[/red]"
                )
                console.print("[red][%] HACKEANDO EL ÁNGULO DEL COCHE[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                    answ = Prompt.ask(
                        "[red][?] ¿QUIERES SALIR?[/red] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 29:  # tire
                console.print("[bold yellow] '[!] INGRESE LOS DETALLES DEL VEHÍCULO[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold yellow] '[!] INTRODUCIR PORCENTAJE[/bold yellow]")
                custom = IntPrompt.ask("[pink][?]﻿INGRESE EL PORCENTAJE DE NEUMÁTICOS QUE DESEA[/pink]")
                console.print("[red][%] Ajuste de porcentaje [/red]: ", end=None)
                if cpm.max_max2(car_id, custom):
                    console.print("[bold yellow] 'EXITOSO[/bold yellow]")
                    answ = Prompt.ask(
                        "[bold green][?] ¿QUIERES SALIR?[/bold green] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 30:  # Millage
                console.print("[bold]INTRODUCIR LOS DATOS DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold]INGRESE NUEVO MILLAGE![/bold]")
                custom = IntPrompt.ask(
                    "[bold blue][?]﻿INGRESE EL KILOMETRAJE QUE DESEE[/bold blue]"
                )
                console.print(
                    "[bold red][%] Ajuste de porcentaje [/bold red]: ", end=None
                )
                if cpm.millage_car(car_id, custom):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 31:  # Brake
                console.print("[bold]INTRODUCIR LOS DATOS DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold]ENTER ¡FRENO NUEVO![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTRA FRENO LO QUE QUIERES[/bold blue]")
                console.print("[bold red][%] Ajuste del FRENO [/bold red]: ", end=None)
                if cpm.brake_car(car_id, custom):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 32:  # Bumper rear
                console.print("[bold]INTRODUCIR LOS DATOS DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print(
                    "[bold red][%] Desmontaje del parachoques trasero [/bold red]: ", end=None
                )
                if cpm.rear_bumper(car_id):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 33:  # Bumper front
                console.print("[bold]¡INGRESE LOS DETALLES DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print(
                    "[bold red][%] Desmontaje del parachoques delantero [/bold red]: ", end=None
                )
                if cpm.front_bumper(car_id):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 75:  # /testin endpoint
                console.print("[bold]INTRODUCIR DATOS DE FLOTACIÓN PERSONALIZADOS[/bold]")
                custom = IntPrompt.ask(
                    "[bold][?] VALUE (e.g. 1 or 0)[/bold]"
                )  # This is the value
                console.print(
                    f"[bold red][%] Configuración de la llave flotante... [/bold red]", end=None
                )
                if cpm.testin(custom):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold yellow]FALLIDO[/bold yellow]")
                    console.print("[bold yellow]POR FAVOR INTÉNTALO DE NUEVO[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 34:
                console.print("[bold]¡Introduzca la nueva contraseña![/bold]")
                new_password = prompt_valid_value(
                    "[bold][?] Nueva Contraseña[/bold]", "Password", password=False
                )
                console.print("[bold red][%] Cambiar contraseña [/bold red]: ", end=None)
                if cpm.change_password(new_password):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white]Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold yellow]FALLIDO[/bold yellow]")
                    console.print("[bold yellow]POR FAVOR INTÉNTALO DE NUEVO[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 36:  # telmunnongodz
                console.print("[bold]INTRODUCIR LOS DATOS DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold]¡INGRESA EL ID DEL SPOILER![/bold]")
                custom = IntPrompt.ask("[bold blue][?]INTRODUZCA EL NUEVO ID DE SPOILER[/bold blue]")
                console.print("[bold red][%] GUARDANDO SUS DATOS [/bold red]: ", end=None)
                if cpm.telmunnongodz(car_id, custom):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 37:  # telmunnongonz
                console.print("[bold]¡INGRESE LOS DETALLES DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold]¡INTRODUCE EL ID DEL BODYKIT![/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERTAR IDENTIFICACIÓN DEL BODYKIT[/bold blue]")
                console.print("[bold red][%] GUARDANDO SUS DATOS [/bold red]: ", end=None)
                if cpm.telmunnongonz(car_id, custom):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 51:  # telmunnongonz
                console.print("[bold]¡INGRESE LOS DETALLES DEL VEHÍCULO![/bold]")
                car_id = IntPrompt.ask("[bold][?] ID DEL COCHE[/bold]")
                console.print("[bold]INTRODUZCA EL VALOR DE LA POSTURA [/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERTAR VALOR[/bold blue]")
                console.print("[bold red][%] GUARDANDO SUS DATOS [/bold red]: ", end=None)
                if cpm.incline(car_id, custom):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 35:
                console.print("[bold]¡Ingrese un nuevo correo electrónico![/bold]")
                new_email = prompt_valid_value(
                    "[bold][?]  Nuevo Correo Electrónico[/bold]", "Email"
                )
                console.print("[bold red][%] Cambiar el correo electrónico [/bold red]: ", end=None)
                if cpm.change_email(new_email):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ¿QUIERES SALIR?[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white]Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        break
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]EL CORREO ELECTRÓNICO YA ESTÁ REGISTRADO [/bold red]")
                    sleep(4)
            elif service == 38:  # SHITTIN
                console.print("[%] Desbloqueo de rines premium..: ", end=None)
                if cpm.shittin():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 39:  # Unlock toyota crown
                console.print(
                    "[!] ⚠️NOTA: Esta función tarda un tiempo en completarse, no la canceles..",
                    end=None,
                )
                console.print("[%] Desbloqueo de Toyota Crown: ", end=None)
                if cpm.unlock_crown():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 40:  # Unlock Hat
                console.print("[%] Desbloqueo del sombrero del clan: ", end=None)
                if cpm.unlock_hat_m():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 41:  # remove head male
                console.print("[%] Quitando la cabeza del personaje (M): ", end=None)
                if cpm.rmhm():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 42:  # remove head female
                console.print("[%] Quitando la cabeza del personaje (F): ", end=None)
                if cpm.rmhfm():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 43:  # Unlock TOPM
                console.print("[%] Desbloqueo de ropa de clan Top 1: ", end=None)
                if cpm.unlock_topm():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 44:  # Unlock TOPMz
                console.print("[%] Desbloqueo de ropa de clan Top 1: ", end=None)
                if cpm.unlock_topmz():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 46:  # Unlock TOPF
                console.print("[%] Desbloqueo de ropa de clan Superior: ", end=None)
                if cpm.unlock_topf():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 47:  # Unlock TOPFZ
                console.print("[%] Desbloqueo de ropa de clan Top 1: ", end=None)
                if cpm.unlock_topfz():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Thank You for using my tool[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 48:  # Unlock Mercedes Cls
                console.print("[%] Desbloqueo de Mercedes Cls: ", end=None)
                if cpm.unlock_cls():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 49:  # modificar todos los autos
                console.print("[bold]INTRODUZCA LOS DETALLES PARA MODIFICAR TODOS LOS AUTOS![/bold]")
                new_hp = IntPrompt.ask("[bold][?] Nuevo HP[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?] Nuevo HP interno[/bold]")
                new_nm = IntPrompt.ask("[bold][?] Nuevo NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?] Nuevo Torque[/bold]")
                console.print(
                    "[bold red][%] modificar todos los coches [/bold red]: ", end=None
                )
                if cpm.modificar_todos_los_autos(new_hp, new_inner_hp, new_nm, new_torque):
                   console.print("[bold green]EXITOSO (✔)[/bold green]")
                   console.print(
                        "[bold green]======================================[/bold green]"
                   )
                   answ = Prompt.ask(
                        "[bold][?]¿QUIERES IRTE?[/bold] ?", choices=["y", "n"], default="n",
                   )
                   if answ == "y":
                       console.print(
                            "Gracias por usar la herramienta"
                       )
                   else:
                       continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue        
            elif service == 50:  # Unlock Paid Cars
                console.print("[%] Desbloquear coches de pago: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                         continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue
            elif service == 52:  # COPY LIVERY
                console.print("[bold]¡INGRESE LOS DETALLES DEL VEHÍCULO![/bold]")
                source_car_id = IntPrompt.ask("[bold][?] ID DEL CARRO QUE TIENE EL DISEÑO[/bold]")
                target_car_id = IntPrompt.ask("[bold][?] ID DE CARRO DONDE IRA EL DISEÑO[/bold]")
                console.print("[%] COPIANDO DISEÑO, POR FAVOR ESPERE: ", end=None)

                if cpm.copy_livery(source_car_id, target_car_id):
                    console.print("[bold green]EXITOSO (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                
                    )
                    answ = Prompt.ask(
                        "[?] ¿Quieres salir?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] Gracias por usar mi herramienta[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FALLIDO[/bold red]")
                    console.print("[bold red]Por favor, inténtalo de nuevo[/bold red]")
                    sleep(2)
                    continue        
                break
            break
