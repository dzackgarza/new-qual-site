---
schema: qual/card@1
id: P-EMCA9
kind: problem
title: Nonconstant entire functions have dense image
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Casorati-Weierstrass
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (9) of Arango-Piñeros, Some quals problems; merged the duplicate E-N6PDJ, whose solution repeats this Liouville argument."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "JHU Spring 2015 poses the same problem; merged its duplicate card P-8XT37, whose solution is the same Liouville argument, and that sitting now lists this card."
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: density fails only
    with a ball disjoint from the image, which gives |f - a| >= r; the reciprocal is then
    entire with |g| <= 1/r because f - a is zero-free; Liouville makes g constant, hence f
    constant; so nonconstant f has dense image. The statement is true as printed, and the
    equivalence "not dense <-> some ball is missed" that the prose used in one sentence is now
    a step. The collection's provenance is the examination paper only, so no retained solution
    set covers the exercise and the argument is the card's own.
---

::: {.problem}
If $f$ is a non-constant entire function, then $f(\CC)$ is dense in the plane.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #not-dense}
If $f(\CC)$ is not dense in $\CC$, there are $a\in\CC$ and $r>0$ with $\abs{f(z)-a}\ge r$ for every $z\in\CC$.

::: pf-proof
A set is dense in $\CC$ exactly when it meets every ball $B(a,r)$ with $r>0$. If $f(\CC)$ is not dense, some ball satisfies $B(a,r)\cap f(\CC)=\emptyset$, which says precisely that no value $f(z)$ lies within distance $r$ of $a$.
:::

:::

::: {.pf-step #reciprocal}
$g(z)\coloneqq\frac{1}{f(z)-a}$ is entire and $\abs{g(z)}\le\frac1r$ for every $z$.

::: pf-proof
$f$ is entire, so $f-a$ is; the bound $\abs{f(z)-a}\ge r>0$ shows $f-a$ has no zeros, so the reciprocal is entire, and $\abs{g(z)}=\frac{1}{\abs{f(z)-a}}\le\frac1r$.
:::

:::

::: {.pf-step}
$f$ is constant.

::: pf-proof
$g$ is entire and bounded, so Liouville's theorem makes $g$ constant, with value $c\ne0$. Then $f(z)=a+\frac1c$ for every $z$, so $f$ is constant.
:::

:::

::: {.pf-step}
$f(\CC)$ is dense in the plane.

::: pf-proof
If $f$ is not constant, step [](#not-dense){.pf-ref} and step [](#reciprocal){.pf-ref} would produce a bounded entire function $g$, which the third step shows forces $f$ to be constant — a contradiction. Hence $f(\CC)$ meets every ball, that is, it is dense.
:::

:::

:::
:::
