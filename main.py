from drafter import *
from bakery import assert_equal
from dataclasses import dataclass
 
set_website_title("Online Crossword Puzzles")
set_site_information(
    author="Emma Highberger",
    description="Website containing free crossword puzzles that can be done online.",
    sources="Thanks to the Brigantine Times for the puzzles!",
    planning=["plan.pdf", "design.pdf"],
    links=["https://github.com/your-username/your-repository"]
)
hide_debug_information()
set_website_framed(False)
# ----------------------------------------------------------------------------
# CONSTANTS (global constants are allowed; there are no global variables)
# ----------------------------------------------------------------------------
 
BLACK = "#"
SIZE = 15

# Puzzle number -> label used on the start-page button AND the puzzle-page header
PUZZLE_TITLES = {
    1: "BIRDS",
    2: "BASEBALL",
    3: "AT AN AMUSEMENT PARK",
    4: "THE 2010s",
}
 
# Crossword 1 answer grid, one string per row. "#" is a black square.
SOLUTION_1 = [
    "USER##PAP###KAY",
    "TAXA#TILE#OPINE",
    "AKIN#UVEA#GHENT",
    "HITCHCOCK#DOVE#",
    "###OUSTS#BEE###",
    "THERMO##CONNOTE",
    "EEC#UNLOAD#ISIS",
    "SLOPS#AWL#EXAMS",
    "TOLU#POLLEX#KEA",
    "STIFLES##CANARY",
    "###FIN#CELLO###",
    "#GRIM#ALBATROSS",
    "CRANE#GOBI#MAMA",
    "DITSY#AVER#AHOY",
    "CPA###RED##LUGS",
]
 
ACROSS_CLUES_1 = {
    1: "Consumer",
    5: "Drivel",
    8: "Mary of direct marketing fame",
    11: "Taxon, pl.",
    12: "Mosaic piece",
    13: "Speculate",
    15: "Similar",
    16: "Eye part",
    17: "Belgian port city",
    18: "*\"The Birds\" producer and director",
    20: "*\"Mourning\" bird",
    21: "Kicks out",
    22: "*\"Birds do it, ___ do it,\" sing.",
    23: "\"Hot\" prefix",
    26: "Suggest",
    30: "Treaty of Rome org.",
    31: "Dump",
    34: "*Horus' mother",
    35: "Spills over a container edge",
    37: "Hole punch",
    38: "Finals",
    39: "Type of balsam",
    40: "Thumb, anatomically speaking",
    42: "*New Zealand parrot",
    43: "Suppresses",
    45: "*\"Big Bird,\" e.g.",
    47: "Shark part",
    48: "Yo-Yo's instrument",
    50: "Bleak",
    52: "*Bird with largest wingspan",
    56: "Popular origami bird",
    57: "Mongolian desert",
    58: "*Hen to chick",
    59: "Silly and scatterbrained",
    60: "Affirm with confidence",
    61: "Sailor's call",
    62: "Number cruncher, acr.",
    63: "Color",
    64: "Totes",
}
 
DOWN_CLUES_1 = {
    1: "D-Day beach",
    2: "H. H. Munro's pseudonym",
    3: "Sign of escape",
    4: "Ill will",
    5: "Basketball foot maneuver",
    6: "Smart ones?",
    7: "Reach a high",
    8: "a.k.a. Kyiv",
    9: "Green Gables resident",
    10: "Hitherto",
    12: "U of A home",
    13: "Poet Nash",
    14: "*Albus Dumbledore's companion",
    19: "Dark fertile soil",
    22: "Board of Directors, acr.",
    23: "MCAT and LSAT, e.g.",
    24: "Serf",
    25: "Cause for food recall",
    26: "Pay a visit",
    27: "Japanese port city",
    28: "Sand clock, e.g.",
    29: "Test form",
    32: "Vietnam's neighbor",
    33: "*Parliament member",
    36: "*\"Barbara's ___ Cereal\"",
    38: "Glorify",
    40: "Mightier than sword",
    41: "Oblong cream puff",
    44: "British sailor, slangily",
    46: "Conventional",
    48: "Garlic unit",
    49: "What tide did",
    50: "Golf club handle",
    51: "Pro ___",
    52: "Lab culture",
    53: "Pearl Harbor island",
    54: "Urban haze",
    55: "Simon does what?",
    56: "Public health org.",
}
 
