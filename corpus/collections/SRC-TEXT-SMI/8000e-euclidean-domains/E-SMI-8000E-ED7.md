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
---

::: {.exercise}
Prove

$$
R^m / (Ra_1 e_1 \times \cdots \times Ra_m e_m) \cong (R/Ra_1) \times \cdots \times (R/Ra_m),
$$

where the $a_i$ are elements of $R$.
:::


::: solution
Let
$$
N=Ra_1e_1+\cdots+Ra_me_m\subseteq R^m.
$$
Because the $e_i$ are the standard coordinate vectors, this is exactly the
submodule whose $i$th coordinate lies in $Ra_i$.

<1>1. Define the coordinatewise quotient map.
::: proof
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

<1>2. The map $\Phi$ is surjective.
::: proof
Given arbitrary residue classes
$$
(r_1+Ra_1,\ldots,r_m+Ra_m),
$$
the vector $(r_1,\ldots,r_m)\in R^m$ maps to them. Hence $\Phi$ is
surjective.
:::

<1>3. The kernel of $\Phi$ is $N$.
::: proof
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

<1>4. Apply the first isomorphism theorem.
::: proof
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
