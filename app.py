#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import subprocess
import ruamel.yaml
import os

def main():
    
    # загрузка данных из файла    
    config_path = os.path.join(os.path.dirname(__file__), 'config.yml')
    with open(config_path) as f:
        data = ruamel.yaml.safe_load(f)
    
#Выбор пары для торговли   
    st.title("Trading Bot")
    status = st.radio('Выберите пару для торговли: ',
                  ('BTCUSDT', 'ETHUSDT', 'ADAUSDT'))
    
    if(status == 'BTCUSDT'):
        data['coin'] = 'BTCUSDT'
    
    elif(status == 'ETHUSDT'):
        data['coin'] = 'ETHUSDT'
        
    elif(status == 'ADAUSDT'):
        data['coin'] = 'ADAUSDT'
        
#Выбор кредитного плеча
    level = st.slider("Выберите плечо", 1, 20)
    st.text('Плечо: {}'.format(level))
    data['leverage'] = level


#Определение риска/прибыли
    stop = st.number_input("Какой будет стоп:")
    data['stop'] = stop
    take = st.number_input("Какой будет тейк:")
    data['take'] = take
    
#Выбор стратегии для торговли
    buttonEMA = st.button("EMA")
    buttonGRID = st.button("GRID")

    if buttonEMA:
        st.write("Вы выбрали стратегию EMA")
        data['traide_type'] = 'EMA'
    elif buttonGRID:
        st.write("Вы выбрали стратегию GRID")
        data['traide_type'] = 'GRID'
        
    with open(config_path, 'w') as f:
        ruamel.yaml.dump(data, f, Dumper=ruamel.yaml.RoundTripDumper, indent=2, default_flow_style=False)
        
#    if st.button('Run Other Module'):
#        subprocess.run(['python', 'main.py'])
                
if __name__ == "__main__":
    main()
        




