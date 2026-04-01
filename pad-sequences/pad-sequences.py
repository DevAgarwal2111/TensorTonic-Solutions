import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0:
        return np.array([]).reshape(0, 0)
        
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    N = len(seqs)
    result = np.full((N, max_len), pad_value)

    for i in range (len(seqs)):
        for j in range (len(seqs[i])):
            if(j>=max_len):
                break
            result[i][j] = seqs[i][j]

    return result
    pass