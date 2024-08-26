from pridobitev_podatkov import atleti
import pycountry_convert as pc
import pypopulation
##### 1. DEL ####

ioc_to_iso = {
    "AIN": "AIN",
    "AFG": "AFG",
    "ALB": "ALB",
    "ALG": "DZA",
    "AND": "AND",
    "ANG": "AGO",
    "ANT": "ATG",
    "ARG": "ARG",
    "ARM": "ARM",
    "ARU": "ABW",
    "ASA": "ASM",
    "AUS": "AUS",
    "AUT": "AUT",
    "AZE": "AZE",
    "BAH": "BHS",
    "BRN": "BHR",
    "BAN": "BGD",
    "BAR": "BRB",
    "BLR": "BLR",
    "BEL": "BEL",
    "BIZ": "BLZ",
    "BEN": "BEN",
    "BER": "BMU",
    "BHU": "BTN",
    "BOL": "BOL",
    "BIH": "BIH",
    "BOT": "BWA",
    "BRA": "BRA",
    "BRU": "BRN",
    "BUL": "BGR",
    "BUR": "BFA",
    "BDI": "BDI",
    "CPV": "CPV",
    "CAM": "KHM",
    "CMR": "CMR",
    "CAN": "CAN",
    "CAY": "CYM",
    "CAF": "CAF",
    "CHA": "TCD",
    "CHI": "CHL",
    "CHN": "CHN",
    "COL": "COL",
    "COM": "COM",
    "CGO": "COG",
    "COD": "COD",
    "COK": "COK",
    "CRC": "CRI",
    "CIV": "CIV",
    "CRO": "HRV",
    "CUB": "CUB",
    "CYP": "CYP",
    "CZE": "CZE",
    "DEN": "DNK",
    "DJI": "DJI",
    "DMA": "DMA",
    "DOM": "DOM",
    "ECU": "ECU",
    "EGY": "EGY",
    "ESA": "SLV",
    "GEQ": "GNQ",
    "ERI": "ERI",
    "EST": "EST",
    "SWZ": "SWZ",
    "ETH": "ETH",
    "FIJ": "FJI",
    "FIN": "FIN",
    "FRA": "FRA",
    "GAB": "GAB",
    "GAM": "GMB",
    "GEO": "GEO",
    "GER": "DEU",
    "GHA": "GHA",
    "GRE": "GRC",
    "GRN": "GRD",
    "GUM": "GUM",
    "GUA": "GTM",
    "GUI": "GIN",
    "GBS": "GNB",
    "GUY": "GUY",
    "HAI": "HTI",
    "HON": "HND",
    "HKG": "HKG",
    "HUN": "HUN",
    "ISL": "ISL",
    "IND": "IND",
    "INA": "IDN",
    "IRI": "IRN",
    "IRQ": "IRQ",
    "IRL": "IRL",
    "ISR": "ISR",
    "ITA": "ITA",
    "JAM": "JAM",
    "JPN": "JPN",
    "JOR": "JOR",
    "KAZ": "KAZ",
    "KEN": "KEN",
    "KIR": "KIR",
    "PRK": "PRK",
    "KOR": "KOR",
    "KOS": "XKX",
    "KUW": "KWT",
    "KGZ": "KGZ",
    "LAO": "LAO",
    "LAT": "LVA",
    "LBN": "LBN",
    "LES": "LSO",
    "LBR": "LBR",
    "LBA": "LBY",
    "LIE": "LIE",
    "LTU": "LTU",
    "LUX": "LUX",
    "MAD": "MDG",
    "MWI": "MWI",
    "MAS": "MYS",
    "MDV": "MDV",
    "MLI": "MLI",
    "MLT": "MLT",
    "MHL": "MHL",
    "MTN": "MRT",
    "MRI": "MUS",
    "MEX": "MEX",
    "FSM": "FSM",
    "MDA": "MDA",
    "MCO": "MCO",
    "MNG": "MNG",
    "MNE": "MNE",
    "MGL": "MNG",
    "MAR": "MAR",
    "MOZ": "MOZ",
    "MYA": "MMR",
    "NAM": "NAM",
    "NRU": "NRU",
    "NEP": "NPL",
    "NED": "NLD",
    "NZL": "NZL",
    "NCA": "NIC",
    "NER": "NER",
    "NGA": "NGA",
    "MKD": "MKD",
    "NOR": "NOR",
    "OMA": "OMN",
    "PAK": "PAK",
    "PLW": "PLW",
    "PAN": "PAN",
    "PNG": "PNG",
    "PAR": "PRY",
    "PER": "PER",
    "PHI": "PHL",
    "POL": "POL",
    "POR": "PRT",
    "PUR": "PRI",
    "QAT": "QAT",
    "ROU": "ROU",
    "RUS": "RUS",
    "RWA": "RWA",
    "SKN": "KNA",
    "LCA": "LCA",
    "VIN": "VCT",
    "SAM": "WSM",
    "SMR": "SMR",
    "STP": "STP",
    "KSA": "SAU",
    "SEN": "SEN",
    "SRB": "SRB",
    "SEY": "SYC",
    "SLE": "SLE",
    "SGP": "SGP",
    "SVK": "SVK",
    "SLO": "SVN",
    "SOL": "SLB",
    "SOM": "SOM",
    "RSA": "ZAF",
    "ESP": "ESP",
    "SRI": "LKA",
    "SUD": "SDN",
    "SUR": "SUR",
    "SWD": "SWZ",
    "SWE": "SWE",
    "SUI": "CHE",
    "SYR": "SYR",
    "TPE": "TWN",
    "TJK": "TJK",
    "TAN": "TZA",
    "THA": "THA",
    "TLS": "TLS",
    "TOG": "TGO",
    "TGA": "TON",
    "TTO": "TTO",
    "TUN": "TUN",
    "TUR": "TUR",
    "TKM": "TKM",
    "UGA": "UGA",
    "UKR": "UKR",
    "UAE": "ARE",
    "GBR": "GBR",
    "USA": "USA",
    "URU": "URY",
    "UZB": "UZB",
    "VAN": "VUT",
    "VEN": "VEN",
    "VIE": "VNM",
    "ISV": "VIR",
    "YEM": "YEM",
    "ZAM": "ZMB",
    "ZIM": "ZWE",
    "EOR": "XXX",  # IOC Refugee Olympic Team (no ISO equivalent)
}

