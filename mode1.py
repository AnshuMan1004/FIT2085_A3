from landsites import Land


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    
    model1navigator class has been created to allocate adventurers to various land sites based on the gold to guardian ratio.

    Data Structures and Data Types used :
    - sites: list of Land objects, each representing a land site with gold and guardians attributes.
    - adventurers: integer representing the number of adventurers available for allocation.

    Example:
    - If we have 5 sites with different gold and guardians, this method will sort these sites based of the gold-to-guardian ratio and allocate all adventurers accordingly.
    
    Complexity Analysis:
    - The select_sites method has a complexity dominated by the sorting step, which is O(n log n), where n is the number of sites.
    - The select_sites_from_adventure_numbers method calls select_sites for each element in the adventure_numbers list, leading to a complexity of O(m * n log n) where m is the length of adventure_numbers.
    - The update_site method performs constant time operations, resulting in O(1) complexity.
    
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case

        Best Case: O(1) - Initialization is constant time as it only involves setting instance variables.
        Worst Case: O(1) - Similar to the best case, it remains constant time for initialization.
        """
        self.sites = sites
        self.adventurers = adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case

        Best Case: O(n log n) - Sorting dominates the complexity, where n is the number of sites.
        Worst Case: O(n log n) - Similar to the best case due to the sorting step.

        Approach:
        - This method sorts the sites based on the ratio of gold to guardians in descending order.
        - It the iterates through the sorted list and allocates adventurers to each site without exceeding the number of guardians.
        - Finally it then adds remaining sites with zero adventurers.
        
        Example:
        - If there are 5 sites and 15 adventurers, the method sorts the sites by their gold-to-guardian ratio and allocates adventurers to maximize the gold obtained.
        """
        sorted_sites = sorted(self.sites, key=lambda x: (x.get_gold() / x.get_guardians(), x.get_gold()), reverse=True)
        remaining_adventurers = self.adventurers
        chosen_sites = []

        for site in sorted_sites:
            if remaining_adventurers == 0:
                break

            # Allocate as many adventurers as possible but not more than guardians
            adventurers_to_send = min(remaining_adventurers, site.get_guardians())
            chosen_sites.append((site, adventurers_to_send))
            remaining_adventurers -= adventurers_to_send

        # Fill in zero for remaining sites
        for site in sorted_sites:
            if site not in [x[0] for x in chosen_sites]:
                chosen_sites.append((site, 0))

        return chosen_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case 
        
        This method Calculates the gold earned based on different numbers of adventurers.
        
        Best Case: O(m * n log n) - Where m is the length of adventure_numbers and n is the number of sites.
        Worst Case: O(m * n log n) - Similar to the best case due to the repeated sorting step in select_sites.

        Approach:
        - For each number of adventurers in the adventure_numbers list, it temporarily sets the number of adventurers and calls select_sites.
        - It calculates the total gold earned for the selected sites.
        
        Example:
        - If adventure_numbers = [5, 10, 15] and there are 3 sites, the method will compute the gold earned for 5, 10, and 15 adventurers by reallocating them accordingly.
        """
        results = []
        for number in adventure_numbers:
            original_adventurers = self.adventurers
            self.adventurers = number
            selected_sites = self.select_sites()
            gold_earned = 0
            for site, adventurers in selected_sites:
                gold_earned += min(site.get_gold() * adventurers / site.get_guardians(), site.get_gold())
            results.append(gold_earned)
            self.adventurers = original_adventurers
        return results

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case

        Updates the gold and guardians for a given land site.

        Best Case: O(1) - Directly sets the attributes.
        Worst Case: O(1) - Similar to the best case, it involves constant time operations.

        Approach:
        - This method uses the setter methods of the Land class to update the gold and guardians.
        
        Example:
        - If a site initially has 100 gold and 10 guardians, calling update_site(site, 150, 5) will update the site to have 150 gold and 5 guardians.
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
