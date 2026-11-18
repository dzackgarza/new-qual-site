---
schema: qual/card@1
id: P-HCAX8
kind: problem
title: Zeros of a polynomial derivative remain in a containing half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Gauss-Lucas Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The reduction to the half-plane {Re z >= 0} is now argued (translation and rotation as an affine substitution, with the effect on p, on its zeros and on p', the factor q' = e^{i theta} p' o phi), which the prose asserted in one clause; the case distinction between a zero of p' that is also a zero of p and one that is not is separated; and the sign computation Re(1/(w - z_j)) = Re(w - z_j)/|w - z_j|^2 < 0 is given with the reason for the strictness (Re w < 0 and Re z_j >= 0). No retained solution set covers the question; the card says the argument is its own.
---

::: {.problem}
Suppose all zeros of a polynomial lie in one closed half-plane.
Show that every zero of its derivative lies in the same half-plane.
:::

::: {.solution}
The collection's provenance is the oral-question extraction, which holds the question and no worked answer, so no retained solution set covers it; the argument is the card's own, and it is the half-plane form of the Gauss-Lucas theorem.

::: pf

::: {.pf-step #logderiv}
Let $p(z)=c\prod_{j=1}^N(z-z_j)$ with $c\ne0$, the zeros listed with multiplicity. At a point $w$ with $p(w)\ne0$,
$$
\frac{p'(w)}{p(w)}=\sum_{j=1}^N\frac{1}{w-z_j}.
$$

::: pf-proof
$p$ is a product of the linear factors $z-z_j$ times the nonzero constant $c$; differentiating logarithmically, $\frac{p'}{p}=\sum_j\frac{(z-z_j)'}{z-z_j}=\sum_j\frac1{z-z_j}$ wherever no factor vanishes, i.e. at $w$ with $p(w)\ne0$.
:::

:::

::: {.pf-step #reduce}
It suffices to prove the claim when $H=\{z:\operatorname{Re}z\ge0\}$.

::: pf-proof
A closed half-plane $H$ is $\{z:\operatorname{Re}(e^{-i\theta}(z-a))\ge0\}$ for some $a\in\CC$ and $\theta\in\RR$. Put $\phi(\zeta)=a+e^{i\theta}\zeta$ and $q(\zeta)=p(\phi(\zeta))$; then $q$ is a polynomial whose zeros are $\phi^{-1}(z_j)$, lying in $\phi^{-1}(H)=\{\operatorname{Re}\zeta\ge0\}$, and $q'(\zeta)=e^{i\theta}p'(\phi(\zeta))$, so zeros of $p'$ correspond to zeros of $q'$ under $\phi$. So it is enough to treat the half-plane $\{\operatorname{Re}\zeta\ge0\}$, and I do so below, dropping the new letter.
:::

:::

::: {.pf-step #trivial}
A zero of $p'$ which is also a zero of $p$ lies in $H$.

::: pf-proof
The zeros of $p$ all lie in $H$ by hypothesis.
:::

:::

::: {.pf-step #main}
If $p'(w)=0$ and $p(w)\ne0$ then $w\in H$.

::: pf-proof
Suppose $w\notin H$, that is $\operatorname{Re}w<0$. For each $j$, $z_j\in H$ gives $\operatorname{Re}z_j\ge0$, hence
$$
\operatorname{Re}(w-z_j)=\operatorname{Re}w-\operatorname{Re}z_j<0 .
$$
Also $w\ne z_j$ because $p(w)\ne0$. Since $\frac1\zeta=\frac{\overline\zeta}{\abs\zeta^2}$,
$$
\operatorname{Re}\frac{1}{w-z_j}=\frac{\operatorname{Re}(w-z_j)}{\abs{w-z_j}^2}<0
$$
for every $j$, so
$$
\operatorname{Re}\sum_{j=1}^N\frac{1}{w-z_j}=\sum_{j=1}^N\operatorname{Re}\frac1{w-z_j}<0 .
$$
But $p'(w)=0$ and $p(w)\ne0$ make that sum equal to $\frac{p'(w)}{p(w)}=0$ by step [](#logderiv){.pf-ref}, a contradiction.
:::

:::

::: {.pf-step}
Every zero of $p'$ lies in $H$.

::: pf-proof
Let $v$ be a zero of $p'$. If $p(v)=0$ then $v\in H$ by step [](#trivial){.pf-ref}; otherwise $v\in H$ by step [](#main){.pf-ref}.
:::

:::

:::
:::
