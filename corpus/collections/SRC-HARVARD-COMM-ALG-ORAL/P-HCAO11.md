---
schema: qual/card@1
id: P-HCAO11
kind: problem
title: Endomorphism ring of the integers
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Describe the ring $\operatorname{End}_{\ZZ}(\ZZ)$.
:::

::: {.solution}
There is a ring isomorphism
$$
\operatorname{End}_{\ZZ}(\ZZ)\cong\ZZ.
$$

::: pf

::: {.pf-step #endomorphism-is-multiplication}
Every $\ZZ$-module endomorphism of $\ZZ$ is multiplication
by a unique integer.

::: pf-proof
Let $f:\ZZ\to\ZZ$ be $\ZZ$-linear and set $n=f(1)$. For every
$m\in\ZZ$,
$$
f(m)=f(m\cdot1)=m f(1)=mn.
$$
Thus $f$ is multiplication by $n$, and $n$ is uniquely determined by $f(1)$.
Conversely, multiplication by any $n\in\ZZ$ is a $\ZZ$-module
endomorphism.
:::

:::

::: pf-step
The map
$$
\Phi:\operatorname{End}_{\ZZ}(\ZZ)\to\ZZ,
\qquad
f\mapsto f(1),
$$
is a ring isomorphism.

::: pf-proof
By step [](#endomorphism-is-multiplication){.pf-ref} it is bijective. If $f(1)=m$ and $g(1)=n$, then
$$
(f+g)(1)=m+n,
$$
while
$$
(f\circ g)(1)=f(n)=nm.
$$
Since integer multiplication is commutative, composition corresponds exactly
to multiplication in $\ZZ$. The identity endomorphism maps to $1$.
:::

:::

:::
:::
