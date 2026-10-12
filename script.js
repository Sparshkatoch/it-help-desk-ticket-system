/**
 * IT Help Desk Ticket Management System - Client Side Scripts
 * Handles responsive mobile navigation, toast auto-dismissal,
 * status change confirmations, and client-side form helpers.
 */

document.addEventListener('DOMContentLoaded', function () {
    // 1. Mobile Navigation Hamburger Toggle
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            navMenu.classList.toggle('is-active');
            const isExpanded = navMenu.classList.contains('is-active');
            navToggle.setAttribute('aria-expanded', isExpanded);
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function (event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('is-active');
            }
        });
    }

    // 2. Auto-dismiss Flash Toasts after 5 seconds
    const toasts = document.querySelectorAll('.toast-alert');
    toasts.forEach(function (toast) {
        setTimeout(function () {
            toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(-8px)';
            setTimeout(function () {
                if (toast.parentElement) {
                    toast.remove();
                }
            }, 400);
        }, 5000);
    });

    // 3. Status Change Confirmation
    const statusForm = document.querySelector('.status-update-form');
    if (statusForm) {
        statusForm.addEventListener('submit', function (e) {
            const statusSelect = document.getElementById('statusSelect');
            if (statusSelect && statusSelect.value === 'Resolved') {
                const confirmed = confirm('Are you sure you want to mark this ticket as RESOLVED? This indicates the IT issue is completely fixed.');
                if (!confirmed) {
                    e.preventDefault();
                }
            }
        });
    }

    // 4. Keyboard Shortcut: Press '/' to focus Search input on Tickets Page
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        document.addEventListener('keydown', function (e) {
            if (e.key === '/' && document.activeElement !== searchInput && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
                e.preventDefault();
                searchInput.focus();
                searchInput.select();
            }
        });
    }

    // 5. Real-time character count helper for Description in Ticket Creation
    const descTextarea = document.getElementById('description');
    if (descTextarea) {
        const helperText = descTextarea.nextElementSibling;
        descTextarea.addEventListener('input', function () {
            const len = descTextarea.value.trim().length;
            if (helperText) {
                if (len < 10) {
                    helperText.textContent = `Minimum 10 characters required (${len}/10 characters entered).`;
                    helperText.style.color = '#dc2626';
                } else {
                    helperText.textContent = `${len} characters entered (Minimum 10 satisfied).`;
                    helperText.style.color = '#059669';
                }
            }
        });
    }
});
