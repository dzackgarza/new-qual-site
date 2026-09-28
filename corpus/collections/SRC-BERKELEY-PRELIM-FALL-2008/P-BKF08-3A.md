---
schema: qual/card@1
id: P-BKF08-3A
kind: problem
title: Eigenvalues of the skew-symmetric circulant matrix with entries $\pm1$ next to the diagonal
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the cyclic row action on Fourier modes and the Vandermonde
    argument showing that the displayed eigenvectors form a basis.
---

::: {.problem}
Find the eigenvalues of the $n\times n$ matrix $(a_{ij})$, where $n>2$, defined by
$$
a_{ij}=\begin{cases}
1,&j-i\equiv1\pmod n,\\
-1,&j-i\equiv-1\pmod n,\\
0,&\text{otherwise}.
\end{cases}
$$
:::

::: {.hint}
Find sequences $(b_i)$ and complex numbers $z$ such that
$$
(z-z^{-1})b_i=b_{i+1}-b_{i-1},\qquad b_i=b_{i+n}
$$
for all integers $i$.
:::

::: {.solution}
For $k=0,1,\ldots,n-1$, put
$$
\zeta_k\coloneqq e^{2\pi i k/n}
$$
and index coordinates by $r\in\ZZ/n\ZZ$.

<1>1. For each $k$, define
$$
v^{(k)}_r\coloneqq\zeta_k^r
\qquad(r\in\ZZ/n\ZZ).
$$
Then $v^{(k)}$ is a well-defined nonzero vector in $\CC^n$.

::: {.proof}
Since $\zeta_k^n=1$, one has
$$
\zeta_k^{r+n}=\zeta_k^r,
$$
so the coordinate assignment is periodic modulo $n$. Its coordinate at
$r=0$ equals $1$, hence the vector is nonzero.
:::

<1>2. The vector $v^{(k)}$ is an eigenvector of $A=(a_{ij})$ with
eigenvalue
$$
\lambda_k=\zeta_k-\zeta_k^{-1}.
$$

::: {.proof}
In row $r$, the only nonzero entries of $A$ occur in columns $r+1$ and
$r-1$ modulo $n$, with coefficients $1$ and $-1$, respectively. Therefore
$$
\begin{aligned}
(Av^{(k)})_r
&=v^{(k)}_{r+1}-v^{(k)}_{r-1}\\
&=\zeta_k^{r+1}-\zeta_k^{r-1}\\
&=(\zeta_k-\zeta_k^{-1})\zeta_k^r\\
&=\lambda_k v^{(k)}_r.
\end{aligned}
$$
Thus $Av^{(k)}=\lambda_kv^{(k)}$.
:::

<1>3. The vectors
$$
v^{(0)},v^{(1)},\ldots,v^{(n-1)}
$$
form a basis of $\CC^n$.

::: {.proof}
The matrix having these vectors as columns is
$$
V=(\zeta_k^r)_{0\le r,k\le n-1}.
$$
This is a Vandermonde matrix in the distinct numbers
$\zeta_0,\ldots,\zeta_{n-1}$. Hence
$$
\det V
=\prod_{0\le k<\ell\le n-1}(\zeta_\ell-\zeta_k)\ne0.
$$
Thus its columns are linearly independent, and there are $n$ of them in
$\CC^n$.
:::

<1>4. The eigenvalues of $A$, counted with algebraic multiplicity, are
$$
\boxed{
\lambda_k
=2i\sin\!\left(\frac{2\pi k}{n}\right),
\qquad k=0,1,\ldots,n-1
}.
$$

::: {.proof}
By steps <1>2 and <1>3, the basis
$v^{(0)},\ldots,v^{(n-1)}$ diagonalizes $A$ with diagonal entries
$\lambda_0,\ldots,\lambda_{n-1}$. Finally,
$$
\zeta_k-\zeta_k^{-1}
=e^{2\pi i k/n}-e^{-2\pi i k/n}
=2i\sin\!\left(\frac{2\pi k}{n}\right).
$$
This gives the complete eigenvalue multiset, including repetitions.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives exactly the requested eigenvalues.
:::
:::
