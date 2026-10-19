# Plataforma IoT SaaS — Contexto del proyecto

Plataforma IoT multi-tenant (freemium) para monitoreo de dispositivos Modbus, LoRaWAN y MQTT:
dashboards, almacenamiento de series de tiempo, alertas y notificaciones personalizadas.

## Arquitectura (resumen)

- **Campo**: equipos Modbus → agente edge (Python/Go) → MQTT/TLS · nodos LoRaWAN → gateway Milesight UG67 → ChirpStack v4 → MQTT · dispositivos MQTT directos.
- **Ingreso de terceros**: gateways externos entran por MQTT directo, HTTP ingest API (API key por gateway) o apuntando a nuestro ChirpStack (Basic Station / UDP) en fase 1; Network Servers externos (TTN, otro ChirpStack) y bridge suscrito al broker del cliente en fase 2. Gateway = dispositivo padre con hijos; equipos nuevos quedan en bandeja "detectados" hasta aprobación. Mapeo de payload por plantillas (Milesight, Dragino, Teltonika, JSON genérico) o editor de campos. Todo ingreso converge al mismo flujo interno.
- **Broker**: EMQX con TLS, credencial única por dispositivo y ACL por prefijo `t/{org_id}/{device_id}/...`.
- **Procesamiento**: worker de ingesta (Go o Node.js) + Redis Streams → decodifica, normaliza, mide uso, evalúa reglas.
- **Datos**: PostgreSQL + TimescaleDB (hypertable `telemetry`, continuous aggregates 5 min / 1 h, compresión > 7 días, retención por plan).
- **Aplicación**: Laravel 12 (API REST, Sanctum, Horizon, Reverb) + React/TypeScript (dashboards con ECharts) + React Native (móvil).
- **Reenvío de datos ("servidor de repetición")**: servicio forwarder separado que consume un stream de reenvío y entrega a destinos externos del cliente (webhook HTTPS con firma HMAC en fase 1; broker MQTT externo en fase 2; AWS IoT, Azure IoT Hub y bases externas en fase 3). Filtros por dispositivo/variable, plantillas de payload, reintentos con backoff, cola persistente por destino, dead-letter, pausa automática, métricas por destino, credenciales cifradas y bloqueo de SSRF. Un destino caído nunca frena la ingesta.
- **Notificaciones**: correo (Resend/SES), SMS/WhatsApp (Twilio, solo planes pagados), push (FCM).
- **Infra**: Docker Compose (dev/MVP) → k3s/Kubernetes. Observabilidad interna: Prometheus, Grafana, Loki.
- Node-RED y Grafana son solo herramientas internas; el cliente nunca accede a ellos.

## Estructura de repositorio esperada

```
/backend        Laravel (API, admin, facturación, colas)
/frontend       React + TypeScript (web)
/mobile         React Native
/ingest         Worker de ingesta y motor de alertas
/forwarder      Servicio de reenvío de datos a servidores externos
/edge           Agente edge Modbus → MQTT
/infra          docker-compose, configs EMQX/ChirpStack/Timescale, CI/CD, runbooks
/tests          integración, carga, seguridad, simulador de dispositivos
/docs           ADRs y documentación
```

## Reglas no negociables

1. **Multi-tenancy**: toda tabla de negocio lleva `org_id`; todo query pasa por global scope; todo tópico MQTT empieza por `t/{org_id}/`.
2. **Test de aislamiento** entre organizaciones (API, MQTT, WebSocket) obligatorio en CI; si falla, no se mergea.
3. **Secretos** nunca en el repo; usar `.env` (no versionado) o vault.
4. **Límites por plan** aplicados en broker y API, no solo en la UI.
5. Toda tarea termina con tests; ningún PR sin pasar CI.
6. **Producción**: ningún agente aplica cambios en producción sin aprobación explícita del humano.

## Flujo de trabajo con agentes

1. El agente principal toma una historia del roadmap, la divide y la asigna.
2. Si la historia tiene interfaz, `ux-designer` entrega flujo, prototipo y estados antes de implementar.
3. `iot-dev` implementa en una rama `feat/...` con tests.
4. `qa-security` revisa, ejecuta pruebas (unitarias, integración, aislamiento, carga, OWASP) y reporta; `ux-designer` revisa usabilidad y accesibilidad de lo construido.
5. Si hay hallazgos, vuelven a `iot-dev`. Si está limpio, `devops` despliega a staging y verifica salud.
6. `docs-writer` actualiza la documentación técnica y el manual de usuario (con capturas desde staging) y las notas de versión.
7. El humano revisa el PR y aprueba el paso a producción.

## Skills del proyecto (`.claude/skills`)

- `ux-heuristic-review` — revisión de usabilidad (Nielsen) y accesibilidad (WCAG 2.2 AA).
- `ux-iot-dashboards` — patrones de dashboards y alarmas IoT/industriales.
- `ux-writing-es` — textos de interfaz, errores y correos de alerta en español.
- `user-manual` — plantilla de manuales con capturas anotadas, diagramas y gráficas.

## Roadmap

- **Fase 0 · Bases**: repo, CI/CD, Docker Compose dev, simulador de dispositivos. Gate: CI y tests verdes.
- **Fase 1 · MVP**: EMQX + ChirpStack, orgs y dispositivos, ingesta a Timescale, dashboard básico, alertas por correo, reenvío por webhook HTTPS, ingreso de gateways de terceros por MQTT/HTTP. Gate: piloto validado.
- **Fase 2 · Monetizar**: planes y límites, pagos recurrentes (Flow/Mercado Pago/Stripe), plantillas de correo, app móvil con push. Gate: pentest aprobado.
- **Fase 3 · Escalar**: SMS/WhatsApp, API pública, agente edge empaquetado, cluster EMQX, reglas combinadas.

## Uso eficiente (ahorro)

- Sesión principal en Sonnet; usa Opus solo para decisiones de arquitectura (`/model opus` y vuelve).
- Cada agente carga solo sus skills y herramientas; Playwright MCP solo existe dentro de `ux-designer`.
- Sin WebSearch; para documentación externa usa WebFetch con la URL oficial.
- No leas `node_modules`, `vendor` ni logs; busca con Grep antes de abrir archivos grandes.
- Tareas pequeñas y concretas por historia; usa `/compact` al cerrar cada historia y `/clear` al cambiar de tema.
- En GitHub, `@claude` corre con Sonnet, máximo 40 turnos y 30 minutos.

## Idioma

Código, nombres de variables y commits en inglés; documentación y comunicación con el usuario en español.
