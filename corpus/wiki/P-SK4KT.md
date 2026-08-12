---
schema: qual/card@1
id: P-SK4KT
kind: problem
title: "Since $A$ is $2\\times 2$ and has 2 eigenvalues, noting that $\\deg \\chi_A(x) = 2$, we have $\\chi_A(x) = (x-1)(x+1) = x^2 -1$."
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
3. 
   1. Since $A$ is $2\times 2$ and has 2 eigenvalues, noting that $\deg \chi_A(x) = 2$, we have $\chi_A(x) = (x-1)(x+1) = x^2 -1$. The minimal polynomial of $A$ divides $\chi_A(x)$, so we have $\chi_A(A) = 0$ and thus $A^2 - I_2 = 0 \implies A^2 = I_2$.

   2. This will happen when $x^2-1 = (x+1)(x-1)$ is not the minimal polynomial, and we can force the minimal polynomial to be degree 3 by inserting a nontrivial Jordan block to a diagonal matrix containing just the eigenvalues $\pm 1$. An example that works:
   $$
   \left(\begin{array}{rr|r}
      1 & 1 & 0 \\
      0 & 1 & 0 \\
      \hline
      0 & 0 & -1
      \end{array}\right),~ A^2 = \left(\begin{array}{rrr}
        1 & 2 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
        \end{array}\right), \quad
      \spec(A) = [-1, 1, 1]
   $$
   1. Every symmetric matrix with $A$ real spectrum admits a real eigendecomposition $\Lambda D \Lambda^T$, where $D$ is diagonal with entries the eigenvalues of $A$ and $\Lambda$ are orthogonal (which are also invertible). Here, we only need the fact that $A$ is diagonalizable by invertible matrices. In our case we have $[D^2]_{ii} = (\pm 1)^2 = 1$ so $D^2 = I_n$. Thus we have 
   $$A^2 = (\Lambda D \Lambda\inv)^2 = \Lambda D^2 \Lambda\inv = \Lambda I_n \Lambda\inv = I_n. \qed$$ 

