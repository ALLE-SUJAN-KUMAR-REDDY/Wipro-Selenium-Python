import xml.etree.ElementTree as ET
import os

# =======================
# READ XML
# =======================
with open(r"C:\Users\Sujan Kumar Reddy\PycharmProjects\PythonAdvancedProgramming\Dataformats\employee.xml", "rb") as file:
    tree = ET.parse(file)
    root = tree.getroot()

print(root.tag)
print(root[0].tag)
print(root[0].attrib)

for employee in root.findall("employee"):
    print(employee.get("id"))

for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name, role, exp)

# =======================
# WRITE XML
# =======================
write_root = ET.Element("employees")

emp1 = ET.SubElement(write_root, "employee", id="101")
ET.SubElement(emp1, "name").text = "Harsha"
ET.SubElement(emp1, "role").text = "Tester"
ET.SubElement(emp1, "experience").text = "5"

emp2 = ET.SubElement(write_root, "employee", id="102")
ET.SubElement(emp2, "name").text = "Amit"
ET.SubElement(emp2, "role").text = "Developer"
ET.SubElement(emp2, "experience").text = "3"

write_tree = ET.ElementTree(write_root)
ET.indent(write_tree, space="    ", level=0)

with open(
    r"C:\Users\Sujan Kumar Reddy\PycharmProjects\PythonAdvancedProgramming\Dataformats\writexml.xml",
    "wb"
) as file:
    write_tree.write(file, encoding="utf-8", xml_declaration=True)

# =======================
# UPDATE XML
# =======================
update_path = r"C:\Users\Sujan Kumar Reddy\PycharmProjects\PythonAdvancedProgramming\Dataformats\updatexml.xml"

# Create base XML if file is empty
if not os.path.exists(update_path) or os.stat(update_path).st_size == 0:
    base_root = ET.Element("employees")
    base_tree = ET.ElementTree(base_root)
    with open(update_path, "wb") as file:
        base_tree.write(file, encoding="utf-8", xml_declaration=True)

with open(update_path, "rb") as file:
    update_tree = ET.parse(file)
    update_root = update_tree.getroot()

for emp in update_root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("experience").text = "16"

ET.indent(update_tree, space="    ", level=0)

with open(update_path, "wb") as file:
    update_tree.write(file, encoding="utf-8", xml_declaration=True)
