import os
import networkx as nx
from flask import Flask, render_template, redirect, url_for, request
from maximum_priority_matching import find_maximum_priority_matching, find_priority_score, find_maximum_priority_matching_bipartite
import matplotlib.pyplot as plt
import re
import ast



app = Flask(__name__)
count = 0


@app.route("/")
def Home():
    return render_template('HomePage.html')


@app.route("/אלגוריתם", methods=['GET', 'POST'])
def Dynamic():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        upload.filename = filename
        file.save(os.path.join('static/txt/', filename))
        return redirect(url_for(upload.__name__))
    else:
        return render_template("Dynamic.html")


@app.route("/אלגוריתם_קובץ", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        upload.filename = filename
        file.save(os.path.join('static/txt/', filename))
        upload.filename = filename
        return redirect(url_for(upload.__name__))
    elif request.method == 'GET':
        if validate_file('static/txt/' + upload.filename):
            variables = execute_commands('static/txt/' + upload.filename)
            G = variables["G"]
            newMatching = find_maximum_priority_matching(G)
            Score = find_priority_score(G)
            Priority = nx.get_node_attributes(G, "priority")
            edge_colors = [ "green" if G[u][v]['isMatched'] else "red" for u,v in G.edges()]
            plt.clf()
            nx.draw(G, with_labels=True, font_weight='bold', edge_color=edge_colors)
            plt.savefig('static/img' + str(count) + '.png')
            image = 'img' + str(count) + '.png'
            count + 1
            Examples = [G, newMatching, Score, Priority, image]
        else:
            Examples = [[{"nodes": "לא תקין","edges":"לא תקין",}],"לא תקין","לא תקין","לא תקין","לא תקין.png"]
    return render_template('Upload.html', Examples=Examples, filename=upload.filename)


upload.filename = 'הקובץ שהוכנס אינו תקין'


@app.route("/אלגוריתם_דוגמא")
def Dynamic1():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('static/txt/', filename))
        upload.filename = filename
        return redirect(url_for(upload.__name__))
    else:
        G = nx.Graph()
        nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),
                 ('7', '3')]
        nodes_attrs = {'1': {"priority": 1}, '2': {"priority": 8}, '3': {"priority": 6}, '4': {"priority": 5},
                       '5': {"priority": 2}, '6': {"priority": 4}, '7': {"priority": 3}, '8': {"priority": 1},
                       '9': {"priority": 7}}
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        nx.set_node_attributes(G, nodes_attrs)
        newMatching = find_maximum_priority_matching(G)
        Score = find_priority_score(G)
        Priority = nx.get_node_attributes(G, "priority")
        edge_colors = [ "green" if G[u][v]['isMatched'] else "red" for u,v in G.edges()]
        labels = nx.get_node_attributes(G, 'priority')
        plt.clf()
        nx.draw(G, with_labels=True, font_weight='bold', edge_color=edge_colors)

        plt.savefig('imageExample.png')
        image = 'imageExample.png'
        count + 1
        Examples = [G, newMatching, Score, Priority, image]
        return render_template("ExampleAlgo.html", Examples=Examples)


@app.route("/אלגוריתם_ראשון")
def Dynamic2():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('static/txt/', filename))
        upload.filename = filename
        return redirect(url_for(upload.__name__))
    else:
        G = nx.Graph()
        nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        edges = [('1', '2'), ('2', '3'), ('3', '4'), ('3', '6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'),
                 ('8', '9'), ('9', '10'), ('10', '11'), ('10', '12'), ('11', '12')]
        nodes_attrs = {'1': {"priority": 1}, '2': {"priority": 2}, '3': {"priority": 1}, '4': {"priority": 1},
                       '5': {"priority": 1}, '6': {"priority": 1}, '7': {"priority": 1}, '8': {"priority": 1},
                       '9': {"priority": 2}, '10': {"priority": 1}, '11': {"priority": 1}, '12': {"priority": 1}}
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        nx.set_node_attributes(G, nodes_attrs)
        newMatching = find_maximum_priority_matching(G)
        Score = find_priority_score(G)
        Priority = nx.get_node_attributes(G, "priority")
        edge_colors = [ "green" if G[u][v]['isMatched'] else "red" for u,v in G.edges()]
        plt.clf()
        nx.draw(G, with_labels=True, font_weight='bold', edge_color=edge_colors)
        plt.savefig('static/imgAlgo1.png')
        image = 'imgAlgo1.png'
        count + 1
        Examples1 = [G, newMatching, Score, Priority, image]
        return render_template("FirstAlgo.html", Examples1=Examples1)


@app.route("/אלגוריתם_שני")
def Dynamic3():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('static/txt/', filename))
        upload.filename = filename
        return redirect(url_for(upload.__name__))
    else:
        G = nx.Graph()
        nodes = ['1', '2', '3', '4', '5', '6']
        edges = [('1', '2'), ('1', '3'), ('2', '4'), ('3', '4'), ('4', '5'), ('4', '6')]
        nodes_attrs = {'1': {"priority": 1, "Group": 1}, '2': {"priority": 2, "Group": 1},
                       '3': {"priority": 3, "Group": 1}, '4': {"priority": 4, "Group": 2},
                       '5': {"priority": 5, "Group": 2}, '6': {"priority": 6, "Group": 2}}
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        nx.set_node_attributes(G, nodes_attrs)
        newMatching = find_maximum_priority_matching_bipartite(G)
        Score = find_priority_score(G)
        Priority = nx.get_node_attributes(G, "priority")
        edge_colors = [ "green" if G[u][v]['isMatched'] else "red" for u,v in G.edges()]
        plt.clf()
        nx.draw(G, with_labels=True, font_weight='bold', edge_color=edge_colors)
        plt.savefig('static/imgAlgo2.png')
        image = 'imgAlgo2.png'
        count + 1
        Examples2 = [G, newMatching, Score, Priority, image]
        return render_template("SecondAlgo.html", Examples2=Examples2)


@app.route("/עבודות")
def Works():
    return render_template("index.html")


def validate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if first line is creating a Graph object
    if not lines[0].strip() == "G = nx.Graph()":
        return False

    # Check if second and third lines define nodes and edges
    if not lines[1].strip().startswith("nodes = ") or not lines[2].strip().startswith("edges = "):
        return False
    nodes = eval(lines[1].strip().split("=")[1])
    edges = eval(lines[2].strip().split("=")[1])

    # Check if fourth line defines node attributes
    if not lines[3].strip().startswith("nodes_attrs = "):
        return False
    nodes_attrs = eval(lines[3].strip().split("=")[1])

    # Check if next three lines add nodes and edges to graph and set node attributes
    if not lines[4].strip() == "G.add_nodes_from(nodes)" or not lines[5].strip() == "G.add_edges_from(edges)" or not lines[6].strip() == "nx.set_node_attributes(G, nodes_attrs)":
        return False

    return True

def execute_commands(file_path):
    if validate_file(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    exec(line)
                except Exception as e:
                    print(f"Error in line {line} : {e}")
        return locals()
    else:
        return



if __name__ == "__main__":
    app.run(debug=True)