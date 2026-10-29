---
schema: qual/card@1
id: P-ALGF18B
kind: problem
title: 'Matrices of $p$-power order in characteristic $p\ge n$ are unipotent with $g^p=I$'
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: 'Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2018 source. Part (b) is false as printed: p=2, n=3 admits a unipotent Jordan block of order 4.'
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Frobenius-power nilpotence argument and the explicit GL_3(F_2) counterexample to part (b).
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The card printed "p is a prime which is at most n", under which part (b) fails (p=2, n=3, a 3x3 unipotent Jordan block). The statement now says "at least n", under which (g-I)^p=0 and g^p=I.
---

::: {.problem}
Suppose $p$ is a prime which is at least $n$, and $F$ is a field of characteristic $p$.
Suppose $g \in \mathrm{GL}_n(F)$ and $g^{p^m} = I$ for some positive integer $m$.

(a) Prove that $g - I$ is a nilpotent matrix.

(b) Prove that $g^p = I$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
The matrix $g-I$ is nilpotent.

::: pf-proof
In characteristic $p$, commuting elements satisfy
$$
(X-Y)^p=X^p-Y^p.
$$
Since $g$ commutes with $I$, iterating this identity $m$ times gives
$$
(g-I)^{p^m}=g^{p^m}-I.
$$
The hypothesis $g^{p^m}=I$ therefore yields
$$
(g-I)^{p^m}=0.
$$
:::

:::

::: {.pf-step #s2}
$g^p=I$.

::: pf-proof
By step [](#s1){.pf-ref}, $N=g-I$ is a nilpotent $n\times n$ matrix, so its minimal polynomial is $x^k$ for some $k\le n$, and hence $N^n=0$. Since $p\ge n$, also $N^p=0$. As $g=I+N$ with $I$ and $N$ commuting, in characteristic $p$
$$
g^p=(I+N)^p=I+N^p=I.
$$
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove parts (a) and (b).
:::

:::
:::
