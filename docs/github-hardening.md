# Controles de seguridad de GitHub

Fecha: 2026-11-14

Registro del endurecimiento aprobado frente a robo de credenciales e inyección CI. No acredita que una cuenta haya sido comprometida. Los cambios conservan el runtime de la aplicación.

## Cambios de servidor verificados

- Actions: habilitado → deshabilitado. No hay workflows; se elimina la ejecución de workflows que pudieran añadirse mediante una credencial robada. Verificado con GET actions/permissions.
- Rama principal: sin protección → PR obligatoria, reglas aplicadas al administrador, historial lineal, conversaciones resueltas y bloqueo de force-push/borrado. Cero aprobaciones obligatorias evita bloquear al propietario único; aporta trazabilidad, no revisión independiente. Verificado con GET de protección.

## Cambios de workflows y verificación

No se añaden workflows, dependencias ni código de aplicación. La validación consiste en lectura posterior de API y comprobación de documentación.

## Límites y reversión

Las credenciales con escritura, el acceso administrativo y las integraciones de producción requieren revisión independiente. Rehabilitar Actions exige revisar las ramas y justificar CI. Restaurar controles anteriores requiere un cambio aprobado; el código se revierte mediante PR, sin reescribir historial.

[Política y registro central de auditoría](https://github.com/notolac/home-lab/blob/main/_shared/orquestacion/github-hardening.md).
