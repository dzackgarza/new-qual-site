---
schema: qual/card@1
id: P-BKS12-8A
kind: problem
title: Eigenvalues are roots of annihilating polynomials
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2012 solution PDF and independently reviewed both annihilating-polynomial arguments.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked evaluation of P(L) on eigenvectors and the minimal-prefix factor argument producing an eigenvalue when P splits.
---

::: {.problem}
Suppose L is a linear operator acting on a non trivial vector space V over a field K. Suppose $P ( x ) \in K [ x ]$ is not identically zero and $P ( L ) = 0$ . Show every eigenvalue of L is a root of P . Show that if P factors completely over K then some roots of P are eigenvalues of L.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If
$$
Lv=\lambda v
$$
with $v\neq0$, then
$$
P(L)v=P(\lambda)v.
$$

::: pf-proof

Write
$$
P(x)=\sum_{j=0}^d a_jx^j.
$$
Since
$$
L^jv=\lambda^jv
$$
for every $j\geq0$,
$$
\begin{aligned}
P(L)v
&=
\sum_{j=0}^d a_jL^jv\\
&=
\sum_{j=0}^d a_j\lambda^jv\\
&=
P(\lambda)v.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

Every eigenvalue of $L$ is a root of $P$.

::: pf-proof

If $\lambda$ is an eigenvalue, choose a nonzero eigenvector $v$. Since
$P(L)=0$, step [](#s1){.pf-ref} gives
$$
0=P(L)v=P(\lambda)v.
$$
Because $v\neq0$ and $K$ is a field,
$$
P(\lambda)=0.
$$

:::

:::

::: {.pf-step #s3}

Suppose $P$ factors completely over $K$. Then its degree is
positive and one may write
$$
P(x)
=
a\prod_{j=1}^d(x-\lambda_j)
$$
with
$$
a\in K^\times,
\qquad
\lambda_j\in K.
$$

::: pf-proof

If $P$ had degree $0$, it would be a nonzero constant $a$, so
$$
P(L)=aI_V\neq0
$$
because $V$ is nontrivial. Thus $d\geq1$. Complete factorization over
$K$ gives the displayed form.

:::

:::

::: {.pf-step #s4}

Under the hypotheses of step [](#s3){.pf-ref}, at least one
$\lambda_j$ is an eigenvalue of $L$.

::: pf-proof

Choose
$$
0\neq v\in V.
$$
For $0\leq k\leq d$, set
$$
Q_k(L)
\coloneqq
\prod_{j=1}^k(L-\lambda_jI),
$$
with $Q_0(L)=I$. Since
$$
P(L)
=
aQ_d(L)
=
0,
$$
one has
$$
Q_d(L)v=0.
$$
Choose the least $k\geq1$ such that
$$
Q_k(L)v=0.
$$
Then
$$
w\coloneqq Q_{k-1}(L)v
\neq
0
$$
by minimality, while
$$
(L-\lambda_kI)w
=
Q_k(L)v
=
0.
$$
Therefore
$$
Lw=\lambda_kw,
$$
so $\lambda_k$ is an eigenvalue.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the first assertion, and step [](#s4){.pf-ref} proves the second.

:::

:::

:::
