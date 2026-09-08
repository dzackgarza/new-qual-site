---
schema: qual/card@1
id: P-ALGS16C
kind: problem
title: Non-abelian group of order $39$
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
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Construct a non-abelian group of order $39$ or prove that no such group exists.
:::


::: {.solution}
<1>1. Let $N=\langle a\rangle\cong C_{13}$. Then $\operatorname{Aut}(N)\cong(\mathbf Z/13\mathbf Z)^\times\cong C_{12}$ contains an automorphism of order $3$.
::: {.proof}
The automorphism group of a cyclic group of order $13$ is the multiplicative group of the field $\mathbf F_{13}$, which is cyclic of order $12$. Since $3\mid12$, it has an element of order $3$; for example $a\mapsto a^3$, because $3^3=27\equiv1\pmod{13}$ while $3\not\equiv1\pmod{13}$.
:::

<1>2. Let $H=\langle b\rangle\cong C_3$ act on $N$ by $bab^{-1}=a^3$, and form the semidirect product
\[
G=C_{13}\rtimes C_3=\langle a,b\mid a^{13}=b^3=1,\ bab^{-1}=a^3\rangle.
\]
::: {.proof}
Step <1>1 gives a homomorphism $C_3\to\operatorname{Aut}(C_{13})$ sending a generator of $C_3$ to the order-$3$ automorphism $a\mapsto a^3$. The corresponding semidirect product therefore exists.
:::

<1>3. The group $G$ has order $39$.
::: {.proof}
As a set, a semidirect product $C_{13}\rtimes C_3$ is $C_{13}\times C_3$, so $|G|=13\cdot3=39$.
:::

<1>4. The group $G$ is nonabelian.
::: {.proof}
The defining relation gives $bab^{-1}=a^3$. Since $a$ has order $13$, one has $a^3\neq a$. Thus $ba\neq ab$.
:::

<1>5. Hence a nonabelian group of order $39$ exists.
::: {.proof}
Steps <1>2--<1>4 construct one explicitly.
:::
:::
