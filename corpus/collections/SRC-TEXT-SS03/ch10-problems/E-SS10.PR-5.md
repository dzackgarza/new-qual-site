---
schema: qual/card@1
id: E-SS10.PR-5
kind: problem
title: Elliptic discriminant and the Dedekind eta function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Modular Forms
relations: []
review: draft
---

::: {.exercise}
The Weierstrass function satisfies
$$
(\wp')^2=4\wp^3-g_2\wp-g_3,
\qquad g_2=60E_4,\quad g_3=140E_6,
$$
where $E_k$ is the Eisenstein series of order $k$. Define the discriminant of $y^2=4x^3-g_2x-g_3$ by $\Delta=g_2^3-27g_3^2$. Prove that
$$
\Delta(\tau)=(2\pi)^{12}\eta(\tau)^{24}
\qquad(\tau\in\halfplane).
$$
:::

::: {.hint}
$\Delta$ and $\eta^{24}$ satisfy the same transformation laws under $\tau\mapsto\tau+1$ and $\tau\mapsto-1/\tau$. Use the fundamental domain in [[E-SS10.PR-2]] and compare behavior at the cusp at infinity.
:::

::: {.solution}
Put $q=e^{2\pi i\tau}$, so $q\to0$ as $\operatorname{Im}\tau\to\infty$.

::: pf

::: {.pf-step #weight-twelve}
Both $\Delta$ and $\eta^{24}$ are holomorphic on $\halfplane$ and transform with weight $12$ under $\tau\mapsto\tau+1$ and $\tau\mapsto-1/\tau$.

::: pf-proof
[[SRC-TEXT-SS03|Stein and Shakarchi, Complex Analysis]], §9.2.1, Theorem 2.1 (p. 274), gives $E_j(\tau+1)=E_j(\tau)$ and $E_j(-1/\tau)=\tau^jE_j(\tau)$ for $j=4,6$. Thus $g_2^3$ and $g_3^2$, and hence $\Delta$, are periodic and acquire the factor $\tau^{12}$ under inversion. The product definition gives $\eta(\tau+1)=e^{\pi i/12}\eta(\tau)$; the same book's §10.1, Proposition 1.9 (p. 292), gives $\eta(-1/\tau)=\sqrt{\tau/i}\,\eta(\tau)$. Taking twenty-fourth powers gives the same two laws for $\eta^{24}$, since $e^{2\pi i}=1$ and $i^{-12}=1$.
:::

:::

::: {.pf-step #cusp}
$\Delta(\tau)=(2\pi)^{12}q+O(q^2)$ and $\eta(\tau)^{24}=q+O(q^2)$ as $q\to0$.

::: pf-proof
[[SRC-TEXT-SS03|Stein and Shakarchi, Complex Analysis]], §9.2.2, Theorem 2.5 (p. 277), and $\zeta(4)=\pi^4/90$, $\zeta(6)=\pi^6/945$ give
$$
g_2=\frac{4\pi^4}{3}(1+240q+O(q^2)),\qquad
g_3=\frac{8\pi^6}{27}(1-504q+O(q^2)).
$$
Their constant terms cancel in $g_2^3-27g_3^2$, and its coefficient of $q$ is
$$
\frac{64\pi^{12}}{27}\bigl(3\cdot240+2\cdot504\bigr)
=4096\pi^{12}=(2\pi)^{12}.
$$
The product $\eta(\tau)^{24}=q\prod_{n\ge1}(1-q^n)^{24}$ gives the second expansion.
:::

:::

::: {.pf-step #invariant}
The function $F=\Delta/((2\pi)^{12}\eta^{24})$ is holomorphic, bounded, and invariant under the modular group on $\halfplane$.

::: pf-proof
The product for $\eta$ converges to a nonzero value for $\abs{q}<1$, so $F$ is holomorphic. Step [](#weight-twelve){.pf-ref} makes $F$ invariant under translation and inversion; [[E-SS10.PR-2]] proves these generate the modular group. Step [](#cusp){.pf-ref} gives $F(\tau)\to1$ as $\operatorname{Im}\tau\to\infty$, uniformly for $\abs{\operatorname{Re}\tau}\le\frac12$. The fundamental domain in [[E-SS10.PR-2]] has a compact part below every fixed height. Continuity bounds $F$ there; the cusp limit bounds it above that height. Invariance then bounds $F$ on all of $\halfplane$.
:::

:::

::: pf-step
Q.E.D. $\Delta=(2\pi)^{12}\eta^{24}$ on $\halfplane$.

::: pf-proof
The group $G$ in [[E-SS10.PR-4]] is a subgroup of the modular group. Thus step [](#invariant){.pf-ref} satisfies that card's boundedness and invariance hypotheses, so $F$ is constant. Its limit in step [](#cusp){.pf-ref} is $1$, so $F=1$.
:::

:::

:::

:::