for atlet in atleti:
    drž = atlet.get('organisation')
    if drž in ioc_to_iso:
        atlet['organisation'] = ioc_to_iso[drž]
        #print(atlet['medals'])
        #print(atlet)
    else:
        continue

############################################################################################################

#### 2. DEL ####

slovar_discplin_z_eventi = {}
slovar_disciplin_podeljenih_medalj = {}
for atlet in atleti:
    for medalja in atlet['medals']:
        ime = medalja.get('disciplineName')
        eventName = medalja.get('eventName')
        category = medalja.get('category')
        if ime not in slovar_discplin_z_eventi:
            slovar_discplin_z_eventi[ime] = [[eventName, category]]
        else:
            if [eventName, category] not in slovar_discplin_z_eventi[ime]:
                slovar_discplin_z_eventi[ime].append([eventName, category])

for disciplina, medalje in slovar_discplin_z_eventi.items():
    slovar_disciplin_podeljenih_medalj[disciplina] = len(medalje)

število_vseh_medalj = 0
for disciplina, medalje in slovar_disciplin_podeljenih_medalj.items():
    število_vseh_medalj += medalje

weightane_vrednosti_evetov = {}
for disciplina, medalje in slovar_discplin_z_eventi.items():
    weightane_vrednosti_evetov[disciplina] = število_vseh_medalj/len(medalje)

#print(weightane_vrednosti_evetov)
#print(število_vseh_medalj)
#print(slovar_disciplin_podeljenih_medalj)
#print(slovar_discplin_z_eventi)

