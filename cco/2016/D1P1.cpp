#include <vector>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

class Graph {
public:
	Graph(int v) {
		V = v;
		nodes.resize(V);		
	}
	void addEdge(int a, int b) {
		nodes[a].push_back(b);
		nodes[b].push_back(a);
	}
	vector<vector<int>> nodes;
	int V;
};

int main() {
	int N, M, K;
	cin >> N >> M >> K;

	Graph graph(N);
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		graph.addEdge(a-1, b-1);
	}

	vector<bool> visited(N, false);
	queue<int> toSearch;
	int breaks = 0;
	int count = 0;
	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			bool loop = true;
			int size = 0;
			visited[i] = true;
			toSearch.push(i);
			while (!toSearch.empty()) {
				size++;
				int current = toSearch.front();
				toSearch.pop();
				if (graph.nodes[current].size() == 1) {
					loop = false;
				}
				for (int x: graph.nodes[current]) {
					if (!visited[x]) {
						visited[x] = true;
						toSearch.push(x);
					}
				}
			}
			count += size - (size % K);
			if (loop && size > K) {
				breaks += 1;
			}
			breaks += ceil((float)size/K) - 1;
		}
	}
	cout << count << " " << breaks << endl;
}