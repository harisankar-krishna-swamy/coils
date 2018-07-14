'''
Created on Nov 8, 2015
@author: hari
'''
from functools import total_ordering
from coils.misc.internstore import InternStore

@total_ordering
class Country(object):
    def __init__(self, country_name = 'US'):
        self._country_name = country_name
    
    @property
    def country_name(self):
        return self._country_name
        
    def __str__(self):
        return '%s' % self._country_name
    
    def __eq__(self, other):
        if other == None or type(other) != type(self):
            return False
        return self._country_name == other.country_name
    
    def __lt__(self, other):
        if other == None or type(other) != type(self):
            return False
        return self._name < other.country_name
    
    def __hash__(self):
        return hash(self._country_name)
    
if __name__ == '__main__':
    US = Country(country_name = 'US')
    IN = Country(country_name = 'IN')
    
    intern_store = InternStore()
    intern_store.intern(obj = US)
    intern_store.intern(obj = IN)
    
    print 'Id of original US object is %d' % id(US)
    
    duplicate_country_US = Country(country_name = 'US')
    print 'id of duplicate US object is %d' % id(duplicate_country_US)
    print 'Interning this new object'
    duplicate_country_US = intern_store.intern(obj = duplicate_country_US)
    print 'After interning we get the original object with id %d' % id(duplicate_country_US)
     
    print 'We might as well do this country = intern_store.intern(Country(name=\'US\'))'