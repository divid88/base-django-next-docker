#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

echo "Setting permissions on staticfiles and db"

# تنظیم دسترسی‌ها برای پوشه staticfiles
# chmod -R 775 /app/staticfiles
# chown -R django:django /app/staticfiles

# # در صورتی که پوشه staticfiles/admin/css وجود نداشته باشد، آن را ایجاد کن
# mkdir -p /app/staticfiles/admin/css
# chmod -R 775 /app/staticfiles/admin/css
# chown -R django:django /app/staticfiles/admin/css

# اجرای migrations برای پایگاه داده
echo "Running migrations"
python manage.py migrate --no-input

# جمع‌آوری فایل‌های استاتیک
echo "Collecting static files"


# اجرای سرور Django
echo "Starting Django server"
exec python manage.py runserver 0.0.0.0:8000