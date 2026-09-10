---
schema: qual/card@1
id: E-AMD-KJ3EIH6T
kind: problem
title: The four groups of order 28
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Re-derived the semidirect-product classification and made the dihedral order convention explicit.
---

::: {.exercise}
Classify all groups of order $28$.
:::

::: {.solution}
Let $|G|=28=4\cdot7$. Sylow gives
\[
n_7\equiv1\pmod7,\qquad n_7\mid4,
\]
so $n_7=1$. Thus the Sylow $7$-subgroup $P\cong C_7$ is normal. If $Q$ is a Sylow $2$-subgroup, then $|Q|=4$, $P\cap Q=1$, and $PQ=G$. Hence
\[
G\cong C_7\rtimes Q,
\]
where $Q\cong C_4$ or $C_2^2$, and the action lands in
\[
\operatorname{Aut}(C_7)\cong C_6.
\]

<1>1. If $Q\cong C_4$, there are two possibilities.
::: {.proof}
The image of $C_4\to C_6$ has order dividing $2$. The trivial action gives
\[
C_7\times C_4\cong C_{28}.
\]
The unique nontrivial action sends a generator of $C_4$ to inversion on $C_7$, giving one nonabelian semidirect product
\[
C_7\rtimes C_4.
\]
:::

<1>2. If $Q\cong C_2^2$, there are two possibilities.
::: {.proof}
Any image lies in the unique subgroup $C_2\le C_6$. The trivial action gives
\[
C_7\times C_2^2\cong C_{14}\times C_2.
\]
Every nonzero homomorphism $C_2^2\to C_2$ is equivalent under $\operatorname{Aut}(C_2^2)$, so there is one nontrivial semidirect product. It is
\[
(C_7\rtimes C_2)\times C_2\cong D_7\times C_2.
\]
With the convention that $D_m$ has order $2m$, this group is also isomorphic to $D_{14}$.
:::

Thus there are exactly four isomorphism types:
\[
C_{28},\qquad C_{14}\times C_2,\qquad C_7\rtimes C_4,\qquad D_7\times C_2\cong D_{14}.
\]
The two abelian groups are distinguished by cyclicity, and the two nonabelian groups by the isomorphism type of their Sylow $2$-subgroups ($C_4$ versus $C_2^2$).
:::
