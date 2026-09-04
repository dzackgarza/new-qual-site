---
schema: qual/card@1
id: P-AY6TZ
kind: problem
title: The torus does not cover $\RP^2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the migrated solution fragment, which falsely said there are no homomorphisms Z^2 -> Z/2, by the required injectivity obstruction.
---

::: problem
Show that there is no covering map
\[
p:T^2=S^1\times S^1\longrightarrow\RP^2.
\]
:::

::: {.solution}
<1>1. A covering map $p:T^2\to\RP^2$ would induce an injective homomorphism
\[
p_*:\pi_1(T^2)\hookrightarrow\pi_1(\RP^2).
\]
::: {.proof}
A covering-space projection induces an injection on fundamental groups of path-connected based spaces.
:::

<1>2. The groups in <1>1 are
\[
\pi_1(T^2)\cong\ZZ^2,
\qquad
\pi_1(\RP^2)\cong\ZZ/2\ZZ.
\]
::: {.proof}
The first follows from
\[
T^2=S^1\times S^1
\]
and the product formula for fundamental groups. The second is the standard computation from the universal double cover
\[
S^2\to\RP^2.
\]
:::

<1>3. No injective homomorphism $\ZZ^2\to\ZZ/2\ZZ$ exists.
::: {.proof}
The image of any such homomorphism is a subgroup of the two-element group $\ZZ/2\ZZ$, hence has at most two elements. The group $\ZZ^2$ is infinite, so an injective map is impossible.
:::

<1>4. No covering map $T^2\to\RP^2$ exists.
::: {.proof}
Otherwise <1>1 and <1>2 would produce the injection ruled out by <1>3.
:::
:::