############################################################################################################

#### 3. DEL ####
def stevilo_medalj_drzave(niz):
    medal_list = []
    slovar = {}
    for atlet in atleti:
        for medal in atlet['medals']:
            medalja = [atlet['organisation'], medal['medalType'], medal['eventName'], medal['category'], medal['disciplineName']]
            if medalja in medal_list:
                continue
            else:
                medal_list.append(medalja)
    #print(medal_list)
    for kolajna in medal_list:
        država = kolajna[0]
        medalčka = kolajna[1]
        if država not in slovar:
            if medalčka == 'ME_GOLD':
                slovar[država] = [1, 0, 0]
            elif medalčka == 'ME_SILVER':
                slovar[država] = [0, 1, 0]
            else:
                slovar[država] = [0, 0, 1]
        else:
            if medalčka == 'ME_GOLD':
                slovar[država][0] += 1
            elif medalčka == 'ME_SILVER':
              slovar[država][1] += 1
            else:
                slovar[država][2] += 1
        sortiran_slovar = dict(sorted(slovar.items(), key=lambda x: sum(x[1]), reverse=True))
    return sortiran_slovar
#print(stevilo_medalj_drzave(atleti))

############################################################################################################

#### 4. DEL ####

#skupno število medalj, brez weightanja in z wegihtanjem z=4, s=2, b=1 točka
alfa = stevilo_medalj_drzave(atleti)
def skupno_število_medalj(slovar, z=1, s=1, b=1):
    nov_slovar = {}
    for država, medalje in slovar.items():
        skupaj = medalje[0] * z + medalje[1] * s + medalje[2] * b
        nov_slovar[država] = skupaj
    povrsti = sorted(nov_slovar.items(), key=lambda x:x[1], reverse=True)
    return dict(povrsti)
#print(skupno_število_medalj(alfa))
#print(skupno_število_medalj(alfa, 4, 2, 1))

############################################################################################################

weightane_vrednosti_evetov
alfa = stevilo_medalj_drzave(atleti)
slovar1 = skupno_število_medalj(alfa, 4, 2, 1)
def število_točk_z_utežmi(atleti, z=1, s=1, b=1):
    slovar_držav = {}
    for atlet in atleti:
        for medal in atlet['medals']:
            država = atlet['organisation']
            medalček = medal['medalType']
            disciplina = medal['disciplineName']
            točke = 0
            if medalček == 'ME_GOLD':
                točke = z
            elif medalček == 'ME_SILVER':
                točke = s
            else:
                točke = b
            if država not in slovar_držav:
                slovar_držav[država] = round(točke * weightane_vrednosti_evetov[disciplina])
            else:
                slovar_držav[država] += round(točke * weightane_vrednosti_evetov[disciplina])
    povrsti = sorted(slovar_držav.items(), key=lambda x:x[1], reverse=True)
    return dict(povrsti)
#print(število_točk_z_utežmi(atleti))
#print(število_točk_z_utežmi(atleti, 4, 2, 1))


############################################################################################################

#### 5. DEL ####

#najbolj uspešen kontinent(štejemo kosovo(xkx) in ain(rusijo in belorusijo) med evropske države, refugeejev pa izpustimo)
slovar_kontinentov = {}
beta = skupno_število_medalj(alfa)
for država in beta:
    if država in ['ROT', 'XXX']:
        continue
    if država in ['AIN', 'XKX']:
        continent_name = 'EU'
        if continent_name not in slovar_kontinentov:
            slovar_kontinentov[continent_name] = beta[država]
        else:
            slovar_kontinentov[continent_name] += beta[država]
    else:
        country_code = pc.country_alpha3_to_country_alpha2(država)
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        if continent_name not in slovar_kontinentov:
            slovar_kontinentov[continent_name] = beta[država]
        else:
            slovar_kontinentov[continent_name] += beta[država]
    sortiran_slovar_kontinentov = dict(sorted(slovar_kontinentov.items(), key=lambda x:x[1], reverse=True))
