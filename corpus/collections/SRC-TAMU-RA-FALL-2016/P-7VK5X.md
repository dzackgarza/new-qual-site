---
schema: qual/card@1
id: P-7VK5X
kind: problem
title: The set $\{(x,y):x-y\in A\}$ is Borel, and null when $A$ is null
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: E is the
    preimage of the Borel set A under the continuous map (x,y) -> x-y, so it is Borel and
    hence m x m-measurable; each section is the translate y + A, of measure m(A) by
    translation invariance; Tonelli then gives (m x m)(E) = 0. The measurability that
    Tonelli requires, and the identification of the sections, were implicit in the prose.
    The title was truncated mid-clause ("and null if A is") and now reads "and null when
    A is null". The collection's provenance is the examination paper only, so no retained
    solution set covers the exercise and the argument is the card's own.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    Title only; the statement is as printed and true.
---

::: {.problem}
Prove that if $A$ is a Borel subset of the line, then $E=\{(x,y):x-y\in A\}$ is a Borel subset of the plane.
Prove that if $m(A)=0$, then $(m\times m)(E)=0$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #continuous}
The map $f:\RR^2\to\RR$, $f(x,y)\coloneqq x-y$, is continuous, and $E=f^{-1}(A)$.

::: pf-proof
The projections $(x,y)\mapsto x$ and $(x,y)\mapsto y$ are continuous, so their difference $f$ is; and $(x,y)\in E$ means $x-y\in A$, that is $f(x,y)\in A$.
:::

:::

::: {.pf-step}
If $A\subseteq\RR$ is Borel then $E=\{(x,y):x-y\in A\}$ is a Borel subset of the plane.

::: pf-proof
The preimage of a Borel set under a continuous map is Borel, and step [](#continuous){.pf-ref} exhibits $E$ as $f^{-1}(A)$.
:::

:::

::: {.pf-step #sections}
For every $y\in\RR$ the section $E^y\coloneqq\{x:(x,y)\in E\}$ equals $y+A$, and if $m(A)=0$ then $m(E^y)=0$.

::: pf-proof
$x\in E^y$ means $x-y\in A$, that is $x\in y+A$; so $E^y=y+A$. Lebesgue measure is translation invariant, so $m(y+A)=m(A)$, which is $0$ under the hypothesis.
:::

:::

::: {.pf-step}
If $m(A)=0$ then $(m\times m)(E)=0$.

::: pf-proof
Step [](#continuous){.pf-ref} and step [](#sections){.pf-ref} make $E$ a Borel, hence $m\times m$-measurable, subset of the plane, and every section $E^y$ is measurable. Tonelli's theorem then computes
$$
(m\times m)(E)=\int_{\RR}m(E^y)\,dm(y)=\int_{\RR}0\,dm(y)=0,
$$
the middle equality holding at every $y$ by step [](#sections){.pf-ref}.
:::

:::

:::
:::
