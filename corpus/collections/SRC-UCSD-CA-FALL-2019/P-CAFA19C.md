---
schema: qual/card@1
id: P-CAFA19C
kind: problem
title: "The annuli A(0;0,1) and A(0;1,2) are not conformally equivalent"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A_1 = \{z \in \mathbb{C} : 0 < |z| < 1\}$ and $A_2 = \{z \in \mathbb{C} : 1 < |z| < 2\}$.
Prove $A_1$ and $A_2$ are not conformally equivalent.
:::

::: {.solution}
**Goal.** Show the punctured disk $A_1$ and the annulus $A_2$ are not conformally equivalent.

<1>1. $A_1$ is conformally equivalent to the punctured disk $\DD \sm \theset{0}$, which is not an annulus of positive modulus.
Proof: $A_1 = \theset{0 < |z| < 1}$ is the punctured unit disk.

<1>2. $A_1$ has a removable singularity at $0$.
<2>1. Any bounded holomorphic function on $A_1$ extends holomorphically to $0$.
Proof: Riemann's removable singularity theorem: a bounded holomorphic function on a punctured disk extends across the puncture.
<2>2. In particular, a conformal equivalence $f: A_1 \to A_2$ (which is bounded, since $A_2$ is bounded) would extend to a holomorphic map $\tilde f: \DD \to \overline{A_2}$.
Proof: $f$ is bounded, so it extends across $0$.

<1>3. The extension $\tilde f$ would map $0$ to a boundary point of $A_2$.
<2>1. $\tilde f(0) \in \overline{A_2}$ and $\tilde f(0) \notin A_2$ (else $f$ would not be onto, or $f^{-1}$ would extend).
Proof: if $\tilde f(0) \in A_2$, then $f$ extends to a homeomorphism of $\DD$ onto a subset of $A_2$, contradicting that $f$ is a bijection onto $A_2$ (the point $\tilde f(0)$ would be hit twice, or $f^{-1}$ would be undefined there).
<2>3. Hence $\tilde f(0) \in \partial A_2 = \theset{|z| = 1} \cup \theset{|z| = 2}$.
Proof: the boundary of $A_2$.

<1>4. Contradiction via the open mapping theorem.
<2>1. $\tilde f$ is holomorphic and nonconstant, so $\tilde f(\DD)$ is open.
Proof: open mapping theorem.
<2>2. But $\tilde f(0) \in \partial A_2$ is a boundary point, and $\tilde f(\DD)$ contains $\tilde f(0)$ with a neighborhood of it (since $\tilde f$ is open at $0$).
Proof: $\tilde f$ maps a neighborhood of $0$ to a neighborhood of $\tilde f(0)$.
<2>3. This forces $\tilde f(0)$ to be an interior point of $\tilde f(\DD) \subseteq \overline{A_2}$, contradicting $\tilde f(0) \in \partial A_2$.
Proof: a boundary point of $A_2$ cannot be an interior point of a subset of $\overline{A_2}$.

<1>5. Q.E.D.
Proof: <1>4.3 gives the contradiction, so $A_1$ and $A_2$ are not conformally equivalent.
:::
