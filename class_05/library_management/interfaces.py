import abc

class TextSearchable(abc.ABC):
    
    @abc.abstractmethod
    def get_searchable_text(self) -> str:
        pass
