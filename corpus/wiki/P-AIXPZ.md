---
schema: qual/card@1
id: P-AIXPZ
kind: problem
title: "Let $A$ be a square matrix over the complex numbers. Suppose\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $A$ be a square matrix over the complex numbers.
Suppose that $A$ is nonsingular
and that $A^{2019}$ is diagonalizable over $\CC$.

Show that $A$ is also diagonalizable over $\CC$.

:::{.concept}
\envlist

- $A$ is diagonalizable iff $\min_A(x)$ is separable.
  - See [further discussion here](https://math.stackexchange.com/questions/3027664/if-a-is-invertible-and-an-is-diagonalizable-then-a-is-diagonalizable).

:::

:::{.solution}
\envlist

:::{.claim}
If $A \in \Gl(m, \FF)$ is invertible and $A^n/\FF$ is diagonalizable, then $A/\FF$ is diagonalizable.
:::


:::{.proof title="of claim"}
- Let $A \in \Gl(m, \FF)$. 
- Since $A^n$ is diagonalizable, $\min_{A^n}(x) \in \FF[x]$ is separable and thus factors as a product of $m$ **distinct** linear factors:
\[
\min_{A^n}(x) = \prod_{i=1}^m (x-\lambda_i), \quad \min_{A^n}(A^n) = 0
\]

  where $\theset{\lambda_i}_{i=1}^m \subset \FF$ are the **distinct** eigenvalues of $A^n$.

- Moreover $A\in \GL(m,\FF) \implies A^n \in \GL(m,\FF)$: $A$ is invertible $\iff \det(A) = d \in \FF\units$, and so $\det(A^n) = \det(A)^n = d^n \in \FF\units$ using the fact that the determinant is a ring morphism $\det: \mat (m\times m) \to\FF$ and $\FF\units$ is closed under multiplication.

- So $A^n$ is invertible, and thus has trivial kernel, and thus zero is not an eigenvalue, so $\lambda_i \neq 0$ for any $i$.

- Since the $\lambda_i$ are distinct and nonzero, this implies $x^k$ is not a factor of $\mu_{A^n}(x)$ for any $k\geq 0$. 
Thus the $m$ terms in the product correspond to precisely $m$ **distinct linear** factors.

- We can now construct a polynomial that annihilates $A$, namely
$$
q_A(x) \definedas \min_{A^n}(x^n) = \prod_{i=1}^m (x^n-\lambda_i) \in \FF[x],
$$

  where we can note that $q_A(A) = \min_{A^n}(A^n) = 0$, and so $\min_A(x) \divides q_A(x)$ by minimality.


:::{.claim}
$q_A(x)$ has exactly $nm$ distinct linear factors in $\FFbar[x]$
:::


- This reduces to showing that no pair $x^n-\lambda_i, x^n-\lambda_j$ share a root.
and that $x^n-\lambda_i$ does not have multiple roots.

- For the first claim, we can factor
  \[
  x^n - \lambda_i = \prod_{k=1}^n (x - \lambda_i^{1\over n} e^{2\pi i k \over n}) \definedas \prod_{k=1}^n (x-\lambda^{1\over n} \zeta_n^k)
  ,\]
  where we now use the fact that $i\neq j \implies \lambda_i^{1\over n} \neq \lambda_j^{1\over n}$. 
  Thus no term in the above product appears as a factor in $x^n - \lambda_j$ for $j\neq i$.

- For the second claim, we can check that $\dd{}{x}\qty{x^n - \lambda_i} = nx^{n-1}\neq 0\in \FF$, and $\gcd(x^n-\lambda_i, nx^{n-1}) = 1$ since the latter term has only the roots $x=0$ with multiplicity $n-1$, whereas $\lambda_i\neq 0 \implies$ zero is not a root of $x^n-\lambda_i$.

But now since $q_A(x)$ has exactly distinct linear factors in $\bar \FF[x]$ and $\min_A(x) \divides q_A(x)$, $\min_A(x) \in \FF[x]$ can only have distinct linear factors, and $A$ is thus diagonalizable over $\FF$.

:::



:::
