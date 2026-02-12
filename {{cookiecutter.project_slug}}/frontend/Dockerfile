FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# Copy static assets and templates directly
COPY static /usr/share/nginx/html/static
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
