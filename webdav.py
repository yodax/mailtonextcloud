import easywebdav


class Webdav:
    remote_webdav = ""

    def __init__(self, server, username, password, webdav_path):
        self.remote_webdav = webdav_path
        self.webdav = easywebdav.connect(
            host=server,
            username=username,
            port=443,
            protocol="https",
            password=password)

    def webdavupload(self, attachment_location, remote_location, filename):

        self.webdav.upload(attachment_location, self.remote_webdav + remote_location + filename)