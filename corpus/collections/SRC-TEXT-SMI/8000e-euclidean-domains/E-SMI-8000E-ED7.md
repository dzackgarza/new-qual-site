---
schema: qual/card@1
id: E-SMI-8000E-ED7
kind: problem
title: Quotienting a free module by coordinate cyclic submodules
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the coordinate quotient statement with the local 8000e extraction, Euclidean-domains problem 7 and its clarification that the a_i are elements of R."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used the coordinatewise quotient map R^m→product R/Ra_i and identified its kernel exactly, then applied the first isomorphism theorem."
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith 8000e.pdf page 2, Euclidean-domain
    problem 7, with the sheet's clarification that the a_i are elements of R. The
    card reads the printed "Ra_1e_1 x ... x Ra_me_m" as the submodule of R^m whose
    i-th coordinate lies in Ra_i, which is what that product means inside R^m, and
    says so. Correct: the coordinatewise quotient has exactly that kernel, so the
    isomorphism follows. No defect.
---
---

::: {.exercise}
Prove

$$
R^m / (Ra_1 e_1 \times \cdots \times Ra_m e_m) \cong (R/Ra_1) \times \cdots \times (R/Ra_m),
$$

where the $a_i$ are elements of $R$.
:::

::: {.solution}
Let
$$
N=Ra_1e_1+\cdots+Ra_me_m\subseteq R^m.
$$
Because the $e_i$ are the standard coordinate vectors, this is exactly the
submodule whose $i$th coordinate lies in $Ra_i$.

::: pf

::: pf-step

Define the coordinatewise quotient map.

::: pf-proof

Set
$$
\Phi:R^m\longrightarrow
(R/Ra_1)\times\cdots\times(R/Ra_m)
$$
by
$$
\Phi(r_1,\ldots,r_m)
=(r_1+Ra_1,\ldots,r_m+Ra_m).
$$
This is an $R$-module homomorphism because each coordinate quotient map is
$R$-linear.

:::

:::

::: pf-step

The map $\Phi$ is surjective.

::: pf-proof

Given arbitrary residue classes
$$
(r_1+Ra_1,\ldots,r_m+Ra_m),
$$
the vector $(r_1,\ldots,r_m)\in R^m$ maps to them. Hence $\Phi$ is
surjective.

:::

:::

::: pf-step

The kernel of $\Phi$ is $N$.

::: pf-proof

A vector $(r_1,\ldots,r_m)$ lies in $\ker\Phi$ exactly when
$$
r_i+Ra_i=Ra_i
$$
for every $i$, equivalently when
$$
r_i\in Ra_i
$$
for every $i$. Thus one can write
$$
r_i=s_i a_i,
$$
and then
$$
(r_1,\ldots,r_m)
=\sum_{i=1}^m s_i a_i e_i\in N.
$$
The converse is immediate, so
$$
\ker\Phi=N.
$$

:::

:::

::: pf-step

Apply the first isomorphism theorem.

::: pf-proof

Since $\Phi$ is surjective and has kernel $N$,
$$
R^m/N\cong
(R/Ra_1)\times\cdots\times(R/Ra_m).
$$
Therefore
$$
\boxed{
R^m/(Ra_1e_1+\cdots+Ra_me_m)
\cong
\prod_{i=1}^m R/Ra_i.}
$$

:::

:::

:::

:::
