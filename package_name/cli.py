from module import print_hello

try:
    from jsonargparse import CLI
except Exception as e:
    "To use this you need to install jsonargparse first! See https://jsonargparse.readthedocs.io/en/latest/#"
    exit()


def weather_forecast(temperature: float) -> None:
    """
    Print the weather forecast after a greeting.

    :param temperature: Measure in Celsius degrees of how warm is it today
    :return: None
    """
    print_hello()
    print(f"Hoy hace un maravilloso dia con una tempratura de {temperature} grados")


if __name__ == "__main__":
    CLI(weather_forecast, dump_header=['TOMCAT Gigafrost Reconstruction Tool'],
        epilog='Created with \u2764\ufe0f  by Dani')
