from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    """Helper function to transform Datastore results into the format expected

    Args:
        entity: entity from Datastore

    Returns:
        List: returns a list of the entity's values
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['quote'], entity['author'], entity['date'], entity['type'], entity['source'], entity['rating']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-rimel-srimel')

    def select(self):
        """Selects all quotes from the datastore of kind 'Quote'

        Returns:
            List: returns a list of all quotes in the datastore
        """
        query = self.client.query(kind = 'Quote')
        entities = list(map(from_datastore, query.fetch()))
        return entities
    
    def insert(self, quote, author, date, type, source, rating):
        """Inserts a quote into the datastore of kind 'Quote'

        Args:
            quote (string): quote to be inserted
            author (string): author of the quote
            date (date): date of the quote
            type (string): type of the quote
            source (string): source of the quote
            rating (float): rating of the quote
        """
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