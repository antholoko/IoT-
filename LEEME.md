# Kit de agentes — Plataforma IoT SaaS

## Contenido
- `CLAUDE.md` — contexto del proyecto, reglas y flujo de trabajo (lo leen todos los agentes).
- `.claude/agents/`
  - `iot-dev.md` — desarrollo (Laravel, React, React Native, ingesta, reenvío, edge, LoRaWAN).
  - `qa-security.md` — pruebas, aislamiento entre organizaciones, auditoría OWASP.
  - `devops.md` — Docker, CI/CD, EMQX, ChirpStack, TimescaleDB, staging y runbooks.
  - `ux-designer.md` — flujos, prototipos, sistema de diseño, revisión de usabilidad y accesibilidad.
  - `docs-writer.md` — documentación técnica y manuales de usuario con diagramas, capturas y gráficas.
- `.claude/skills/`
  - `ux-heuristic-review`, `ux-iot-dashboards`, `ux-writing-es`, `user-manual`.

## Cómo usarlo
1. Crea el repositorio del proyecto y copia este contenido en su raíz (incluida la carpeta oculta `.claude`).
2. Abre Claude Code en esa carpeta.
3. Empieza por la fase 0, por ejemplo:
   > Inicia la Fase 0: estructura del repo, docker-compose de desarrollo, CI y simulador de dispositivos. Coordina a los agentes según CLAUDE.md.
4. Claude principal reparte el trabajo entre los agentes; tú revisas los PR y apruebas el paso a producción.

Los agentes trabajan mientras haya una sesión abierta y solo con los accesos que tú configures.