# Crossword 2 (baseball theme) answer grid. "#" is a black square.
SOLUTION_2 = [
    "SCUBA#ASH##ROCK",
    "POPUP#RAY#BOULE",
    "ACORN#TEE#ASSAY",
    "YANKEES#NINETY#",
    "###AID#TART####",
    "BAN#CECA#KARATE",
    "ODOR#MOBE#METAL",
    "NIPA#ABUTS#TOPI",
    "DEANS#BLUE#ENID",
    "SULTAN#AIDE#ERE",
    "####DEER#GNP###",
    "#LOADED#SEVENTH",
    "CIVIL#URN#INURE",
    "ANELE#COO#ENTER",
    "LENS##EBB#DESKS",
]
 
ACROSS_CLUES_2 = {
    1: "Diver's acronym",
    6: "*Bat wood",
    9: "1970s \"pet\"",
    13: "*High-flying fly ball",
    14: "*Tampa Bay player",
    15: "Round loaf, in Paris",
    16: "Oak fruit",
    17: "Golf peg",
    18: "Investigative report",
    19: "*Winningest World Series team",
    21: "*How many feet between bases?",
    23: "Help",
    24: "Queen of Hearts' pastry",
    25: "*80-game restriction, e.g.",
    28: "Cecum, pl.",
    30: "Mr. Miyagi's forte",
    35: "Some soaps have none",
    37: "Mobile phone in Britain, slangily",
    39: "Heat-conducting material",
    40: "Australian palm",
    41: "Borders on",
    43: "Large African antelope",
    44: "Campus VIPs",
    46: "*Umpires: Men in ___",
    47: "Wednesday Addams' roommate",
    48: "*Babe Ruth, a.k.a. the ___ of Swat",
    50: "Campaign worker",
    52: "Before, old-fashioned",
    53: "Buck or doe",
    55: "GDP predecessor",
    57: "*Grand slam: home run with bases ___",
    60: "*___-inning stretch",
    64: "Courteous and respectful",
    65: "Large coffee pot",
    67: "Habituate",
    68: "Administer ceremonial oil",
    69: "Bird word",
    70: "Come in",
    71: "Magnifying glass",
    72: "Flow's partner",
    73: "Classroom furniture pieces",
}
 
DOWN_CLUES_2 = {
    1: "Fix a cat",
    2: "Kind of cola",
    3: "\"Once ___ a time...\"",
    4: "Muslim woman's cover",
    5: "Relating to apnea",
    6: "Crafts' partner",
    7: "Ed's request",
    8: "Laughing predator",
    9: "*Record holder for most career hits",
    10: "Give a boot",
    11: "Modeling material",
    12: "Piano's E or G, e.g.",
    15: "Small chicken variety",
    20: "Organ swelling",
    22: "Rub the wrong way",
    24: "Arranged in rows and columns",
    25: "*Record holder for most career home runs",
    26: "Farewell, in France",
    27: "Edible cactus",
    29: "*One of five first Hall of Fame inductees",
    31: "Blood vessel network",
    32: "Repent",
    33: "Short-trunked ungulate",
    34: "Exclude or omit",
    36: "Rave's partner",
    38: "Needle case",
    42: "Swamp plant",
    45: "Equestrian's seat",
    49: "Born, in bio",
    51: "Begrudged",
    54: "Derive",
    56: "Tubular pasta",
    57: "*Third base ___",
    58: "Kitchen appliance",
    59: "Pains",
    60: "Nose-in-the-air type",
    61: "Bonkers",
    62: "Hiker's journey",
    63: "Not his",
    64: "*___ Ripken Jr.",
    66: "*Umpire's blown call",
}

SOLUTION_3 = [
    "SHOE##CPA##LIED",
    "CERN#HAIR#GUNNY",
    "ARAB#ANTI#ANODE",
    "DOLLYWOOD#MANS#",
    "###OAKEN#NIP###",
    "CLICHE##CANASTA",
    "EON#ORDAIN#REEL",
    "DISCO#ANT#SKOAL",
    "AREA#PRIEST#USE",
    "RETREAT##WALLEY",
    "###OUT#DEIFY###",
    "#SOUL#DEEPFRIED",
    "CEASE#ACRE#INTO",
    "UTTER#DAIS#SCUT",
    "DAHL##ALE##THIS",
]
 
