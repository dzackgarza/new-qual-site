---
schema: qual/card@1
id: PR-IV6RB
kind: proposition
title: JCF Algorithm for generalized eigenvectors
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
---

:::{.proposition}
The following algorithm always works for computing $\JCF(A)$:

- Compute and factor the characteristic polynomial as $\chi_A(x) = \prod_{i} (x-\lambda_i)^{m_i}$.
- For each $\lambda_i$, find the constant $\ell_i$ such that
\[
\cdots
\rank (A-\lambda_i I)^{\ell_i - 1}
> \rank (A-\lambda_i I)^{\ell_i}
{\color{red} = }
\rank (A-\lambda_i I)^{\ell_i+1}
{\color{red} = }
\rank (A-\lambda_i I)^{\ell_i+1}
{\color{red} = } \cdots
.\]
- Find as many usual eigenvectors $\vector v_i$ as you can.
   The number of eigenvectors you find will be $\dim E_{\lambda_i}$.
  Suppose you just get one, $\vector v$.
- Solve the systems:
\[
(A - \lambda_i I)\vector v_1 = \vector v &\implies \vector v_1 = ? \\
(A - \lambda_i I)^2\vector v_2 = \vector v_1 &\implies \vector v_2 = ? \\
&\vdots \\
,\]
  which can be solved by putting the $\vector v_i$ in an augmented matrix and computing the RREF.
- This terminates in at most $\ell_i$ steps, and these vectors correspond to a single Jordan block.
- If there are other eigenvectors $\vector w, \cdots$ for $\lambda_i$, repeating this process yields a Jordan block for each of them.
  Assemble $P$ by placing these $\vector v_i$ in the appropriate columns.
:::
