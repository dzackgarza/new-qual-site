---
schema: qual/card@1
id: P-BKF05-3B
kind: problem
title: Realizable pairs of characteristic and minimal polynomials
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained criterion and construction. Necessity
    is m|p plus equality of root sets; sufficiency is realized by one Jordan
    block of the required maximal size for each eigenvalue and scalar blocks
    for the remaining multiplicity.
---

::: {.problem}
For which pairs of monic polynomials \((p(x),m(x))\) over \(\mathbb C\) does there exist a matrix \(A\in M_n(\mathbb C)\) whose characteristic polynomial is \(p\) and whose minimal polynomial is \(m\)?
:::

::: {.solution}

::: pf

::: {.pf-step #necessary-degree-and-divisibility}
If such a matrix $A\in M_n(\CC)$ exists, then
$$
\deg p=n
\qquad\text{and}\qquad
m\mid p.
$$

::: pf-proof
The characteristic polynomial of an $n\times n$ matrix is monic of
degree $n$, so $\deg p=n$.

By the Cayley--Hamilton theorem,
$$
p(A)=0.
$$
Divide $p$ by the minimal polynomial:
$$
p=qm+r,
\qquad
\deg r<\deg m.
$$
Evaluating at $A$ gives
$$
0=p(A)=q(A)m(A)+r(A)=r(A).
$$
By the defining minimality of $m$, no nonzero polynomial of degree
less than $\deg m$ annihilates $A$. Hence $r=0$, so $m\mid p$.
:::

:::

::: {.pf-step #root-of-p-is-root-of-m}
If such a matrix exists, every root of $p$ is a root of $m$.

::: pf-proof
Let $\lambda$ be a root of $p$. Over $\CC$, this means that
$\lambda$ is an eigenvalue of $A$. Choose a nonzero eigenvector $v$:
$$
Av=\lambda v.
$$
Since $m(A)=0$,
$$
0=m(A)v=m(\lambda)v.
$$
Because $v\ne0$, one has $m(\lambda)=0$.
:::

:::

::: {.pf-step #necessary-conditions-combined}
Thus the necessary conditions are
$$
\deg p=n,\qquad m\mid p,
$$
and $p,m$ have the same set of roots.

::: pf-proof
Steps [](#necessary-degree-and-divisibility){.pf-ref} and [](#root-of-p-is-root-of-m){.pf-ref} give the first two assertions and show that every
root of $p$ is a root of $m$. Conversely, because $m\mid p$, every
root of $m$ is a root of $p$. Hence their root sets are equal.
:::

:::

::: {.pf-step #factor-exponents}
Assume the conditions in step [](#necessary-conditions-combined){.pf-ref}. Write
$$
p(x)=\prod_{j=1}^d(x-\lambda_j)^{n_j},
$$
where the $\lambda_j$ are distinct. Then
$$
m(x)=\prod_{j=1}^d(x-\lambda_j)^{r_j}
$$
for integers
$$
1\le r_j\le n_j.
$$

::: pf-proof
The common-root condition forces precisely the same distinct linear
factors to occur in $p$ and $m$. Since $m\mid p$, the exponent of each
factor in $m$ is at most its exponent in $p$. Each exponent in $m$ is
positive because each $\lambda_j$ is a root of $m$.
:::

:::

::: {.pf-step #A-char-poly-is-p}
For each $j$, let
$$
A_j
=
J_{r_j}(\lambda_j)
\oplus
\lambda_j I_{n_j-r_j},
$$
where the second summand is omitted when $r_j=n_j$, and set
$$
A=A_1\oplus\cdots\oplus A_d.
$$
Then the characteristic polynomial of $A$ is $p$.

::: pf-proof
The block $J_{r_j}(\lambda_j)$ has characteristic polynomial
$(x-\lambda_j)^{r_j}$, while
$\lambda_j I_{n_j-r_j}$ has characteristic polynomial
$(x-\lambda_j)^{n_j-r_j}$. Hence
$$
\chi_{A_j}(x)=(x-\lambda_j)^{n_j}.
$$
Characteristic polynomials multiply under direct sums, so
$$
\chi_A(x)
=
\prod_{j=1}^d(x-\lambda_j)^{n_j}
=
p(x).
$$
Also
$$
\sum_{j=1}^d n_j=\deg p=n,
$$
so $A$ is indeed an $n\times n$ matrix.
:::

:::

::: {.pf-step #A-min-poly-is-m}
The minimal polynomial of the matrix $A$ from step [](#A-char-poly-is-p){.pf-ref} is
$m$.

::: pf-proof
For a Jordan block $J_{r_j}(\lambda_j)$, the minimal polynomial is
$(x-\lambda_j)^{r_j}$. The scalar block
$\lambda_j I_{n_j-r_j}$, when present, has minimal polynomial
$x-\lambda_j$, which divides $(x-\lambda_j)^{r_j}$. Therefore
$$
\mu_{A_j}(x)=(x-\lambda_j)^{r_j}.
$$

The minimal polynomial of a direct sum is the least common multiple of
the minimal polynomials of its summands. Since the factors
$x-\lambda_j$ are pairwise distinct,
$$
\mu_A(x)
=
\operatorname{lcm}_{1\le j\le d}
(x-\lambda_j)^{r_j}
=
\prod_{j=1}^d(x-\lambda_j)^{r_j}
=
m(x).
$$
:::

:::

::: {.pf-step #classification}
Therefore such a matrix exists exactly for the pairs satisfying
$$
\boxed{
\deg p=n,\qquad
m\mid p,\qquad
\{\text{roots of }m\}=\{\text{roots of }p\}
}.
$$

::: pf-proof
Necessity is step [](#necessary-conditions-combined){.pf-ref}. Under those conditions, steps [](#factor-exponents){.pf-ref}, [](#A-char-poly-is-p){.pf-ref} and [](#A-min-poly-is-m){.pf-ref}
construct an $A\in M_n(\CC)$ with characteristic polynomial $p$ and
minimal polynomial $m$, proving sufficiency.
:::

:::

::: pf-qed
Step [](#classification){.pf-ref} gives the complete classification.
:::

:::

:::
