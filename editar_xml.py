from lxml import etree

tree = etree.parse(r"C:\Users\922027\Documents\Babis\catalogos_git\catalogo_1\teste_1.xml")
root = tree.getroot()

table = root.find(".//table")

# inclui conteudo da nova coluna
nova_coluna = etree.Element("column")
nova_coluna.set("bdcolname", "NOVA_COLUNA")
nova_coluna.set("bdtype", "VARCHAR2(50)")
nova_coluna.set("dbn0type", "ID")
nova_coluna.set("id", "NOVA_COLUNA")
nova_coluna.set("udn", "novaColuna")

table.append(nova_coluna)

# encontra coluna para excluir
coluna = table.find('.//column[@id="AZIMUTH"]')

table.remove(coluna)

tree.write(
    r"C:\Users\922027\Documents\Babis\catalogos_git\catalogo_1\teste_1.xml",
    encoding="utf-8",
    xml_declaration=True,
    pretty_print=True
)
