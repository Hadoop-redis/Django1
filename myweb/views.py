from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
# 页面查询用户信息
from myweb.models import Linux
import csv


def queryLinux(request):
    # 到数据库查询用户信息
    lx = Linux.objects.all()
    # 将数据发送给页面
    context = {"ls": lx}
    return render(request, "linux.html", context)


# 打开添加页面
def openAdd(request):
    return render(request, "linuxAdd.html")


# 保存数据
def saveLinux(request):
    counts = Linux.objects.filter()
    for count in counts:
        print(count)
    try:
        linux_ip = request.GET.get('linux_ip')
        linux_name = request.GET.get('linux_name')
        linux_cpu = request.GET.get('linux_cpu')
        linux_notes = request.GET.get('linux_notes')
        Linux.objects.create(linux_ip=linux_ip, linux_name=linux_name, linux_cpu=linux_cpu, linux_notes=linux_notes)
        # redirect重定向,比如我们输入www.baidu.com 会自动重定位到https://www.baidu.com/ 这个过程就是重定向
        return redirect("/myweb/queryLinuxs")
    except Exception as e:
        print("ip地址已经存在，请重新输入" + str(e))
        # return redirect("/myweb/queryLinuxs")
        return render(request, 'error.html')


# 打开修改页面
def openEdit(request):
    id = request.GET.get('id')
    # 到数据库查询用户信息
    m = Linux.objects.filter(id=id).first()
    # 将数据发给页面
    context = {"m": m}
    return render(request, "linuxEdit.html", context)


# 更新数据
def updateLinux(request):
    id = request.GET.get('id')
    linux_ip = request.GET.get('linux_ip')
    linux_name = request.GET.get('linux_name')
    linux_cpu = request.GET.get('linux_cpu')
    linux_notes = request.GET.get('linux_notes')
    # 更新数据库的信息
    Linux.objects.filter(id=id).update(linux_ip=linux_ip, linux_name=linux_name, linux_cpu=linux_cpu, linux_notes=linux_notes)
    # 永久修改名称：hostnamectl set-hostname 主机名
    # try:
    #     ssh_client = paramiko.SSHClient()
    #     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh_client.connect(linux_ip, 22, "root", "root")
    #     ssh_client.exec_command("hostnamectl set-hostname " + linux_name)
    #     ssh_client.close()
    # except Exception as e:
    #     print(e)
    # return redirect("/myweb/queryLinuxs")
    return render(request, 'update_ok.html')


# 删除数据
def deleteLinux(request):
    id = request.GET.get('id')
    Linux.objects.filter(id=id).delete()
    return redirect("/myweb/queryLinuxs")


def daochu(request):
    list1 = []
    lx = Linux.objects.all()
    for x in lx:
        list1.append([x.id, x.linux_ip, x.linux_name, x.linux_cpu, x.linux_notes])
    line1 = ['id', '虚拟机ip', '虚拟机名称', 'cpu', '注释']
    with open('D:/A/Code/Python/September/mysite/templates/static/linux.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(line1)
        for row in list1:
            writer.writerow(row)
    return render(request, 'download.html')


def download(request):
    file = open('templates/static/linux.csv', 'rb')
    response = HttpResponse(file)
    response['Content-type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="linux.csv'
    return response
