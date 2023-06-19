import os
import subprocess
import main
import streamlit as st
import ruamel.yaml

CONFIG_FNAME = "config.yml"
CONFIG_PATH = os.path.join(os.path.dirname(__file__), CONFIG_FNAME)
COINS = ("BTCUSDT", "ETHUSDT", "ADAUSDT")
STRATEGIES = ["EMA", "GRID"]


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        config = ruamel.yaml.safe_load(f)

    return config


def dump_config(config: dict) -> None:
    with open(CONFIG_PATH, 'w') as f:
        ruamel.yaml.dump(config, f, Dumper=ruamel.yaml.RoundTripDumper, indent=2, default_flow_style=False)


def data_from_web_form() -> dict:
    traiding_data = {}

    st.title("Trading Bot")
    traiding_data['coin'] = st.radio('Выберите пару для торговли: ', COINS)

    level = st.slider("Выберите плечо", 1, 20)
    st.text('Плечо: {}'.format(level))
    traiding_data['leverage'] = level

    traiding_data['stop'] = st.number_input("Какой будет стоп:")
    traiding_data['take'] = st.number_input("Какой будет тейк:")

    traiding_data['traide_type'] = st.radio("Стратегия", STRATEGIES)

    return traiding_data

def run_main():
    MAIN_NAME = "main.py"
    MAIN_RUN = os.path.join(os.path.dirname(os.path.abspath(__file__)), MAIN_NAME)
    
    subprocess.run(["python", MAIN_RUN])

def main() -> None:
    config = load_config()
    traiding_data = data_from_web_form()

    if st.button("Сохранить"):
        config["traiding"].update(traiding_data)
        dump_config(config)
        st.write("Конфигурация сохранена")
    
    if st.button("Run Main"):
        run_main()


if __name__ == "__main__":
    main()
