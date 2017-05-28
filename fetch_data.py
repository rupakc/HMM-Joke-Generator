import urllib2
import json


class Joke:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = urllib2.urlopen(self.url)
        data = response.read()
        return data

    @staticmethod
    def extract_joke_list(response_json_or_dict,value_field='value',joke_field='joke'):
        value_list = response_json_or_dict[value_field]
        joke_list = list([])
        for value in value_list:
            joke_list.append(value[joke_field])
        return joke_list

    @staticmethod
    def write_joke_to_file(joke_list,filename):
        file_to_write = open(filename,mode='w')
        for joke in joke_list:
            file_to_write.write(joke)
            file_to_write.write('\n')
            file_to_write.flush()
        file_to_write.close()

    def joke_fetch_and_persist_pipeline(self,filename):
        response_data = json.loads(self.fetch_data())
        joke_list = self.extract_joke_list(response_data)
        self.write_joke_to_file(joke_list,filename)
