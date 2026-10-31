---
schema: qual/card@1
id: E-HAT-1.1-18
kind: problem
title: Attaching cells of dimension $\geq 2$ gives surjection on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - CW Complexes
  - Cell Attachments
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Applied Lemma 1.15 to the standard two-open-set cover of a cell attachment and then iterated the one-cell result over the CW skeleta.
---

::: {.problem}
Using Lemma 1.15, show that if a space $X$ is obtained from a path-connected subspace $A$ by attaching a cell $e^n$ with $n \geq 2$, then the inclusion $A \hookrightarrow X$ induces a surjection on $\pi_1$.
Apply this to show:

(a) The wedge sum $S^1 \lor S^2$ has fundamental group $\ZZ$.

(b) For a path-connected CW complex $X$ the inclusion map $X^1 \hookrightarrow X$ of its 1 skeleton induces a surjection $\pi_1(X^1) \longrightarrow \pi_1(X)$.
[For the case that $X$ has infinitely many cells, see Proposition A.1 in the Appendix.]
:::

::: {.solution}
Write $X=A\cup_\varphi D^n$, where $n\ge2$, and let $c$ be the image of the center of $D^n$.

::: pf

::: {.pf-step #open-cover}
The sets $U=X\setminus\{c\}$ and $V=\operatorname{int}(e^n)$ form an open cover of $X$. The space $U$ deformation retracts onto $A$, the space $V$ is contractible, and $U\cap V$ is path connected.

::: pf-proof
The quotient map is a homeomorphism on the open cell. Its inverse images show that both $U$ and $V$ are open in $X$. Radial expansion from the center of $D^n$ to its boundary defines a deformation retraction of $U$ onto $A$; this homotopy fixes the attaching boundary, so it descends through the quotient. The set $V$ is an open $n$-ball, while $U\cap V$ is that ball without its center. The latter is path connected since $n\ge2$.
:::

:::

::: {.pf-step #cell-surjection}
The inclusion $A\hookrightarrow X$ induces a surjection on fundamental groups.

::: pf-proof
Let $\gamma$ be a loop in $X$ based at $x_0\in A$. Apply the subdivision argument of Lemma 1.15 to the open cover in step [](#open-cover){.pf-ref}, with the first and last pieces chosen in $U$. Combine consecutive pieces that lie in the same cover set. Each remaining $V$ piece has both endpoints in $U\cap V$. Replace it by a path in $U\cap V$ with the same endpoints. The replacement is homotopic relative to endpoints in $V$, because $V$ is simply connected. This yields a loop in $U$ homotopic to $\gamma$ relative to $x_0$. The deformation retraction $U\to A$ then gives a loop in $A$ representing $[\gamma]$.
:::

:::

::: pf-step
The wedge $S^1\vee S^2$ has fundamental group $\ZZ$.

::: pf-proof
It is obtained from $S^1$ by attaching a $2$-cell by the constant map. Step [](#cell-surjection){.pf-ref} makes $\pi_1(S^1)\to\pi_1(S^1\vee S^2)$ surjective. Collapsing the $S^2$ summand gives a retraction onto $S^1$, so the same map is injective. It is therefore an isomorphism, and $\pi_1(S^1)\cong\ZZ$.
:::

:::

::: pf-step
For every path-connected CW complex $X$, the inclusion $X^1\hookrightarrow X$ induces a surjection on fundamental groups.

::: pf-proof
For a finite CW complex, attach its cells of dimension at least $2$ one at a time. Step [](#cell-surjection){.pf-ref} applies to each attachment, and the composite of these surjections is surjective. For an arbitrary CW complex, Proposition A.1 places the compact image of any loop in a finite subcomplex $K$. Apply the finite case to the path component of $K$ containing the loop. Its $1$-skeleton lies in $X^1$, so the loop class comes from $\pi_1(X^1)$.
:::

:::

:::

:::
