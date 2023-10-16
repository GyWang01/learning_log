from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # 新建空白注册表单
        form = UserCreationForm()
    else:
        # 执行表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 保存用户信息并重定向到login页面
            login(request, new_user)
        return redirect('learning_logs:index')
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)