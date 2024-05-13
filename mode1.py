from landsites import Land


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sites
        self.adventurers = adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
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
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
