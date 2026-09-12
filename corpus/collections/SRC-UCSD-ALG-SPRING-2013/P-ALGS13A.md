---
schema: qual/card@1
id: P-ALGS13A
kind: problem
title: Existence of a non-abelian group of order $2013$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared against the official UCSD Spring 2013 Algebra qualifying exam; statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Constructed an explicit nonabelian semidirect product of order 2013.
---

::: problem
Does there exist a non-Abelian group of order $2013 = (3)(11)(61)$?
Justify your answer.
:::

::: {.solution}
Yes.

<1>1. The automorphism group of $C_{61}$ contains an element of order $3$.
::: {.proof}
Since $61$ is prime,
\[
\operatorname{Aut}(C_{61})\cong (\mathbb Z/61\mathbb Z)^\times,
\]
which is cyclic of order $60$.
Because $3\mid60$, it contains an element $\varphi$ of order $3$.
:::

<1>2. Form the semidirect product
\[
H=C_{61}\rtimes_{\varphi} C_3.
\]
Then $|H|=183$ and $H$ is nonabelian.
::: {.proof}
Let $a$ generate $C_{61}$ and $b$ generate $C_3$, with conjugation by $b$ acting as the nontrivial automorphism $\varphi$:
\[
bab^{-1}=\varphi(a)\neq a.
\]
Thus $a$ and $b$ do not commute, so $H$ is nonabelian.
Its order is $61\cdot3=183$.
:::

<1>3. Set
\[
G=H\times C_{11}.
\]
Then $G$ is a nonabelian group of order $2013$.
::: {.proof}
We have
\[
|G|=183\cdot11=3\cdot11\cdot61=2013.
\]
Since the factor $H$ is nonabelian, the direct product $G$ is nonabelian.
:::
:::
