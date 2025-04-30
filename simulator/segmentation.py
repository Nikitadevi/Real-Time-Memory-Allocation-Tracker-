class Segment:
    def __init__(self, base, limit):
        self.base = base
        self.limit = limit

class SegmentationSimulator:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.segments = []

    def allocate_segment(self, size):
        if not self.segments:
            base = 0
        else:
            base = self.segments[-1].base + self.segments[-1].limit
        if base + size <= self.memory_size:
            segment = Segment(base, size)
            self.segments.append(segment)
            print(f"Allocated Segment - Base: {base}, Limit: {size}")
        else:
            print("Memory full. Cannot allocate segment.")
