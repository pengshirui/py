def coo2csr(coo_rows, coo_cols, coo_vals):
        # zip and sort
        zipped = zip(coo_rows, coo_cols, coo_vals)
        list = sorted(zipped, key = lambda x: x[0])

        csr_rows = [x[0] for x in list]
        csr_inds = [x[1] for x in list]
        csr_vals = [x[2] for x in list]

        csr_ptrs = []
        rows = max(coo_rows)
        j = 0 
        for i in range(rows + 1):
            csr_ptrs.append(j)
            if i == csr_rows[j]:
                # move to next one
                cur_row = csr_rows[j]
                while j < len(csr_rows) and csr_rows[j] == cur_row:
                    j += 1
            
        csr_ptrs.append(j)
        return csr_ptrs, csr_inds, csr_vals
    

rows   = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]
cols   = [1, 2, 4, 0, 2, 3, 0, 1, 3, 4, 1, 2, 5, 6, 0, 2, 5, 3, 4, 6, 3, 5]
values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
r = coo2csr(rows, cols, values)

B_coo_rows = [2, 2, 2, 5, 5, 5, 6, 6]
B_coo_cols = [5, 0, 3, 1, 4, 6, 2, 3]
B_coo_vals = [1, 1, 1, 1, 1, 1, 1, 1]
r = coo2csr(B_coo_rows, B_coo_cols, B_coo_vals)
assert(r[0] == [0, 0, 0, 3, 3, 3, 6, 8])