"""reads a tsp file and returns a list of vertices and a dict of edges with their corresponding costs"""

def read_tsp(tsp_file):
    
    import xmltodict
    
    vertices = []
    edges = {}
    
    with open(tsp_file) as file:
        data = xmltodict.parse(file.read(), dict_constructor=dict)
    
        vertices_dict = data["travellingSalesmanProblemInstance"]["graph"]["vertex"]
        
        for i, vertice in enumerate(vertices_dict):
            vertices.append(i)
            
            for edge in vertice["edge"]:
                edges[(str(i), edge["#text"])] = float(edge["@cost"])
                
                
    return vertices, edges
                
   



