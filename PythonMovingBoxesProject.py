"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150167534
Name:       Mikel Robredo Manero
Email:      pqmiro@tuni.fi

Student Id: 150360467
Name:       Edna Toscano
Email:      edna.toscanocabrera@tuni.fi

12.5 ⌚⌚⌚ Moving Boxes
This program creates a dictionary in which different boxes will be stored.
At the same time, different items will be added to these boxes, and with this,
different operations will be performed.
"""


class MovingBox:
    """
    A class for keeping track of the contents of
    a moving box. Items can be added to, removed from,
    itemized (i.e. listed), and searched from a moving box.
    The number of items in a box can also be queried
    and items can be transferred between two boxes.
    """

    def __init__(self, box_name):
        """
        Initializes the object and sets its attributes.

        :param box_name: str, name of the box object created.
        """

        # The inner dict in which items will be stored.
        inner_dict = {}
        self.__boxname = box_name
        self.__itembox = inner_dict
        # A repeated box name should replace the already stored name and its
        # content in the dictionary since the new object removes completely
        # the old one.

    def add_item(self, item_name, item_count):
        """
        This method adds a newly created item to the target box, in this case,
        the self object. If the name of the item is not in the given, it
        creates a new item in the box, with the input quantity. Otherwise, the
        newly inputted quantity is added to the current quantity of the
        specific item.

        :param item_name: str, name of the item created.
        :param item_count: int, value of the number of that type of item.
        """

        if item_name not in self.__itembox:
            self.__itembox[item_name] = item_count
        else:
            new_count_item = self.__itembox.get(item_name) + item_count
            self.__itembox[item_name] = new_count_item

    def list_content(self):
        """
        Prints the list of the items and their quantity of the given box.
        Then, each item and its quantity is printed, only if the quantity is
        greater than 0.
        """

        total = 0
        for item in self.__itembox:
            total += self.__itembox.get(item)

        print(f"""Box "{self.__boxname}" contains {total} items.""")

        for item in sorted(self.__itembox):
            if self.__itembox.get(item) > 0:
                print(f"""{self.__itembox.get(item):3} {item}""")

    def remove_item(self, item_name, item_count):
        """
        Returns False if the stated conditions are fulfilled:

            -If the name of the item doesn't exist in the box, it returns False.
            -Then if the specified quantity of the item is greater than the
            current quantity in the box, it also returns False.

        Otherwise, this method removes the specified quantity of an item from
        the box.

        :param item_name: str, name of the specified item.
        :param item_count: int, quantity of the specified item.
        :return: boolean, it returns true if the method call has been correctly
        done and false otherwise.
        """

        if item_name not in self.__itembox:
            return False
        else:
            if item_count > self.__itembox[item_name]:
                return False
            else:
                item_to_remove = self.__itembox.get(item_name) - item_count
                self.__itembox.update({item_name: item_to_remove})
                return True

    def transfer_item(self, target_box, item_name, item_count):
        """
        Returns False if the stated conditions are fulfilled:

            -If the name of the item doesn't exist in the box, it returns False.
            -Then if the specified quantity of the item is greater than the
            current quantity in the box, it also returns False.

        Otherwise, this method transfers the specified quantity of an item to
        the target box by using the remove method in the initial box and using
        the add method for the target box.

        :param target_box: obj, the box where the items will be transferred.
        :param item_name: str, name of the item to transfer.
        :param item_count: int, quantity of the item to transfer.
        :return: boolean, it returns true if the method call has been correctly
        done and false otherwise.
        """

        if item_name not in self.__itembox:
            return False
        else:
            if item_count > self.__itembox[item_name]:
                return False
            else:
                self.remove_item(item_name, item_count)
                target_box.add_item(item_name, item_count)
                return True

    def search_item(self, item_name):
        """
        Returns False if the specified item is not in the box. Otherwise, this
        method finds the quantity of a specified item within all the boxes and
        returns it.

        :param item_name: str, name of the specified item.
        :return: returns the box name where the item is located and the
        quantity of the item. If the operation is not correctly done, returns
        False.
        """

        if item_name not in self.__itembox:
            return False
        else:
            return self.__itembox[item_name]


def convert_str_to_int(word):
    """
    Converts the parameter string *word* in to an integer value.
    If conversion is successful returns the resulting integer.
    In the case of an error, returns None.

    :param (str) word: a word supposedly representing an integer value.
    :return: int | NoneType
    """
    try:
        result = int(word)
    except ValueError:
        return None

    return result


# NOTE!
# The following functions have a second parameter whose type is always
# a list containing strings, even in those cases when the list is empty.
# The reason for this is that the command interface
# in the main function was kept very simple: different commands
# require a different number of words of user input. The main function
# just stores all the extra words given after the actual command word in
# the user input line in single list without worrying
# if they are correct or not. This list is then passed as
# a parameter to the actual command functions below. It is their
# job to check that the words in the list makes sense in the context
# of the command in question.


def newbox(all_boxes, list_of_additional_info):
    """
    Creates a new moving box named after the first element in
    the parameter *list_of_additional_info*. The new box is stored
    in the dictionary *all_boxes* using the box's name as the key.
    If *all_boxes* already contains a box with the same name,
    it will be removed and replaced with the new box.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing a single element:
           the name of the moving box (str) to be created.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of initial data: can't create a new box.")
        return

    box_name = list_of_additional_info[0]
    all_boxes[box_name] = MovingBox(box_name)


