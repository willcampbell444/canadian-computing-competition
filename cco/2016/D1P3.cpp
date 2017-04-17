#include <vector>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

struct Edge {
	Edge() {};
	Edge(int from, int to): from(from), to(to) {};
	int from, to;
};

class Graph {
public:
	Graph(int v) {
		V = v;
		nodes.resize(V);		
	}
	void addEdge(int a, int b) {
		nodes[a].push_back(Edge(a, b));
		nodes[b].push_back(Edge(b, a));
	}
	vector<vector<Edge>> nodes;
	int V;
};

bool flask(Graph g) {
	return false;
}

bool fox(Graph g) {
	// vector<bool> visited(g.V, false);
	// vector<Edge> toSearch;
	// toSearch.emplace_back(-1, 0);
	// visited[0] = true;
	// while (!toSearch.empty()) {
	// 	Edge x = toSearch.back();
	// 	toSearch.pop_back();
	// 	for (Edge e: g.nodes[x.to]) {
	// 		if (visited[e.to] && x.from != e.to) {
	// 			int z = e.from;
	// 			int above = 0;
	// 			if (g.nodes[e.to].size() >= 3) {
	// 				above = 1;
	// 			}
	// 			while(z != e.to) {
	// 				cout << from[-1] << endl;
	// 				if (g.nodes[z].size() >= 3) {
	// 					above += 1;
	// 				}
	// 				z = from[z];
	// 			}
	// 			if (above >= 2) {
	// 				return true;
	// 			}
	// 		} else if (!visited[e.to]) {
	// 			toSearch.push_back(e);
	// 			visited[e.to] = true;
	// 			from[e.to] = e.from;
	// 		}
	// 	}
	// }
	return false;
}

bool sun(Graph g) {
	vector<bool> visited(g.V, false);
	queue<Edge> toSearch;
	toSearch.emplace(-1, 0);
	visited[0] = true;
	while (!toSearch.empty()) {
		Edge x = toSearch.front();
		toSearch.pop();
		for (Edge e: g.nodes[x.to]) {
			if (visited[e.to] && x.from != e.to) {
				bool success = true;
				for (Edge e2: g.nodes[x.from]) {
					if (e2.to == e.to) {
						success = false;
						break;
					}
				}
				if (success) {
					return true;
				}
			} else if (!visited[e.to]) {
				toSearch.push(e);
				visited[e.to] = true;
			}
		}
	}
	return false;
}

bool moon(Graph g) {
	vector<bool> visited(g.V, false);
	queue<Edge> toSearch;
	toSearch.emplace(-1, 0);
	visited[0] = true;
	while (!toSearch.empty()) {
		Edge x = toSearch.front();
		toSearch.pop();
		for (Edge e: g.nodes[x.to]) {
			if (visited[e.to] && x.from != e.to) {
				return true;
			} else if (!visited[e.to]) {
				toSearch.push(e);
				visited[e.to] = true;
			}
		}
	}
	return false;
}

bool talon(Graph g) {
	for (int i = 0; i < g.V; i++) {
		if (g.nodes[i].size() >= 3) {
			return true;
		}
	}
	return false;
}

int main() {
	int task, num_cases;
	cin >> task >> num_cases;

	for (int c = 0; c < num_cases; c++) {
		int num_cities, num_roads;
		cin >> num_cities >> num_roads;

		Graph g(num_cities);

		for (int i = 0; i < num_roads; i++) {
			int a, b;
			cin >> a >> b;

			g.addEdge(a-1, b-1);
		}

		if (task == 1) {
			if (flask(g)) {
				cout << "YES" << endl;
			} else {
				cout << "NO" << endl;
			}
		} else if (task == 2) {
			if (moon(g)) {
				cout << "YES" << endl;
			} else {
				cout << "NO" << endl;
			}
		} else if (task == 3) {
			if (sun(g)) {
				cout << "YES" << endl;
			} else {
				cout << "NO" << endl;
			}
		} else if (task == 4) {
			if (talon(g)) {
				cout << "YES" << endl;
			} else {
				cout << "NO" << endl;
			}
		} else if (task == 5) {
			if (fox(g)) {
				cout << "YES" << endl;
			} else {
				cout << "NO" << endl;
			}
		}
	}
}