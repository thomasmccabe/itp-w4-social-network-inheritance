from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp == None:
            self.timestamp = datetime.now().strftime("%A, %b %d, %Y") 
            
        elif timestamp != None:
            self.timestamp = timestamp.strftime("%A, %b %d, %Y")
        self.post_info = {'text' : self.text, 'timestamp' : self.timestamp}
        self.user = None

    def set_user(self, user):
        self.post_info['first_name'] = user.first_name
        self.post_info['last_name'] = user.last_name
        user.posts.append(self)
        self.user = user


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
        self.post_info = {'text' : self.text, 'timestamp' : self.timestamp}

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{timestamp}'.format(**self.post_info)


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        self.post_info = {'text' : self.text, 'timestamp' : self.timestamp, 'image_url' : image_url}

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{image_url}\n\t{timestamp}'.format(**self.post_info)


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        self.post_info = {'text' : self.text, 'timestamp' : self.timestamp, 'latitude' : self.latitude, 'longitude' : self.longitude}

    def __str__(self):
        return '@{first_name} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(**self.post_info)
        