ACROSS_CLUES_3 = {
    1: "If it fits...",
    5: "Accounting pro",
    8: "What Pinocchio did",
    12: "What discern and concern have in common",
    13: "\"The American Tribal Love-Rock Musical\"",
    14: "Sack fabric",
    15: "A in UAE",
    16: "Not with us, prefix",
    17: "Opposite of cathode",
    18: "*Late Parton's amusement venue",
    20: "Dog is ___ best friend",
    21: "Made out of certain hard-wood",
    22: "Tiny sip",
    23: "Trite one",
    26: "Type of rummy",
    30: "Bajillion years",
    31: "Appoint #40 Across",
    34: "Film wheel",
    35: "\"Saturday Night Fever\" music",
    37: "Adam of \"Stand and Deliver\"",
    38: "Smokeless tobacco brand",
    39: "Region",
    40: "Religious minister",
    42: "Wear and tear",
    43: "Opposite of advance",
    45: "*___ World, Griswalds' destination",
    47: "Not in",
    48: "Worship like god",
    50: "Music genre",
    52: "*Like funnel cakes and elephant ears",
    56: "Halt",
    57: "*Disney World in Florida spans over 25,000 of these",
    58: "Not out of",
    59: "Like complete nonsense",
    60: "Podium",
    61: "Cottontail's tail",
    62: "Willy Wonka's creator",
    63: "Bass, e.g.",
    64: "Not that",
}
 
DOWN_CLUES_3 = {
    1: "Tropical marine fish",
    2: "Submarine sandwich",
    3: "Like traditional storytelling",
    4: "All together (2 words)",
    5: "Not kayak?",
    6: "Mountain climber's spike",
    7: "Like dry clime",
    8: "*Coney Island's original (2 words)",
    9: "Aware of a secret (2 words)",
    10: "Make them meet",
    11: "Food coloring, e.g.",
    13: "*a.k.a. game barker",
    14: "Gavroche, e.g.",
    19: "Cowboy's cry of joy",
    22: "Bobbsey twin",
    23: "Wood in the closet?",
    24: "France's longest river",
    25: "Garment insert",
    26: "Quote",
    27: "\"Gangnam Style\" capital",
    28: "Badger",
    29: "*2021 movie \"Nightmare ___\"",
    32: "*Balloon popper",
    33: "\"Wheel of Fortune\" request, 2 words",
    36: "*a.k.a. merry-go-round",
    38: "Walking stick",
    40: "Singer Benatar",
    41: "Steals",
    44: "Famous Swiss mathematician Leonhard ___",
    46: "Lyre player",
    48: "Hot rod sticker",
    49: "Spooky",
    50: "___ ___ good example",
    51: "Four-letter word",
    52: "Bit of baby talk",
    53: "Mark on a ruler",
    54: "Tiny purse",
    55: "Popular movie candy",
    56: "Something to chew on",
}

SOLUTION_4 = [
    "SWAG##CAM###NTH",
    "NASA#COPE#SPARE",
    "LIEU#ACRE#LOGON",
    "#FACEBOOK#OKAY#",
    "###HEMAN#ROE###",
    "FEDORA##TOPMOST",
    "ERE#INKPOT#ORCA",
    "TAWSE#NOR#ANION",
    "ASAP#SEPSIS#ORG",
    "SERIATE##SKINNY",
    "###NAY#SALES###",
    "#TANH#FIREWORK#",
    "MELEE#REST#BAIT",
    "BEARD#EGOS#ANTI",
    "ADS###EEN##RISC",
]
 
