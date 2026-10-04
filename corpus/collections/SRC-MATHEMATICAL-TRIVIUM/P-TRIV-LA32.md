---
schema: qual/card@1
id: P-TRIV-LA32
kind: problem
title: $e^Ae^B=e^{A+B}$ for commuting matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the matrices A, B such that $[ A , B ] = 0$ . Show that in this case $e ^ { A } e ^ { B } = e ^ { B } e ^ { A } = e ^ { A + B }$
:::

::: {.solution}
<1>1. Since
$$
[A,B]=0,
$$
one has
$$
AB=BA.
$$

::: {.proof}
This is the definition of the commutator.
:::

<1>2. For every $n\geq0$,
$$
(A+B)^n
=
\sum_{k=0}^{n}
\binom{n}{k}A^kB^{n-k}.
$$

::: {.proof}
Because $A$ and $B$ commute, every word of length $n$ containing $k$ copies of
$A$ and $n-k$ copies of $B$ equals
$$
A^kB^{n-k}.
$$
There are $\binom nk$ such words. Thus the ordinary binomial theorem applies.
:::

<1>3. The product of the two exponential series is
$$
e^Ae^B
=
\sum_{k=0}^{\infty}
\sum_{m=0}^{\infty}
\frac{A^kB^m}{k!m!}.
$$

::: {.proof}
By definition,
$$
e^A
=
\sum_{k=0}^{\infty}\frac{A^k}{k!},
\qquad
e^B
=
\sum_{m=0}^{\infty}\frac{B^m}{m!}.
$$
The series converge absolutely in any matrix norm, so their product may be
formed by the Cauchy product.
:::

<1>4. Regrouping the double sum in step <1>3 by total degree $n=k+m$ gives
$$
e^Ae^B
=
\sum_{n=0}^{\infty}
\frac1{n!}
\sum_{k=0}^{n}
\binom nk
A^kB^{n-k}.
$$

::: {.proof}
For fixed $n=k+m$,
$$
\frac1{k!m!}
=
\frac1{n!}
\binom nk.
$$
Substitute $m=n-k$.
:::

<1>5. Therefore
$$
\boxed{e^Ae^B=e^{A+B}}.
$$

::: {.proof}
By step <1>2, the inner sum in step <1>4 is
$$
(A+B)^n.
$$
Hence
$$
e^Ae^B
=
\sum_{n=0}^{\infty}
\frac{(A+B)^n}{n!}
=
e^{A+B}.
$$
:::

<1>6. One also has
$$
\boxed{e^Be^A=e^{A+B}}.
$$

::: {.proof}
The hypothesis $AB=BA$ is symmetric in $A$ and $B$. Apply step <1>5 with the
roles of $A$ and $B$ exchanged.
:::

<1>7. Consequently,
$$
\boxed{e^Ae^B=e^Be^A=e^{A+B}}.
$$

::: {.proof}
Combine steps <1>5 and <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required identity.
:::
:::
