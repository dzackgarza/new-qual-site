---
schema: qual/card@1
id: P-ALGS17E
kind: problem
title: "Jordan canonical form of the square of a Jordan block"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $J$ be an $n \times n$ Jordan block with eigenvalue $\lambda \in \mathbb{C}$.

(a) Suppose that $\lambda \neq 0$.
Show that the Jordan canonical form of $J^2$ is an $n \times n$ Jordan block with eigenvalue $\lambda^2$.

(b) Suppose that $\lambda = 0$.
Show that the Jordan canonical form of $J^2$ has two Jordan blocks with eigenvalue 0; if $n$ is even these Jordan blocks have size $n/2 \times n/2$ and if $n$ is odd one Jordan block has size $(n+1)/2 \times (n+1)/2$ and the other has size $(n-1)/2 \times (n-1)/2$.
:::

::: {.solution}
Write
\[
J=\lambda I+N,
\]
where $N=J_n(0)$ is the nilpotent Jordan block of size $n$.

<1>1. Suppose first that $\lambda\ne0$.
Then
\[
J^2=\lambda^2I+Q,
\qquad
Q=2\lambda N+N^2=N(2\lambda I+N).
\]
::: {.proof}
This is the direct expansion of $(\lambda I+N)^2$.
:::

<1>2. The operator $2\lambda I+N$ is invertible and commutes with $N$.
::: {.proof}
Since $N$ is nilpotent and $2\lambda\ne0$,
\[
2\lambda I+N
=2\lambda\left(I+\frac{N}{2\lambda}\right)
\]
is invertible by the finite geometric-series inverse.
It is a polynomial in $N$, hence commutes with $N$.
:::

<1>3. For every $k\ge1$,
\[
Q^k=N^k(2\lambda I+N)^k,
\]
and therefore
\[
\ker Q^k=\ker N^k.
\]
::: {.proof}
The factorization follows from commutativity in <1>2. The factor $(2\lambda I+N)^k$ is invertible and commutes with $N^k$, so
\[
Q^kv=0
\iff N^k(2\lambda I+N)^kv=0
\iff N^kv=0.
\]
:::

<1>4. Hence the nilpotent operator $Q$ has one Jordan block of size $n$.
::: {.proof}
For the single nilpotent Jordan block $N$, one has
\[
\dim\ker N^k=\min(k,n).
\]
By <1>3 the same is true for $Q$.
The sequence of dimensions $\dim\ker Q^k$ determines the nilpotent Jordan block sizes; the sequence $1,2,\ldots,n$ is exactly that of one block of size $n$.
:::

<1>5. Therefore the Jordan canonical form of $J^2$ is the single block
\[
J_n(\lambda^2).
\]
::: {.proof}
By <1>1, $J^2=\lambda^2I+Q$, and by <1>4 the nilpotent part $Q$ has one Jordan block of size $n$.
:::

<1>6. Now suppose $\lambda=0$.
Then $J=N$ and $J^2=N^2$.
::: {.proof}
Immediate from the definition of $N$.
:::

<1>7. Choose a Jordan chain $e_1,\dots,e_n$ for $N$ with
\[
Ne_1=0,
\qquad
Ne_j=e_{j-1}\quad (j\ge2).
\]
Then
\[
N^2e_j=e_{j-2}\quad (j\ge3),
\qquad
N^2e_1=N^2e_2=0.
\]
::: {.proof}
Apply $N$ twice to the Jordan-chain relations.
:::

<1>8. Under $N^2$, the vectors with odd indices form one Jordan chain and the vectors with even indices form another:
\[
e_1,e_3,e_5,\dots
\qquad\text{and}\qquad
e_2,e_4,e_6,\dots.
\]
::: {.proof}
By <1>7, $N^2$ sends each vector in either displayed sequence to the preceding vector in that same sequence and kills the first vector.
Their union is the original basis, so these are the complete Jordan chains for $N^2$.
:::

<1>9. The two Jordan block sizes are
\[
\left\lceil\frac n2\right\rceil
\quad\text{and}\quad
\left\lfloor\frac n2\right\rfloor.
\]
Thus if $n$ is even both have size $n/2$, while if $n$ is odd they have sizes $(n+1)/2$ and $(n-1)/2$.
::: {.proof}
The odd-indexed basis vectors number $\lceil n/2\rceil$ and the even-indexed basis vectors number $\lfloor n/2\rfloor$.
By <1>8 these are exactly the two Jordan-chain lengths.
:::
:::
