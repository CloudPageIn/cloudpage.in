# How to Add Real Telugu Song Videos

The Movie Music tab is now set up with category buttons. You need to replace the placeholder video IDs with real Telugu song YouTube video IDs.

## How to Get YouTube Video ID:

1. Go to any YouTube video
2. Look at the URL: `https://www.youtube.com/watch?v=VIDEO_ID_HERE`
3. Copy the VIDEO_ID_HERE part
4. Replace `dQw4w9WgXcQ` in the videos.html file

## Where to Replace:

In `videos.html`, find these sections and replace the video IDs:

### Latest Hits Category (Line ~XXX)
```html
<iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID_1" ...></iframe>
<iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID_2" ...></iframe>
<iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID_3" ...></iframe>
```

### Romantic Category
Replace 3 video IDs with Telugu romantic songs

### Dance Category
Replace 3 video IDs with Telugu dance songs

### Melody Category
Replace 3 video IDs with Telugu melody songs

### Item Songs Category
Replace 3 video IDs with Telugu item songs

### Folk Category
Replace 3 video IDs with Telugu folk songs

## Example:
If you want to add the song "Butta Bomma":
1. YouTube URL: `https://www.youtube.com/watch?v=JFcgOboQZ08`
2. Video ID: `JFcgOboQZ08`
3. Replace in HTML: `<iframe src="https://www.youtube.com/embed/JFcgOboQZ08" ...>`

## Current Structure:
- 6 Categories (Latest Hits, Romantic, Dance, Melody, Item Songs, Folk)
- 3 Videos per category
- Total: 18 video slots to fill

Once you add the real video IDs, the videos will play directly on your website!