ACROSS_CLUES_4 = {
    1: "Convention freebie",
    5: "*Tucker of TV's \"Modern Family\"",
    8: "To the ___ degree",
    11: "*Space Shuttle Program org.",
    12: "Deal with it",
    13: "Extra tire",
    15: "Stead",
    16: "Real estate land unit",
    17: "Enter user name and password (2 words)",
    18: "*Instagram's parent company",
    20: "\"Fine by me\"",
    21: "Strong virile man",
    22: "Caviar alternative",
    23: "*Bruno Mars' hat",
    26: "Highest-reaching",
    30: "Before of yore",
    31: "Quill-dipping vessel",
    34: "Popular aquarium show star",
    35: "Schoolmarm's whip",
    37: "Neither here ___ there",
    38: "Opposite of cation",
    39: "Hurry up, acr.",
    40: "Blood infection",
    42: "Not com or edu",
    43: "Arranged in order",
    45: "Inside info",
    47: "Aye's opposite",
    48: "B2C business",
    50: "Hyperbolic tangent",
    52: "*Katy Perry's 2010 hit",
    55: "Battle royal",
    56: "One R in R&R",
    57: "Nightcrawler",
    59: "*Hipsters' facial trend",
    60: "Prima donnas' problems",
    61: "Not in favor",
    62: "Public promotions",
    63: "Even, to a poet",
    64: "CISC alternative",
}
 
DOWN_CLUES_4 = {
    1: "*Pete Davidson's TV show",
    2: "Ragamuffin",
    3: "On a deck, perhaps",
    4: "Cowboy, in South America",
    5: "Popular warming drink",
    6: "Chef's garb",
    7: "Opposite of domineering and bold",
    8: "Hindu serpent deity",
    9: "Legendary King Priam's city",
    10: "Chicken coop dweller",
    12: "Taxi driver",
    13: "Ship with a single mast",
    14: "*___ GO game",
    19: "Spooky",
    22: "Decay",
    23: "Greek cheese, pl.",
    24: "Remove from existence",
    25: "___'s, blended Scotch whisky",
    26: "High rocky hills",
    27: "Celestial hunter",
    28: "Open disrespect",
    29: "Sour-tasting",
    32: "Capped joint",
    33: "*Funko ___!",
    36: "*Toy for the fidgety",
    38: "Off kilter",
    40: "Dirty dwelling",
    41: "Specks in the sea",
    44: "Oohed and ___",
    46: "Atmospheric pressure line, on a weather map",
    48: "Military blockade",
    49: "Fire-raising",
    50: "___ off on a golf course. past tense",
    51: "Exclamation of sorrow",
    52: "*___ solo, Alex Honnold's feat",
    53: "Raja's daughter",
    54: "Baby fox and baby beaver",
    55: "Business school degree, acr.",
    58: "Habitual twitching",
}
 
 
# ----------------------------------------------------------------------------
# DATACLASSES
# ----------------------------------------------------------------------------
 
@dataclass
class Clue:
    puzzle: int             # which crossword this clue belongs to (1-4)
    number: int
    direction: str          # "Across" or "Down"
    text: str
    answer: str
    crossed_out: bool = False
 
 
@dataclass
class State:
    clues: list[Clue]               # every Clue for every crossword
    entries: dict[str, str]         # "cell_puzzle_row_col" -> letter the user typed
    current_puzzle: int             # which crossword is open (0 = start page)
    check_count: dict[str, int]     # puzzle number (as text) -> times Check was pressed
    correct_count: dict[str, int]   # puzzle number (as text) -> cells matching the answer
 
 
# ----------------------------------------------------------------------------
# GRID HELPERS (plain functions, not routes)
# ----------------------------------------------------------------------------
 
def get_solution(puzzle: int) -> list[str]:
    """The answer grid for the given crossword."""
    if puzzle == 2:
        return SOLUTION_2
    if puzzle == 3:
        return SOLUTION_3
    if puzzle == 4:
        return SOLUTION_4
    return SOLUTION_1
 
 
def get_clue_text(puzzle: int, direction: str) -> dict[int, str]:
    """The clue-number -> clue-text dictionary for a crossword and direction."""
    if puzzle == 2:
        if direction == "Across":
            return ACROSS_CLUES_2
        return DOWN_CLUES_2
    if puzzle == 3:
        if direction == "Across":
            return ACROSS_CLUES_3
        return DOWN_CLUES_3
    if puzzle == 4:
        if direction == "Across":
            return ACROSS_CLUES_4
        return DOWN_CLUES_4
    if direction == "Across":
        return ACROSS_CLUES_1
    return DOWN_CLUES_1
 
 