#print(sortiran_slovar_kontinentov)

############################################################################################################

#### 6. DEL ####

#koliko medalj ima vsaka država (v primeru da v skupinskih športih štejemo vsakemu svojo)
def skupno_število_medalj_vsakemu_svojo(niz):
    države = {}
    for atlet in niz:
        cntr = atlet['organisation']
        total = atlet['medalsTotal']
        if cntr not in države:
            države[cntr] = total
        else:
            države[cntr] += total
        povrsti = sorted(države.items(), key=lambda x:x[1], reverse=True)
        skupno = dict(povrsti)
    return skupno
#print(skupno_število_medalj_vsakemu_svojo(atleti))

############################################################################################################

#### 7. DEL ####

#koliko prebivalcev vsake države ima medaljo (če imaš eno ali dve je rezultat isti)
def št_prebivalcev_z_medaljo(niz):
    države2 = {}
    for atlet in niz:
        cntr = atlet['organisation']
        if cntr not in države2:
            države2[cntr] = 1
        else:
            države2[cntr] += 1
        povrsti2 = sorted(države2.items(), key=lambda x:x[1], reverse=True)
        št_prebivalcev = dict(povrsti2)
    return št_prebivalcev
#print(št_prebivalcev_z_medaljo(atleti))

############################################################################################################

#### 8. DEL ####

