---
schema: qual/card@1
id: P-UCLAB12-05
kind: problem
title: $\QQ$ is not a $G_\delta$ subset of $\RR$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
A subset $E$ of a metric space $X$ is a $G_\delta$ set if $E = \bigcap_{n=1}^\infty G_n$ where each $G_n$ is open in $X$. Use Problem 4 to prove that the set of rational numbers is not a $G_\delta$ subset of the set of real numbers.
:::

::: {.solution}

Suppose for contradiction that
\[
\QQ=\bigcap_{n=1}^{\infty}G_n,
\]
where every $G_n$ is open in $\RR$.

::: pf

::: {.pf-step #s1-1}

Every $G_n$ is dense in $\RR$.


::: pf-proof

Since
\[
\QQ\subseteq G_n
\]
for every $n$ and $\QQ$ is dense in $\RR$,
\[
\overline{G_n}
\supseteq
\overline{\QQ}
=
\RR.
\]
Thus $\overline{G_n}=\RR$, so $G_n$ is dense.

:::

:::

::: {.pf-step #s1-2}

For each $n$, the complement
\[
F_n=\RR\setminus G_n
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
\QQ=\{q_1,q_2,\ldots\}.
\]
Then each singleton
\[
\{q_m\}
\]
is closed and nowhere dense.


::: pf-proof

Singletons are closed in $\RR$. They have empty interior, so they are nowhere dense.

:::

:::

::: {.pf-step #s1-4}

Under the assumption that $\QQ=\bigcap_nG_n$,
\[
\RR
=
\left(\bigcup_{n=1}^{\infty}F_n\right)
\cup
\left(\bigcup_{m=1}^{\infty}\{q_m\}\right).
\]


::: pf-proof

By De Morgan's law,
\[
\RR\setminus\QQ
=
\RR\setminus\bigcap_{n=1}^{\infty}G_n
=
\bigcup_{n=1}^{\infty}(\RR\setminus G_n)
=
\bigcup_{n=1}^{\infty}F_n.
\]
Also
\[
\QQ
=
\bigcup_{m=1}^{\infty}\{q_m\}.
\]
Taking the union of $\QQ$ and its complement gives the displayed equality.

:::

:::

::: {.pf-step #s1-5}

The equality in step [](#s1-4){.pf-ref} contradicts the Baire category theorem.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, every set appearing in the two countable unions of step [](#s1-4){.pf-ref} is closed and nowhere dense.
The real line with its usual metric is complete.
Problem 4 therefore implies that $\RR$ cannot be a countable union of such sets.

:::

:::

::: {.pf-step #s1-6}

Hence
\[
\boxed{\QQ\text{ is not a }G_\delta\text{ subset of }\RR}.
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