def is_white(puzzle: int, row: int, col: int) -> bool:
    """True if (row, col) is on the board and is not a black square."""
    if row < 0 or col < 0 or row >= SIZE or col >= SIZE:
        return False
    return get_solution(puzzle)[row][col] != BLACK
 
 
def starts_across(puzzle: int, row: int, col: int) -> bool:
    return (is_white(puzzle, row, col) and not is_white(puzzle, row, col - 1)
            and is_white(puzzle, row, col + 1))
 
 
def starts_down(puzzle: int, row: int, col: int) -> bool:
    return (is_white(puzzle, row, col) and not is_white(puzzle, row - 1, col)
            and is_white(puzzle, row + 1, col))
 
 
def read_answer(puzzle: int, row: int, col: int, direction: str) -> str:
    """Collect the letters of the word that starts at (row, col)."""
    solution = get_solution(puzzle)
    letters = ""
    while is_white(puzzle, row, col):
        letters += solution[row][col]
        if direction == "Across":
            col += 1
        else:
            row += 1
    return letters
 
 
def cell_key(puzzle: int, row: int, col: int) -> str:
    return f"cell_{puzzle}_{row}_{col}"
 
 
def cell_numbers(puzzle: int) -> dict[str, int]:
    """Number the grid the standard way, left to right, top to bottom."""
    numbers = {}
    count = 0
    for row in range(SIZE):
        for col in range(SIZE):
            if starts_across(puzzle, row, col) or starts_down(puzzle, row, col):
                count += 1
                numbers[cell_key(puzzle, row, col)] = count
    return numbers
 
 
def clue_field(clue: Clue) -> str:
    return f"clue_{clue.puzzle}_{clue.direction[0]}_{clue.number}"
 
 
def build_clues(puzzle: int) -> list[Clue]:
    """Create every Clue (across first, then down) for one crossword
    from its grid + clue text."""
    numbers = cell_numbers(puzzle)
    across_text = get_clue_text(puzzle, "Across")
    down_text = get_clue_text(puzzle, "Down")
    across = []
    down = []
    for row in range(SIZE):
        for col in range(SIZE):
            number = numbers.get(cell_key(puzzle, row, col), 0)
            if starts_across(puzzle, row, col):
                across.append(Clue(puzzle, number, "Across", across_text[number],
                                   read_answer(puzzle, row, col, "Across")))
            if starts_down(puzzle, row, col):
                down.append(Clue(puzzle, number, "Down", down_text[number],
                                 read_answer(puzzle, row, col, "Down")))
    return across + down
 
 
def count_white_cells(puzzle: int) -> int:
    total = 0
    for row in range(SIZE):
        for col in range(SIZE):
            if is_white(puzzle, row, col):
                total += 1
    return total
 
 
def count_correct(puzzle: int, entries: dict[str, str]) -> int:
    solution = get_solution(puzzle)
    correct = 0
    for row in range(SIZE):
        for col in range(SIZE):
            if (is_white(puzzle, row, col)
                    and entries.get(cell_key(puzzle, row, col), "") == solution[row][col]):
                correct += 1
    return correct
 
 
