print("Using DOM:")
# Remind the user

# Using DOM
import xml.dom.minidom
import matplotlib.pyplot as plt
import datetime
# Import necessary libraries

start_time1 = datetime.datetime.now()
# Record the start time

DOMTree = xml.dom.minidom.parse("go_obo.xml")
# Read the xml file using DOM and store in DOMTree
collection1 = DOMTree.documentElement
# Store the root elements as collection1

terms = collection1.getElementsByTagName('term')
# Distract every term and save as terms

def count(namespaces):
# Define a function to distract and count different namespaces
    count_by_namespace = {namespace: 0 for namespace in namespaces}
    # Create a dictionary, keys are namespaces, values are 0
    for term in terms:
    # Traverse every term
        namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        # Extract namespace for the firstChild of namespace element
        if namespace in count_by_namespace:
            count_by_namespace[namespace] += 1
            # Filter namespaces of interest and count
    return count_by_namespace
    # Return to the results

namespaces = ['molecular_function', 'biological_process', 'cellular_component']
# Define namespaces of interest

term_counts = count(namespaces)
# Count every namespace

for key, value in term_counts.items():
    print(f"{key}: {value}")
# Print every namespace and matching count

plt.bar(namespaces, list(term_counts.values()))
plt.xlabel('Namespace')
plt.ylabel('Term counts')
# Using matplotlib to draw a bar chart, define the xlabel and ylabel

end_time1 = datetime.datetime.now()
# Record the end time aftering forming the chart
used_time1 = end_time1 - start_time1
print('The time taken by DOM is ', used_time1)
# Calculate for the used time and print

plt.show()
# Show the bar chart
plt.close()
# Ensure the bar chart has been closed

print("Using SAX:")
# Remind the user

# Using SAX
import xml.sax
import matplotlib.pyplot as plt
import datetime
# Import necessary libraries

start_time2 = datetime.datetime.now()
# Record the start time

class goHandler(xml.sax.ContentHandler):
# Define a class goHandler, inheriting from xml.sax.ContentHandler
    def __init__(self):
        self.namespace = ""
        self.current_data = ""
        self.current_element = ""
        # Define different attributes
        self.namespace_counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        # Create a dictionary to store the counts

    def startElement(self, tag, attrs):
    # Start
        self.current_element = tag
        # Let current element be tag

    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace += content.strip()
    # Distract the characters from namespace

    def endElement(self, tag):
    # End after distracting namespace or tag equals to term
        if tag == 'namespace' and self.namespace in self.namespace_counts.keys():
        # namespace is an end tag in case of several namespaces in one term
            self.namespace_counts[self.namespace] = self.namespace_counts.get(self.namespace, 0) + 1
            self.namespace = ""
            # Reset namespace
        elif tag == 'term':
            self.current_element = ""
        # If tag is term, the element should be reset

parser = xml.sax.make_parser()
# Created an SAX parser instance
handler = goHandler()
# Create a goHandler instance
parser.setContentHandler(handler)
# Set an instance of the goHandler class to be the parser's content handler
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
plt.close()
# Ensure the bar chart has been closed

if used_time1 > used_time2:
    print("SAX was the quickest recorded.")
elif used_time1 < used_time2:
    print("DOM was the quickest recorded.")
else:
    print("DOM and SAX used the same time.")
# Compare the time used by different methods and print the result

# The result will be "SAX was the quickest recorded". That is because SAX only read the xml file.