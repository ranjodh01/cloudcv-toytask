from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ImageForm
from .models import Image
import os
from subprocess import PIPE, Popen
import json

neural_vqa_path = "/home/ranjodh/dev/neural-vqa"
checkpoints_path = os.path.join(neural_vqa_path, "checkpoints/vqa_epoch23.26_0.4610_cpu.t7")
# input_image = os.path.join(os.getcwd(), "media", )


def image_view(request):
	i = Image.objects.all()
	
	for x in i:
		os.remove(os.path.join(os.getcwd(), "media", x.image.name))
	i.delete()
	form = ImageForm()
	return render(request, "main/image_form.html", {"form": form})

def answer_view(request):
	ans = {'hello': 'world'}
	# input_image = os.path.join(os.getcwd)
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		# img = Image(image = request.FILES)
		# form = ImageForm(data=request.POST, instance=img)
		if form.is_valid():
			ans['success'] = True
			question = form.cleaned_data['ques']
			image = form.cleaned_data['image']
			i = Image(ques=question, image=image)
			i.save()
			obj = Image.objects.all()[0]
			ans['image'] = obj.image.name
			ans['questions'] = obj.ques
			img = os.path.join(os.getcwd(), "media", obj.image.name)
			ans['img_path'] = img

			process = Popen(["th", "predict.lua", "-checkpoint_file", "checkpoints/vqa_epoch23.26_0.4610_cpu.t7", "-input_image_path", img, "-question", obj.ques], cwd=r'/home/ranjodh/dev/toytask/neural-vqa', stdout=PIPE)


			# process = Popen(["th", os.path.join(neural_vqa_path, "predict.lua"), "-checkpoint_file", checkpoints_path, "-input_image_path", img, "-question", obj.ques ], stdout = PIPE)
			

			(output, err) = process.communicate()
			o = output.decode("utf-8")
			out = o.split("\n")[-2]
			# o = output.split("\n")[-2].split("\t")[0]
			ans['out'] = out
		else:
			ans['success'] = False


	return HttpResponse(json.dumps(ans), content_type="application/json")