import random

class PagingSimulator:
    def __init__(self, memory_size, page_size, num_pages):
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_pages = num_pages
        self.page_table = {}
        self.memory = [None] * memory_size

    def allocate_page(self, process_id):
        if len(self.page_table) >= self.num_pages:
            print("Page table is full. Performing replacement.")
            self.replace_page(process_id)
        else:
            page_number = len(self.page_table)
            frame_number = random.randint(0, self.memory_size - 1)
            self.page_table[process_id] = (page_number, frame_number)
            self.memory[frame_number] = process_id
            print(f"Allocated page {page_number} for Process {process_id} at Frame {frame_number}")

    def replace_page(self, process_id):
        victim = random.choice(list(self.page_table.keys()))
        frame_number = self.page_table[victim][1]
        del self.page_table[victim]
        self.memory[frame_number] = process_id
        print(f"Replaced Process {victim} with Process {process_id} at Frame {frame_number}")
