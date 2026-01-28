import base64
from django.shortcuts import render
from .forms import CodeForm
from .utils import create_code_image

def index(request):
    image_data = None
    
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            # Generate Image
            image_io = create_code_image(
                code=form.cleaned_data['code'],
                lang=form.cleaned_data['language'],
                theme=form.cleaned_data['theme'],
                line_numbers=form.cleaned_data['line_numbers'],
                font_name=form.cleaned_data['font'],
                mac_buttons=form.cleaned_data['mac_buttons'],
                bg_gradient=form.cleaned_data['background_gradient'],
                padding=form.cleaned_data['padding'],
                watermark=form.cleaned_data['watermark'],
                watermark_text=form.cleaned_data['watermark_text']
            )
            image_data = base64.b64encode(image_io.getvalue()).decode('utf-8')
    else:
        form = CodeForm()

    return render(request, 'index.html', {'form': form, 'image_data': image_data})