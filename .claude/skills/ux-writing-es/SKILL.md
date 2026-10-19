---
name: ux-writing-es
description: "Textos de interfaz en español (botones, errores, estados vacíos, avisos de plan, correos y push de alerta)."
---

# UX writing en español

## Tono
- Claro, directo y cercano; trato de "tú" en la app (configurable a "usted" para clientes empresa si lo piden).
- Frases cortas, voz activa, verbos concretos. Sin jerga interna ni anglicismos innecesarios ("payload" → "datos del mensaje").
- Términos únicos en todo el producto: dispositivo, gateway, sitio, variable, alerta, regla, reenvío, organización.

## Patrones
| Elemento | Regla | Ejemplo |
| --- | --- | --- |
| Botón | Verbo + objeto | "Agregar dispositivo", no "Aceptar" |
| Error | Qué pasó + qué hacer | "No pudimos conectar con el gateway. Revisa que tenga internet e inténtalo de nuevo." |
| Estado vacío | Qué falta + primera acción | "Aún no tienes dispositivos. Conecta el primero en 5 minutos." |
| Confirmación destructiva | Consecuencia explícita | "Se eliminarán el dispositivo y 30 días de datos. Esta acción no se puede deshacer." |
| Éxito | Breve, sin exclamaciones repetidas | "Regla guardada." |
| Límite de plan | Hecho + opción, sin culpa | "Usas 3 de 3 dispositivos del plan Free. Mejora tu plan para agregar más." |

## Alertas por correo, push y SMS
- Asunto o primera línea: severidad + qué + dónde. "Crítica · Nivel bajo en Estanque 2 (Planta Norte)".
- Cuerpo: valor actual, umbral, desde cuándo, enlace directo a la vista del dispositivo, cómo silenciar.
- SMS ≤ 160 caracteres; push ≤ 2 líneas.

## Formatos
- Números con coma decimal y punto de miles (7,2 · 1.250) según la configuración regional de la organización.
- Fechas "19 oct 2026, 09:38"; zona horaria de la organización, indicada si difiere de la del usuario.
- Unidades con espacio: "25 °C", "3,4 bar".
