import numpy as np
from string import ascii_letters
from random import randint, choices
from typing import List, Tuple, Union
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def r_str(alpha: str = ascii_letters,
          val_range: Tuple[int, int] = (1, 200)) -> str:
    '''
    Produces a random string of characters of random length

    Parameters:
    * alpha: a string that contains possible characters
    \t* e.g., 'ACGU' or 'abcdeEF'
    * range: range of possible values to as a length
    \t* e.g., (1, 40), (3, 3) etc. (note ends are inclusive)
    '''
    a, b = val_range
    length = randint(a, b)

    r_str: str = ''.join(choices(alpha, k=length))

    return r_str


def pad_sequences(sequences: 'List[List[str]]',
                  pad_type: Literal['end', 'symmetric', 'dual'],
                  *,
                  pad_str: str = 'AU',
                  pad_length: Union[int, Literal['max']] = 148) -> 'List[str]':
    '''
    Pads a list of sequences represented as a list of strings.

    Parameters:
    * sequences: list of sequences, each represented as a list of strings
    * pad_type: how the sequences should be padded
    \t* end: adds the padding to the end of the sequence
    \t* symmetric: adds the padding between 'chunks' of the sequence
    \t* dual: pads both the end and beginning equally
    * pad_str: the text to pad with
    * pad_length: 'max' or int
    \t* Max finds the length of the largest input sequence and
    \t  formats to that length

    Return: a list of formatted sequences as strings
    '''
    r_list = []

    if pad_length == 'max':
        sequences_as_str = [''.join(s) for s in sequences]
        max_len = max(sequences_as_str, key=lambda x: len(x))
        pad_length = len(max_len)

    if pad_type == 'end':
        sequences: 'List[str]' = [''.join(s) for s in sequences]
        for sequence in sequences:
            length = len(sequence)

            if length < pad_length:
                add_pad_length = pad_length - length

                additonal_padding = [pad_str] * \
                    ((add_pad_length // len(pad_str)) + 1)
                additonal_padding = ''.join(additonal_padding)
                additonal_padding = additonal_padding[:add_pad_length]

                r_list.append(sequence + additonal_padding)
            if length > pad_length:
                r_list.append(sequence[:pad_length])
            if length == pad_length:
                r_list.append(sequence)

    elif pad_type == 'dual':
        sequences: 'List[str]' = [''.join(s) for s in sequences]
        for sequence in sequences:
            length = len(sequence)

            if length < pad_length:
                add_pad_length = pad_length - length

                pad_rep = ((add_pad_length // (len(pad_str))) + 1)

                pre_reps = pad_rep // 2
                post_reps = pre_reps + 1 if pad_rep % 2 == 1 else pre_reps

                pre_str = ''.join([pad_str] * pre_reps)
                post_str = ''.join([pad_str] * post_reps)

                r_list.append((pre_str + sequence + post_str)[:pad_length])
            if length > pad_length:
                r_list.append(sequence[:pad_length])
            if length == pad_length:
                r_list.append(sequence)

    elif pad_type == 'symmetric':
        num_chunks = len(sequences)
        for sequence in sequences:
            length = len(''.join(sequence))

            if length < pad_length:
                add_pad_length = pad_length - length

                num_sub_chunk = \
                    (add_pad_length // ((num_chunks - 1) * len(pad_str)))

                symmetric_possible = num_sub_chunk > 1

                if not symmetric_possible:
                    p_seq = pad_sequences([sequence],
                                          'end',
                                          pad_str=pad_str,
                                          pad_length=pad_length)
                    p_seq = p_seq[0]

                else:
                    p_seq = [item
                             for pair in
                             zip(sequence,
                                 [pad_str] *
                                 ((num_chunks - 1) * num_sub_chunk))
                             for item in pair][:-1]

                    p_seq = ''.join(p_seq)

                    if len(p_seq) < pad_length:
                        p_seq = pad_sequences([p_seq],
                                              'end',
                                              pad_str=pad_str,
                                              pad_length=pad_length)
                        p_seq = p_seq[0]

                r_list.append(p_seq)

            if length > pad_length:
                r_list.append((''.join(sequence))[:pad_length])
            if length == pad_length:
                r_list.append(''.join(sequence))

    else:
        raise ValueError(f'Undefined padding type: {pad_type}. '
                         f'Must be one of \'end\', \'symmetric\', '
                         'or \'dual\'.')

    return r_list


def batch_encode(data_batch: 'list[str]',
                 encoding_type: Literal['onehot', 'label'] = 'onehot'):
    '''
    Batch encodes a list of RNA Sequences to onehot (default) or labels
    '''

    # Ensure that data has been properly padded/averaged before use
    lens = {len(x) for x in data_batch}
    if len(lens) != 1:
        raise ValueError('String Sequences should be of the same length.')

    # Convert to array
    data_batch = [np.array(list(data)) for data in data_batch]

    # Encode to labels
    label_encoder = LabelEncoder()
    data_batch = [label_encoder.fit_transform(data) for data in data_batch]

    if encoding_type == 'label':
        return data_batch

    # If desired, (assumed default) one_hot encode
    try:
        onehot_encoder = OneHotEncoder(sparse=False, categories='auto')
    except TypeError:
        onehot_encoder = OneHotEncoder(sparse_output=False, categories='auto')

    data_batch = [data.reshape(-1, 1) for data in data_batch]
    data_batch = [onehot_encoder.fit_transform(data) for data in data_batch]

    return data_batch


# Unit testing
if __name__ == '__main__':
    from sys import argv

    test_batch = [r_str('-') for _ in range(20)]

    verbose = '-v' in argv or '--verbose' in argv

    if verbose:
        for x in test_batch:
            print(len(x))

    for length_type in [145, 'max']:
        for p_type in ['end', 'symmetric', 'dual']:
            try:
                padded = pad_sequences(test_batch,
                                       p_type,
                                       pad_length=length_type)
            except NotImplementedError:
                print(f'Skipping unimplemented \'{p_type}\'.\n')
                continue
            max_length = len(max(test_batch, key=lambda x: len(x)))

            v_lengths = [len(val) == length_type for val in padded] \
                if length_type == 145 \
                else [len(val) == max_length for val in padded]

            try:
                assert all(v_lengths)
            except AssertionError:
                print(f'Failed test for \'{p_type}\''
                      f' with \'{length_type}\' length.\n')
                continue

            print(f'Succeeded \'{p_type}\' with \'{length_type}\' length.')
            if verbose:
                for val in padded:
                    print(f'{len(val)}: {val}')

            print()
