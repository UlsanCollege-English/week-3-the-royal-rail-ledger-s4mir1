def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    """Build and return a singly linked list from a Python list."""
    sll = SinglyLinkedList()
    if not values:
        return sll

    sll.head = SLLNode(values[0])
    current = sll.head
    for v in values[1:]:
        current.next = SLLNode(v)
        current = current.next

    return sll


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    """Return all values from a singly linked list as a Python list."""
    result: list[int] = []
    current = sll.head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    """Return the first repeated value seen from left to right.

    Return None if no value repeats.
    """
    seen: set[int] = set()
    current = sll.head
    while current is not None:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next
    return None


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    """Remove all nodes whose value equals target.

    Update dll.head and dll.tail correctly.
    Return None.
    """
    current = dll.head
    while current is not None:
        nxt = current.next

        if current.value == target:
            # Update previous link
            if current.prev is not None:
                current.prev.next = current.next
            else:
                dll.head = current.next

            # Update next link
            if current.next is not None:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev

        current = nxt


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    """Stretch: return True if the DLL reads the same forward and backward."""
    left = dll.head
    right = dll.tail

    while left is not None and right is not None:
        if left.value != right.value:
            return False
        if left == right or left.next == right:
            break
        left = left.next
        right = right.prev

    return True