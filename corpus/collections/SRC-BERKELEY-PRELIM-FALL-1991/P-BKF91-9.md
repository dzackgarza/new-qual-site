---
schema: qual/card@1
id: P-BKF91-9
kind: problem
title: A group of order $2p$ with a normal subgroup of order $2$ is cyclic
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Showed the nontrivial element of the normal order-two subgroup is central,
    then multiplied it by a generator of a Sylow p-subgroup to obtain an
    element of order 2p.
---

::: {.problem}
Let $G$ be a group of order $2p$, where $p$ is an odd prime. Assume that $G$ has a normal subgroup of order $2$. Prove that $G$ is cyclic.
:::

::: {.solution}
Let
$$
N=\{e,z\}
$$
be the given normal subgroup of order $2$.

<1>1. The element $z$ is central in $G$.

::: {.proof}
For every $g\in G$, normality gives
$$
gzg^{-1}\in N.
$$
Conjugation preserves order, and $z$ has order $2$, so $gzg^{-1}$ cannot be $e$. Hence
$$
gzg^{-1}=z,
$$
which is equivalent to $gz=zg$.
:::

<1>2. There exists an element $x\in G$ of order $p$.

::: {.proof}
By Cauchy's theorem, since $p$ divides $\abs G=2p$, the group $G$ contains an element of order $p$.
:::

<1>3. The element $xz$ has order $2p$.

::: {.proof}
By step <1>1, $x$ and $z$ commute. Hence
$$
(xz)^{2p}=x^{2p}z^{2p}=e.
$$
Conversely, suppose $(xz)^m=e$. Then
$$
x^m=z^{-m}.
$$
The left-hand side lies in $\langle x\rangle$, while the right-hand side lies in $N$. Since
$$
\abs{\langle x\rangle}=p,
\qquad
\abs N=2,
$$
their intersection is trivial. Thus $x^m=e$ and $z^m=e$, so
$$
p\mid m
\qquad\text{and}\qquad
2\mid m.
$$
Because $p$ is odd, $2p\mid m$. Therefore the order of $xz$ is exactly $2p$.
:::

<1>4. The group $G$ is cyclic.

::: {.proof}
By step <1>3, the cyclic subgroup $\langle xz\rangle$ has order $2p=\abs G$. Hence
$$
\langle xz\rangle=G.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the assertion.
:::
:::
