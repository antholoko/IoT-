-- Esquema inicial de telemetría (Fase 0). Las tablas de negocio las crean las migraciones de Laravel en la Fase 1.
CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE IF NOT EXISTS telemetry (
    time        TIMESTAMPTZ      NOT NULL,
    org_id      BIGINT           NOT NULL,
    device_id   TEXT             NOT NULL,
    variable    TEXT             NOT NULL,
    value       DOUBLE PRECISION,
    quality     SMALLINT         NOT NULL DEFAULT 0  -- 0 ok, 1 fuera de rango, 2 inválido
);

SELECT create_hypertable('telemetry', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS telemetry_org_device_time_idx
    ON telemetry (org_id, device_id, variable, time DESC);

ALTER TABLE telemetry SET (
    timescaledb.compress,
    timescaledb.compress_segmentby = 'org_id, device_id, variable'
);
SELECT add_compression_policy('telemetry', INTERVAL '7 days', if_not_exists => TRUE);
