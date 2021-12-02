from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'coden.urls', name='www'),
    host(r'services', 'services.urls', name='services'),
)