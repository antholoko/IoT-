"""Simulador de dispositivos IoT para desarrollo y pruebas de carga.

Publica telemetría JSON en t/{org_id}/{device_id}/up y estado en t/{org_id}/{device_id}/status.

Ejemplos:
    python simulator.py --devices 5 --interval 10
    python simulator.py --org 2 --devices 100 --interval 1 --duration 300
"""

import argparse
import json
import math
import random
import signal
import sys
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

VARIABLES = {
    # nombre: (base, amplitud, ruido, unidad)
    "temperatura": (22.0, 4.0, 0.3, "°C"),
    "presion": (3.2, 0.4, 0.05, "bar"),
    "nivel": (65.0, 20.0, 1.0, "%"),
    "ph": (7.2, 0.4, 0.05, "pH"),
}


def build_payload(device_index: int, t: float) -> dict:
    """Valores con ciclo diario simulado, ruido y un fuera de rango ocasional."""
    values = {}
    for i, (name, (base, amp, noise, _unit)) in enumerate(VARIABLES.items()):
        phase = device_index * 0.7 + i
        value = base + amp * math.sin(t / 600 + phase) + random.gauss(0, noise)
        if random.random() < 0.01:  # 1 % de lecturas anómalas para probar alertas
            value *= 1.8
        values[name] = round(value, 3)
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "values": values,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulador de dispositivos MQTT")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=1883)
    parser.add_argument("--org", type=int, default=1, help="org_id de los dispositivos")
    parser.add_argument("--devices", type=int, default=3)
    parser.add_argument("--interval", type=float, default=5.0, help="segundos entre envíos por dispositivo")
    parser.add_argument("--duration", type=float, default=0, help="segundos totales; 0 = sin límite")
    parser.add_argument("--username", default=None)
    parser.add_argument("--password", default=None)
    args = parser.parse_args()

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"simulator-org{args.org}")
    if args.username:
        client.username_pw_set(args.username, args.password)

    # Una sola conexión para todos los dispositivos simulados; en la Fase 1 cada uno
    # tendrá su propia credencial y LWT para probar las ACL por dispositivo.
    device_ids = [f"sim-{args.org}-{n:04d}" for n in range(args.devices)]

    client.connect(args.host, args.port, keepalive=30)
    client.loop_start()

    running = True

    def stop(*_):
        nonlocal running
        running = False

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)

    for device_id in device_ids:
        client.publish(f"t/{args.org}/{device_id}/status", "online", qos=1, retain=True)

    start = time.time()
    sent = 0
    while running:
        cycle_start = time.time()
        for index, device_id in enumerate(device_ids):
            payload = build_payload(index, cycle_start)
            client.publish(f"t/{args.org}/{device_id}/up", json.dumps(payload), qos=1)
            sent += 1
        if args.duration and time.time() - start >= args.duration:
            break
        time.sleep(max(0.0, args.interval - (time.time() - cycle_start)))

    for device_id in device_ids:
        client.publish(f"t/{args.org}/{device_id}/status", "offline", qos=1, retain=True)
    client.loop_stop()
    client.disconnect()
    print(f"Mensajes enviados: {sent}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
