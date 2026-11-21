---
schema: qual/card@1
id: E-SS2.EX-10
kind: problem
title: Not every continuous function on the closed disc is a uniform limit of polynomials in $z$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Cauchy's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. Three steps are now separate:
    Cauchy's theorem giving the vanishing of the integral of each polynomial over the circle,
    the passage to the limit justified by uniform convergence on the compact circle, and the
    direct computation of the integral of z-bar, which is where the contradiction sits. The
    card also states that z-bar is continuous, which is what makes the example admissible
    against Weierstrass's theorem in one real variable. Not checked: the book's own text of the
    exercise, since no copy of Stein and Shakarchi is retained in this checkout; the statement
    is as transcribed on the card. No retained solution set covers the exercise (the
    collection's provenance is a Google Books record), so the argument is the card's own. No
    statement repair.
---

::: {.exercise}
Weierstrass's theorem states that a continuous function on $[0,1]$ can be uniformly approximated by polynomials.
Can every continuous function on the closed unit disc be approximated uniformly by polynomials in the variable $z$?
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. The answer is no. Let $\overline\DD=\{z:\abs{z}\le1\}$ and $C$ be the unit circle traversed counterclockwise, and take
$$
f(z)=\overline z,
$$
which is continuous on $\overline\DD$.

::: pf

::: {.pf-step #zero}
For every polynomial $p$ one has $\int_Cp(z)\,dz=0$.

::: pf-proof
A polynomial is entire, so it has a primitive on $\CC$, and the integral of a derivative over a closed contour vanishes; this is Cauchy's theorem for a function with a primitive. Explicitly, if $p=\sum_kc_kz^k$ then $\int_Cp\,dz=\sum_kc_k\int_Cz^k\,dz=0$, because $\int_Cz^k\,dz=\bigl[z^{k+1}/(k+1)\bigr]$ along a closed curve, and for $k\ge0$ the antiderivative is single valued.
:::

:::

::: {.pf-step #limit}
If polynomials $p_n$ converge uniformly to $f$ on $C$, then $\int_Cf\,dz=0$.

::: pf-proof
Uniform convergence on $C$ means $\sup_C\abs{p_n-f}\to0$. Then
$$
\abs{\int_Cf\,dz-\int_Cp_n\,dz}=\abs{\int_C(f-p_n)\,dz}\le\sup_C\abs{f-p_n}\cdot\text{length}(C)\to0
$$
because $C$ has finite length $2\pi$, so the integrals converge; by step [](#zero){.pf-ref} all the terms of the left side vanish, hence so does the limit.
:::

:::

::: {.pf-step #compute}
$\int_C\overline z\,dz=2\pi i\ne0$.

::: pf-proof
Parametrize $C$ by $z=e^{i\theta}$, $0\le\theta\le2\pi$, so $\overline z=e^{-i\theta}$ and $dz=ie^{i\theta}d\theta$; then $\overline z\,dz=e^{-i\theta}ie^{i\theta}d\theta=i\,d\theta$ and
$$
\int_C\overline z\,dz=\int_0^{2\pi}i\,d\theta=2\pi i\ne0 .
$$
:::

:::

::: {.pf-step}
No sequence of polynomials in $z$ converges uniformly to $\overline z$ on the closed unit disc.

::: pf-proof
Uniform convergence on the closed disc restricts to uniform convergence on $C$, so such a sequence would give $\int_C\overline z\,dz=0$ by step [](#limit){.pf-ref}, contradicting step [](#compute){.pf-ref}. Hence not every continuous function on the closed disc is a uniform limit of polynomials in $z$, although $z\mapsto\overline z$ is continuous and Weierstrass's theorem applies to its real and imaginary parts as functions of two real variables. This answers the question in the negative.
:::

:::

:::

:::
