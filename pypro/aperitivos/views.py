from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '754804288?h=243c51ec88'}
    return render(request, 'aperitivos/video.html', context={'video': video})
