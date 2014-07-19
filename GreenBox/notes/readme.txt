
0) Please read this:
   http://blog.manbolo.com/2013/05/02/build-and-deploy-a-django-project-on-osx-from-scratch

1) Enable and configure Virtual Host

   cd /etc/apache2
   sudo vi httpd.conf

   !Uncomment
   #Include /private/etc/apache2/extra/httpd-vhosts.conf


2) Configure greenbox.com as a virtual host
   cd /etc/apache2/extra/ 
   sudo vim httpd-vhosts.conf 

   !Add this line
   include /private/etc/apache2/extra/vhosts/dev.greenbox.com.conf

3) Configure greenbox.com virtual host as in 
   /my_github/MyPublicRepo1/GreenBox/apache_config_notes/dev.greenbox.com.conf

4) !Call
   cd /my_github/MyPublicRepo1/GreenBox ; python manage.py collectstatic

5) Restart Apache
   sudo apachectl graceful


