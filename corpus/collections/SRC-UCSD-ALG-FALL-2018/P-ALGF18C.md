---
schema: qual/card@1
id: P-ALGF18C
kind: problem
title: Module vanishing and flatness checked at maximal ideals
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problems 3 and 4 of the official UCSD Algebra Qualifying Exam, Fall 2018 source; both localization statements agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified vanishing via an annihilator contained in a maximal ideal and flatness by localizing the kernel of each tensor-induced map.
---

::: problem
Suppose $A$ is a commutative unital ring, and $M$ is an $A$-module.

(a) Prove that, if $M_{\mathfrak{m}} = 0$ for any maximal ideal $\mathfrak{m}$ of $A$, then $M = 0$.

(b) Prove that if $M_{\mathfrak{m}}$ is a flat $A_{\mathfrak{m}}$-module for any maximal ideal $\mathfrak{m}$ of $A$, then $M$ is a flat module.
(You do not need to prove that localization is an exact functor.)
:::

::: {.solution}
<1>1. If $M\neq0$, then $M_{\mathfrak m}\neq0$ for some maximal ideal $\mathfrak m$ of $A$.
::: {.proof}
Choose a nonzero element
\[
x\in M.
\]
Its annihilator
\[
\operatorname{Ann}_A(x):=\{a\in A:ax=0\}
\]
is a proper ideal, because $1\notin\operatorname{Ann}_A(x)$.
Choose a maximal ideal $\mathfrak m$ containing $\operatorname{Ann}_A(x)$.

Suppose that the image $x/1$ were zero in $M_{\mathfrak m}$.
By the definition of localization, there would then exist
\[
s\in A\setminus\mathfrak m
\]
such that
\[
sx=0.
\]
This says
\[
s\in\operatorname{Ann}_A(x)\subseteq\mathfrak m,
\]
contradicting $s\notin\mathfrak m$.
Therefore
\[
x/1\neq0
\]
in $M_{\mathfrak m}$, so $M_{\mathfrak m}\neq0$.
:::

<1>2. If $M_{\mathfrak m}=0$ for every maximal ideal $\mathfrak m$ of $A$, then $M=0$.
::: {.proof}
This is the contrapositive of <1>1, proving part (a).
:::

<1>3. Let $f:N\to P$ be an injective $A$-linear map and set
\[
K:=\ker\bigl(M\otimes_A N\xrightarrow{\,1_M\otimes f\,}M\otimes_A P\bigr).
\]
Then
\[
K_{\mathfrak m}=0
\]
for every maximal ideal $\mathfrak m$ of $A$.
::: {.proof}
Fix a maximal ideal $\mathfrak m$.
Localization is exact, so $f$ induces an injection
\[
f_{\mathfrak m}:N_{\mathfrak m}\longrightarrow P_{\mathfrak m},
\]
and localizing the defining kernel sequence for $K$ gives
\[
K_{\mathfrak m}
=
\ker\left(
(M\otimes_A N)_{\mathfrak m}
\longrightarrow
(M\otimes_A P)_{\mathfrak m}
\right).
\]
There are canonical isomorphisms
\[
(M\otimes_A N)_{\mathfrak m}
\cong
M_{\mathfrak m}\otimes_{A_{\mathfrak m}}N_{\mathfrak m}
\]
and
\[
(M\otimes_A P)_{\mathfrak m}
\cong
M_{\mathfrak m}\otimes_{A_{\mathfrak m}}P_{\mathfrak m}.
\]
Under these identifications, the localized map is
\[
1_{M_{\mathfrak m}}\otimes f_{\mathfrak m}.
\]
By hypothesis, $M_{\mathfrak m}$ is flat over $A_{\mathfrak m}$.
Since $f_{\mathfrak m}$ is injective, this tensor-induced map is injective.
Thus its kernel, and hence $K_{\mathfrak m}$, is zero.
:::

<1>4. The module $M$ is flat over $A$.
::: {.proof}
By <1>3,
\[
K_{\mathfrak m}=0
\]
for every maximal ideal $\mathfrak m$.
Applying part (a), proved in <1>2, to the $A$-module $K$ gives
\[
K=0.
\]
Therefore, for every injective $A$-linear map $f:N\to P$, the map
\[
M\otimes_A N\longrightarrow M\otimes_A P
\]
is injective.
This is precisely the defining flatness condition, proving part (b).
:::
:::