#število poslanih atletov vsake države, slovar iz reddita 
število_atletov_iz_vsake_države = {
    "GBR": 327,
    "AFG": 6,
    "ALB": 8,
    "DZA": 45,
    "ASM": 2,
    "AND": 2,
    "AGO": 24,
    "ATG": 5,
    "ARG": 136,
    "ARM": 15,
    "ABW": 6,
    "AUS": 461,
    "AUT": 78,
    "AZE": 48,
    "BHS": 18,
    "BHR": 13,
    "BGD": 5,
    "BRB": 4,
    "BEL": 165,
    "BLZ": 1,
    "BEN": 5,
    "BMU": 8,
    "BTN": 3,
    "BOL": 4,
    "BIH": 5,
    "BWA": 11,
    "BRA": 277,
    "VGB": 4,
    "BRN": 3,
    "BGR": 46,
    "BFA": 8,
    "BDI": 7,
    "KHM": 3,
    "CMR": 6,
    "CAN": 315,
    "CPV": 7,
    "CYM": 4,
    "CAF": 4,
    "TCD": 3,
    "CHL": 48,
    "CHN": 388,
    "COL": 87,
    "COM": 4,
    "COG": 4,
    "CRI": 6,
    "CIV": 11,
    "HRV": 73,
    "CUB": 61,
    "CYP": 16,
    "CZE": 111,
    "COD": 6,
    "DNK": 124,
    "DJI": 7,
    "DMA": 4,
    "DOM": 58,
    "ECU": 40,
    "EGY": 148,
    "SLV": 8,
    "GNQ": 3,
    "ERI": 12,
    "EST": 24,
    "ETH": 34,
    "FJI": 33,
    "FIN": 56,
    "FRA": 573,
    "GAB": 5,
    "GMB": 7,
    "GEO": 28,
    "DEU": 428,
    "GHA": 8,
    "GRC": 100,
    "GRD": 6,
    "GUM": 8,
    "GTM": 16,
    "GIN": 24,
    "GNB": 6,
    "GUY": 5,
    "HTI": 7,
    "HND": 4,
    "HKG": 36,
    "HUN": 170,
    "ISL": 5,
    "IND": 117,
    "IDN": 29,
    "IRQ": 22,
    "IRL": 134,
    "IRN": 41,
    "ISR": 88,
    "ITA": 402,
    "JAM": 58,
    "JPN": 403,
    "JOR": 12,
    "KAZ": 79,
    "KEN": 72,
    "KIR": 3,
    "XKX": 9,
    "KWT": 9,
    "KGZ": 16,
    "LAO": 4,
    "LVA": 29,
    "LBN": 10,
    "LSO": 3,
    "LBR": 8,
    "LBY": 6,
    "LIE": 1,
    "LTU": 51,
    "LUX": 14,
    "MKD": 7,
    "MDG": 7,
    "MWI": 3,
    "MYS": 26,
    "MDV": 5,
    "MLI": 23,
    "MLT": 5,
    "MHL": 4,
    "MRT": 2,
    "MUS": 13,
    "MEX": 107,
    "FSM": 3,
    "MCO": 6,
    "MNG": 32,
    "MNE": 19,
    "MAR": 59,
    "MOZ": 7,
    "MMR": 2,
    "NAM": 4,
    "NRU": 1,
    "NPL": 7,
    "NLD": 273,
    "NZL": 195,
    "NIC": 7,
    "NER": 7,
    "NGA": 88,
    "PRK": 16,
    "NOR": 107,
    "OMN": 4,
    "PAK": 7,
    "PLW": 3,
    "PSE": 8,
    "PAN": 8,
    "PNG": 7,
    "PRY": 28,
    "PER": 26,
    "PHL": 22,
    "POL": 210,
    "PRT": 73,
    "PRI": 51,
    "QAT": 14,
    "ROT": 37,
    "MDA": 26,
    "ROU": 106,
    "RWA": 8,
    "KNA": 3,
    "LCA": 4,
    "WSM": 24,
    "SMR": 5,
    "STP": 3,
    "SAU": 9,
    "SEN": 11,
    "SRB": 112,
    "SYC": 3,
    "SLE": 4,
    "SGP": 23,
    "SVK": 28,
    "SVN": 90,
    "SLB": 2,
    "SOM": 1,
    "ZAF": 149,
    "KOR": 141,
    "SSD": 14,
    "ESP": 383,
    "LKA": 6,
    "VCT": 4,
    "SDN": 4,
    "SUR": 5,
    "SWZ": 3,
    "SWE": 118,
    "CHE": 127,
    "SYR": 6,
    "TJK": 14,
    "TZA": 7,
    "THA": 51,
    "TLS": 4,
    "TGO": 5,
    "TON": 4,
    "TTO": 18,
    "TUN": 27,
    "TUR": 101,
    "TKM": 6,
    "TUV": 2,
    "UGA": 24,
    "UKR": 140,
    "ARE": 13,
    "USA": 592,
    "URY": 25,
    "VIR": 5,
    "UZB": 86,
    "VUT": 6,
    "VEN": 33,
    "VNM": 16,
    "YEM": 4,
    "ZMB": 27,
    "ZWE": 7,
    "AIN": 32,
    "COK": 2,
    "TWN": 60
}
število_atletov_po_vrsti_neurejeno = sorted(število_atletov_iz_vsake_države.items(), key=lambda x:x[1], reverse=True)
število_atletov_po_vrsti = dict(število_atletov_po_vrsti_neurejeno)
#print(število_atletov_po_vrsti)

############################################################################################################

#### 9. DEL ####

#na koliko prebivalcev je en atlet, Ekipo migrantov izpustimo, saj vključuje različne države. Najprej če upoštevamo vse države
#Problem je v tem, da imajo majhne države prednost, zato v naslednjem cellu omejimo število prebivalcev
def koliko_prebivalcev_na_atleta(slv, i = 0):
    slovar = {}
    št_preb_taiwana = 23201184
    št_preb_cok = 17459
    for država, koliko_atletov in slv.items():
        if država not in ['TWN', 'AIN', 'ROT', 'COK']:
            #POPULACIJE TAIWANA, RUSIJE IN BELORUSIJE SKUPAJ, EKIPE MIGRANTOV IN COOKOVIH OTOKOV NISO V PYPOPULATION
            vseh_v_državi = pypopulation.get_population(država)
            if vseh_v_državi > i:
                procenti_države = f"{(vseh_v_državi)/(koliko_atletov):.0f}"
                slovar[država] = int(procenti_države)
        if država == 'AIN':
            vseh_v_državi = pypopulation.get_population('RUS') + pypopulation.get_population('BLR')
            if vseh_v_državi > i:
                procenti_ain = f"{(vseh_v_državi)/(koliko_atletov):.0f}"
                slovar[država] = int(procenti_ain)
        if država == 'TWN':
            if št_preb_taiwana > i:
                procenti_tai = f"{(št_preb_taiwana)/(koliko_atletov):.0f}"
                slovar['TWN'] = int(procenti_tai)
        if država == 'COK':
            if št_preb_cok > i:
                procenti_cok = f"{(št_preb_cok)/(koliko_atletov):.0f}"
                slovar['COK'] = int(procenti_cok)
        sortiran_slovar = dict(sorted(slovar.items(), key=lambda item: float(item[1])))
    return sortiran_slovar
        
