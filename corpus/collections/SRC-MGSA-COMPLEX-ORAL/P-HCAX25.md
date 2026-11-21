---
schema: qual/card@1
id: P-HCAX25
kind: problem
title: A mild growth bound makes a puncture removable
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the card's own argument, which is correct and is
    kept: the Laurent coefficients of negative index are bounded by r^m times the maximum
    of |f| on the circle of radius r, and the bound |f| <= |z|^{-1/2} makes that
    r^{m-1/2}, which tends to zero as r does. Added in the restructuring: the coefficient
    formula is the one for the annulus 0 < |z| < 1 with the circle of radius r traced
    counterclockwise (so the sign and the power z^{m-1} are those of the standard
    formula), the estimate |integral| <= length times maximum is cited, and the passage
    from "no principal part" to "the singularity is removable" is stated as the
    construction of a holomorphic extension on the whole disc. No statement repair. No
    retained solution set covers this problem: the collection's provenance,
    assets/attachments/MGSA_Complex_Analysis_Oral_Questions.pdf, is the exam's question
    sheet.
---

::: {.problem}
Let $f$ be holomorphic on the punctured unit disk and suppose
$$
\abs{f(z)}\leq \frac1{\sqrt{\abs{z}}}.
$$
Show that the singularity at the origin is removable.
:::

::: {.solution}
No retained solution set covers this problem — the collection's provenance, `assets/attachments/MGSA_Complex_Analysis_Oral_Questions.pdf`, is the question sheet — so the argument is the card's own, in the standard removable-singularity form.

Throughout, $f$ is holomorphic on the punctured disc $D^{*}=\{z : 0<\abs z<1\}$ and satisfies $\abs{f(z)}\le\abs z^{-1/2}$, $D$ is the open unit disc, and for $0<r<1$ the circle $\abs z=r$ is traced counterclockwise.

::: pf

::: {.pf-step #laurent}
$f$ has a Laurent expansion $f(z)=\sum_{n\in\ZZ}a_nz^{n}$ converging on $D^{*}$, and for every $m\ge1$ and every $0<r<1$ the coefficient $a_{-m}$ is $\frac{1}{2\pi i}\int_{\abs z=r}f(z)z^{m-1}\,dz$.

::: pf-proof
$f$ is holomorphic on the annulus $0<\abs z<1$, so it has a Laurent expansion there, converging uniformly on compact subsets of the annulus, and its coefficients are given by Cauchy's integral formula for an annulus applied to the circle $\abs z=r$: $a_{k}=\frac{1}{2\pi i}\int_{\abs z=r}f(z)z^{-k-1}\,dz$. Putting $k=-m$ gives $a_{-m}=\frac{1}{2\pi i}\int_{\abs z=r}f(z)z^{m-1}\,dz$, the circle lying in the annulus because $0<r<1$.
:::

:::

::: {.pf-step #bound}
For $m\ge1$ and $0<r<1$, $\abs{a_{-m}}\le r^{m-1/2}$.

::: pf-proof
On $\abs z=r$ we have $\abs{f(z)}\le r^{-1/2}$ by hypothesis and $\abs{z^{m-1}}=r^{m-1}$. Estimating the integral of step [](#laurent){.pf-ref} by the length of the circle times the maximum of its integrand,
\[
\abs{a_{-m}}\le\frac{1}{2\pi}\cdot2\pi r\cdot r^{-1/2}\cdot r^{m-1}=r^{m}\cdot r^{-1/2}=r^{m-1/2}.
\]
:::

:::

::: {.pf-step #vanish}
$a_{-m}=0$ for every $m\ge1$.

::: pf-proof
Fix $m\ge1$. The number $a_{-m}$ does not depend on $r$, and step [](#bound){.pf-ref} gives $\abs{a_{-m}}\le r^{m-1/2}$ for every $0<r<1$. Since $m-\tfrac12>0$, $r^{m-1/2}\to0$ as $r\downarrow0$, so $\abs{a_{-m}}\le0$ and $a_{-m}=0$.
:::

:::

::: {.pf-step #removable}
$f$ agrees on $D^{*}$ with a function holomorphic on $D$; hence the singularity at $0$ is removable.

::: pf-proof
By step [](#vanish){.pf-ref} the Laurent series of $f$ has no negative-index term, so $f(z)=\sum_{n\ge0}a_nz^{n}$ on $D^{*}$. The power series $g(z)=\sum_{n\ge0}a_nz^{n}$ has radius of convergence at least $1$ — its coefficients are those of the Laurent expansion, which converges on $D^{*}$ — so $g$ is holomorphic on $D$ and agrees with $f$ on $D^{*}$. Extending $f$ by $f(0)=g(0)$ therefore gives a holomorphic function on $D$, which is exactly the assertion that the singularity at the origin is removable.
:::

:::

:::
:::
