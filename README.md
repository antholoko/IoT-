# Plataforma IoT SaaS

Plataforma multi-tenant para monitoreo de dispositivos Modbus, LoRaWAN y MQTT: dashboards, series de tiempo, alertas, notificaciones, ingreso de gateways de terceros y reenvío de datos a servidores externos.

Arquitectura, reglas y roadmap: [CLAUDE.md](CLAUDE.md). Agentes y skills: [LEEME.md](LEEME.md).

## Estado

**Fase 0 · Bases** — en curso.

## Desarrollo local

Requisitos: Docker y Python 3.12.

```bash
cp infra/.env.example infra/.env          # y cambia las contraseñas
docker compose -f infra/docker-compose.yml up -d --wait

pip install -r tests/simulator/requirements.txt
python tests/simulator/simulator.py --devices 5 --interval 5
```

| Servicio | Dirección local |
| --- | --- |
| MQTT (EMQX) | `localhost:1883` |
| Dashboard EMQX | http://localhost:18083 |
| PostgreSQL + TimescaleDB | `localhost:5432` |
| Redis | `localhost:6379` |

## Trabajar con los agentes

- **Local**: abre Claude Code en la raíz del repo; lee `CLAUDE.md` y los agentes de `.claude/agents` automáticamente.
- **GitHub**: escribe `@claude` en un issue o PR. Requiere la app de Claude instalada en el repo y el secreto `CLAUDE_CODE_OAUTH_TOKEN` (generado con `claude setup-token`).
