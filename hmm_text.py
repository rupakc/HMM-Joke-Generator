import markovify
import pickle


class TextGen:

    def __init__(self,text_file_path):
        self.text_file = text_file_path

    def train_model(self,state_size=2):
        text_string = ''
        with open(self.text_file) as tf:
            text_string = tf.read()
        self.hmm_model = markovify.Text(text_string,state_size=state_size)

    def get_model(self):
        return self.hmm_model

    def get_sentence(self,tries=100):
        return self.hmm_model.make_sentence(tries=tries)

    def get_short_sentence(self,length_in_characters=140):
        return self.hmm_model.make_short_sentence(char_limit=length_in_characters)

    def save_model(self,filename):
        dump_file = open(filename,mode='wb')
        pickle.dump(self.hmm_model,dump_file)
        dump_file.close()

    def load_model(self,filename):
        model_file = open(filename,mode='rb')
        self.hmm_model = pickle.load(model_file)
        model_file.close()

    def model_train_and_save_pipeline(self,persist_filename):
        self.train_model()
        self.save_model(persist_filename)
