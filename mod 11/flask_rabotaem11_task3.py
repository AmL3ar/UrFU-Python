import logging
import random
import threading
import time

COUNT_SELLERS = 2
COUNT_TICKETS = 3
TOTAL_COUNT_TICKETS = 10

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TicketsOffice:
    def __init__(self):
        self.count_tickets = COUNT_TICKETS
        self.sellers = list()
        self.director = None

    def add_seller(self, seller):
        self.sellers.append(seller)

    def set_direction(self, director):
        self.director = director


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, tickets_office: TicketsOffice):
        super().__init__()
        self.sem = semaphore
        self.tickets_office = tickets_office
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if self.tickets_office.count_tickets <= 0:
                    break
                self.tickets_sold += 1
                self.tickets_office.count_tickets -= 1
                logger.info(f'{self.name} sold one;  {self.tickets_office.count_tickets} left in the tickets office')

        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    @staticmethod
    def random_sleep():
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, sellers, tickets_office):
        super().__init__()
        self.sem = semaphore
        self.sellers = sellers
        self.tickets_office = tickets_office
        self.all_tickets = TOTAL_COUNT_TICKETS
        self.tickets_added = 0
        logger.info('Director started work')

    def run(self):
        is_running = True
        while is_running:
            if self.tickets_office.count_tickets == len(self.sellers):
                with self.sem:
                    tickets = min(self.all_tickets, 10 - self.tickets_office.count_tickets)
                    self.tickets_office.count_tickets += tickets
                    self.all_tickets -= tickets
                    self.tickets_added += tickets
                    logger.info(f'Director added {tickets} tickets in the tickets office; {self.all_tickets} left from the director')
                    if self.all_tickets == 0:
                        is_running = False
        logger.info(f'Director give {self.tickets_added} tickets in the tickets office')


def main():
    tickets_office = TicketsOffice()
    semaphore = threading.Semaphore()

    all_workers = []
    for _ in range(COUNT_SELLERS):
        seller = Seller(semaphore, tickets_office)
        tickets_office.add_seller(seller)
        seller.start()
        all_workers.append(seller)

    director = Director(semaphore, all_workers, tickets_office)
    tickets_office.set_direction(director)
    director.start()
    all_workers.append(director)

    for seller in all_workers:
        seller.join()

if __name__ == '__main__':
    main()
