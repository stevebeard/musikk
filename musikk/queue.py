class Queue():

    def __init__(self):
        self.__queue = []
        self.__index = 0

    def get_items(self):
        return self.__queue.copy()

    def add_items(self, items, append=False):
        if not append:
            self.clear()
        for item in items:
            self.__queue.append(item)

    def size(self):
        return len(self.__queue)

    def clear(self):
        self.__queue.clear()
        # reset index
        self.__index = 0

    def get_index(self):
        return self.__index

    def get_item(self, index):
        if index < 0 or index >= len(self.__queue):
            return None
        return self.__queue[index]

    def set_index(self, index):
        _item = self.get_item(index)
        if _item is not None:
            self.__index = index
        return _item

    def get_current(self):
        try:
            return self.__queue[self.__index]
        except IndexError:
            return None

    def get_next(self):
        return self.get_item(self.__index + 1)

    def next(self):
        _next = self.get_next()
        if _next is not None:
            self.__index += 1
        return _next

    def get_previous(self):
        return self.get_item(self.__index - 1)

    def previous(self):
        _previous = self.get_previous()
        if _previous is not None:
            self.__index -= 1
        return _previous

