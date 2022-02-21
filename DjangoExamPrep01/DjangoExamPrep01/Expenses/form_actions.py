from django.shortcuts import redirect, render


class FormAction:

    @staticmethod
    def form_without_instance(request, template, context, redirect_to, form, media=False):
        if request.method == 'POST':
            if media:
                form = form(request.POST, request.FILES)
            else:
                form = form(request.POST)

            if form.is_valid():
                form.save()
                return redirect(redirect_to)
        else:
            context['form'] = form()

        return render(request, template, context)

    @staticmethod
    def form_with_instance(request, template, context, redirect_to, form, instance, media=False):
        if request.method == 'POST':
            if media:
                form = form(request.POST, request.FILES, instance=instance)
            else:
                form = form(request.POST, instance=instance)

            if form.is_valid():
                form.save()
                return redirect(redirect_to)
        else:
            context['form'] = form(instance=instance)

        return render(request, template, context)
