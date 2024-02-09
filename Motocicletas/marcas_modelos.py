# Mapeo con marcas, modelos y especificaciones de las motocicletas
marcas_motos = {
    "YAMAHA": {
        "YBR125": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "125cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "110 km/h",
            "capacidad_tanque": "12 litros"
        },
        "FZ150": {
            "año": 2019,
            "motor": "4 tiempos",
            "cilindrada": "150cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "120 km/h",
            "capacidad_tanque": "14 litros"
        },
        "FAZER250": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "140 km/h",
            "capacidad_tanque": "15 litros"
        },
        "XTZ250": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "130 km/h",
            "capacidad_tanque": "13 litros"
        },
        "MT-03": {
            "año": 2023,
            "motor": "4 tiempos",
            "cilindrada": "300cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "150 km/h",
            "capacidad_tanque": "14 litros"
        }
    },
    "HONDA": {
        "CBR250": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "160 km/h",
            "capacidad_tanque": "13 litros"
        },
        "CBF150": {
            "año": 2018,
            "motor": "4 tiempos",
            "cilindrada": "150cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "130 km/h",
            "capacidad_tanque": "12 litros"
        },
        "CG125": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "125cc",
            "transmision": "4 velocidades",
            "velocidad_maxima": "110 km/h",
            "capacidad_tanque": "11 litros"
        },
        "XR150": {
            "año": 2019,
            "motor": "4 tiempos",
            "cilindrada": "150cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "120 km/h",
            "capacidad_tanque": "12 litros"
        },
        "CB190": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "190cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "140 km/h",
            "capacidad_tanque": "14 litros"
        }
    },
    "SUZUKI": {
        "GSX-R150": {
            "año": 2019,
            "motor": "4 tiempos",
            "cilindrada": "150cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "140 km/h",
            "capacidad_tanque": "11 litros"
        },
        "GIXXERSF250": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "155 km/h",
            "capacidad_tanque": "12 litros"
        },
        "V-STROM250": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "150 km/h",
            "capacidad_tanque": "17 litros"
        },
        "GSX-S150": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "150cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "135 km/h",
            "capacidad_tanque": "13 litros"
        },
        "INTRUDER250": {
            "año": 2023,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "145 km/h",
            "capacidad_tanque": "15 litros"
        }
    },
    "TRIUMPH": {
        "STREET_TRIPLE_S": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "765cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "220 km/h",
            "capacidad_tanque": "17.4 litros"
        },
        "BONNEVILLE_T100": {
            "año": 2019,
            "motor": "4 tiempos",
            "cilindrada": "900cc",
            "transmision": "5 velocidades",
            "velocidad_maxima": "180 km/h",
            "capacidad_tanque": "14.5 litros"
        },
        "SPEED_TRIPLE_R": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "1050cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "240 km/h",
            "capacidad_tanque": "16 litros"
        },
        "TIGER_900_GT": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "888cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "215 km/h",
            "capacidad_tanque": "20 litros"
        },
        "ROCKET_3_GT": {
            "año": 2023,
            "motor": "4 tiempos",
            "cilindrada": "2500cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "225 km/h",
            "capacidad_tanque": "18 litros"
        }
    },
    "KAWASAKI": {
        "NINJA250": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "250cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "170 km/h",
            "capacidad_tanque": "15 litros"
        },
        "Z650": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "650cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "200 km/h",
            "capacidad_tanque": "15 litros"
        },
        "VERSYS-X300": {
            "año": 2019,
            "motor": "4 tiempos",
            "cilindrada": "296cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "160 km/h",
            "capacidad_tanque": "17 litros"
        },
        "Z900": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "948cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "230 km/h",
            "capacidad_tanque": "17 litros"
        },
        "NINJA650": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "649cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "210 km/h",
            "capacidad_tanque": "15 litros"
        }
    },
    "BMW": {
        "S1000RR": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "999cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "299 km/h",
            "capacidad_tanque": "16.5 litros"
        },
        "R1250GS": {
            "año": 2023,
            "motor": "4 tiempos",
            "cilindrada": "1254cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "215 km/h",
            "capacidad_tanque": "20 litros"
        },
        "G310R": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "313cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "143 km/h",
            "capacidad_tanque": "11 litros"
        },
        "F900R": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "895cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "220 km/h",
            "capacidad_tanque": "13 litros"
        },
        "R18": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "1802cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "180 km/h",
            "capacidad_tanque": "16 litros"
        }
    },
    "DUCATI": {
        "PANIGALE V2": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "955cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "280 km/h",
            "capacidad_tanque": "17 litros"
        },
        "MONSTER": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "937cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "250 km/h",
            "capacidad_tanque": "14.5 litros"
        },
        "STREETFIGTHER V4": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "1103cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "305 km/h",
            "capacidad_tanque": "16 litros"
        },
        "MULTISTRADA V4": {
            "año": 2023,
            "motor": "4 tiempos",
            "cilindrada": "1158cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "250 km/h",
            "capacidad_tanque": "22 litros"
        },
        "DIABOLIK": {
            "año": 2024,
            "motor": "4 tiempos",
            "cilindrada": "1260cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "280 km/h",
            "capacidad_tanque": "17 litros"
        }
    },
    "DUKE": {
        "DUKE 200": {
            "año": 2023,
            "motor": "4 tiempos",
            "cilindrada": "200cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "135 km/h",
            "capacidad_tanque": "10 litros"
        },
        "DUKE 390": {
            "año": 2022,
            "motor": "4 tiempos",
            "cilindrada": "373cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "170 km/h",
            "capacidad_tanque": "13.5 litros"
        },
        "DUKE 790": {
            "año": 2021,
            "motor": "4 tiempos",
            "cilindrada": "799cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "220 km/h",
            "capacidad_tanque": "14 litros"
        },
        "DUKE 890": {
            "año": 2020,
            "motor": "4 tiempos",
            "cilindrada": "889cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "230 km/h",
            "capacidad_tanque": "14 litros"
        },
        "DUKE 1290": {
            "año": 2019,
            "motor": "4 tiempos",
            "cilindrada": "1301cc",
            "transmision": "6 velocidades",
            "velocidad_maxima": "250 km/h",
            "capacidad_tanque": "16 litros"
        }
    }
}

