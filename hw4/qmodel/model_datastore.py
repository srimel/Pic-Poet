from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['quote'], entity['author'], entity['date'], entity['type'], entity['source'], entity['rating']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-rimel-srimel')

    def select(self):
        query = self.client.query(kind = 'Quote')
        entities = list(map(from_datastore, query.fetch()))
        return entities
    
    def insert(self, quote, author, date, type, source, rating):
        key = self.client.key('Quote')
        qt = datastore.Entity(key)
        qt.update( {
            'quote': quote,
            'author': author,
            'date': date,
            'type': type,
            'source': source,
            'rating': rating
        })
        self.client.put(qt)
        return True