def is_checked(value) -> bool:
    """Form values for check boxes may arrive as a bool or as text."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("true", "on", "1", "yes")
 
 
# ----------------------------------------------------------------------------
# PAGE-BUILDING HELPERS
# ----------------------------------------------------------------------------
 
def build_cell(state: State, puzzle: int, row: int, col: int, numbers: dict[str, int]):
    size = "36px"
    if not is_white(puzzle, row, col):
        return Div(style_width=size, style_height=size,
                   style_background_color="black", style_box_sizing="border-box")
 
    key = cell_key(puzzle, row, col)
    letter = state.entries.get(key, "")
    color = "black"
    if letter != "" and letter != get_solution(puzzle)[row][col]:
        color = "red"
 
    pieces = []
    if key in numbers:
        pieces.append(Span(str(numbers[key]),
                           style_position="absolute", style_top="0px", style_left="2px",
                           style_font_size="10px", style_line_height="10px",
                           style_pointer_events="none"))
    pieces.append(TextBox(key, letter, maxlength="1",
                          style_width="34px", style_height="34px", style_padding="0px",
                          style_margin="0px", style_border="none",
                          style_text_align="center", style_font_size="20px",
                          style_text_transform="uppercase",
                          style_background_color="transparent", style_color=color))
    return Div(*pieces, style_position="relative", style_width=size, style_height=size,
               style_border="1px solid black", style_box_sizing="border-box")
 
 
def build_grid(state: State, puzzle: int):
    numbers = cell_numbers(puzzle)
    rows = []
    for row in range(SIZE):
        cells = []
        for col in range(SIZE):
            cells.append(build_cell(state, puzzle, row, col, numbers))
        rows.append(Div(*cells, style_display="flex"))
    return Div(*rows)
 
 
def build_clue_column(state: State, puzzle: int, direction: str):
    items = [Header(direction.upper(), 3)]
    for clue in state.clues:
        if clue.puzzle == puzzle and clue.direction == direction:
            label = f"{clue.number}. {clue.text}"
            if clue.crossed_out:
                words = Span(label, style_text_decoration="line-through", style_color="gray")
            else:
                words = Span(label)
            items.append(Div(CheckBox(clue_field(clue), clue.crossed_out), words))
    return Div(*items)
 
 
def puzzle_page(state: State) -> Page:
    puzzle = state.current_puzzle
    clue_panel = Div(build_clue_column(state, puzzle, "Across"),
                     build_clue_column(state, puzzle, "Down"),
                     style_max_height="620px", style_overflow_y="auto",
                     style_padding_right="10px")
    layout = Div(build_grid(state, puzzle), clue_panel,
                 style_display="flex", style_gap="40px", style_align_items="flex-start")
    checks = state.check_count.get(str(puzzle), 0)
    correct = state.correct_count.get(str(puzzle), 0)
    status = f"Checks made: {checks}   |   Correct letters: {correct} of {count_white_cells(puzzle)}"
    return Page(state, [
        Header(PUZZLE_TITLES.get(puzzle, "CROSSWORD"), 1),
        Text(status),
        layout,
        Button("Check Answers", update_puzzle),
        Button("Clear Puzzle", reset_puzzle),
        Button("Back to Start", index),
    ])
 
 
def centered(component):
    """Put one component on its own centered line."""
    return Div(component, style_text_align="center")


def make_state() -> State:
    """A fresh State holding every clue for all four crosswords."""
    return State(build_clues(1) + build_clues(2) + build_clues(3) + build_clues(4),
                 {}, 0,
                 {"1": 0, "2": 0, "3": 0, "4": 0},
                 {"1": 0, "2": 0, "3": 0, "4": 0})


# ----------------------------------------------------------------------------
# ROUTES
# ----------------------------------------------------------------------------
 
@route
def index(state: State) -> Page:
    state.current_puzzle = 0
    return Page(state, [
        centered(Header("Online Crossword Puzzles", 1)),
        centered(Text("Please enjoy the following four free crosswords.")),
        centered(Text("Special thanks to the Brigantine Times for the crosswords used here!")),
        centered(Text("Created by Emma Highberger")),
        centered(Button(PUZZLE_TITLES[1], crossword_1)),
        centered(Button(PUZZLE_TITLES[2], crossword_2)),
        centered(Button(PUZZLE_TITLES[3], crossword_3)),
        centered(Button(PUZZLE_TITLES[4], crossword_4)),
    ])


@route
def crossword_1(state: State) -> Page:
    state.current_puzzle = 1
    return puzzle_page(state)
 
 
@route
def crossword_2(state: State) -> Page:
    state.current_puzzle = 2
    return puzzle_page(state)
 
 
@route
def crossword_3(state: State) -> Page:
    state.current_puzzle = 3
    return puzzle_page(state)
 
 
@route
def crossword_4(state: State) -> Page:
    state.current_puzzle = 4
    return puzzle_page(state)
 
 
@route
def update_puzzle(state: State, **fields) -> Page:
    """Save every letter the user typed, apply the clue check boxes,
    and recount how many cells are correct (for the open puzzle only)."""
    puzzle = state.current_puzzle
 
    for name, value in fields.items():
        if name.startswith("cell_"):
            state.entries[name] = str(value).strip().upper()[:1]
 
    for clue in state.clues:
        if clue.puzzle == puzzle:
            if is_checked(fields.get(clue_field(clue), False)):
                clue.crossed_out = True
            else:
                clue.crossed_out = False
 
    state.check_count[str(puzzle)] = state.check_count.get(str(puzzle), 0) + 1
    state.correct_count[str(puzzle)] = count_correct(puzzle, state.entries)
    return puzzle_page(state)
 
 
@route
def reset_puzzle(state: State) -> Page:
    """Clear only the puzzle that is currently open."""
    puzzle = state.current_puzzle
    prefix = f"cell_{puzzle}_"
 
    kept = {}
    for key, letter in state.entries.items():
        if not key.startswith(prefix):
            kept[key] = letter
    state.entries = kept
 
    for clue in state.clues:
        if clue.puzzle == puzzle:
            clue.crossed_out = False
    state.check_count[str(puzzle)] = 0
    state.correct_count[str(puzzle)] = 0
    return puzzle_page(state)
 
 
# ----------------------------------------------------------------------------
# UNIT TESTS (run with the program; results are printed by bakery)
# ----------------------------------------------------------------------------

# --- index ---
page = index(make_state())
assert_equal(len(page.content), 8)
assert_equal(page.content[0], centered(Header("Online Crossword Puzzles", 1)))
assert_equal(page.content[4], centered(Button("BIRDS", crossword_1)))
assert_equal(page.content[5], centered(Button("BASEBALL", crossword_2)))
assert_equal(page.content[6], centered(Button("AT AN AMUSEMENT PARK", crossword_3)))
assert_equal(page.content[7], centered(Button("THE 2010s", crossword_4)))
open_state = make_state()
open_state.current_puzzle = 3
assert_equal(index(open_state).state.current_puzzle, 0)

# --- crossword_1 .. crossword_4 ---
page = crossword_1(make_state())
assert_equal(page.state.current_puzzle, 1)
assert_equal(page.content[0], Header("BIRDS", 1))

page = crossword_2(make_state())
assert_equal(page.state.current_puzzle, 2)
assert_equal(page.content[0], Header("BASEBALL", 1))

page = crossword_3(make_state())
assert_equal(page.state.current_puzzle, 3)
assert_equal(page.content[0], Header("AT AN AMUSEMENT PARK", 1))

page = crossword_4(make_state())
assert_equal(page.state.current_puzzle, 4)
assert_equal(page.content[0], Header("THE 2010s", 1))

# --- update_puzzle ---
check_state = make_state()
check_state.current_puzzle = 1
page = update_puzzle(check_state, cell_1_0_0="u", cell_1_0_1="x", clue_1_A_1=True)
assert_equal(page.state.entries["cell_1_0_0"], "U")        # saved in upper case
assert_equal(page.state.entries["cell_1_0_1"], "X")        # wrong letters are still saved
assert_equal(page.state.clues[0].crossed_out, True)        # 1 Across was checked
assert_equal(page.state.clues[1].crossed_out, False)       # 5 Across was not
assert_equal(page.state.check_count["1"], 1)
assert_equal(page.state.correct_count["1"], 1)             # only the U matches
assert_equal(page.state.check_count["2"], 0)               # other puzzles untouched
assert_equal(page.content[0], Header("BIRDS", 1))

# --- reset_puzzle ---
reset_state = make_state()
reset_state.current_puzzle = 2
reset_state.entries = {"cell_1_0_0": "U", "cell_2_0_0": "S"}
reset_state.check_count["2"] = 3
reset_state.correct_count["2"] = 1
for clue in reset_state.clues:
    clue.crossed_out = True
page = reset_puzzle(reset_state)
assert_equal(page.state.entries, {"cell_1_0_0": "U"})      # only puzzle 2 was cleared
assert_equal(page.state.check_count["2"], 0)
assert_equal(page.state.correct_count["2"], 0)
assert_equal(page.state.clues[0].crossed_out, True)        # puzzle 1 clue kept
assert_equal(page.state.clues[-1].crossed_out, True)       # puzzle 4 clue kept
puzzle_2_clues = [clue for clue in page.state.clues if clue.puzzle == 2]
assert_equal(puzzle_2_clues[0].crossed_out, False)         # puzzle 2 clue cleared
assert_equal(page.content[0], Header("BASEBALL", 1))

start_server(make_state())
