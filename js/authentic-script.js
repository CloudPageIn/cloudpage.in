// Gallery Image Switcher
function changeImage(thumbnail) {
    const mainImage = document.getElementById('mainImage');
    const thumbnails = document.querySelectorAll('.thumbnail-item');
    
    // Update main image with fade effect
    mainImage.style.opacity = '0.5';
    
    setTimeout(() => {
        mainImage.src = thumbnail.src;
        mainImage.style.opacity = '1';
    }, 200);
    
    // Update active thumbnail
    thumbnails.forEach(item => item.classList.remove('active'));
    thumbnail.parentElement.classList.add('active');
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Image preloader for gallery
window.addEventListener('load', function() {
    const images = document.querySelectorAll('.thumbnail-item img');
    images.forEach(img => {
        const newImg = new Image();
        newImg.src = img.src;
    });
});

// Add transition effect to main image
document.addEventListener('DOMContentLoaded', function() {
    const mainImage = document.getElementById('mainImage');
    if (mainImage) {
        mainImage.style.transition = 'opacity 0.3s ease';
    }
});
