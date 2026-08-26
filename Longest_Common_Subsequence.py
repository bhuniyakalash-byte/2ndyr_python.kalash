def find_lcs(s1, s2):
    m = len(s1)
    n = len(s2)

    # Initialize the (m+1) x (n+1) DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse because we traced backwards from the end
    lcs_chars.reverse()
    lcs_string = "".join(lcs_chars)

    return dp[m][n], lcs_string


if __name__ == "__main__":
    # Test inputs (e.g., standard lab manual strings: "ABCBDAB" and "BDCABA")
    seq1 = input("Enter first sequence: ").strip()
    seq2 = input("Enter second sequence: ").strip()

    if not seq1 or not seq2:
        print("Sequences cannot be empty.")
    else:
        length, lcs = find_lcs(seq1, seq2)
        print("\n--- LCS Result ---")
        print(f"Length of LCS: {length}")
        print(f"Longest Common Subsequence: {lcs}")