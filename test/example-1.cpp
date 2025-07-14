#include <vector>
#include <unordered_map>
#include <set>
#include <iostream>

std::vector<int> getStaleServerCount(int n, std::vector<std::vector<int>>& log_data, std::vector<int>& query, int x) {
    // Step 1: Create a mapping of each server to the times it received requests
    std::unordered_map<int, std::set<int>> server_logs;
    for (const auto& log : log_data) {
        int server_id = log[0];
        int time = log[1];
        server_logs[server_id].insert(time);
    }

    std::vector<int> result;
    
    // Step 2: Process each query
    for (const auto& q : query) {
        int start_time = q - x;
        int end_time = q;
        int stale_count = 0;

        // Step 3: Check each server
        for (int server_id = 1; server_id <= n; ++server_id) {
            bool is_stale = true;
            if (server_logs.find(server_id) != server_logs.end()) {
                for (const auto& time : server_logs[server_id]) {
                    if (time >= start_time && time <= end_time) {
                        is_stale = false;
                        break;
                    }
                }
            }
            if (is_stale) {
                ++stale_count;
            }
        }
        
        // Step 4: Store the result for the current query
        result.push_back(stale_count);
    }
    
    return result;
}

int main() {
    int n = 3;
    std::vector<std::vector<int>> log_data = {{1, 1}, {2, 2}, {3, 3}, {1, 4}, {2, 5}, {3, 6}};
    std::vector<int> query = {3, 6, 9};
    int x = 2;
    std::vector<int> result = getStaleServerCount(n, log_data, query, x);
    for (int i = 0; i < result.size(); i++) {
        std::cout << result[i] << " ";
    }
    return 0;
}