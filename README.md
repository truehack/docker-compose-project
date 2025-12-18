# docker-compose-project
```
┌─────────────┐     HTTP/80     ┌─────────────┐     Redis     ┌─────────────┐
│   Frontend  │◄───────────────►│   Backend   │◄─────────────►│   Redis     │
│   (Nginx)   │   API прокси    │   (Flask)   │    Port 6379  │   Database  │
└─────────────┘                 └─────────────┘               └─────────────┘
       ▲                                                            │
       │ HTTP/80                                                    │ Volume
       ▼                                                            ▼
┌─────────────┐                                              ┌─────────────┐
│ Пользователь │                                              │ Данные Redis│
│  (Браузер)   │                                              │ сохраняются │
└─────────────┘                                              └─────────────┘

```

Технологии
Frontend: Nginx + HTML/CSS/JS (порт 80)

Backend: Flask REST API (порт 5000)

Database: Redis с persistent volume (порт 6379)

Orchestration: Docker Compose с сетями и health checks
```
Инструкция по запуску
1.Склонировать репозиторий:https://github.com/truehack/docker-compose-project.git
2.Перейти в проект: cd docker-compose-project
3.Запуск одной командой: docker-compose up --build -d
```
