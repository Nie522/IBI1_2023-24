# Using SAX
import xml.sax
import matplotlib.pyplot as plt
import datetime
# Import necessary libraries

class goHandler(xml.sax.ContentHandler):
# Define a class goHandler, inheriting from xml.sax.ContentHandler
    def __init__(self):
        self.namespace = ""
        self.current_data = ""
        self.current_element = ""
        self.namespace_counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        # Create a dictionary to store the counts

    def startElement(self, tag, attrs):
        self.current_element = tag

    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace += content.strip()

    def endElement(self, tag):
        if tag == 'namespace' and self.namespace in self.namespace_counts.keys():
        # namespace is an end tag in case of several namespaces in one term
            self.namespace_counts[self.namespace] = self.namespace_counts.get(self.namespace, 0) + 1
            self.namespace = ""
            # Reset namespace
        elif tag == 'term':
            self.current_element = ""
        # If tag is term, the element should be reset

start_time2 = datetime.datetime.now()
# Record the start time

parser = xml.sax.make_parser()
# Created an SAX parser instance
handler = goHandler()
# Create a goHandler instance
parser.setContentHandler(handler)  # 将goHandler类的实例设置为解析器的内容处理器。
parser.parse("go_obo.xml")
# Begin parsing the xml file

for key, value in handler.namespace_counts.items():
    print(f"{key}: {value}")
    # Print namespaces and counts in the dictionary

plt.bar(list(handler.namespace_counts.keys()), list(handler.namespace_counts.values()))
plt.xlabel('Namespace')
plt.ylabel('Term counts')
# Plot the information using a bar chart, define the xlabel and ylabel

end_time2 = datetime.datetime.now()
# Record the end time
used_time2 = end_time2 - start_time2
# Calculate the taken time
print('The time taken by SAX is ', used_time2)
# Print the taken time

plt.show()
# Show the bar chart