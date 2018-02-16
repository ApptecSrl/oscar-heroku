"""Custom S3 storage backends to store files in subfolders."""
from storages.backends.s3boto3 import S3Boto3Storage


class MediaRootS3BotoStorage(S3Boto3Storage):
    location = 'media'


class StaticRootS3BotoStorage(S3Boto3Storage):
    location = 'static'


class SitemapRootS3BotoStorage(S3Boto3Storage):
    location = 'sitemaps'

    def __init__(self, *args, **kwargs):
        kwargs['location'] = self.location
        super(SitemapRootS3BotoStorage, self).__init__(*args, **kwargs)
