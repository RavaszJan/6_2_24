# Dp dezing Patterns
# Singleton
# class Singleton:
#     _instance=None
#
#     def __init__(self):
#         if Singleton._instance is not None:
#             raise Exception("Tato trieda je Singleton a uz bola instancovana")
#         else:
#             self.meno="Patrik"
#             Singleton._instance= self
#
#     @staticmethod
#     def getInstance():
#         if Singleton._instance is None:
#             Singleton()
#         return Singleton._instance
#
#
# s1=Singleton.getInstance()
# print(s1.meno)
# s2=Singleton.getInstance()
# s1.meno="Milan"
# print(s2.meno)
# s3=Singleton()

#
# # Factory
# class Document:
#     def create(self):
#         raise NotImplementedError("Metoda create() musi byt prepisana")
#
# class PDFDocument(Document):
#     def create(self):
#         return "Vytvara sa PDF dokument"
#
# class WorfDocument(Document):
#     def create(self):
#         return "Vytvarame Word document"
#
# class TextDocument(Document):
#     def create(self):
#         return "Vztvarame Text document"
#
#
# class Factory:
#     def create_document(self,type):
#         if type=="pdf":
#             return PDFDocument()
#         elif type=="word":
#             return WorfDocument()
#         elif type=="text":
#             return TextDocument()
#         else:
#             raise ValueError("Neznamy typ dokumentu")
#
#
# factory=Factory()
#
# pdf=factory.create_document("pdf")
# print(pdf.create())
#
# word=factory.create_document("word")
# print(word.create())
#
# text=factory.create_document("text")
# print(text.create())

# BUILDER
class Form:
    def __init__(self):
        self.fields=[]

    def add_field(self,field):
        self.fields.append(field)

    def __str__(self):
        return "\n".join(self.fields)

class FormBuilder:
    def __init__(self):
        self.form=Form()

    def add_name_field(self):
        self.form.add_field("Name: [____________]")
        return self
    def add__address_field(self):
        self.form.add_field("Adress: [__________]")
        return self
    def add_email_field(self):
        self.form.add_field("Email: [____________")
        return self
    def add_country_field(self):
        self.form.add_field("Country: [____________")
        return self

    def build(self):
        return self.form

builder=FormBuilder()
form=builder.add_name_field().add__address_field().add_email_field().add_country_field().build()
print(form)
