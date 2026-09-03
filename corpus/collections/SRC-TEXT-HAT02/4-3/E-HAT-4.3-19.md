---
schema: qual/card@1
id: E-HAT-4.3-19
kind: problem
title: "Exactness improvement via $B$-action"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Given a fibration $F \to E \xrightarrow{p} B$, define a natural action of $B$ on the homotopy fiber $F_p$ and use this to show that exactness at $\langle X, F \rangle$ in the long exact sequence can be improved to the statement that two elements of $\langle X, F \rangle$ have the same image in $\langle X, E \rangle$ if they are in the same orbit of the induced action of $\langle X, B \rangle$ on $\langle X, F \rangle$.

::: {.solution}
**Goal.** Define the action of $\pi_1(B)$ on the homotopy fiber $F_p$ of a fibration, and use it to sharpen exactness of the long exact sequence at $\langle X, F\rangle$.

<1>1. The homotopy fiber and its $\pi_1(B)$-action.
<2>1. The homotopy fiber over $p \in B$ is $F_p \definedas \theset{(e, \gamma) \suchthat e \in E,\ \gamma: I \to B,\ \gamma(0) = p(e),\ \gamma(1) = p}$.
::: {.proof}
this is the pullback of $E \xrightarrow{p} B$ along the path fibration $PB \to B$, $\gamma \mapsto \gamma(1)$.
:::
<2>2. A loop $\lambda \in \Omega B$ (based at $p$) acts by $\lambda \cdot (e, \gamma) \definedas (e, \lambda \cdot \gamma)$, where $\lambda \cdot \gamma$ is the concatenation of $\gamma$ followed by $\lambda$.
::: {.proof}
$\lambda \cdot \gamma$ is a path from $p(e)$ to $p$ (since $\lambda$ is a loop at $p$), so the result lies in $F_p$; this is a continuous action of $\Omega B$ on $F_p$.
:::
<2>3. This descends to an action of $\pi_1(B, p) = \pi_0(\Omega B)$ on $F_p$, hence on $\pi_n(F_p)$ and on $\langle X, F_p\rangle$.
::: {.proof}
homotopic loops give homotopic self-maps of $F_p$, so the action factors through $\pi_1(B, p)$.
:::

<1>2. Sharpened exactness at $\langle X, F\rangle$.
<2>1. The map $i: F_p \to E$, $(e, \gamma) \mapsto e$, fits into the fibration sequence $F_p \xrightarrow{i} E \xrightarrow{p} B$, giving exactness $\langle X, F_p\rangle \xrightarrow{i_*} \langle X, E\rangle \xrightarrow{p_*} \langle X, B\rangle$.
::: {.proof}
the long exact sequence of homotopy groups, applied to the fibration.
:::
<2>2. Claim: for $f, g: X \to F_p$, one has $i \circ f \simeq i \circ g$ iff $f$ and $g$ are in the same $\pi_1(B)$-orbit.
::: {.proof}
a homotopy $H: X \times I \to E$ from $i \circ f$ to $i \circ g$ projects to $p \circ H: X \times I \to B$, a homotopy of paths from $p \circ f$ to $p \circ g$; for each $x \in X$ the loop $p \circ H(x, -)$ (closed up by the constant paths at $p$) is an element of $\pi_1(B, p)$, and this loop acts on $f(x)$ to give $g(x)$.
:::
<2>3. Hence two elements of $\langle X, F\rangle$ have the same image in $\langle X, E\rangle$ iff they are in the same orbit of the $\pi_1(B)$-action.
::: {.proof}
<1>2.2 restates the kernel of $i_*$ as the orbit relation.
:::

<1>3. Q.E.D.
::: {.proof}
<1>2.3 is the sharpened exactness statement.
:::
:::
