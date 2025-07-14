/*An university has exactly one turnstile. It can be used either as an exit or an entrance. Unfortunately, sometimes many people want to pass through the turnstile and their directions can be different. The ith person comes to the turnstile at time[i] and wants to either exit the university if direction[i]=1 or enter the university if direction[i]=0. People form 2 queues, one to exit and one to enter. They are ordered by the time when they came to the turnstile and, if the times are equal, by their indices. If some person wants to enter the university and another person wants to leave the university at the same moment, there are three cases:
 1. If in the previous second the turnstile was not used (maybe it was used before, but not at the previous second), then the person who wants to leave goes first.
 2. If in the previous second the turnstile was used as an exit, then the person who wants to leave goes first.
 3. If in the previous second the turnstile was used as an entrance, then the person who wants to enter goes first.

Passing through the turnstile takes 1 second.
For each person, find the time when they will pass through the turnstile.

Function description:
Complete the function getTimes, it has the following parameters:
  int time[n], an array of n integer where the value at index i is the time in seconds when the ith person will come to the turnstile.
  int direction[n]: an array of n integer where the value at index i is the direction of the ith person.
  
Returns:
  int[n]: an array of n integers where the value at index i is the time when the ith person will pass the turnstile.
  
Constraints:
  1. 1<=n<=100000
  2. 0<=time[i] <= 1000000000 for 0 <=i<=n-1
  3. time[i] <= time[i+1] for 0<=i<=n-2
  4. 0 <= direction[i]<=1 for 0<=i<=n-1
*/
#include <vector>
#include <queue>

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