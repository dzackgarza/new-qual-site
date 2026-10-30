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
Consider the matrices $A$, $B$ such that $[A, B] = 0$. Show that in this case $e^A e^B = e^B e^A = e^{A+B}$.
:::

::: {.solution}

::: pf

::: pf-step

Since
$$
[A,B]=0,
$$
one has
$$
AB=BA.
$$


::: pf-proof

This is the definition of the commutator.

:::

:::

::: {.pf-step #s1-2}

For every $n\geq0$,
$$
(A+B)^n
=
\sum_{k=0}^{n}
\binom{n}{k}A^kB^{n-k}.
$$


::: pf-proof

Because $A$ and $B$ commute, every word of length $n$ containing $k$ copies of
$A$ and $n-k$ copies of $B$ equals
$$
A^kB^{n-k}.
$$
There are $\binom nk$ such words. Thus the ordinary binomial theorem applies.

:::

:::

::: {.pf-step #s1-3}

The product of the two exponential series is
$$
e^Ae^B
=
\sum_{k=0}^{\infty}
\sum_{m=0}^{\infty}
\frac{A^kB^m}{k!m!}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-4}

Regrouping the double sum in step [](#s1-3){.pf-ref} by total degree $n=k+m$ gives
$$
e^Ae^B
=
\sum_{n=0}^{\infty}
\frac1{n!}
\sum_{k=0}^{n}
\binom nk
A^kB^{n-k}.
$$


::: pf-proof

For fixed $n=k+m$,
$$
\frac1{k!m!}
=
\frac1{n!}
\binom nk.
$$
Substitute $m=n-k$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{e^Ae^B=e^{A+B}}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the inner sum in step [](#s1-4){.pf-ref} is
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

:::

::: {.pf-step #s1-6}

One also has
$$
\boxed{e^Be^A=e^{A+B}}.
$$


::: pf-proof

The hypothesis $AB=BA$ is symmetric in $A$ and $B$. Apply step [](#s1-5){.pf-ref} with the
roles of $A$ and $B$ exchanged.

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{e^Ae^B=e^Be^A=e^{A+B}}.
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required identity.

:::

:::

:::
