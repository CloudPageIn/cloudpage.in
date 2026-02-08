# Load More Songs Feature

## What's Added:

Each music category now has a "Load More Songs" button that reveals 3 additional songs when clicked.

## How It Works:

1. **Initial View**: Shows 3 songs per category
2. **Click "Load More Songs"**: Reveals 3 more songs (total 6 songs visible)
3. **Button Changes**: Text changes to "Show Less" with minus icon
4. **Click "Show Less"**: Hides the additional songs, back to 3 songs
5. **Smooth Scroll**: Automatically scrolls to show new content

## Current Implementation:

### Latest Hits Category:
- **Initial 3**: Butta Bomma, Saami Saami, Oo Antava
- **More 3**: Naatu Naatu, Srivalli, Vachinde

### To Add More Categories:

You need to add the same structure for:
- Romantic
- Dance  
- Melody
- Item Songs
- Folk

## Structure for Each Category:

```html
<div id="CATEGORY-category" class="music-category">
    <!-- First 3 videos in video-grid -->
    <div class="video-grid">
        <!-- 3 video items -->
    </div>
    
    <!-- Additional 3 videos in more-videos-grid -->
    <div class="more-videos-grid" id="CATEGORY-more" style="display: none;">
        <!-- 3 more video items -->
    </div>
    
    <!-- Load More Button -->
    <div class="load-more-btn-container">
        <button class="load-more-btn" onclick="loadMoreSongs('CATEGORY')">
            <i class="fas fa-plus-circle"></i> Load More Songs
        </button>
    </div>
</div>
```

## Features:

- ✅ Toggle functionality (show/hide)
- ✅ Icon changes (plus/minus)
- ✅ Text changes (Load More/Show Less)
- ✅ Smooth animations
- ✅ Responsive design
- ✅ All videos play on your website (no redirect)

## Next Steps:

Add the same "more-videos-grid" and "load-more-btn-container" structure to the remaining 5 categories (Romantic, Dance, Melody, Item Songs, Folk) with different Telugu songs for each.
