---
schema: qual/card@1
id: P-WESTOP09-I4
kind: problem
title: Cardinality of spaces of continuous maps into the unit interval
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $I=[0,1]$, let $C(X,I)$ be the set of continuous functions from $X$ to $I$, and let $\mathfrak c=|I|$.

1. Prove that if $X\ne\varnothing$, then $|C(X,I)|\ge\mathfrak c$.
2. Prove that the set of all functions $I\to I$ has cardinality strictly greater than $\mathfrak c$.
3. Prove that $|C(I,I)|=\mathfrak c$. The source hints that continuity allows a function on $I$ to be determined by its values on a smaller subset.
:::

::: pf

::: pf-step

If $X\ne\varnothing$, then
\[
\boxed{|C(X,I)|\ge\mathfrak c}.
\]


::: pf-proof

For every $t\in I$, let
\[
c_t:X\to I,
\qquad
c_t(x)=t.
\]
Each $c_t$ is continuous. Since $X$ is nonempty, $t\ne s$ implies
$c_t\ne c_s$. Thus
\[
t\longmapsto c_t
\]
is an injection from $I$ into $C(X,I)$, proving the inequality.

:::

:::

::: pf-step

The set of all functions $I\to I$ has cardinality strictly larger than
$\mathfrak c$.


::: pf-proof

Every function
\[
\chi:I\to\{0,1\}
\]
is also a function $I\to I$. Hence
\[
|I^I|\ge|\{0,1\}^I|=2^{|I|}=2^{\mathfrak c}.
\]
Cantor's theorem gives
\[
2^{\mathfrak c}>\mathfrak c.
\]
Therefore
\[
\boxed{|I^I|>\mathfrak c}.
\]

:::

:::

::: pf-step

A continuous function $f:I\to I$ is uniquely determined by its
restriction to
\[
Q=\mathbb Q\cap I.
\]


::: pf-proof

The set $Q$ is dense in $I$. If $f,g\in C(I,I)$ agree on $Q$, then for any
$x\in I$ choose a sequence $(q_n)$ in $Q$ with $q_n\to x$. Continuity gives
\[
f(x)=\lim_{n\to\infty}f(q_n)
=\lim_{n\to\infty}g(q_n)
=g(x).
\]
Thus $f=g$.

:::

:::

::: pf-step

One has
\[
|C(I,I)|\le\mathfrak c.
\]


::: pf-proof

By step <1>3, restriction defines an injection
\[
C(I,I)\hookrightarrow I^Q.
\]
Since $Q$ is countable,
\[
|I^Q|
=\mathfrak c^{\aleph_0}
=(2^{\aleph_0})^{\aleph_0}
=2^{\aleph_0\cdot\aleph_0}
=2^{\aleph_0}
=\mathfrak c.
\]
Hence $|C(I,I)|\le\mathfrak c$.

:::

:::

::: pf-step

Therefore
\[
\boxed{|C(I,I)|=\mathfrak c}.
\]


::: pf-proof

Applying step <1>1 with $X=I$ gives
$|C(I,I)|\ge\mathfrak c$, while step <1>4 gives the reverse inequality.

:::

:::

::: pf-qed

Steps <1>1, <1>2, and <1>5 prove the three requested assertions.

:::

:::
