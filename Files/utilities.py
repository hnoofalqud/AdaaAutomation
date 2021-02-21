import logging


class Utilities:
    """
    Define the columns
    __NameColumn = "A{0}"
    __Name2Column = "B{0}"
    ....

    Define the setters & getters

    """
    __functionColumn = "A{0}"
    __functionParameterColumn = "B{0}"
    __inputDataColumn = "C{0}"
    __extraDataColumn = "D{0}"
    __questionValueColumn = "E{0}"
    __parameterColumn = "F{0}"

    welcome = """

                     _   _   _ _____ ___  __  __    _  _____ ___ ___  _   _
                    / \ | | | |_   _/ _ \|  \/  |  / \|_   _|_ _/ _ \| \ | |
                   / _ \| | | | | || | | | |\/| | / _ \ | |  | | | | |  \| |
                  / ___ \ |_| | | || |_| | |  | |/ ___ \| |  | | |_| | |\  |
                 /_/   \_\___/  |_| \___/|_|  |_/_/   \_\_| |___\___/|_| \_|

        <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> <>-<> 

                 """
    done = """
           ____    ___     ___    ____      ____   __   __  _____   _   _   _ 
          / ___|  / _ \   / _ \  |  _ \    | __ )  \ \ / / | ____| | | | | | |
         | |  _  | | | | | | | | | | | |   |  _ \   \ V /  |  _|   | | | | | |
         | |_| | | |_| | | |_| | | |_| |   | |_) |   | |   | |___  |_| |_| |_|
          \____|  \___/   \___/  |____/    |____/    |_|   |_____| (_) (_) (_)


    """
    error = """
 _________        .------------------.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  TEST ERROR!!! | |             
|:______B:|      | |                | |             
|:______B:|      | |  >SUDDEN STOP< | |             
|         |      | |                | |             
|:_______:|      | |       :(       | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|         |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:
    
    """


    def get_function_from_row(self, rowNumber):
        return self.readExcel.getCellFromSheet(sheet=self.sheet,
                                               cell=self.__functionColumn.format(rowNumber))

    def get_parameter_from_row(self, rowNumber):
        return self.readExcel.getCellFromSheet(sheet=self.sheet,
                                               cell=self.__functionParameterColumn.format(rowNumber))

    def get_input_data_from_row(self, rowNumber):
        return self.readExcel.getCellFromSheet(sheet=self.sheet,
                                               cell=self.__inputDataColumn.format(rowNumber))

    def get_extra_data_from_row(self, rowNumber):
        return self.readExcel.getCellFromSheet(sheet=self.sheet,
                                               cell=self.__extraDataColumn.format(rowNumber))