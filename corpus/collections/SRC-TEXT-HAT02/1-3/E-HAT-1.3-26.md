---
schema: qual/card@1
id: E-HAT-1.3-26
kind: problem
title: "Covering spaces and fundamental groups"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 26; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified monodromy orbits with path components and stabilizers with closed lifts of based loops.
---

For a covering space $p: \tilde{X} \to X$ with $X$ connected, locally path-connected, and semilocally simply-connected, show:

(a) The components of $\tilde{X}$ are in one-to-one correspondence with the orbits of the action of $\pi_1(X, x_0)$ on the fiber $p^{-1}(x_0)$.

(b) Under the Galois correspondence between connected covering spaces of $X$ and subgroups of $\pi_1(X, x_0)$, the subgroup corresponding to the component of $\tilde{X}$ containing a given lift $\tilde{x}_0$ of $x_0$ is the stabilizer of $\tilde{x}_0$, the subgroup consisting of elements whose action on the fiber leaves $\tilde{x}_0$ fixed.


::: {.solution}
Let
\[
G=\pi_1(X,x_0)
\]
act on the fiber $F=p^{-1}(x_0)$ by lifting based loops.

<1>1. Two points $\tilde x_0,\tilde x_1\in F$ lie in the same $G$-orbit if and only if they lie in the same path component of $\widetilde X$.
::: {.proof}
Suppose first that $\tilde x_1$ is obtained from $\tilde x_0$ by the action of $[\gamma]\in G$.
By definition, a lift of $\gamma$ joins these two fiber points, so they lie in the same path component.

Conversely, suppose a path
\[
\tilde\alpha:I\to\widetilde X
\]
joins $\tilde x_0$ to $\tilde x_1$.
Then
\[
\alpha=p\circ\tilde\alpha
\]
is a loop at $x_0$.
The path $\tilde\alpha$ is a lift of this loop, so the monodromy action of $[\alpha]$ sends one endpoint to the other, according to the convention used for the action.
Thus the two fiber points lie in the same orbit.
:::

<1>2. Since $X$ is locally path connected, every component of $\widetilde X$ is path connected.
Hence the components of $\widetilde X$ are in bijection with the $G$-orbits in $F$.
::: {.proof}
A covering space of a locally path-connected space is locally path connected.
In a locally path-connected space, components are open and equal path components.
Now apply <1>1.
This proves part (a).
:::

<1>3. Fix $\tilde x_0\in F$ and let $\widetilde X_0$ be its component.
The stabilizer of $\tilde x_0$ is
\[
\operatorname{Stab}_G(\tilde x_0)
=\{[\gamma]\in G:\text{the lift of $\gamma$ at $\tilde x_0$ is closed}\}.
\]
::: {.proof}
By definition, $[\gamma]$ fixes $\tilde x_0$ exactly when the lift of $\gamma$ beginning at $\tilde x_0$ ends again at $\tilde x_0$.
:::

<1>4. One has
\[
\operatorname{Stab}_G(\tilde x_0)
=p_*\pi_1(\widetilde X_0,\tilde x_0).
\]
::: {.proof}
If $[\tilde\gamma]\in\pi_1(\widetilde X_0,\tilde x_0)$, then $p\circ\tilde\gamma$ is a loop whose lift beginning at $\tilde x_0$ is precisely $\tilde\gamma$, hence is closed.
Therefore its class lies in the stabilizer.

Conversely, if $[\gamma]$ stabilizes $\tilde x_0$, its lift at $\tilde x_0$ is a loop in the component $\widetilde X_0$, and
\[
p_*[\tilde\gamma]=[\gamma].
\]
Thus the two subgroups coincide.
:::

<1>5. Under the connected-covering/subgroup correspondence, the component $\widetilde X_0\to X$ corresponds exactly to the stabilizer of $\tilde x_0$.
::: {.proof}
The subgroup assigned by the Galois correspondence to the pointed connected cover
\[
(\widetilde X_0,\tilde x_0)\to(X,x_0)
\]
is by definition
\[
p_*\pi_1(\widetilde X_0,\tilde x_0).
\]
By <1>4 this is the stabilizer.
This proves part (b).
:::
:::