sinonimos_marcas = {
    "YAMAHA": ["YAMAHA", "YAMA", "YMH","YAMA","YAM","AMAHA","YAMAH"],
    "HONDA": ["HONDA", "HNDA", "HND","ONDA","HOND","HON"],
    "SUZUKI": ["SUZUKI", "SUZ", "SZK","SUSUKI"],
    "TRIUMPH": {"TRM","TRPH","TRIUMF"},
    "ZANELLA": ["ZAN","ZNL","SANELA","SANELLA","ZANE","ZANEL","ZANELL"],
    "MOTOMEL": ["MOTO","MOT","OTOMEL", "MOTOM","MOTOME"],
    "ZONTES": ["ZON", "ZNS", "ZNTS","ZONTE","SONTES","SONT","ZONT"],
    "KAWASAKI": ["KAWASAKI", "KAWA", "KAW","KAWASAK","KAWASKI","KAWAS"],
    "BMW": ["BMW", "BM", "BIM","BWM"],
    "DUCATI": ["DUCATI", "DUC", "DU","DCATI"],
    "DUKE": ["DUKE", "DK", "DE","DKE"]
}

sinonimos_modelos = {
    # YAMAHA
    "YBR125": ["YBR", "YBR125", "YBR 125","YR","YB"],
    "FZ150": ["FZ", "FZ150"],
    "FAZER250": ["FAZER", "FAZER250", "FAZER 250"],
    "XTZ250": ["XTZ", "XTZ250"],
    "MT-03": ["MT-03", "MT 03", "MT03", "MT", "MT3"],
    # HONDA
    "CBR250": ["CBR250"],
    "CBF150": ["CBF150"],
    "CG125": ["CG125"],
    "XR150": ["XR150"],
    "CB190": ["CB190"],
    # SUZUKI
    "GSX-R150": ["GSX-R150"],
    "GIXXERSF250": ["GIXXERSF250"],
    "V-STROM250": ["V-STROM250"],
    "GSX-S150": ["GSX-S150"],
    "INTRUDER250": ["INTRUDER250"],
    # TRIUMPH
    "STREET_TRIPLE_S": ["STREET_TRIPLE_S"],
    "BONNEVILLE_T100": ["BONNEVILLE_T100"],
    "SPEED_TRIPLE_R": ["SPEED_TRIPLE_R"],
    "TIGER_900_GT": ["TIGER_900_GT"],
    "ROCKET_3_GT": ["ROCKET_3_GT"],
    # ZANELLA
    "RX_150": ["RX_150"],
    "RX_200": ["RX_200"],
    "ZB_110": ["ZB_110"],
    "RX_250": ["RX_250"],
    "STYLER_CRUISER_150": ["STYLER_CRUISER_150"],
    # MOTOMEL
    "SKUA_150": ["SKUA_150"],
    "SKUA_250": ["SKUA_250"],
    "SIRIUS_200": ["SIRIUS_200"],
    "S2_250": ["S2_250"],
    "MAX_125_R": ["MAX_125_R"],
    # ZONTES
    "ZT_250_T": ["ZT_250_T"],
    "M_310": ["M_310"],
    "T_310": ["T_310"],
    "R_250": ["R_250"],
    "U_125": ["U_125"],
    # KAWASAKI
    "NINJA250": ["NINJA250"],
    "Z650": ["Z650"],
    "VERSYS-X300": ["VERSYS-X300"],
    # BMW
    "S1000RR": ["S1000RR"],
    "R1250GS": ["R1250GS"],
    "G310R": ["G310R"],
    # DUCATI
    "PANIGALE V2": ["PANIGALE V2"],
    "MONSTER": ["MONSTER"],
    "MULTISTRADA": ["MULTISTRADA"],
    # DUKE
    "DUKE_390": ["DUKE_390"],
    "DUKE_200": ["DUKE_200"],
    "DUKE_125": ["DUKE_125"],
    "RC_390": ["RC_390"],
    "RC_200": ["RC_200"]
}
