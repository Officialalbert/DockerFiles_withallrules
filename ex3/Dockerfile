FROM golang:1.26 AS builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

#copy from builder (multi-stage)
FROM alpine:latest

RUN apk add --no-cache curl

RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

COPY --from=builder /app/main .

RUN chown appuser:appuser /app/main && chmod +x /app/main

USER appuser

HEALTHCHECK --interval=30s --timeout=3s \
 CMD curl -f http://localhost:8080/health || exit 1 # exit 1 = unhealthy

CMD ["./main"]
