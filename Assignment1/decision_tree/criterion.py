"""
criterion
"""
import math
def entropy(y):
    """Calculate the entropy for label y"""
    # label y: {label,count}
    total = sum(y.values())
    entropy_val = 0
    for label in y.keys():
        if y[label] > 0:
            entropy_val -= (y[label] / total) * math.log((y[label] / total),2)
    return entropy_val

def get_criterion_function(criterion):
    if criterion == "info_gain":
        return __info_gain
    elif criterion == "info_gain_ratio":
        return __info_gain_ratio
    elif criterion == "gini":
        return __gini_index
    elif criterion == "error_rate":
        return __error_rate


def __label_stat(y, l_y, r_y):
    """Count the number of labels of nodes"""
    left_labels = {}
    right_labels = {}
    all_labels = {}
    for t in y.reshape(-1):
        if t not in all_labels:
            all_labels[t] = 0
        all_labels[t] += 1
    for t in l_y.reshape(-1):
        if t not in left_labels:
            left_labels[t] = 0
        left_labels[t] += 1
    for t in r_y.reshape(-1):
        if t not in right_labels:
            right_labels[t] = 0
        right_labels[t] += 1

    return all_labels, left_labels, right_labels


def __info_gain(y, l_y, r_y):
    """
    Calculate the info gain

    y, l_y, r_y: label array of father node, left child node, right child node
    """
    # node labels are stored as dictionaries
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    info_gain = 0.0
    ###########################################################################
    # TODO:                                                                   #
    # Implement this method. Calculate the info gain if splitting y into      #
    # l_y and r_y                                                             #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    # 结点分裂之后熵是否增加/减少
    left_num = sum(left_labels.values())
    right_num = sum(right_labels.values())
    total = sum(all_labels.values())
    info_gain = entropy(all_labels) - entropy(left_labels) * (left_num/total) - entropy(right_labels) * (right_num/total)
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    return info_gain


def __info_gain_ratio(y, l_y, r_y):
    """
    Calculate the info gain ratio

    y, l_y, r_y: label array of father node, left child node, right child node
    """
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    info_gain = __info_gain(y, l_y, r_y)
    # info gain ration 就是 info gain / 原先的 熵
    ###########################################################################
    # TODO:                                                                   #
    # Implement this method. Calculate the info gain ratio if splitting y     #
    # into l_y and r_y                                                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    if entropy(all_labels) == 0:
        return 0
    info_gain_ratio = info_gain / entropy(all_labels)
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return info_gain_ratio


def __gini_index(y, l_y, r_y):
    """
    Calculate the gini index

    y, l_y, r_y: label array of father node, left child node, right child node
    """
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    before = 0.0
    after = 0.0
    def gini(label):
        # calculate gini val for dict {label,count}
        gini_val = 1
        total = sum(label.values())
        for key in label.keys():
            gini_val -= (label[key] / total) ** 2
        return gini_val
    ###########################################################################
    # TODO:                                                                   #
    # Implement this method. Calculate the gini index value before and        #
    # after splitting y into l_y and r_y                                      #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    before = gini(all_labels)
    after = gini(left_labels) * (sum(left_labels.values())/sum(all_labels.values())) + gini(right_labels) * ((sum(right_labels.values())/sum(all_labels.values())))
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return before - after


def __error_rate(y, l_y, r_y):
    """Calculate the error rate"""
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    before = 0.0
    after = 0.0
    def error_rate(label):
        # calculate error rate for dict label {label,count}
        # error rate  =  1 - max p_i
        max_val = 0
        for key,value in label.items():
            if value > max_val:
                max_val = value
        if sum(label.values()) == 0:
            return 0
        error = 1 - max_val/sum(label.values())
        return error
        
    ###########################################################################
    # TODO:                                                                   #
    # Implement this method. Calculate the error rate value before and        #
    # after splitting y into l_y and r_y                                      #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    before = error_rate(all_labels)
    after = error_rate(left_labels) * (sum(left_labels.values()) / sum(all_labels.values())) + error_rate(right_labels) * (sum(right_labels.values()) / sum(all_labels.values()))
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return before - after
