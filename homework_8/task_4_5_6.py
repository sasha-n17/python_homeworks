class MyOwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


class WareHouse:
    def __init__(self):
        self._printers_list = []
        self._scanners_list = []
        self._xerox_list = []

        self.__printers_dict = {}
        self.__scanners_dict = {}
        self.__xerox_dict = {}

        self.storage_warehouse_main = {'Printer': 0,
                                       'Scanner': 0,
                                       'Xerox': 0}
        self.storage_warehouse_detail_info = {'Printer': self.__printers_dict,
                                              'Scanner': self.__scanners_dict,
                                              'Xerox': self.__xerox_dict}

    @staticmethod
    def input_valid(product):
        input_types_dict = {'Printer': ['str', 'int', 'str', 'int', 'bool', 'int', 'str', 'int'],
                            'Scanner': ['str', 'int', 'str', 'int', 'bool', 'str', 'str', 'int'],
                            'Xerox': ['str', 'int', 'str', 'int', 'bool', 'int', 'str', 'bool', 'bool']}
        type_product = product.__class__.__name__
        product_dict = product.__dict__
        try:
            for i, el in enumerate(list(product_dict.values())):
                if el.__class__.__name__ != input_types_dict[type_product][i]:
                    raise MyOwnException('Некорректный ввод данных. Несовпадение типов')
        except MyOwnException as error:
            return error
        return 'Типы соблюдены'

    def goods_arrival(self, product):
        type_product = product.__class__.__name__
        product_dict = product.__dict__
        brand, price = list(product_dict.values())[0:2]
        if WareHouse.input_valid(product) == 'Типы соблюдены':
            if type_product == 'Printer':
                self._printers_list.append(product_dict)
                self.storage_warehouse_main['Printer'] = len(self._printers_list)
                if brand not in self.__printers_dict:
                    self.__printers_dict[brand] = {'count': 1, 'sum_price': price}
                else:
                    self.__printers_dict[brand]['count'] += 1
                    self.__printers_dict[brand]['sum_price'] += price
            elif type_product == 'Scanner':
                self._scanners_list.append(product_dict)
                self.storage_warehouse_main['Scanner'] = len(self._scanners_list)
                if brand not in self.__scanners_dict:
                    self.__scanners_dict[brand] = {'count': 1, 'sum_price': price}
                else:
                    self.__scanners_dict[brand]['count'] += 1
                    self.__scanners_dict[brand]['sum_price'] += price
            else:
                self._xerox_list.append(product_dict)
                self.storage_warehouse_main['Xerox'] = len(self._xerox_list)
                if brand not in self.__xerox_dict:
                    self.__xerox_dict[brand] = {'count': 1, 'sum_price': price}
                else:
                    self.__xerox_dict[brand]['count'] += 1
                    self.__xerox_dict[brand]['sum_price'] += price
        else:
            print(WareHouse.input_valid(product))

    def transfer_of_goods(self, type_of_equipment, quantity):
        if type_of_equipment == 'Printer':
            if quantity <= self.storage_warehouse_main['Printer']:
                return 'Выдача возможна. На складе достаточно принтеров'
            else:
                return f"На складе недостаточно товара. " \
                       f"Запрошено: {quantity} ед., на складе: {self.storage_warehouse_main['Printer']} ед."
        elif type_of_equipment == 'Scanner':
            if quantity <= self.storage_warehouse_main['Scanner']:
                return 'Выдача возможна. На складе достаточно сканеров'
            else:
                return f"На складе недостаточно товара. " \
                       f"Запрошено: {quantity} ед., на складе: {self.storage_warehouse_main['Scanner']} ед."
        else:
            if quantity <= self.storage_warehouse_main['Printer']:
                return 'Выдача возможна. На складе достаточно ксероксов'
            else:
                return f"На складе недостаточно товара. " \
                       f"Запрошено: {quantity} ед., на складе: {self.storage_warehouse_main['Xerox']} ед."


class OfficeEquipment:
    def __init__(self, brand, price, color, warranty, wifi_support):
        self.brand = brand
        self.price = price
        self.color = color
        self.warranty = warranty
        self.wifi_support = wifi_support


class Printer(OfficeEquipment):
    def __init__(self, brand, price, color, warranty, wifi_support, print_speed, print_type, paper_feed_tray_capacity):
        super().__init__(brand, price, color, warranty, wifi_support)
        self.print_speed = print_speed
        self.print_type = print_type
        self.paper_feed_tray_capacity = paper_feed_tray_capacity


class Scanner(OfficeEquipment):
    def __init__(self, brand, price, color, warranty, wifi_support, scanner_type, scan_type, scanning_speed):
        super().__init__(brand, price, color, warranty, wifi_support)
        self.scanner_type = scanner_type
        self.scan_type = scan_type
        self.scanning_speed = scanning_speed


class Xerox(OfficeEquipment):
    def __init__(self, brand, price, color, warranty, wifi_support, print_speed, print_type, built_in_copier,
                 built_in_scanner):
        super().__init__(brand, price, color, warranty, wifi_support)
        self.print_speed = print_speed
        self.print_type = print_type
        self.built_in_copier = built_in_copier
        self.built_in_scanner = built_in_scanner


printer = Printer('hp', 8690, 'white', 1, True, 18, 'лазерный', 150)
printer_2 = Printer('epson', 11990, 'black', 1, True, 27, 'струйный', 100)
printer_3 = Printer('canon', 9990, 'black', 1, True, 9, 'струйный', 100)
scanner = Scanner('canon', 6490, 'black', 1, True, 'планшетный', 'однопроходный', 8)
scanner_2 = Scanner('fujitsu', 22990, 'black', 1, True, 'протяжной,двусторонний,автопадача', 'однопроходный', 6)
xerox = Xerox('МФУ Xerox', 12990, 'white', 1, True, 20, 'лазерный', True, True)
xerox_2 = Xerox('МФУ Xerox', 19990, 'white', 1, True, 30, 'лазерный', True, True)
xerox_3 = Xerox('МФУ Xerox', 15390, 'white', 1, True, 30, 'лазерный', True, True)
xerox_4 = Xerox('МФУ Xerox', 'AAAAAAA', 'white', 1, 'AAAAAAA', 30, 'лазерный', True, 'AAAAAAA')
test = WareHouse()
test.goods_arrival(printer)
test.goods_arrival(printer_2)
test.goods_arrival(printer_3)
test.goods_arrival(scanner)
test.goods_arrival(scanner_2)
test.goods_arrival(xerox)
test.goods_arrival(xerox_2)
test.goods_arrival(xerox_3)
test.goods_arrival(xerox_4)
print(test.storage_warehouse_main)
print(test.storage_warehouse_detail_info)
print(test.transfer_of_goods('Printer', 3))
print(test.transfer_of_goods('Scanner', 5))
print(test.transfer_of_goods('Xerox', 2))
