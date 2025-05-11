# Stage 0: Base Python image
FROM python:3.12.2-slim-bookworm as base

# Stage 1: Build dependencies (wheel)
FROM base as build

ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY ./requirements ./

RUN pip wheel --wheel-dir /wheels -r ${BUILD_ENVIRONMENT}.txt

# Stage 2: Final run image
FROM base as final

ARG BUILD_ENVIRONMENT=local
ENV BUILD_ENV ${BUILD_ENVIRONMENT}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# نصب پکیج‌های مورد نیاز سیستم
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    sudo \
    git \
    nano \
    bash-completion \
    ssh \
 && rm -rf /var/lib/apt/lists/*

# ساخت یوزر django
# RUN addgroup --system django && adduser --system --ingroup django django

# # ساخت فولدر staticfiles و تنظیم دسترسی
# RUN mkdir -p ${APP_HOME}/staticfiles/admin/css \
#   && chown -R django:django ${APP_HOME}/staticfiles \
#   && chmod -R 775 ${APP_HOME}/staticfiles

# نصب پکیج‌ها از build stage
COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
 && rm -rf /wheels

# کپی اسکریپت‌ها
COPY ./docker/local/django/entrypoint.sh /entrypoint
COPY ./docker/local/django/start.sh /start

RUN chmod +x /entrypoint /start \
 && sed -i 's/\r$//' /entrypoint /start

COPY ./docker/local/django/celery/worker/start.sh /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker
 
COPY ./docker/local/django/celery/beat/start.sh /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat
 
COPY ./docker/local/django/celery/flower/start.sh /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# کپی کل پروژه و تعیین مالکیت
COPY . ${APP_HOME}
# RUN chown -R django:django ${APP_HOME}

# USER django

ENTRYPOINT ["/entrypoint"]
