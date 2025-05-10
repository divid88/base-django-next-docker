FROM node:20.10-alpine AS base
# استفاده از تصویر رسمی نود


# تنظیم مسیر کاری
WORKDIR /app

# کپی فایل‌های موردنیاز
COPY package.json package-lock.json ./
RUN npm install -g npm@10.9.2
# نصب وابستگی‌ها
RUN npm install

# کپی فایل‌های پروژه
COPY . .

# ساخت پروژه برای محیط تولید (Production)




# اجرای پروژه نکس‌جی‌اس
CMD ["npm", "run", "dev"]
