---
schema: qual/card@1
id: E-SS2.EX-6
kind: problem
title: Cauchy's theorem for a triangle with one bounded interior singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy's Theorem
  - Removable Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
Let $\Omega$ be an open subset of $\CC$ and let $T \subset \Omega$ be a triangle whose interior is also contained in $\Omega$. Suppose that $f$ is a function holomorphic in $\Omega$ except possibly at a point $w$ inside $T$. Prove that if $f$ is bounded near $w$, then

$$
\int_T f(z)\, dz = 0.
$$
:::

::: {.solution}

The argument is the card's own: excise a small square around the exceptional point, apply Goursat off it, and let the square shrink.

::: pf

::: {.pf-step #excision}

There is $r>0$ and $M$ with the closed square $Q_{r}$ around $w$ inside $T$ and $\abs{f}\le M$ on it.

::: pf-proof

$f$ is holomorphic on $\Omega$ except possibly at $w$, and is bounded near $w$: there are $\eta>0$ and $M$ with $\abs{f}\le M$ on $D(w,\eta)\cap(\Omega-\{w\})$. Since $w$ lies in the interior of $T$ and $T$ with its interior lies in the open set $\Omega$, a small square centred at $w$ is contained in the interior of $T$ and in $D(w,\eta)$; choose $r>0$ that small and increase $M$ to cover the finitely many points if necessary.

:::

:::

::: {.pf-step #goursat}

$\displaystyle\int_{T}f\,dz=\int_{\partial Q_{r}}f\,dz$.

::: pf-proof

The compact polygonal region $T-\operatorname{int}(Q_{r})$ can be triangulated into finitely many closed triangles each lying in $T$ and meeting the boundary of $Q_{r}$ along an edge, and each avoiding $w$ in its closure by the choice of $Q_{r}\subset\operatorname{int}T$. On each such triangle $f$ is holomorphic in a neighbourhood of the closed triangle, since that neighbourhood avoids $w$; Goursat's theorem then gives zero integral of $f$ around its boundary. Summing these vanishing integrals cancels every interior edge, which appears twice with opposite orientations, leaving the boundary of $T$ together with the boundary of $Q_{r}$ traversed negatively:
$$
\int_{\partial T}f\,dz-\int_{\partial Q_{r}}f\,dz=0.
$$

:::

:::

::: {.pf-step #bound}

$\abs{\int_{\partial Q_{r}}f\,dz}\le 8Mr$.

::: pf-proof

The boundary of $Q_{r}$ consists of four segments each of length $2r$, so its total length is $8r$. On it, $\abs{f}\le M$ by step [](#excision){.pf-ref}. The standard estimate for a contour integral bounds the modulus of the integral by the maximum of the integrand times the length of the contour.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle\int_{T}f\,dz=0$.

::: pf-proof

Steps [](#goursat){.pf-ref} and [](#bound){.pf-ref} give $\abs{\int_{T}f\,dz}=\abs{\int_{\partial Q_{r}}f\,dz}\le 8Mr$ for every sufficiently small $r>0$, and $8Mr\to0$ as $r\downarrow0$; the left side does not depend on $r$. A nonnegative real number bounded by arbitrarily small positive numbers is $0$, so
$$
\boxed{\int_{T}f(z)\,dz=0.}
$$

:::

:::

:::

:::
