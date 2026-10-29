---
schema: qual/card@1
id: P-XWNF6
kind: problem
title: $\pi_1(\bigvee S^1)$ is free, and $S^2\not\cong S^3$
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source problem block held a worked answer: a theorem with proof that pi_1 of a wedge of circles is free (with the index k and n mixed), a lemma that F_n is not isomorphic to F_m for n != m, and an argument that S^2 and S^3 are not homeomorphic citing 'the previous problems'. The statement now poses those three claims, and the solution carries the arguments."
---

::: {.problem}
(a) Show that $\pi_1\left(\bigvee_{i=1}^n S^1\right)$ is the free group $F_n$ on $n$ generators.

(b) Show that $F_n \not\cong F_m$ for $n \neq m$.

(c) Show that $S^2$ and $S^3$ are not homeomorphic.
:::

::: {.solution}

::: pf

::: pf-step
(a) For $n\ge1$, $\pi_1\left(\bigvee_{i=1}^nS^1\right)\cong F_n$.

::: pf-proof
We induct on $n$; the case $n = 1$ is $\pi_1(S^1) \cong \ZZ = F_1$.
For $n > 1$, write $X = \bigvee^n S^1$ with wedge point $p$, and let $U$ be the union of the first $n-1$ circles with a small open arc about $p$ in the last circle, and $V$ the last circle with small open arcs about $p$ in the others.
Then $U$ and $V$ are open and path connected, $U \simeq \bigvee^{n-1} S^1$, $V \simeq S^1$, and $U \cap V$ is contractible.
By van Kampen's theorem and the induction hypothesis, $\pi_1(X) \cong F_{n-1} * \ZZ \cong F_n$.
:::

:::

::: pf-step
(b) If $F_n\cong F_m$, then $n=m$.

::: pf-proof
Abelianizing gives $\ZZ^n\cong\ZZ^m$, and tensoring with $\ZZ/2$ gives $(\ZZ/2)^n \cong (\ZZ/2)^m$, groups of orders $2^n$ and $2^m$.
:::

:::

::: pf-step
(c) $S^2$ and $S^3$ are not homeomorphic.

::: pf-proof
A homeomorphism $h\colon S^2 \to S^3$ would restrict to a homeomorphism $S^2\setminus\{p,q\} \to S^3\setminus\{h(p),h(q)\}$.
But $S^2\setminus\{p,q\}\simeq S^1$, by the deformation retraction of [[P-6DZST]], and $S^3\setminus\{p',q'\}\simeq S^2$, since by stereographic projection from $p'$ it is $\RR^3$ minus a point.
Their fundamental groups are $\ZZ$ and $0$, so the punctured spaces are not homotopy equivalent, hence not homeomorphic.
:::

:::

:::

:::
