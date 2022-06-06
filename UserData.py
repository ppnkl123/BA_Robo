class User:
      
    def __init__(self, user_id, start_time, end_time, images, file_path, log_file_path, detected_object):
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self. images = {1.1: None, 1.2: None, 2.1: None, 2.2: None}
        self.file_path = file_path
        self.log_file_path = log_file_path
        self.detected_object = {'name': None, 'probability': None}


    # get user id
    def get_user_id(self):
        return self.user_id

    # set user id
    def set_user_id(self, x):
        self.user_id = x
        
    # get user id
    def get_start_time(self):
        return self.start_time

    # set user id
    def set_start_time(self, x):
        self.start_time = x
        
    # get user id
    def get_end_time(self):
        return self.end_time

    # set user id
    def set_end_time(self, x):
        self.end_time = x
        
    # get user id
    def get_image_info(self, key):
        return self.images[key]

    # set user id
    def set_image_info(self, key, x):
        self.images[key] = x
        
    # get user id
    def get_file_path(self):
        return self.file_path

    # set user id
    def set_file_path(self, x):
        self.file_path = x
        
     # get user id
    def get_log_file_path(self):
        return self.log_file_path

    # set user id
    def set_log_file_path(self, x):
        self.log_file_path = x
    
    # get detected object
    def get_detected_object(self, key):
        return self.detected_object[key]
        
    # set detected object
    def set_detected_object(self, x, y):
        self.detected_object['name'] = x
        self.detected_object['probability'] = y
        
        
    def print_instance(self):
        print("User Id: ", self.user_id)
        print("Start Time: ", self.start_time)
        print("End Time: ", self.end_time)
        print("Image Files: ", self.images)
        print("User File Path: ", self.file_path)
        print("Log File Path: ", self.log_file_path)
        print("Object: ", self.detected_object['name'], "Probability: ", self.detected_object['probability'])
        