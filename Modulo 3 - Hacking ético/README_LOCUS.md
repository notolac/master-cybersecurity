# README_LOCUS - Guia de uso de `locust.py`

Este documento explica como usar el archivo `locust.py` para hacer pruebas de carga de forma controlada y etica.

## 1) Que hace este script

El script define un usuario virtual (`WebsiteUser`) con dos tareas:

- `GET /` con peso `5` (mas frecuente)
- `GET /search?q=test` con peso `1` (menos frecuente)

Con esta configuracion, Locust ejecuta aproximadamente 5 peticiones al home por cada 1 peticion de busqueda.

## 2) Requisitos

- Python 3.8+ (recomendado)
- Permiso explicito para probar el objetivo (muy importante en hacking etico)

Instalacion de Locust:

```bash
pip install locust
```

Verificar instalacion:

```bash
locust --version
```

## 3) Ejecucion basica (interfaz web)

Desde la carpeta `Modulo 3 | Hacking ético`:

```bash
locust -f "locust.py" --host https://objetivo-autorizado.com
```

Luego abrir:

- `http://localhost:8089`

Parametros en la UI:

- **Number of users**: usuarios concurrentes a simular
- **Spawn rate**: velocidad de arranque (usuarios por segundo)
- **Run time** (opcional): duracion de la prueba

## 4) Ejecucion headless (sin UI)

Ideal para terminal, automatizacion o CI:

```bash
locust -f "locust.py" \
  --host https://objetivo-autorizado.com \
  --headless \
  -u 100 \
  -r 10 \
  -t 2m
```

Significado:

- `-u 100`: 100 usuarios maximos
- `-r 10`: arranque de 10 usuarios por segundo
- `-t 2m`: prueba de 2 minutos

## 5) Comandos conocidos y utiles

### Cambiar puerto web

```bash
locust -f "locust.py" --host https://objetivo-autorizado.com --web-port 8090
```

### Exportar metricas CSV

```bash
locust -f "locust.py" \
  --host https://objetivo-autorizado.com \
  --headless -u 50 -r 5 -t 1m \
  --csv reporte_locust
```

Genera archivos como:

- `reporte_locust_stats.csv`
- `reporte_locust_failures.csv`
- `reporte_locust_exceptions.csv`

### Generar reporte HTML

```bash
locust -f "locust.py" \
  --host https://objetivo-autorizado.com \
  --headless -u 50 -r 5 -t 1m \
  --html reporte_locust.html
```

### Ajustar nivel de logs

```bash
locust -f "locust.py" --host https://objetivo-autorizado.com --loglevel INFO
```

## 6) Casos de uso (hacking etico)

Usa Locust solo con autorizacion. Algunos escenarios legitimos:

1. **Prueba de estres gradual**
   - Subir carga por etapas para encontrar limites de capacidad.
2. **Deteccion de cuellos de botella**
   - Identificar endpoints lentos bajo concurrencia.
3. **Validacion de mitigaciones DoS (no destructivo)**
   - Comprobar rate limiting, WAF o autoscaling en ventanas controladas.
4. **Comparacion antes/despues**
   - Medir rendimiento antes y despues de cambios de infraestructura o codigo.
5. **Pruebas de resiliencia de busquedas**
   - Evaluar la estabilidad de rutas tipo `/search` con trafico sostenido.

## 7) Interpretacion rapida de resultados

En la UI de Locust enfocate en:

- **Failures**: errores HTTP o timeouts
- **Response time (p95/p99)**: latencia en percentiles altos
- **RPS**: peticiones por segundo sostenidas
- **Endpoint stats**: comparativa entre `/` y `/search`

Una señal de alerta comun:

- RPS estancado + p95 subiendo + fallos creciendo = posible saturacion.

## 8) Buenas practicas y limites eticos

- Ejecutar pruebas solo en entornos autorizados.
- Definir ventanas de prueba con el equipo responsable.
- Empezar con baja carga y escalar gradualmente.
- Evitar pruebas en horario critico de negocio.
- Documentar alcance, riesgo y resultados.

## 9) Comandos ejemplo por escenario

### Escenario A - Smoke test rapido

```bash
locust -f "locust.py" --host https://objetivo-autorizado.com --headless -u 10 -r 2 -t 1m
```

### Escenario B - Carga media sostenida

```bash
locust -f "locust.py" --host https://objetivo-autorizado.com --headless -u 100 -r 10 -t 10m
```

### Escenario C - Pico corto controlado

```bash
locust -f "locust.py" --host https://objetivo-autorizado.com --headless -u 300 -r 30 -t 2m
```

## 10) Nota final

`locust.py` es una base minima y didactica. Puedes extenderlo luego con:

- autenticacion (`on_start`)
- cabeceras personalizadas
- validaciones de respuesta
- mas tareas con pesos por comportamiento real de usuarios

