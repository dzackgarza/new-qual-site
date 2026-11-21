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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/MATH-220-EXAM-Fall-2019.pdf,
    page 3, problem 3: the punctured disk 0 < |z| < 1 and the annulus
    1 < |z| < 2, to be shown not conformally equivalent. The card agrees.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The argument is correct though written loosely at one point. A conformal
    equivalence f onto the bounded annulus is bounded, so Riemann's removable
    singularity theorem extends it to a holomorphic map of the disk. That
    extension is injective, because a value taken at 0 is also taken at some
    interior point of the punctured disk by surjectivity, so the extended value
    cannot lie in the annulus; it lies on its boundary. The open mapping theorem
    makes the image of the disk open, so the value at 0 is an interior point of
    the image, which is contained in the annulus together with that one point;
    but a boundary point of the annulus has every neighbourhood meeting its
    complement. That contradiction is the conclusion. Nothing was changed.
---

::: {.problem}
Let $A_1 = \{z \in \CC : 0 < \abs{z} < 1\}$ and $A_2 = \{z \in \CC : 1 < \abs{z} < 2\}$.
Prove $A_1$ and $A_2$ are not conformally equivalent.
:::

::: {.solution}
**Goal.** Show the punctured disk $A_1$ and the annulus $A_2$ are not conformally equivalent.

::: pf

::: pf-step
$A_1$ is conformally equivalent to the punctured disk $\DD \sm \theset{0}$, which is not an annulus of positive modulus.

::: pf-proof
$A_1 = \theset{0 < \abs{z} < 1}$ is the punctured unit disk.
:::

:::

::: pf-step
$A_1$ has a removable singularity at $0$.

::: pf-proof

::: pf-step
Any bounded holomorphic function on $A_1$ extends holomorphically to $0$.

::: pf-proof
Riemann's removable singularity theorem: a bounded holomorphic function on a punctured disk extends across the puncture.
:::

:::

::: pf-step
In particular, a conformal equivalence $f: A_1 \to A_2$ (which is bounded, since $A_2$ is bounded) would extend to a holomorphic map $\tilde f: \DD \to \overline{A_2}$.

::: pf-proof
$f$ is bounded, so it extends across $0$.
:::

:::

:::

:::

::: pf-step
The extension $\tilde f$ would map $0$ to a boundary point of $A_2$.

::: pf-proof

::: pf-step
$\tilde f(0) \in \overline{A_2}$ and $\tilde f(0) \notin A_2$ (else $f$ would not be onto, or $f^{-1}$ would extend).

::: pf-proof
if $\tilde f(0) \in A_2$, then $f$ extends to a homeomorphism of $\DD$ onto a subset of $A_2$, contradicting that $f$ is a bijection onto $A_2$ (the point $\tilde f(0)$ would be hit twice, or $f^{-1}$ would be undefined there).
:::

:::

::: pf-step
Hence $\tilde f(0) \in \partial A_2 = \theset{\abs{z} = 1} \cup \theset{\abs{z} = 2}$.

::: pf-proof
the boundary of $A_2$.
:::

:::

:::

:::

::: pf-step
Contradiction via the open mapping theorem.

::: pf-proof

::: pf-step
$\tilde f$ is holomorphic and nonconstant, so $\tilde f(\DD)$ is open.

::: pf-proof
open mapping theorem.
:::

:::

::: pf-step
But $\tilde f(0) \in \partial A_2$ is a boundary point, and $\tilde f(\DD)$ contains $\tilde f(0)$ with a neighborhood of it (since $\tilde f$ is open at $0$).

::: pf-proof
$\tilde f$ maps a neighborhood of $0$ to a neighborhood of $\tilde f(0)$.
:::

:::

::: {.pf-step #s4-3}
This forces $\tilde f(0)$ to be an interior point of $\tilde f(\DD) \subseteq \overline{A_2}$, contradicting $\tilde f(0) \in \partial A_2$.

::: pf-proof
a boundary point of $A_2$ cannot be an interior point of a subset of $\overline{A_2}$.
:::

:::

:::

:::

::: pf-qed
step [](#s4-3){.pf-ref} gives the contradiction, so $A_1$ and $A_2$ are not conformally equivalent.
:::

:::
:::
