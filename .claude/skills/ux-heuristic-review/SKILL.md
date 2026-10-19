---
name: ux-heuristic-review
description: "Revisión de usabilidad (heurísticas de Nielsen) y accesibilidad WCAG 2.2 AA de pantallas web y móvil."
---

# Revisión heurística UX

## Proceso
1. Identifica el flujo y el objetivo del usuario (ej. "conectar un gateway Milesight").
2. Recorre el flujo completo en el prototipo o en staging (Playwright si es web), tomando captura de cada paso.
3. Evalúa cada heurística y la lista de accesibilidad.
4. Registra hallazgos en `/docs/ux/revisiones/<fecha>-<flujo>.md` con el formato de la tabla.

## Heurísticas (Nielsen)
1. Visibilidad del estado del sistema: ¿se ve si un dispositivo está en línea, cuándo llegó el último dato, si una acción se guardó?
2. Coincidencia con el mundo real: términos del usuario ("sensor", "equipo"), no internos ("device_id", "payload").
3. Control y libertad: deshacer, cancelar, volver sin perder lo escrito.
4. Consistencia y estándares: mismos nombres, iconos y colores en web y móvil.
5. Prevención de errores: validar antes de enviar, confirmar acciones destructivas, valores por defecto seguros.
6. Reconocer antes que recordar: mostrar opciones, ejemplos y valores recientes.
7. Flexibilidad y eficiencia: atajos y acciones masivas para usuarios con muchos dispositivos.
8. Diseño estético y minimalista: cada elemento debe ayudar a decidir o actuar.
9. Ayudar a reconocer y recuperarse de errores: qué pasó, por qué y qué hacer, en lenguaje simple.
10. Ayuda y documentación: ayuda contextual enlazada al manual.

## Accesibilidad (WCAG 2.2 AA)
- Contraste de texto ≥ 4.5:1 (3:1 para texto grande y elementos gráficos).
- Navegación completa por teclado, foco visible, orden lógico.
- El color nunca es el único indicador de estado (agregar icono o texto).
- Etiquetas en todos los campos; gráficos con resumen textual.
- Objetivos táctiles ≥ 24×24 px (recomendado 44×44 en móvil).
- Ejecutar axe-core y adjuntar el resultado.

## Formato de hallazgos
| # | Pantalla | Heurística / criterio | Problema | Severidad (0–4) | Recomendación |
| --- | --- | --- | --- | --- | --- |

Severidad: 0 no es problema · 1 cosmético · 2 menor · 3 mayor · 4 catastrófico (bloquea la tarea). Los de severidad 3–4 bloquean el release.
