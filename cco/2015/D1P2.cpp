#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
	Edge(int from, int to, int dist): from(from), to(to), dist(dist) {}
	Edge() {}
	bool operator<(const Edge other) const {
		return dist < other.dist;
	}
	int from, to, dist;
};

class Graph {
public:
	Graph(int n): V(n) {
		nodes.resize(V);
	}
	void addEdge(int a, int b, int dist) {
		nodes[a].emplace_back(a, b, dist);
	}
	int V;
	vector<vector<Edge>> nodes;
};

int main() {
	int cities, roads;
	cin >> cities >> roads;

	Graph graph(cities);

	for (int i = 0; i < roads; i++) {
		int a, b, dist;
		cin >> a >> b >> dist;
		graph.addEdge(a, b, dist);
	}

	vector<int> distTo(cities, 0);

	priority_queue<Edge> edges;
}