---
schema: qual/card@1
id: E-SS3.EX-16
kind: problem
title: The zero of $f+\epsilon g$ near a simple zero of $f$ is unique and continuous in $\epsilon$
classification:
  areas:
    - complex-analysis
  topics: [Rouché's Theorem, Zeros of Holomorphic Functions, Perturbation]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into numbered steps for issue #2: the small circle isolating the zero, Rouché inside it, the
      annulus bound outside it, and the subsequence argument for continuity. No retained solution set covers
      this exercise (the collection retains the textbook, not a solutions manual), so the argument is the
      card's own; it was re-read for this pass.
---

::: {.exercise}
Suppose $f$ and $g$ are holomorphic in a region containing the disc $\abs{z} \leq 1$. Suppose that $f$ has a simple zero at $z = 0$ and vanishes nowhere else in $\abs{z} \leq 1$. Let
$$
f_\epsilon(z) = f(z) + \epsilon g(z).
$$
Show that if $\epsilon$ is sufficiently small, then

(a) $f_\epsilon(z)$ has a unique zero in $\abs{z} \leq 1$, and

(b) if $z_\epsilon$ is this zero, the mapping $\epsilon \mapsto z_\epsilon$ is continuous.
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own.

::: pf

::: {.pf-step #circle}
There are $0<r<1$, $m>0$ and $M<\infty$ with $0$ the only zero of $f$ in $\abs{z}\le r$, $\abs{f}\ge m$ on $\abs{z}=r$ and $\abs{g}\le M$ on $\abs{z}=r$.

::: pf-proof
The zeros of $f$ in the compact disc $\abs{z}\le1$ are isolated, and $0$ is the only one by hypothesis, so there is $r<1$ with no other zero in $\abs{z}\le r$. On the compact circle $\abs{z}=r$ the continuous function $\abs{f}$ is nowhere zero, so it has a positive minimum $m$; and $\abs{g}$ attains a maximum $M$ there.
:::

:::

::: {.pf-step #inside}
If $\abs{\epsilon}M<m$, then $f_{\epsilon}=f+\epsilon g$ has exactly one zero in $\abs{z}<r$, counted with multiplicity.

::: pf-proof
On $\abs{z}=r$ we have $\abs{\epsilon g}\le\abs{\epsilon}M<m\le\abs{f}$, so $\abs{\epsilon g}<\abs{f}$ strictly on the circle. Rouché's theorem then gives $f_{\epsilon}$ and $f$ the same number of zeros inside the circle, counted with multiplicity; $f$ has exactly one there, namely the simple zero at $0$.
:::

:::

::: {.pf-step #outside}
There is $\delta>0$ such that for $\abs{\epsilon}<\delta$ the function $f_{\epsilon}$ has no zero on $r\le\abs{z}\le1$.

::: pf-proof
On the compact annulus $r\le\abs{z}\le1$ the function $f$ has no zero, so $\abs{f}$ has a positive minimum $m_{1}$ there, while $\abs{g}$ has a finite maximum $M_{1}$. Taking $\delta=\min\{m/M,\,m_{1}/M_{1}\}$ (with $M_{1}=0$ allowed, in which case the second bound is vacuous) gives $\abs{\epsilon g}<\abs{f}$ at every point of the annulus, so $f_{\epsilon}$ never vanishes there.
:::

:::

::: {.pf-step #unique}
(a) For $\abs{\epsilon}<\delta$ the function $f_{\epsilon}$ has a unique zero $z_{\epsilon}$ in $\abs{z}\le1$.

::: pf-proof
By step [](#inside){.pf-ref} there is exactly one zero in $\abs{z}<r$ and by step [](#outside){.pf-ref} none on the annulus $r\le\abs{z}\le1$; the disc $\abs{z}\le1$ is the union of the two, so that one zero, which we call $z_{\epsilon}$, is the only zero there.
:::

:::

::: {.pf-step}
(b) The map $\epsilon\mapsto z_{\epsilon}$ is continuous on $\abs{\epsilon}<\delta$.

::: pf-proof
Let $\epsilon_{n}\to\epsilon$ with all $\abs{\epsilon_{n}}<\delta$. Then $f(z_{\epsilon_{n}})+\epsilon_{n}g(z_{\epsilon_{n}})=0$ and all $z_{\epsilon_{n}}$ lie in the compact disc $\abs{z}\le r$, so some subsequence converges, say to $z_{*}$; letting $n\to\infty$ along it and using continuity of $f$ and $g$ gives $f(z_{*})+\epsilon g(z_{*})=0$, that is $z_{*}$ is a zero of $f_{\epsilon}$ in $\abs{z}\le1$, hence $z_{*}=z_{\epsilon}$ by step [](#unique){.pf-ref}. Every convergent subsequence has the same limit, and the sequence lies in a compact set, so the whole sequence converges to $z_{\epsilon}$; hence the map is continuous, which is part (b).
:::

:::

:::
:::
