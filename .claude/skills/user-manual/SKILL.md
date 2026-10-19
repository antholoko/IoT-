---
name: user-manual
description: "Plantilla y proceso para manuales de usuario con capturas anotadas, diagramas Mermaid y gráficas."
---

# Manual de usuario

## Estructura de cada capítulo
```markdown
# <Tarea en infinitivo> (ej. "Conectar un gateway LoRaWAN")

> Para quién · Tiempo estimado · Plan requerido

## Antes de empezar
- Requisitos (equipo, credenciales, permisos)

## Cómo funciona
<diagrama Mermaid de 3–6 nodos>

## Pasos
1. **Acción.** Resultado esperado.
   ![Texto alternativo](img/<capitulo>-01.png)
...

## Verificar que funciona
## Problemas frecuentes
| Síntoma | Causa probable | Solución |
## Siguiente paso
```

## Capturas
1. Escribe o actualiza el escenario en `/docs/scripts/screenshots/<capitulo>.spec.ts` (Playwright) contra staging con la organización de demostración.
2. Resolución 1440×900 en escritorio y 390×844 en móvil; tema claro.
3. Anotar con números circulares en el orden de los pasos y un recuadro en el elemento clave (script de anotación con sharp o Pillow).
4. Nombre: `<capitulo>-<paso>.png`; regenerar todas antes de cada release.

## Diagramas
- Mermaid: `flowchart LR` para flujos, `sequenceDiagram` para integraciones (gateway → broker → plataforma), máximo ~8 nodos.
- Etiquetas en el idioma del usuario, nunca nombres de servicios internos en el manual de usuario final.

## Gráficas
- Generadas por script desde datos del simulador (`/docs/scripts/charts`), en SVG.
- Cada gráfica tiene título que diga la conclusión y una frase debajo que explique qué mirar.

## Checklist antes de publicar
- [ ] Procedimiento ejecutado de punta a punta en staging
- [ ] Capturas actuales y sin datos reales
- [ ] Textos revisados con `ux-writing-es`
- [ ] Enlaces y comandos probados
- [ ] Exportación a PDF revisada
