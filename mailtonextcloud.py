import os
import aaargh

from imap import Imap
from webdav import Webdav

app = aaargh.App(description="Download attachments from unread emails and uploads them to a webdav share, both the "
                             "email server and the webdav server should use the same credentials")

app.arg('--server', help="This is the hostname of both the email server and the webdav host")
app.arg('--username', help="Username")
app.arg('--password', help="Password")
app.arg('--webdavpath', help="This is the location where the webdav server lives", default="/cloud/remote.php/webdav/")
app.arg('--remotepath', help="This is the location where the files should be uploaded on the server", default="/")


@app.cmd
def upload(server, username, password, webdavpath, remotepath):
    imap = Imap(server, username, password)
    webdav = Webdav(server, username, password, webdavpath)
    unread_messages = imap.fetch_unread_messages()
    for message in unread_messages:
        attachment_location = imap.save_attachment(message)

        filename = os.path.basename(attachment_location)

        webdav.webdavupload(attachment_location, remotepath, filename)

        os.remove(attachment_location)
    imap.close_connection()


if __name__ == "__main__":

    app.run()

