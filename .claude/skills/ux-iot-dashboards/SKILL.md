---
name: ux-iot-dashboards
description: "Patrones de dashboards y alarmas IoT/industriales (estilo ISA-101) para diseñar o revisar vistas de monitoreo."
---

# Dashboards IoT — patrones

## Principios
- **Gris por defecto, color para lo anormal**: la pantalla en operación normal es neutra; el color se reserva para alarmas y estados que requieren acción. Un dashboard multicolor esconde la alarma.
- **Contexto antes que número**: todo valor muestra unidad, rango normal y tendencia reciente (sparkline). "7,2" no dice nada; "7,2 pH · normal 6,5–8,5 · ↗" sí.
- **Frescura del dato siempre visible**: hora del último dato y marca de "desactualizado" si supera 2× el intervalo esperado. Un dato viejo nunca debe verse igual que uno en vivo.
- **Jerarquía de 3 niveles**: resumen de la organización → sitio → dispositivo con detalle e historial.

## Colores de estado (tokens)
| Estado | Uso | Además del color |
| --- | --- | --- |
| Crítico | Alarma activa sin reconocer | Icono + parpadeo suave solo si no está reconocida |
| Advertencia | Fuera de rango leve | Icono |
| Sin datos / desconectado | Dispositivo offline o dato vencido | Icono + texto "sin datos desde …" |
| Normal | Operación normal | Neutro, sin color de énfasis |
| Mantenimiento | Silenciado por el usuario | Icono + texto |

## Widgets recomendados
- Valor actual con rango y tendencia (KPI).
- Serie de tiempo con bandas de umbral y marcadores de alarmas; selector de rango (1 h, 24 h, 7 d, 30 d, personalizado) limitado por la retención del plan.
- Estado de flota: grilla de dispositivos con estado y último dato, ordenable por severidad.
- Mapa de sitios con estado agregado.
- Lista de alarmas: activas primero, por severidad y antigüedad; reconocer en un toque.
- Evitar gauges circulares grandes salvo un indicador principal; usar barras con rango.

## Alarmas
- Cada alarma dice qué, dónde, desde cuándo y qué hacer.
- Reconocer ≠ resolver: se muestran distinto.
- Agrupar repeticiones; nunca más de una notificación por regla dentro del cooldown.

## Móvil
- Primera pantalla: alarmas activas y dispositivos con problema; los dashboards completos van después.
- Gráficos con zoom táctil y valor al tocar; nada que dependa de hover.

## Planes
- Mostrar el uso del plan (dispositivos, retención, alertas) en la configuración, con aviso al 80 %.
- Funciones premium visibles pero marcadas, con explicación del beneficio; nunca rotas o vacías.
