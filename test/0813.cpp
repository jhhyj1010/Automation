#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <iostream>

std::vector<int> order(int cityNodes, std::vector<int>& cityFrom, std::vector<int>& cityTo, int company) {
    // Step 1: Create the adjacency list
    std::unordered_map<int, std::vector<int>> graph;
    for (size_t i = 0; i < cityFrom.size(); ++i) {
        graph[cityFrom[i]].push_back(cityTo[i]);
        graph[cityTo[i]].push_back(cityFrom[i]);
    }

    // Step 2: Perform BFS to find the shortest distance from the company to all other cities
    std::vector<int> distance(cityNodes + 1, -1);
    std::queue<int> q;
    q.push(company);
    distance[company] = 0;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        for (int neighbor : graph[current]) {
            if (distance[neighbor] == -1) {
                distance[neighbor] = distance[current] + 1;
                q.push(neighbor);
            }
        }
    }

    // Step 3: Collect all cities with their distances
    std::vector<std::pair<int, int>> cities;
    for (int i = 1; i <= cityNodes; ++i) {
        if (i != company && distance[i] != -1) {
            cities.emplace_back(distance[i], i);
        }
    }

    // Step 4: Sort cities by distance, then by city number
    std::sort(cities.begin(), cities.end());

    // Step 5: Extract the sorted city numbers
    std::vector<int> result;
    for (const auto& city : cities) {
        result.push_back(city.second);
    }

    return result;
}

/*
int main() {
    int cityNodes = 4;
    std::vector<int> cityFrom = {1, 2, 2};
    std::vector<int> cityTo = {2, 3, 4};
    int company = 1;

    std::vector<int> result = order(cityNodes, cityFrom, cityTo, company);
    for (int city : result) {
        std::cout << city << " ";
    }
    // Output: 2 3 4
    return 0;
}*/