# cython:language_level=3
from django.db import models
from django.contrib import admin


class RustDeskToken(models.Model):
    ''' Token
    '''
    username = models.CharField(verbose_name='用户名', max_length=20)
    rid = models.CharField(verbose_name='RustDesk ID', max_length=16)
    uid = models.CharField(verbose_name='用户ID', max_length=16)
    uuid = models.CharField(verbose_name='uuid', max_length=60)
    access_token = models.CharField(verbose_name='access_token', max_length=60, blank=True)
    create_time = models.DateTimeField(verbose_name='登录时间', auto_now_add=True)
    #expire_time = models.DateTimeField(verbose_name='过期时间')
    class Meta:
        ordering = ('-username',)
        verbose_name = "Token"
        verbose_name_plural = "Token列表" 

class RustDeskTokenAdmin(admin.ModelAdmin):
    list_display = ('username', 'uid')
    search_fields = ('username', 'uid')
    list_filter = ('create_time', ) #过滤器
    

class RustDeskTag(models.Model):
    ''' Tags
    '''
    uid = models.CharField(verbose_name='所属用户ID', max_length=16)
    tag_name = models.CharField(verbose_name='标签名称', max_length=60)
    tag_color = models.CharField(verbose_name='标签颜色', max_length=60, blank=True)
    
    class Meta:
        ordering = ('-uid',)
        verbose_name = "Tags"
        verbose_name_plural = "Tags列表"

class RustDeskTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'uid', 'tag_color')
    search_fields = ('tag_name', 'uid')
    list_filter = ('uid', )
    

class RustDeskPeer(models.Model):
    ''' Pees
    '''
    uid = models.CharField(verbose_name='用户ID', max_length=16)
    rid = models.CharField(verbose_name='客户端ID', max_length=60)
    username = models.CharField(verbose_name='系统用户名', max_length=20)
    hostname = models.CharField(verbose_name='操作系统名', max_length=30)
    alias = models.CharField(verbose_name='别名', max_length=30)
    platform = models.CharField(verbose_name='平台', max_length=30)
    tags = models.CharField(verbose_name='标签', max_length=30)
    rhash = models.CharField(verbose_name='设备链接密码', max_length=60)
    
    class Meta:
        ordering = ('-username',)
        verbose_name = "Peers"
        verbose_name_plural = "Peers列表" 
        

class RustDeskPeerAdmin(admin.ModelAdmin):
    list_display = ('rid', 'uid', 'username', 'hostname', 'platform', 'alias', 'tags')
    search_fields = ('deviceid', 'alias')
    list_filter = ('rid', 'uid', )
    
    
class RustDesDevice(models.Model):
    rid = models.CharField(verbose_name='客户端ID', max_length=60, blank=True)
    cpu = models.CharField(verbose_name='CPU', max_length=20)
    hostname = models.CharField(verbose_name='主机名', max_length=20)
    memory = models.CharField(verbose_name='内存', max_length=20)
    os = models.CharField(verbose_name='操作系统', max_length=20)
    uuid = models.CharField(verbose_name='uuid', max_length=60)
    username = models.CharField(verbose_name='系统用户名', max_length=60, blank=True)
    version = models.CharField(verbose_name='客户端版本', max_length=20)
    create_time = models.DateTimeField(verbose_name='设备注册时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='设备更新时间', auto_now=True, blank=True)
    
    class Meta:
        ordering = ('-rid',)
        verbose_name = "设备"
        verbose_name_plural = "设备列表" 
    
class RustDesDeviceAdmin(admin.ModelAdmin):
    list_display = ('rid', 'hostname', 'memory', 'uuid', 'version', 'create_time', 'update_time')
    search_fields = ('hostname', 'memory')
    list_filter = ('rid', )
    