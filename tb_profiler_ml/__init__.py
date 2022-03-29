__version__ = "0.0.1"
import json
import pickle
import csv

class model_class:
    def __init__(self,models,drugs,variants):
        self.models = models
        self.drugs = drugs
        self.variants = variants
    def predict(self,jsonfile):
        resistance = []
        result = json.load(open(jsonfile))
        muts = [(v['gene'],v['change']) for v in result["dr_variants"] + result["other_variants"]]
        for model,drug,variants in zip(self.models,self.drugs,self.variants):
            X = [[1.0 if v in muts else 0.0 for v in variants]]
            pred = model.predict(X)[0]
            if pred==1:
                resistance.append(drug)
        
        return resistance

    def dump(self,outfile):
        pickle.dump(self,open(outfile,"wb"))

    
def create_model_file(args):
    models = [pickle.load(open(f,"rb")) for f in args.models]
    drugs = args.drugs
    variants = [[(row['gene'],row['change']) for row in csv.DictReader(open(f))] for f in args.variants]

    model = model_class(models,drugs,variants)
    model.dump(args.outfile)
    
def predict_with_model(args):
    model = pickle.load(open(args.model,"rb"))
    predictions = model.predict(args.result)
    result = {
        "drugs_tested":model.drugs,
        "predictions": predictions
    }
    json.dump(result,open(args.outfile,"w"))