def add_to_box(all_boxes, list_of_additional_info):
    """
    Adds a new item into a box stored in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is shown.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be added (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't add into a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't add to a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't add to a box.")
        return

    all_boxes[box_name].add_item(item_name, item_count)


def remove_from_box(all_boxes, list_of_additional_info):
    """
    Removes a given amount of named items from a box stored
    in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is displayed.
    If the box exits but doesn't contain the named item,
    then an error message is also displayed.
    If the parameter giving the number of items to be removed
    is larger than what's available in the box, then again
    an error message is displayed.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be removed (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't remove from a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't remove from a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't remove from a box.")
        return

    if not all_boxes[box_name].remove_item(item_name, item_count):
        print("Error: removing an item from a box failed.")


def transfer_from_box_to_another_box(all_boxes, list_of_additional_info):
    """
    Transfers some amount of named items from one moving box to into another.

    :param all_boxes: all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 4 elements:
           the name of the source box (str),
           the name of the target box (str),
           the name of the item to move (str), and
           the number of items to move (str)
    :return: None
    """

    if len(list_of_additional_info) != 4:
        print("Error: wrong number of elements: can't transfer items.")
        return

    source_name, target_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't transfer items.")
        return

    if source_name not in all_boxes or target_name not in all_boxes:
        print("Error: unknown box name: can't transfer items.")

    if not all_boxes[source_name].transfer_item(all_boxes[target_name], item_name, item_count):
        print("Error: item transfer failed for some reason.")


def list_box_content(all_boxes, list_of_additional_info):
    """
    Displays the contents of a single box in *all_boxes*
    dictionary. If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is displayed.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 1 element:
           the name of the box (str)
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't list contents.")
        return

    box_name = list_of_additional_info[0]

    if box_name not in all_boxes:
        print("Error: box does not exist: can't list content.")
        return

    all_boxes[box_name].list_content()


def list_all_boxes(all_boxes, list_of_additional_info):
    """
    Prints the contents of all boxes on the screen.
    The boxes are printed in an alphabetical order.
    The content of each individual box is printed
    in the same format as it is done in the function
    *list_box_content* above.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: An empty list since this function
           does not require any other data than *all_boxes*.
    :return: None
    """

    if len(list_of_additional_info) != 0:
        print("Error: wrong number of elements: boxes not listed.")
        return

    for box_name in sorted(all_boxes):
        list_box_content(all_boxes, [box_name])


def search_all_boxes(all_boxes, list_of_additional_info):
    """
    Searches a particular item in all of the boxes and
    and prints which boxes contained the item and how
    many of it there was. The boxes in *all_boxes* are
    checked in an alphabetical order. If no items are found,
    the function prints nothing.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing one element (str)
           which is the name of the item the function should search for.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't search boxes.")
        return

    item_name = list_of_additional_info[0]

    for box_name in sorted(all_boxes):
        item_count = all_boxes[box_name].search_item(item_name)

        if item_count > 0:
            print(f"Box {box_name}: {item_count}")


def count_specific_items(all_boxes, list_of_additional_info):
    """
    Counts and prints the number of a particular items
    inside all of the boxes contained in *all_boxes*.
    Zero is printed if there are none.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing one element (str)
           which is the name of the item the function should count.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't count items.")
        return

    item_name = list_of_additional_info[0]

    item_count = 0
    for box in all_boxes.values():
        item_count += box.search_item(item_name)

    print(f"There are total {item_count} {item_name}(s) in the boxes.")


def main():
    """
    In this project *main* function contains the top level
    part of the program's user interface.

    **Do not modify the main function in any way: the automated
    tests rely it to behave in a pre-defined way.**
    """
    boxes = {}

    while True:
        command_line = input("next command> ").strip()
        if command_line == "":
            break

        command_words = command_line.split()
        first_word = command_words[0]
        list_of_other_words = command_words[1:]

        if first_word == "quit":
            break

        elif first_word == "newbox":
            newbox(boxes, list_of_other_words)

        elif first_word == "add":
            add_to_box(boxes, list_of_other_words)

        elif first_word == "remove":
            remove_from_box(boxes, list_of_other_words)

        elif first_word == "transfer":
            transfer_from_box_to_another_box(boxes, list_of_other_words)

        elif first_word == "list":
            list_box_content(boxes, list_of_other_words)

        elif first_word == "list_all":
            list_all_boxes(boxes, list_of_other_words)

        elif first_word == "search":
            search_all_boxes(boxes, list_of_other_words)

        elif first_word == "count":
            count_specific_items(boxes, list_of_other_words)

        else:
            print(f"Error: \"{first_word}\" is not a recognized command!")


if __name__ == "__main__":
    main()
