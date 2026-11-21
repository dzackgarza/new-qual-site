---
schema: qual/card@1
id: P-CAFA22F
kind: problem
title: "Polynomial minus exponential has infinitely many zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, with one
    statement sharpened: the prose said F cannot be rational "because e^{az} is transcendental
    and p is a nonzero polynomial", which is not the reason. The card now argues that a
    rational F would make e^{az} = pF rational, hence a polynomial, and that e^{az} is not a
    polynomial because it grows faster than any polynomial along a ray. Also added: that the
    poles of F are exactly the zeros of p, that the singularity at infinity is neither a pole
    nor removable and hence essential, and that the exceptional value of Picard's theorem is
    at most one while 0 is omitted, so 1 is attained infinitely often. Not claimed: a retained
    solution set; the provenance names the examination paper.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, with one
    statement sharpened: the prose said F cannot be rational "because e^{az} is transcendental
    and p is a nonzero polynomial", which is not the reason. The card now argues that a
    rational F would make e^{az} = pF rational, hence a polynomial, and that e^{az} is not a
    polynomial because it grows faster than any polynomial along a ray. Also added: that the
    poles of F are exactly the zeros of p, that the singularity at infinity is neither a pole
    nor removable and hence essential, and that the exceptional value of Picard's theorem is
    at most one while 0 is omitted, so 1 is attained infinitely often. Not claimed: a retained
    solution set; the provenance names the examination paper.
---

::: {.problem}
If $p \neq 0$ is a polynomial and $a \neq 0$ is a complex number, show that $p(z) - e^{az}$ has infinitely many zeros.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/FA22_COMPLEX_220ABC.pdf`, the examination paper (it opens with the three-hour instructions), which carries no solutions. The argument below is the card's own and follows the card's previous prose, with the reason $F$ is not rational made a statement about $e^{az}$ rather than a claim about "transcendence".

Throughout $p\ne0$ is a polynomial and $a\ne0$ a complex number, and $F(z)=e^{az}/p(z)$ is meromorphic on $\CC$, with poles at the zeros of $p$.

::: pf

::: {.pf-step #poles}
$p$ has finitely many zeros, so $F$ is meromorphic on $\CC$ with finitely many poles, and $F$ is not a rational function.

::: pf-proof
A nonzero polynomial has finitely many roots, each a pole of $F$ of finite order, and $e^{az}$ is entire and never zero, so $F$ is meromorphic with exactly those poles. If $F$ were rational, then $e^{az}=p(z)F(z)$ would be rational: a product of rational functions is rational. But an entire rational function is a polynomial, and $e^{az}$ is not a polynomial for $a\ne0$ — along the real axis with $a$ real and positive, $e^{ax}$ grows faster than any polynomial in $x$, and for complex $a$ the same holds along the ray where $\operatorname{Re}(az)>0$ and $\abs z=t\to\infty$.

:::

:::

::: {.pf-step #essential}
$F$ has an essential singularity at $\infty$.

::: pf-proof
The isolated singularities of a meromorphic function on the sphere are its poles, and $\infty$ is not a pole of $F$: a pole at $\infty$ would make $F$ rational (multiplying by a suitable polynomial would make it entire and vanish at $\infty$). Nor is $\infty$ removable, since then $F$ would again be rational. So $\infty$ is an essential singularity, by the classification of isolated singularities.

:::

:::

::: {.pf-step #picard}
$F$ assumes the value $1$ infinitely often.

::: pf-proof
By the great Picard theorem, in every punctured neighbourhood of an essential singularity a meromorphic function assumes every value with at most one exception, infinitely often. The value $0$ is never assumed, since $e^{az}\ne0$; as $0\ne1$, the value $1$ is not the exceptional value, so $F^{-1}(1)$ is infinite.

:::

:::

::: {.pf-step #zeros}
$p(z)-e^{az}$ has infinitely many zeros.

::: pf-proof
At a point $z$ with $F(z)=1$ one has $e^{az}=p(z)$ with $p(z)\ne0$, because $F$ is defined there; so such a $z$ is a zero of $p-e^{az}$. By step [](#picard){.pf-ref} there are infinitely many such points, hence infinitely many zeros.

:::

:::

:::
:::
