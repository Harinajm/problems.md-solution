def combine_lists(list1, list2):
    """
    Combines two lists of elements based on positional overlap.


    The lists are expected to be sorted by the 'left_position'.
    Elements are combined if more than half of one is contained within the other.
    The combined element takes the position of the element that appears first.


    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.


    Returns:
        list: The new combined list.
    """
    result = []
    i, j = 0, 0  # Pointers for list1 and list2


    while i < len(list1) and j < len(list2):
        e1 = list1[i]
        e2 = list2[j]


        l1, r1 = e1["positions"]
        l2, r2 = e2["positions"]
        len1, len2 = r1 - l1, r2 - l2


        # Calculate the length of the overlap
        overlap_start = max(l1, l2)
        overlap_end = min(r1, r2)
        overlap_len = max(0, overlap_end - overlap_start)


        # Check the combination condition
        if overlap_len > len1 / 2 or overlap_len > len2 / 2:
            # Combine the elements
            # The new element takes the position of the one that starts earlier
            if l1 <= l2:
                new_element = {
                    "positions": [l1, r1],
                    "values": e1["values"] + e2["values"]
                }
            else:
                new_element = {
                    "positions": [l2, r2],
                    "values": e1["values"] + e2["values"]
                }
            result.append(new_element)
            i += 1
            j += 1
        else:
            # If no combination, add the element that comes first and advance its pointer
            if l1 <= l2:
                result.append(e1)
                i += 1
            else:
                result.append(e2)
                j += 1


    # Add any remaining elements from either list
    result.extend(list1[i:])
    result.extend(list2[j:])


    return result


# --- Example Usage ---
if __name__ == "__main__":
    list_a = [
        {"positions": [10, 20], "values": ["A"]},
        {"positions": [30, 40], "values": ["B"]},
        {"positions": [50, 65], "values": ["C"]}
    ]


    list_b = [
        {"positions": [12, 25], "values": ["X"]}, # Overlaps with A significantly
        {"positions": [45, 55], "values": ["Y"]}, # Overlaps with C, but not enough
        {"positions": [80, 90], "values": ["Z"]}
    ]


    combined_list = combine_lists(list_a, list_b)
   
    import json
    print("List A:\n", json.dumps(list_a, indent=4))
    print("\nList B:\n", json.dumps(list_b, indent=4))
    print("\nCombined List:\n", json.dumps(combined_list, indent=4))
   
    # Expected output explanation:
    # 1. A([10,20]) and X([12,25]) overlap by 8 units (from 12 to 20).
    #    Length of A is 10. Overlap (8) > 10/2 (5). So they combine.
    #    The combined element takes A's position [10, 20] and values ["A", "X"].
    # 2. B([30,40]) is added next as it comes before Y.
    # 3. Y([45,55]) and C([50,65]) overlap by 5 units (from 50 to 55).
    #    Length of Y is 10. Overlap (5) is not > 10/2 (5).
    #    Length of C is 15. Overlap (5) is not > 15/2 (7.5).
    #    They do not combine. Y is added first as it starts earlier.
    # 4. C([50,65]) is added.
    # 5. Z([80,90]) is added.
