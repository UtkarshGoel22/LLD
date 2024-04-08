"""
Adapter Design Pattern

Adapter is a structural design pattern that allows objects with
incompatible interfaces to collaborate.
This pattern involves a single class, known as the adapter, which is
responsible for joining functionalities of independent or incompatible interfaces.

Link: https://www.youtube.com/watch?v=2PKQtcJjYvc&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=8
"""

class XMLData:

    def __init__(self, xml_data: str) -> None:
        self.xml_data: str = xml_data

    def get_xml_data(self) -> str:
        return self.xml_data

class DataAnalyticsTool:

    def __init__(self, json_data: str):
        self.json_data: str = json_data

    def analyze_data(self):
        print("Analyzing json data.")

class Adapter(DataAnalyticsTool):

    def __init__(self, xml_data: XMLData):
        self.xml_data: XMLData = xml_data

    def analyze_data(self):
        print(self.xml_data.get_xml_data())
        print("Converting XML data to json data.")
        print("Analysing the converted JSON data.")

class Client:

    def process_data(self, tool: DataAnalyticsTool):
        tool.analyze_data()

xml_data: XMLData = XMLData("Sample XML data")
data_analytics_tool: DataAnalyticsTool = Adapter(xml_data)
client: Client = Client();
client.process_data(data_analytics_tool)
