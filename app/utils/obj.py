from ..utils.filetypes import get_file_type
class CDNO:
    def __init__(self, name, bucket, special_name:str = None):
        self.name = name
        self.bucket = bucket
        self.type = get_file_type(name)
        self.correct_name = special_name or name
    
    def generate_dl_link(self):
        return f"https://cdn-minio.vofasn.easypanel.host/{self.bucket}/{self.name}"