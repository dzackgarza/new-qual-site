---
schema: qual/card@1
id: P-BKS00-8
kind: problem
title: Cardinality of the set of subrings of $\QQ$
classification:
  areas: [prelim]
  topics: []
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
    The power set of Q gives the continuum upper bound. For the lower
    bound, distinct subsets S of the primes give distinct localization
    subrings Z[S^{-1}], distinguished by which reciprocals 1/p they
    contain.
---

::: {.problem}
Find the cardinality of the set of all subrings of the field $\mathbb Q$.
:::

::: {.solution}
Let $\mathcal R$ denote the set of subrings of $\QQ$, and let
$\mathcal S$ denote the set of prime numbers.

::: pf

::: {.pf-step #s1}

The cardinality of $\mathcal R$ is at most
$$
2^{\aleph_0}.
$$

::: pf-proof

Every subring of $\QQ$ is a subset of $\QQ$. Since $\QQ$ is
countably infinite,
$$
\abs{\mathcal R}
\leq
\abs{\mathcal P(\QQ)}
=
2^{\aleph_0}.
$$

:::

:::

::: {.pf-step #s2}

For each subset $S\subseteq\mathcal S$, define
$$
R_S
=
\ZZ\left[\frac1p:p\in S\right]
\subseteq
\QQ.
$$
Then $R_S$ is a subring of $\QQ$.

::: pf-proof

By definition, $R_S$ is the smallest subring of $\QQ$ containing
$\ZZ$ and the elements $1/p$ for $p\in S$. Equivalently, its elements
are the fractions
$$
\frac{a}{b},
\qquad
a\in\ZZ,
$$
whose denominator $b>0$ has no prime divisor outside $S$. This set is
closed under addition, subtraction, and multiplication.

:::

:::

::: {.pf-step #s3}

If $S,T\subseteq\mathcal S$ and $S\ne T$, then
$$
R_S\ne R_T.
$$

::: pf-proof

Choose a prime $p$ in the symmetric difference of $S$ and $T$. After
interchanging $S$ and $T$ if necessary, assume
$$
p\in S\setminus T.
$$
Then $1/p\in R_S$. On the other hand, every element of $R_T$, written
in lowest terms, has denominator divisible only by primes in $T$.
Since $p\notin T$,
$$
\frac1p\notin R_T.
$$
Hence $R_S\ne R_T$.

:::

:::

::: {.pf-step #s4}

The cardinality of $\mathcal R$ is at least
$$
2^{\aleph_0}.
$$

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give an injection
$$
\mathcal P(\mathcal S)
\longrightarrow
\mathcal R,
\qquad
S\longmapsto R_S.
$$
The set $\mathcal S$ of primes is countably infinite, so
$$
\abs{\mathcal P(\mathcal S)}
=
2^{\aleph_0}.
$$

:::

:::

::: {.pf-step #s5}

The set of all subrings of $\QQ$ has cardinality
$$
\boxed{2^{\aleph_0}}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the upper bound, and step [](#s4){.pf-ref} gives the matching lower
bound.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested cardinality.

:::

:::

:::
