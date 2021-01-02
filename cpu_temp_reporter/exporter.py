from prometheus_client import Gauge, start_http_server

cpu_temp_gauge = Gauge("cpu_temp", "CPU Temperature in Celsius")


@cpu_temp_gauge.time()
def get_cpu_temp():
    """Get the temperature of the CPU as reported by the Linux Kernel.

    Data is pulled from /sys/class/thermal/thermal_zone0/temp
    """
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as fp:
        str_temp = fp.readline().strip()
    temp_in_c = round(float(str_temp / 100), 4)
    cpu_temp_gauge.set(temp_in_c)


if __name__ == '__main__':
    start_http_server(8000)
    while True:
        get_cpu_temp()
