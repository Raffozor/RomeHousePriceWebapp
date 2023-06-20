import pandas as pd


def organize_data_collected(lat, lon, year, surface, floor, new, luxury, features, rooms, bathrooms, garage, typology,
                            condition):
    y_n_dict = {"Yes": 1, "No": 0}

    df = pd.DataFrame([[0, 0, 0, 0, 0]], columns=['Balcony', 'Terrace', 'Cellar', 'Swimming-pool', 'Garden'])

    for col in df:
        if col in features:
            df[col] = 1
        else:
            df[col] = 0

    df_rooms = pd.DataFrame([[0, 0, 0, 0, 0]], columns=["1", "2", "3", "4", "5"])

    for col in df_rooms:
        if col == rooms:
            df_rooms[col] = 1
        else:
            df_rooms[col] = 0

    df_bathrooms = pd.DataFrame([[0, 0, 0]], columns=["1", "2", "3"])

    for col in df_bathrooms:
        if col == bathrooms:
            df_bathrooms[col] = 1
        else:
            df_bathrooms[col] = 0

    df_garage = pd.DataFrame([[0, 0, 0, 0, 0]], columns=["0", "1", "2", "3", "4"])

    for col in df_garage:
        if col == garage:
            df_garage[col] = 1
        else:
            df_garage[col] = 0

    df_type = pd.DataFrame([[0, 0, 0, 0, 0, 0]],
                           columns=["Flat - Appartamento", "House - Casa indipendente", "Loft", "Penthouse - Attico",
                                    "Country house - Casale", "Villa"])

    for col in df_type:
        if col in typology:
            df_type[col] = 1
        else:
            df_type[col] = 0

    df_condition = pd.DataFrame([[0, 0, 0, 0]], columns=["Good - Buono/Abitabile", "To be renovated - Da ristrutturare",
                                                         "New/Under construction - Nuovo/In costruzione",
                                                         "Excellent/Renovated - Ottimo/Ristrutturato"])

    for col in df_condition:
        if col in condition:
            df_condition[col] = 1
        else:
            df_condition[col] = 0

    data = pd.DataFrame([[lat,
                          lon,
                          year,
                          surface,
                          floor,
                          y_n_dict[new],
                          y_n_dict[luxury],
                          df["Balcony"][0],
                          df["Terrace"][0],
                          df["Cellar"][0],
                          df["Swimming-pool"][0],
                          df["Garden"][0],
                          df_rooms["1"][0],
                          df_rooms["2"][0],
                          df_rooms["3"][0],
                          df_rooms["4"][0],
                          df_rooms["5"][0],
                          df_bathrooms["1"][0],
                          df_bathrooms["2"][0],
                          df_bathrooms["3"][0],
                          df_garage["0"][0],
                          df_garage["1"][0],
                          df_garage["2"][0],
                          df_garage["3"][0],
                          df_garage["4"][0],
                          df_type["Flat - Appartamento"][0],
                          df_type["House - Casa indipendente"][0],
                          df_type["Loft"][0],
                          df_type["Penthouse - Attico"][0],
                          df_type["Country house - Casale"][0],
                          df_type["Villa"][0],
                          df_condition["Good - Buono/Abitabile"][0],
                          df_condition["To be renovated - Da ristrutturare"][0],
                          df_condition["New/Under construction - Nuovo/In costruzione"][0],
                          df_condition["Excellent/Renovated - Ottimo/Ristrutturato"][0]]],
                        columns=["lat", "lon", "year", "surface", "floor", "new", "luxury", "balcony", "Terrace",
                                 "Cellar",
                                 "Swimming-pool", "Garden", "room1", "room2", "room3", "room4", "room5",
                                 "bathroom1", "bathroom2", "bathroom3", "garage0", "garage1", "garage2",
                                 "garage3", "garage4", "Flat", "House", "Loft", "Penthouse", "Country house", "Villa",
                                 "Good - Buono / Abitabile", "To be renovated - Da ristrutturare",
                                 "New/Under construction - Nuovo/In costruzione",
                                 "Excellent/Renovated - Ottimo/Ristrutturato"])
    return data
