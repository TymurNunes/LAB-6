mountains = {
    "Pip Ivan Chernogirsky (Chorna gora)": 2028,
    "Gutin Tomnatyk": 2016,
    "Dzembronia": 1878,
    "Rebra": 2001,
    "Breskul": 1911,
    "Brebenescul": 2032,
    "Pops Ivan": 1936,
    "Hoverla": 2061,
    "Petros": 2020,
    "Turkul": 1933,
}

sorted_mountains = sorted(mountains.items(), key=lambda x: x[1], reverse=True)

for name, height in sorted_mountains[:3]:
    print(name, ":", height, "m")