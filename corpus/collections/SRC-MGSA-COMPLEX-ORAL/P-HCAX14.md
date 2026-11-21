---
schema: qual/card@1
id: P-HCAX14
kind: problem
title: Poles and residues of the cosecant function
classification:
  areas:
    - complex-analysis
  topics:
    - Residues
    - Poles
relations: []
review: draft
audit:
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      The statement is the oral-examination question recorded for this collection, "Find all
      poles and residues of 1/sin z". No retained solution set for the collection covers it,
      so the argument on the card is its own.
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Restructured the card's own prose into numbered steps. The steps prove the two facts
      the prose states without derivation: that the zeros of sin are exactly the integer
      multiples of pi (from the identity sin(z) = 0 iff e^{iz} = e^{-iz}), and the rule that
      a quotient 1/g has residue 1/g'(a) at a simple zero a of g, which is obtained from the
      Laurent expansion rather than quoted.
---

::: {.problem}
Find all poles and residues of $1/\sin z$.
:::

::: {.solution}

The statement is the question recorded for this collection; no retained solution set covers
it, so the argument below is the card's own.

::: pf

::: {.pf-step #zeros}

$\sin z=0$ exactly for $z=n\pi$, $n\in\ZZ$.

::: pf-proof

$\sin z=(e^{iz}-e^{-iz})/(2i)$, which vanishes exactly when $e^{iz}=e^{-iz}$, that is
$e^{2iz}=1$, that is $2iz\in2\pi i\ZZ$, that is $z\in\pi\ZZ$.

:::

:::

::: {.pf-step #simple}

Every zero of $\sin$ is simple.

::: pf-proof

$(\sin z)'=\cos z$ and $\cos(n\pi)=(-1)^{n}\ne0$ for every integer $n$, while
$\sin(n\pi)=0$ by step [](#zeros){.pf-ref}. A zero at which the derivative does not vanish is
simple, since $\sin z=(z-n\pi)h(z)$ with $h(n\pi)=\cos(n\pi)\ne0$.

:::

:::

::: {.pf-step #poles}

$1/\sin z$ has a simple pole at each $n\pi$ and no other poles.

::: pf-proof

$\sin$ is entire, so $1/\sin z$ is holomorphic off the zeros of $\sin$, which are the points
$n\pi$ by step [](#zeros){.pf-ref}. At $z=n\pi$ write $\sin z=(z-n\pi)h(z)$ with $h$
holomorphic and $h(n\pi)\ne0$ (step [](#simple){.pf-ref}); then
$1/\sin z=(z-n\pi)^{-1}\cdot(1/h(z))$ with $1/h$ holomorphic near $n\pi$, which exhibits a
simple pole.

:::

:::

::: {.pf-step #residue}

For a function $g$ holomorphic near $a$ with a simple zero at $a$, the residue of $1/g$ at
$a$ is $1/g'(a)$.

::: pf-proof

Write $g(z)=(z-a)h(z)$ with $h$ holomorphic near $a$ and $h(a)=g'(a)\ne0$. Then
$1/g(z)=(z-a)^{-1}\cdot(1/h(z))$, and $1/h$ is holomorphic near $a$ with value $1/g'(a)$
there. Comparing with the Laurent expansion $\sum_{k\ge-1}c_{k}(z-a)^{k}$ of $1/g$ about $a$
gives $c_{-1}=1/g'(a)$, which is the residue.

:::

:::

::: {.pf-step #answer}

$\operatorname{Res}_{z=n\pi}\dfrac{1}{\sin z}=(-1)^{n}$, and these are all the residues.

::: pf-proof

By steps [](#poles){.pf-ref} and [](#residue){.pf-ref} with $g=\sin$, $a=n\pi$,
$\operatorname{Res}_{z=n\pi}1/\sin z=1/\cos(n\pi)=(-1)^{n}$. Step [](#poles){.pf-ref} also
shows there are no other poles and hence no other residues.

:::

:::

:::

:::
