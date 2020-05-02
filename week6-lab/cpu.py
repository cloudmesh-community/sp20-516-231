import platform
import re
import subprocess

from flask import jsonify

from cpuinfo import get_cpu_info

def get_processor_name() -> str:
    """
    The name of the processor

    :return: the name of the processor
    """
    #if platform.system() == "Windows":
    #    p = platform.processor()
    #elif platform.system() == "Darwin":
    #    command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
    #    p = subprocess.check_output(command, shell=True).strip().decode()
    #elif platform.system() == "Linux":
    #    command = "cat /proc/cpuinfo"
    #    all_info = subprocess.check_output(command, shell=True).strip().decode()
    #    for line in all_info.split("\n"):
    #        if "model name" in line:
    #            p = re.sub(".*model name.*:", "", line, 1)
    #else:
    #    p = "cannot find cpuinfo"
    
    i = get_cpu_info()
    p = i['brand']

    pinfo = {"model": p}

    return jsonify(pinfo)

def get_cache_size(level: str='') -> str:
    """
    The cache size of the processor

    :return: the cache size
    """

    i = get_cpu_info()
    l2 = i['l2_cache_size']
    l3 = i['l3_cache_size']
    if level == 'l2':
        cinfo = {level: l2}
    elif level == 'l3':
        cinfo = {level: l3}
    else:
        cinfo = {
                 'caches': {
                   'l3': l3,
                   'l2': l2
                   }
                 }
    return jsonify(cinfo)
                   
