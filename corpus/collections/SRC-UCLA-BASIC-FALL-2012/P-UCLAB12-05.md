---
schema: qual/card@1
id: P-UCLAB12-05
kind: problem
title: $\mathbb Q$ is not a $G_\delta$ subset of $\mathbb R$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
A subset E of a metric space X is a $G _ { \delta }$ set if $\textstyle E = \bigcap _ { n = 1 } ^ { \infty } G _ { n }$ where each $G _ { n }$ is open in X. Use Problem 4 to prove that the set of rational numbers is not a $G _ { \delta }$ subset of the set of real numbers.
:::

::: {.solution}
Suppose for contradiction that
\[
\mathbb Q=\bigcap_{n=1}^{\infty}G_n,
\]
where every $G_n$ is open in $\mathbb R$.

<1>1. Every $G_n$ is dense in $\mathbb R$.

::: {.proof}
Since
\[
\mathbb Q\subseteq G_n
\]
for every $n$ and $\mathbb Q$ is dense in $\mathbb R$,
\[
\overline{G_n}
\supseteq
\overline{\mathbb Q}
=
\mathbb R.
\]
Thus $\overline{G_n}=\mathbb R$, so $G_n$ is dense.
:::

<1>2. For each $n$, the complement
\[
F_n=\mathbb R\setminus G_n
\]
is closed and nowhere dense.

::: {.proof}
Because $G_n$ is open, $F_n$ is closed.
Because $G_n$ is dense by step <1>1, no nonempty open interval can lie inside $F_n$. Thus $F_n$ has empty interior, so it is nowhere dense.
:::

<1>3. Enumerate the rational numbers as
\[
\mathbb Q=\{q_1,q_2,\ldots\}.
\]
Then each singleton
\[
\{q_m\}
\]
is closed and nowhere dense.

::: {.proof}
Singletons are closed in $\mathbb R$. They have empty interior, so they are nowhere dense.
:::

<1>4. Under the assumption that $\mathbb Q=\bigcap_nG_n$,
\[
\mathbb R
=
\left(\bigcup_{n=1}^{\infty}F_n\right)
\cup
\left(\bigcup_{m=1}^{\infty}\{q_m\}\right).
\]

::: {.proof}
By De Morgan's law,
\[
\mathbb R\setminus\mathbb Q
=
\mathbb R\setminus\bigcap_{n=1}^{\infty}G_n
=
\bigcup_{n=1}^{\infty}(\mathbb R\setminus G_n)
=
\bigcup_{n=1}^{\infty}F_n.
\]
Also
\[
\mathbb Q
=
\bigcup_{m=1}^{\infty}\{q_m\}.
\]
Taking the union of $\mathbb Q$ and its complement gives the displayed equality.
:::

<1>5. The equality in step <1>4 contradicts the Baire category theorem.

::: {.proof}
By steps <1>2--<1>3, every set appearing in the two countable unions of step <1>4 is closed and nowhere dense.
The real line with its usual metric is complete.
Problem 4 therefore implies that $\mathbb R$ cannot be a countable union of such sets.
:::

<1>6. Hence
\[
\boxed{\mathbb Q\text{ is not a }G_\delta\text{ subset of }\mathbb R}.
\]

::: {.proof}
Step <1>5 contradicts the assumption that such open sets $G_n$ exist.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
