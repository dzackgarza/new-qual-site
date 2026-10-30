---
schema: qual/card@1
id: P-ALGPAN11-04
kind: problem
title: Number of field automorphisms of the rationals
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
An automorphism $\phi$ of a field $F$ is a one-to-one mapping of $F$ onto itself such that $\phi(a+b)=\phi(a)+\phi(b)$ and $\phi(ab)=\phi(a)\phi(b)$ for all $a,b\in F$.
If $F$ is the field of rational numbers, then the number of distinct automorphisms of $F$ is

(A) $0$ (B) $1$ (C) $2$ (D) $4$ (E) infinite
:::

::: {.solution}
Every field automorphism of $\QQ$ is the identity, so the answer is $\boxed{\text{(B)}\ 1}$.

::: pf

::: {.pf-step #s1}

Any automorphism fixes every rational number.

::: pf-proof

Let $\varphi:\QQ\to\QQ$ be a field automorphism.
Since $\varphi(1)=1$, additivity gives $\varphi(n)=n$ for every $n\in\ZZ$.
For $m/n\in\QQ$ with $n\ne0$,
$$
\varphi(m/n)=\varphi(m)\varphi(n)^{-1}=m/n.
$$
Thus $\varphi=\operatorname{id}_{\QQ}$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves that the identity is the only field automorphism of $\QQ$, so choice (B) is correct.

:::

:::

:::
