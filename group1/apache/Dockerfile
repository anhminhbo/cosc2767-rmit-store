FROM centos:centos7.9.2009

# Install Apache
RUN yum -y update
RUN yum -y install httpd
RUN yum install -y mariadb-server
RUN yum install -y php php-mysql
RUN yum install -y git
RUN git clone https://github.com/anhminhbo/cosc2767-rmit-store.git /var/www/html/
# Install EPEL Repo
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
 && rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN sed -E -i -e '/<Directory "\/var\/www\/html">/,/<\/Directory>/s/AllowOverrideNone/AllowOverriDe All/' /etc/httpd/conf/httpd.conf
RUN sed -E -i -e 's/DirectoryIndex (.*)$/DirectoryIndex index.php \1/g' /etc/httpd/conf/httpd.conf
EXPOSE 80 443
# Start Apache
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]