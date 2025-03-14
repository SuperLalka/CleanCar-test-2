<!-- PROJECT LOGO -->
<div align="center">
  <h2>CleanCar-test-2</h2>

  <h3 align="center">README тестового задания</h3>

  <p align="center">
    React-приложение, которое позволяет загружать фото и следить
    за прогрессом загрузки в реальном времени через WebSockets.
  </p>
</div>

<a name="readme-top"></a>

<hr>

<!-- ABOUT THE PROJECT -->
## About The Project

Требования:

1. Загрузка фото через drag & drop (React).
2. Показ прогресса загрузки в реальном времени.
3. WebSockets: после загрузки приходит статус обработки.
4. Сохранение файлов в S3 (Minio).
5. Отображение загруженных фото в галерее.

Требуемый стек технологий:

* React + TypeScript – (фронтенд).
* Django + DRF – (бэкенд).
* Django Channels (WebSockets).
* S3 (Minio) – хранение файлов.
* React Query + Zustand – управление состоянием.
* Jest + Testing Library – (тесты фронта).
* Pytest + Factory Boy – (тесты бэка).


### Built With

* [![React][React-badge]][React-url]
* [![Django][Django-badge]][Django-url]
* [![Postgres][Postgres-badge]][Postgres-url]
* [![Celery][Celery-badge]][Celery-url]
* [![Redis][Redis-badge]][Redis-url]
* [![Minio][Minio-badge]][Minio-url]
* [![Docker][Docker-badge]][Docker-url]


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Скопировать проект в репозиторий на локальной машине (HTTPS или SSH)
  ```sh
  git clone https://github.com/SuperLalka/CleanCar-test-2.git
  ```
  ```sh
  git clone git@github.com:SuperLalka/CleanCar-test-2.git
  ```

### Installation

Для запуска проекта достаточно собрать и запустить контейнеры Docker.

```sh
docker-compose -f docker-compose.yml up -d --build
```

Запуск тестов:

```sh
sh start_tests.sh
```


### Documentation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[React-badge]: https://img.shields.io/badge/react-%2361DAFB.svg?style=for-the-badge&logo=react&logoColor=white
[React-url]: https://react.dev/
[Django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/
[Postgres-badge]: https://img.shields.io/badge/postgresql-%234169E1.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Celery-badge]: https://img.shields.io/badge/celery-%2337814A.svg?style=for-the-badge&logo=celery&logoColor=white
[Celery-url]: https://docs.celeryq.dev/
[Redis-badge]: https://img.shields.io/badge/redis-%23FF4438.svg?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
[Minio-badge]: https://img.shields.io/badge/minio-%23C72E49.svg?style=for-the-badge&logo=minio&logoColor=white
[Minio-url]: https://min.io/
[Docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
