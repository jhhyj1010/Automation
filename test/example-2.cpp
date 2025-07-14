#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <iostream>

int findLowestPrice(std::vector<std::vector<std::string>>& products, std::vector<std::vector<std::string>>& discounts) {
    std::unordered_map<std::string, std::pair<int, double>> discount_map;
    
    // Parse discounts
    for (const auto& discount : discounts) {
        std::string tag = discount[0];
        int type = std::stoi(discount[1]);
        double amount = std::stod(discount[2]);
        discount_map[tag] = {type, amount};
    }
    
    int total_cost = 0;
    
    // Parse products and calculate minimum cost
    for (const auto& product : products) {
        double base_price = std::stod(product[0]);
        double min_price = base_price;
        
        for (size_t i = 1; i < product.size(); ++i) {
            std::string tag = product[i];
            if (discount_map.find(tag) != discount_map.end()) {
                int type = discount_map[tag].first;
                double amount = discount_map[tag].second;
                
                if (type == 0) {
                    min_price = std::min(min_price, amount);
                } else if (type == 1) {
                    min_price = std::min(min_price, base_price * (1 - amount / 100));
                } else if (type == 2) {
                    min_price = std::min(min_price, base_price - amount);
                }
            }
        }
        
        total_cost += static_cast<int>(std::floor(min_price));
    }
    
    return total_cost;
}

int main() {
    std::vector<std::vector<std::string>> products = {{"100.00", "sale"}, {"200.00", "sale", "clearance"}};
    std::vector<std::vector<std::string>> discounts = {{"sale", "0", "50.00"}, {"clearance", "2", "50.00"}};

    std::vector<std::vector<std::string>> products1 = {{"10", "sale", "jan-sale"}, {"200", "sale", "EMPTY"}};
    std::vector<std::vector<std::string>> discounts1 = {{"sale", "0", "10"}, {"jan-sale", "1", "10"}};
    int result = findLowestPrice(products1, discounts1);
    std::cout << "Result: " << result << std::endl;
    return 0;
}