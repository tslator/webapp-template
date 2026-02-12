/**
 * Main frontend JavaScript
 */

// Initialize HTMX
document.addEventListener('DOMContentLoaded', function() {
  console.log('Application loaded');

  // HTMX event listeners
  document.body.addEventListener('htmx:afterSwap', function(evt) {
    console.log('Content swapped:', evt.detail);
  });

  document.body.addEventListener('htmx:responseError', function(evt) {
    console.error('HTMX error:', evt.detail);
    // Show error message to user
  });

  document.body.addEventListener('htmx:sendError', function(evt) {
    console.error('HTMX send error:', evt.detail);
  });
});

/**
 * Utility function to make API calls
 */
async function apiCall(url, method = 'GET', data = null) {
  const options = {
    method: method,
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
    },
  };

  if (data) {
    options.body = JSON.stringify(data);
  }

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('API call failed:', error);
    throw error;
  }
}

/**
 * Show notification to user
 */
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.textContent = message;

  document.body.insertBefore(notification, document.body.firstChild);

  setTimeout(() => {
    notification.remove();
  }, 5000);
}
