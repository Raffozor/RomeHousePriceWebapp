import pandas as pd
import numpy as np
import joblib
import sklearn
from xgboost import XGBRegressor


def organize_data_collected(lat, lon, year, surface, floor, new, luxury, features, rooms, bathrooms, garage, typology,
                            condition):
    encoding_diz = {'buildingYear': {1500.0: [1953206.896551724, 1906150.5782843065],
                                     1600.0: [1312510.2040816327, 1317075.8982567054],
                                     1700.0: [1281751.0416666667, 1412028.5176392687],
                                     1800.0: [1129454.5454545454, 1670420.2094296685],
                                     1890.0: [788386.3636363636, 718508.4426332836],
                                     1900.0: [880319.2307692308, 1073825.403910872],
                                     1920.0: [691836.2962962963, 536739.374983634],
                                     1925.0: [813800.0, 1067027.9727996085],
                                     1930.0: [560906.3670411985, 570286.337060168],
                                     1935.0: [296619.04761904763, 147438.9623506881],
                                     1939.0: [705416.6666666666, 1616908.5206917904],
                                     1940.0: [509944.18604651163, 527826.7063317036],
                                     1950.0: [422237.57223796035, 456024.22876318364],
                                     1952.0: [374045.45454545453, 316993.08649104147],
                                     1953.0: [538781.25, 762666.7870205137],
                                     1954.0: [399384.6153846154, 226937.69320937028],
                                     1955.0: [379876.92307692306, 281049.03025818075],
                                     1956.0: [408857.14285714284, 375294.05137838254],
                                     1957.0: [371649.1228070175, 309900.314688223],
                                     1958.0: [374101.2658227848, 507628.0082323738],
                                     1959.0: [362433.3333333333, 346889.9910765527],
                                     1960.0: [359641.27059436915, 364630.0916715881],
                                     1961.0: [500363.63636363635, 327675.3988614762],
                                     1962.0: [380673.07692307694, 209607.0499401568],
                                     1963.0: [421423.9130434783, 292819.7598004184],
                                     1964.0: [365860.4651162791, 219859.10797549668],
                                     1965.0: [335374.45652173914, 224075.31273786302],
                                     1966.0: [322005.6224489796, 243485.79440565073],
                                     1967.0: [328006.5789473684, 236545.50327916007],
                                     1968.0: [429671.4285714286, 283952.3408393244],
                                     1969.0: [392295.9183673469, 252235.00777976844],
                                     1970.0: [428993.0327868852, 456251.20590783434],
                                     1971.0: [442100.0, 202506.89396971936],
                                     1972.0: [472562.5, 256031.4159190235],
                                     1973.0: [524970.9302325582, 793094.3396439698],
                                     1974.0: [453571.4285714286, 203493.89869655232],
                                     1975.0: [451720.14925373136, 480940.1409895156],
                                     1977.0: [526480.0, 443334.34711663536],
                                     1978.0: [411771.9298245614, 243523.24746343595],
                                     1979.0: [479000.0, 442221.77694003267],
                                     1980.0: [389549.1712707182, 453692.8312458229],
                                     1982.0: [390875.0, 293899.4670616645],
                                     1984.0: [402692.3076923077, 179763.1818211436],
                                     1985.0: [357104.5918367347, 290433.5541667219],
                                     1986.0: [360322.5806451613, 244695.7821590957],
                                     1987.0: [330432.2916666667, 144700.53868457742],
                                     1988.0: [391950.0, 314742.5806993124],
                                     1990.0: [445834.6666666667, 882405.0869213254],
                                     1992.0: [353214.28571428574, 137985.60234686246],
                                     1994.0: [290904.7619047619, 110825.04444479359],
                                     1995.0: [392000.0, 150075.04295691047],
                                     2000.0: [355965.5172413793, 216951.47074306314],
                                     2002.0: [501000.0, 571343.292508748],
                                     2004.0: [445600.0, 232250.63594043578],
                                     2005.0: [372166.6666666667, 256773.49956975866],
                                     2007.0: [273923.07692307694, 133927.42006831104],
                                     2008.0: [285852.9411764706, 102494.08921699181],
                                     2009.0: [343965.5172413793, 162942.90909891037],
                                     2010.0: [437999.9811320755, 652063.2711159864],
                                     2011.0: [528234.0425531915, 1711991.6727342932],
                                     2012.0: [292611.0833333333, 206319.64318771768],
                                     2013.0: [293714.28571428574, 114256.9738994346],
                                     2014.0: [355852.9411764706, 427889.11990196863],
                                     2015.0: [355800.0, 180481.99833816648],
                                     2016.0: [310863.09523809527, 303368.3223931748],
                                     2017.0: [353963.63636363635, 581395.4465936805],
                                     2018.0: [365011.62790697673, 143112.7381261133],
                                     2019.0: [562902.4390243902, 582711.0799906781],
                                     2020.0: [524974.358974359, 533835.4017553926],
                                     2021.0: [391211.86440677964, 182671.1574205425],
                                     2022.0: [339396.57754010695, 215017.2710428593],
                                     2023.0: [408503.8022813688, 281034.9874730206],
                                     2024.0: [433522.22222222225, 306220.1807841816],
                                     0.0: [451263.70602571644, 559400.4868349863]},
                    'floor': {'1': [382085.0834392207, 289738.3171533722],
                              '2': [419868.1883597884, 420826.55145987],
                              '3': [441675.06337135617, 427696.58855075546],
                              '4': [474544.11937716266, 504231.4843793135],
                              '5': [546578.5184210526, 604374.5517264488],
                              '6': [533555.6, 917122.3746965826],
                              '7': [344762.24832214764, 211313.4854921008],
                              '8': [361795.0310559006, 383381.9752872523],
                              '9': [351758.6206896552, 182389.03772909116],
                              'Mezzanine floor - Piano Rialzato': [329468.58638743457, 297892.2417997918],
                              'Underground floor - Sottosuolo': [210131.914893617, 143331.2002023485],
                              'Ground floor - Piano terra': [321185.00211565587, 256107.89429065544],
                              'Other': [451263.70602571644, 559400.4868349863]}}

    if year in encoding_diz['buildingYear'].values():
        mu_year = encoding_diz['buildingYear'][year][0]
        sigma_year = encoding_diz['buildingYear'][year][1]
        rng = np.random.default_rng(seed=42)
        encoded_year = rng.normal(mu_year, sigma_year * 0.1, 1)[0]
    else:
        mu_year = encoding_diz['buildingYear'][0][0]
        sigma_year = encoding_diz['buildingYear'][0][1]
        rng = np.random.default_rng(seed=42)
        encoded_year = rng.normal(mu_year, sigma_year * 0.1, 1)[0]

    mu_floor = encoding_diz['floor'][floor][0]
    sigma_floor = encoding_diz['floor'][floor][1]
    rng = np.random.default_rng(seed=42)
    encoded_floor = rng.normal(mu_floor, sigma_floor * 0.1, 1)[0]

    y_n_dict = {"Yes": 1, "No": 0}

    df_features = pd.DataFrame([[0, 0, 0, 0, 0]], columns=['Balcony', 'Terrace', 'Cellar', 'Swimming-pool', 'Garden'])

    for col in df_features:
        if col in features:
            df_features[col] = 1
        else:
            df_features[col] = 0

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
                          encoded_year,
                          surface,
                          encoded_floor,
                          y_n_dict[new],
                          y_n_dict[luxury],
                          df_features["Balcony"][0],
                          df_features["Terrace"][0],
                          df_features["Cellar"][0],
                          df_features["Swimming-pool"][0],
                          df_features["Garden"][0],
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


def scaling_values(data_to_numpy):
    scaler = joblib.load('./model/scaler.save')
    data_to_numpy = data_to_numpy.to_numpy()
    scaled_values = scaler.transform(data_to_numpy)
    return scaled_values


def price_prediction(numpy_data):
    model = XGBRegressor()
    model.load_model('./model/xgb_model.json')
    price = model.predict(numpy_data)[0]
    price = '{:,.2f} €'.format(price).replace(',', '_').replace('.', ',').replace('_', '.')
    return price
