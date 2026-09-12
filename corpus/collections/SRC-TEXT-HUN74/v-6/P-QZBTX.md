---
schema: qual/card@1
id: P-QZBTX
kind: problem
title: Degree prime to the characteristic implies separability
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction of the Hungerford exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $\mathrm{char} K = p \neq 0$ and $[F: K]$ is finite and not divisible by $p$, then $F$ is separable over $K$.
:::

::: solution
Suppose, toward a contradiction, that $F/K$ is not separable.

<1>1. There exists $u\in F$ whose minimal polynomial over $K$ is inseparable.
::: proof
By definition, an algebraic extension is separable if every element is separable.
Since $F/K$ is finite, it is algebraic. Thus failure of separability provides
such an element $u$.
:::

<1>2. If an irreducible polynomial $m(x)\in K[x]$ is inseparable in
characteristic $p$, then $p$ divides $\deg m$.
::: proof
An irreducible polynomial is inseparable exactly when its formal derivative is
zero. Write
\[
m(x)=\sum_j a_jx^j.
\]
The equation $m'(x)=0$ means that $j a_j=0$ for every $j$. In characteristic
$p$, whenever $a_j\ne0$ this forces $p\mid j$. Hence all exponents occurring in
$m$ are multiples of $p$, so
\[
m(x)=g(x^p)
\]
for some $g\in K[x]$. In particular $p\mid\deg m$.
:::

<1>3. The degree $[K(u):K]$ is divisible by $p$.
::: proof
Let $m_u$ be the minimal polynomial of $u$ over $K$. By <1>1 it is inseparable,
so <1>2 gives
\[
p\mid\deg m_u=[K(u):K].
\]
:::

<1>4. This contradicts the hypothesis that $p\nmid[F:K]$.
::: proof
The tower law for
\[
K\subseteq K(u)\subseteq F
\]
gives
\[
[F:K]=[F:K(u)][K(u):K].
\]
By <1>3 the second factor is divisible by $p$, so $p\mid[F:K]$, contrary to
hypothesis.
:::

<1>5. Therefore $F/K$ is separable.
::: proof
The assumption of inseparability led to the contradiction in <1>4.
:::
:::
