# Frontend Dockerfile using Nginx
FROM node:20-alpine as builder

WORKDIR /app

# Copy frontend dependencies
COPY package*.json ./

# Install dependencies and build CSS
RUN npm ci && npm run build:css


# Production image
FROM nginx:alpine

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files from builder
COPY --from=builder /app/static /usr/share/nginx/html/static
COPY templates /usr/share/nginx/html/templates

# Create non-root user for nginx
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

# Expose port
EXPOSE 80

# Run nginx
CMD ["nginx", "-g", "daemon off;"]
