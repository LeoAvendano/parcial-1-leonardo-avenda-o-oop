# parcial-1-leonardo-avenda-o-oop
class Libro:
    def __init__(self, autor, titulo, editorial):
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
 
    
    def autor(self):
        return self._autor
 
    
    def autor(self, autor):
        self._autor = autor
 
   
    def titulo(self):
        return self._titulo
 
    
    def titulo(self, titulo):
        self._titulo = titulo
 
    
    def editorial(self):
        return self._editorial
 
   
    def editorial(self, editorial):
        self._editorial = editorial
