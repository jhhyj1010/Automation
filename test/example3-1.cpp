#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <iostream>

std::vector<int> getTimes(std::vector<int>& time, std::vector<int>& direction) {
    int n = time.size();
    std::vector<int> result(n, -1);
    std::queue<int> enter_queue, exit_queue;
    int current_time = 0;
    int last_direction = -1; // -1 means turnstile was not used in the previous second

    for (int i = 0; i < n; ++i) {
        if (direction[i] == 0) {
            enter_queue.push(i);
        } else {
            exit_queue.push(i);
        }
    }

    while (!enter_queue.empty() || !exit_queue.empty()) {
        bool used = false;

        if (!exit_queue.empty() && (last_direction == 1 || last_direction == -1 || enter_queue.empty() || time[exit_queue.front()] <= current_time)) {
            int idx = exit_queue.front();
            if (time[idx] <= current_time) {
                result[idx] = current_time;
                exit_queue.pop();
                used = true;
                last_direction = 1;
            }
        }

        if (!used && !enter_queue.empty() && (last_direction == 0 || last_direction == -1 || exit_queue.empty() || time[enter_queue.front()] <= current_time)) {
            int idx = enter_queue.front();
            if (time[idx] <= current_time) {
                result[idx] = current_time;
                enter_queue.pop();
                used = true;
                last_direction = 0;
            }
        }

        if (!used) {
            current_time = std::min(enter_queue.empty() ? INT_MAX : time[enter_queue.front()],
                                    exit_queue.empty() ? INT_MAX : time[exit_queue.front()]);
        } else {
            ++current_time;
        }
    }

    return result;
}

int main() {
    std::vector<int> time = {0, 0, 1, 5};
    std::vector<int> direction = {0, 1, 1, 0};
    std::vector<int> result = getTimes(time, direction);
    for (int i = 0; i < result.size(); i++) {
        std::cout << result[i] << " "<<std::endl;
    }
    return 0;
}