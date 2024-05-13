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

        # We will track changes to gold and guardians in a temporary structure to avoid mid-iteration updates.
        site_updates = {site.get_name(): [site.get_gold(), site.get_guardians()] for site in self.sites}

        for _ in range(self.n_teams):
            best_score = float('-inf')
            best_choice = (None, 0)  # Option to do nothing

            for site in self.sites:
                current_gold, current_guardians = site_updates[site.get_name()]
                if current_guardians > 0:
                    adventurers_used = min(adventurer_size, current_guardians)
                    gold_received = min((current_gold * adventurers_used) / current_guardians, current_gold)
                else:
                    adventurers_used = adventurer_size
                    gold_received = current_gold

                remaining_adventurers = adventurer_size - adventurers_used
                potential_score = 2.5 * remaining_adventurers + gold_received

                if potential_score > best_score:
                    best_score = potential_score
                    best_choice = (site, adventurers_used)

            results.append(best_choice)
            if best_choice[0]:
                site = best_choice[0]
                _, current_guardians = site_updates[site.get_name()]
                current_gold, _ = site_updates[site.get_name()]
                site_updates[site.get_name()][0] -= gold_received
                site_updates[site.get_name()][1] -= adventurers_used

        # Update the actual site information only after all decisions have been made.
        for site in self.sites:
            updates = site_updates[site.get_name()]
            site.set_gold(updates[0])
            site.set_guardians(updates[1])

        return results

