from abc import ABC, abstractmethod


class PriceProvider(ABC):
    @abstractmethod
    def get_price(self):
        pass


class DocumentProvider(ABC):
    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def get_payment(self):
        pass


class MarketingProvider(ABC):
    @abstractmethod
    def claim_sales(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass


class FirstShopDocumentProvider(DocumentProvider):
    def __init__(self, title, action):
        self.title = title
        self.action = action

    def get_document(self):
        print('FrstShopDocumentProvider - get_document')

    def get_payment(self):
        print('FrstShopDocumentProvider - get_document')


class FistShopPriceProvider(PriceProvider):
    def __init__(self, id):
        self.id = id

    def get_price(self):
        print('FistShopPriceProvider - get_price')


class FirstShopMarketingProvider(MarketingProvider):
    def claim_sales(self):
        print('FirstShopMarketingProvider - claim_sales')

    def calculate_bonus(self):
        print('FirstShopMarketingProvider - calculate_bonus')

class ExchangeFactory(ABC):
    @abstractmethod
    def create__price_provider(self):
        pass

    @abstractmethod
    def create__document_provider(self):
        pass

    @abstractmethod
    def create__marketing_provider(self):
        pass


class FirstShopExchangeFactory(ExchangeFactory):
    def create__price_provider(self):
        return FistShopPriceProvider('plate_id')

    def create__document_provider(self):
        return FirstShopDocumentProvider('plate', 'move')

    def create__marketing_provider(self):
        return FirstShopMarketingProvider()


class Factory:
    SUPPLIER_ONE = 'FistShop'
    SUPPLIER_TWO = 'SecondShop'

    @classmethod
    def create_factory(cls, creator):
        if creator == cls.SUPPLIER_ONE:
            return FirstShopExchangeFactory()
        else:
            return None


first_try = Factory.create_factory('FistShop')
doc = first_try.create__document_provider()
print(doc.title)
