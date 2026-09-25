---
schema: qual/card@1
id: P-BKS09-2A
kind: problem
title: Real matrices with $X^2=-I$ have even size
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
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed its three proposed arguments.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the determinant argument over the real numbers.
---

::: {.problem}
Prove that if an $n \times n$ matrix X over R satisfies $X ^ { 2 } = - I$ , then n is even.
:::

::: {.solution}
<1>1. One has
$$
(\det X)^2=(-1)^n.
$$

::: {.proof}
By multiplicativity of the determinant and the relation $X^2=-I$,
$$
(\det X)^2
=
\det(X^2)
=
\det(-I)
=
(-1)^n.
$$
:::

<1>2. One has $(-1)^n=1$.

::: {.proof}
Because $X$ is a real matrix, $\det X\in\RR$, so
$$
(\det X)^2\geq0.
$$
By step <1>1, this square equals $(-1)^n$, which is either $1$ or $-1$.
It therefore must equal $1$.
:::

<1>3. The integer $n$ is even.

::: {.proof}
By step <1>2,
$$
(-1)^n=1.
$$
This holds exactly when $n$ is even.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