#print(koliko_prebivalcev_na_atleta(število_atletov_iz_vsake_države))
#print(koliko_prebivalcev_na_atleta(število_atletov_iz_vsake_države, 500000))

############################################################################################################

#### 10. DEL ####

#na koliko prebivalcev je ena olimpijska medalja
gama = št_prebivalcev_z_medaljo(atleti)
def prebivalcev_na_medaljo(slovar_zmagovalcev, i = 0):
    slovar = {}
    št_preb_taiwana = 23201184
    št_preb_cok = 17459
    for država, št_preb_z_med in slovar_zmagovalcev.items():
        if država not in ['TWN', 'AIN', 'ROT', 'COK', 'XXX']:
            št_vseh = pypopulation.get_population(država)
            if št_vseh > i:
                procent_z_medaljo = f"{ št_vseh / št_preb_z_med :.0f}" 
                slovar[država] = int(procent_z_medaljo)
            #print(procent_z_medaljo)
            #print(slovar)
        if država == 'TWN':
            if št_preb_taiwana > i:
                procent_z_medaljo = f"{ št_preb_taiwana / št_preb_z_med :.0f}" 
                slovar[država] = int(procent_z_medaljo)
            #print(procent_z_medaljo)
            #print(slovar)
        if država == 'COK':
            if št_preb_cok > i:
                procent_z_medaljo = f"{ št_preb_cok / št_preb_z_med :.0f}" 
                slovar[država] = int(procent_z_medaljo)
            #print(procent_z_medaljo)
            #print(slovar)
        if država == 'AIN':
            vseh_v_ain = pypopulation.get_population('RUS') + pypopulation.get_population('BLR')
            if vseh_v_ain > i:
                procenti_ain = f"{ vseh_v_ain / št_preb_z_med :.0f}" 
                slovar[država] = int(procenti_ain)
            #print(procent_z_medaljo)
            #print(slovar)
        sortiran_slovar = dict(sorted(slovar.items(), key=lambda item: float(item[1])))
    return sortiran_slovar

#print(prebivalcev_na_medaljo(gama))
#print(prebivalcev_na_medaljo(gama, 500000))

############################################################################################################

#### 11. DEL ####

#kakšen procent atletov na OI je dobilo olimpijsko medaljo
prvi = št_prebivalcev_z_medaljo(atleti)
drugi = število_atletov_iz_vsake_države

def procent_atletov_z_medaljo(slovar1, slovar2):
    slovar = {}
    for država, število in slovar1.items():
        for country, number in slovar2.items():
            if država == country:
                procent = f"{100 * število / number :.2f}"
                slovar[država] = float(procent)
    sortiran_slovar = dict(sorted(slovar.items(), key=lambda item: float(item[1]), reverse=True))
    return sortiran_slovar
#print(procent_atletov_z_medaljo(prvi, drugi))

############################################################################################################

#### 12. DEL ####

#koliko pa je vseh medalj ki so jih športniki vsake države prinesli nazaj glede na število poslanih atletov
prvi = skupno_število_medalj_vsakemu_svojo(atleti)
drugi = število_atletov_iz_vsake_države
#print(procent_atletov_z_medaljo(prvi, drugi))