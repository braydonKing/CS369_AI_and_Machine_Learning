import math

ATTRIBUTES = ('Alternative', 'Bar', 'Friday/Saturday', 'Hungry', 'Patrons', 'Price', 'Raining',
              'Reservation', 'Type', 'Wait')


class Datum:
    def __init__(self, target, *values):
        self.target = target
        self.attributes = dict(zip(ATTRIBUTES, values))


data = (Datum(True, True, False, False, True, 'Some', '$$$', False, True, 'French', '0-10'),
        Datum(False, True, False, False, True, 'Full', '$', False, False, 'Thai', '30-60'),
        Datum(True, False, True, False, False, 'Some', '$', False, False, 'Burger', '0-10'),
        Datum(True, True, False, True, True, 'Full', '$', True, False, 'Thai', '10-30'),
        Datum(False, True, False, True, False, 'Full', '$$$', False, True, 'French', '>60'),
        Datum(True, False, True, False, True, 'Some', '$$', True, True, 'Italian', '0-10'),
        Datum(False, False, True, False, False, 'None', '$', True, False, 'Burger', '0-10'),
        Datum(True, False, False, False, True, 'Some', '$$', True, True, 'Thai', '0-10'),
        Datum(False, False, True, True, False, 'Full', '$', True, False, 'Burger', '>60'),
        Datum(False, True, True, True, True, 'Full', '$$$', False, True, 'Italian', '10-30'),
        Datum(False, False, False, False, False, 'None', '$', False, False, 'Thai', '0-10'),
        Datum(True, True, True, True, True, 'Full', '$', False, False, 'Burger', '30-60'))


def impurity(data):
    """
    :param data: A sequence of Datum objects.
    :return: The Gini impurity of the data, as per equation 6.1 on p. 197 of Géron.
    """
    #Gi = 1 - sum of pi,k^2
    p_instances = {}

    for datum in data:
        target = datum.target
        if target in p_instances:
            p_instances[target] += 1
        else:
            p_instances[target] = 1

    k = len(data)

    # Calculate the sum of (pi,k^2) for each target's probability to get Geni impurity
    Gi = 1 - sum((pi / k) ** 2 for pi in p_instances.values())

    return Gi


def split_cost(data, attribute, value):
    """
    :param data: A sequence of Datum objects.
    :param attribute: An attribute on which to split.
    :param value: The value to distinguish from other values at this node.
    :return: The cost of splitting in this way, as per equation 6.2 on p. 200 of Géron.
    """
    left_data = [datum for datum in data if datum.attributes[attribute] == value]
    right_data = [datum for datum in data if datum.attributes[attribute] != value]

    m_left = len(left_data)
    m_right = len(right_data)

    m=len(data)

    left_Gi = impurity(left_data)
    right_Gi = impurity(right_data)

    split_cost_value = (m_left / m) * left_Gi + (m_right / m) * right_Gi

    return split_cost_value

def best_split(data):
    """
    :param data: A sequence of Datum objects.
    :return: The best attribute and value to split on at this node.
    """
    # Hint: Return two values
    best_attribute = None #best_attribute and best_value initialized to None
    best_value = None
    best_split_cost = float('inf') # best_split_cost initialized to very high value

    for attribute in ATTRIBUTES:
        unique_values = set(datum.attributes[attribute] for datum in data)

        for value in unique_values:
            value_cost = split_cost(data, attribute, value)
            if value_cost < best_split_cost:
                best_split_cost = value_cost
                best_attribute = attribute
                best_value = value
    return best_attribute, best_value


class Tree:

    def __init__(self, data):
        # TODO You have to write this to build the tree from data
        # Hint: It's recursive, because you may be building subtree

        self.data = data
        self.left = None
        self.right = None
        self.split_attribute = None
        self.split_value = None
        self.prediction = None


        pass

    def __repr__(self, indent=''):
        # TODO You have to write this
        # Hint: It's recursive. A recursive call might be something like:
        # self.left.__repr__(indent + '  ')
        pass

    def predict(self, datum):
        """
        :param datum: A Datum object.
        :return: The tree's prediction for the attribute values of datum.
        """
        # TODO You have to write this
        # Hint: You guessed it, recursive!


def main():
    tree = Tree(data)
    print(tree)


if __name__ == '__main__':
    main()
