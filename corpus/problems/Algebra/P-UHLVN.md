---
schema: qual/card@1
id: P-UHLVN
kind: problem
title: Galois groups of cubics
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What are the possible Galois groups for a cubic polynomial $f(x) \in K[x]$ over a field $K$ (of characteristic $\ne 2, 3$)?
Classify them completely using the discriminant and irreducibility.
:::

::: {.solution}
Let $L$ be the splitting field of a cubic $f\in K[x]$, with $\ch K\ne2,3$.

::: pf

::: {.pf-step #reducible}
If $f$ splits over $K$, then $\Gal(L/K)=1$; if $f=(x-a)q(x)$ with $q$ irreducible quadratic, then $\Gal(L/K)\cong C_2$.

::: pf-proof
In the first case $L=K$.
In the second case $L$ is the splitting field of $q$, a quadratic extension, which is Galois since $\ch K\ne2$.
:::

:::

::: {.pf-step #transitive}
If $f$ is irreducible, then $G=\Gal(L/K)$ is $A_3\cong C_3$ or $S_3$.

::: pf-proof
An irreducible polynomial in characteristic $\ne3$ has nonzero derivative, so its roots are distinct, and $G$ acts on them as a transitive subgroup of $S_3$.
:::

:::

::: {.pf-step #discriminant}
If $f$ is irreducible, then $G\subseteq A_3$ if and only if the discriminant $\Delta(f)$ is a square in $K$.

::: pf-proof
Let $\delta=(\alpha_1-\alpha_2)(\alpha_1-\alpha_3)(\alpha_2-\alpha_3)$, so $\Delta(f)=\delta^2\in K$ and $\delta\ne0$.
A permutation of the roots sends $\delta$ to its sign times $\delta$, and $\delta\ne-\delta$ since $\ch K\ne2$.
So $G\subseteq A_3$ if and only if $\delta\in L^G=K$, which holds if and only if $\Delta(f)$ is a square in $K$.
:::

:::

::: pf-step
The possible Galois groups are
$$
\boxed{
\Gal(L/K)\cong
\begin{cases}
1,& f\text{ splits over }K,\\
C_2,& f=(x-a)q\text{ with }q\text{ irreducible quadratic},\\
C_3,& f\text{ irreducible and }\Delta(f)\text{ a square in }K,\\
S_3,& f\text{ irreducible and }\Delta(f)\text{ not a square in }K.
\end{cases}}
$$

::: pf-proof
A cubic either splits, has exactly one root in $K$, or has none and is then irreducible; steps [](#reducible){.pf-ref}, [](#transitive){.pf-ref} and [](#discriminant){.pf-ref} treat these cases.
:::

:::

:::

:::
