---
schema: qual/card@1
id: P-UCLAB02W-04
kind: problem
title: The irrationals are not an $F_\sigma$ subset of the real line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
Prove that the set of irrational numbers in $\RR$ is not a countable union of closed subsets of $\RR$.
:::

::: {.solution}

Let $P=\RR\setminus\QQ$ denote the set of irrational numbers.

::: pf

::: {.pf-step #s1-1}

Every closed subset $F\subseteq P$ has empty interior in $\RR$.


::: pf-proof

Suppose instead that $F$ contained a nonempty open interval $I$. Every nonempty open interval in $\RR$ contains a rational number, so there would be some
$$
q\in I\cap\QQ.
$$
But $I\subseteq F\subseteq P$ contains no rational numbers, a contradiction. Hence $F$ has empty interior.

:::

:::

::: {.pf-step #s1-2}

Every closed subset $F\subseteq P$ is nowhere dense in $\RR$.


::: pf-proof

Because $F$ is closed,
$$
\overline F=F.
$$
By step [](#s1-1){.pf-ref}, the interior of $F$ is empty. Therefore
$$
\operatorname{int}(\overline F)=\varnothing,
$$
which is exactly the definition that $F$ is nowhere dense.

:::

:::

::: {.pf-step #s1-3}

The rational numbers form a countable union of nowhere-dense subsets of $\RR$.


::: pf-proof

Enumerate
$$
\QQ=\{q_1,q_2,\ldots\}.
$$
Each singleton $\{q_n\}$ is closed and has empty interior, hence is nowhere dense. Thus
$$
\QQ=\bigcup_{n=1}^{\infty}\{q_n\}
$$
is a countable union of nowhere-dense sets.

:::

:::

::: {.pf-step #s1-4}

The irrational numbers cannot be a countable union of closed subsets of $\RR$.


::: pf-proof

Assume for contradiction that
$$
P=\bigcup_{n=1}^{\infty}F_n,
$$
where every $F_n$ is closed in $\RR$. Since each $F_n\subseteq P$, step [](#s1-2){.pf-ref} shows that every $F_n$ is nowhere dense. By step [](#s1-3){.pf-ref},
$$
\RR
=P\cup\QQ
=\left(\bigcup_{n=1}^{\infty}F_n\right)
\cup
\left(\bigcup_{n=1}^{\infty}\{q_n\}\right)
$$
would be a countable union of nowhere-dense subsets of $\RR$.

This contradicts the Baire category theorem, because $\RR$ is a complete metric space and therefore is not a countable union of nowhere-dense subsets of itself.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required assertion.

:::

:::

:::
