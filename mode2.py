from landsites import Land
import random

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_teams = n_teams
        self.sites = []

    def add_sites(self, sites: list[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites.extend(sites)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        results = []
        if not self.sites:
            return [(None, 0)] * self.n_teams  # Handle case with no sites available

        for _ in range(self.n_teams):
            best_score = float('-inf')
            best_choice = (None, 0)  # Option to do nothing

            for site in self.sites:
                if site.get_guardians() > 0:
                    gold_received = min((site.get_gold() * adventurer_size) / site.get_guardians(), site.get_gold())
                else:
                    gold_received = site.get_gold()

                remaining_adventurers = max(0, adventurer_size - site.get_guardians())
                potential_score = 2.5 * remaining_adventurers + gold_received

                if potential_score > best_score:
                    best_score = potential_score
                    best_choice = (site, adventurer_size)

            if best_choice[0]:
                # Update the site's gold and guardians
                site = best_choice[0]
                if site.get_guardians() > 0:
                    gold_received = min((site.get_gold() * adventurer_size) / site.get_guardians(), site.get_gold())
                else:
                    gold_received = site.get_gold()
                
                site.set_gold(site.get_gold() - gold_received)
                site.set_guardians(max(0, site.get_guardians() - adventurer_size))
                results.append(best_choice)
            else:
                results.append(best_choice)

        return results

