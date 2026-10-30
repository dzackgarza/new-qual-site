---
schema: qual/card@1
id: P-ALGPAN11-03
kind: problem
title: Which direct product of cyclic groups is not cyclic
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Statement and choices transcribed from the ALGEBRA_REVIEW1.pdf page render; the machine extractions were garbled at this item.
---
::: {.problem}
Let $G_n$ denote the cyclic group of order $n$.
Which of the following direct products is NOT cyclic?

(A) $G_{17}\times G_{11}$

(B) $G_{17}\times G_{11}\times G_5$

(C) $G_{17}\times G_{33}$

(D) $G_{22}\times G_{33}$

(E) $G_{49}\times G_{121}$
:::

::: {.solution}
A finite direct product of cyclic groups is cyclic exactly when the factor orders are pairwise coprime.

::: pf

::: {.pf-step #s1}

Apply the criterion to the five choices.

::: pf-proof

The orders in (A), (B), (C), and (E) are pairwise coprime:
$$
\gcd(17,11)=1,
\quad \gcd(17,11)=\gcd(17,5)=\gcd(11,5)=1,
$$
$$
\gcd(17,33)=1,
\qquad \gcd(49,121)=1.
$$
Thus those products are cyclic.
In (D),
$$
\gcd(22,33)=11>1,
$$
so $G_{22}\times G_{33}$ is not cyclic.

:::

:::

::: pf-step

Hence the answer is $\boxed{\text{(D)}}$.

::: pf-proof

Step [](#s1){.pf-ref} shows that (A), (B), (C), and (E) are cyclic and that (D) is not.

:::

:::

::: pf-qed

The preceding conclusion identifies the unique noncyclic choice.

:::

:::

:::
