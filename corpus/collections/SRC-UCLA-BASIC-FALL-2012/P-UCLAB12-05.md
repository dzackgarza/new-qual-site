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

::: pf

::: {.pf-step #s1-1}

Every $G_n$ is dense in $\mathbb R$.


::: pf-proof

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

:::

::: {.pf-step #s1-2}

For each $n$, the complement
\[
F_n=\mathbb R\setminus G_n
\]
is closed and nowhere dense.


::: pf-proof

Because $G_n$ is open, $F_n$ is closed.
Because $G_n$ is dense by step [](#s1-1){.pf-ref}, no nonempty open interval can lie inside $F_n$. Thus $F_n$ has empty interior, so it is nowhere dense.

:::

:::

::: {.pf-step #s1-3}

Enumerate the rational numbers as
\[
\mathbb Q=\{q_1,q_2,\ldots\}.
\]
Then each singleton
\[
\{q_m\}
\]
is closed and nowhere dense.


::: pf-proof

Singletons are closed in $\mathbb R$. They have empty interior, so they are nowhere dense.

:::

:::

::: {.pf-step #s1-4}

Under the assumption that $\mathbb Q=\bigcap_nG_n$,
\[
\mathbb R
=
\left(\bigcup_{n=1}^{\infty}F_n\right)
\cup
\left(\bigcup_{m=1}^{\infty}\{q_m\}\right).
\]


::: pf-proof

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

:::

::: {.pf-step #s1-5}

The equality in step [](#s1-4){.pf-ref} contradicts the Baire category theorem.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, every set appearing in the two countable unions of step [](#s1-4){.pf-ref} is closed and nowhere dense.
The real line with its usual metric is complete.
Problem 4 therefore implies that $\mathbb R$ cannot be a countable union of such sets.

:::

:::

::: {.pf-step #s1-6}

Hence
\[
\boxed{\mathbb Q\text{ is not a }G_\delta\text{ subset of }\mathbb R}.
\]


::: pf-proof

Step [](#s1-5){.pf-ref} contradicts the assumption that such open sets $G_n$ exist.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
