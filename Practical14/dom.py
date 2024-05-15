# Using DOM
import xml.dom.minidom
import matplotlib.pyplot as plt
import datetime
# Import necessary libraries

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection1 = DOMTree.documentElement

terms = collection1.getElementsByTagName('term')

def count(namespaces):
    count_by_namespace = {namespace: 0 for namespace in namespaces}

    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        if namespace in count_by_namespace:
            count_by_namespace[namespace] += 1
    return count_by_namespace

start_time1 = datetime.datetime.now()

namespaces = ['molecular_function', 'biological_process', 'cellular_component']

# Count every namespace
term_counts = count(namespaces)

print(term_counts)

plt.bar(namespaces, list(term_counts.values()))
plt.xlabel('Namespace')
plt.ylabel('Term counts')

end_time1 = datetime.datetime.now()
used_time1 = end_time1 - start_time1
print('The time taken by DOM is ', used_time1)

plt.show()
# Show the bar chart