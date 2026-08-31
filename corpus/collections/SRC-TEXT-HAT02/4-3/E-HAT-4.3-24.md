---
schema: qual/card@1
id: E-HAT-4.3-24
kind: exercise
title: "Obstructions for homotopy of lifts"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

In the situation of the relative lifting problem, suppose one has two different lifts $W \to X$ that agree on the subspace $A \subset W$.
Show that the obstructions to finding a homotopy rel $A$ between these two lifts lie in the groups $H^n(W, A; \pi_n F)$.

::: {.solution}
<1>1. Reformulation on the cylinder $W \times I$:
<2>1. Let $p: X \to B$ be a fibration with fiber $F$. Suppose $f_0, f_1: W \to X$ are two lifts of $g: W \to B$ such that $f_0|_A = f_1|_A$.
::: {.proof}
setup.
:::
<2>2. A homotopy $H: W \times I \to X$ between $f_0$ and $f_1$ rel $A$ lifting $G(w, t) = g(w)$ is equivalent to extending a partially defined lift $H$ from the subspace:
\[
Y = (W \times \{0\}) \cup (A \times I) \cup (W \times \{1\}) \subset W \times I
\]
to the entire cylinder $W \times I$, where $H(w, 0) = f_0(w)$, $H(w, 1) = f_1(w)$, and $H(a, t) = f_0(a) = f_1(a)$ for $a \in A$.
::: {.proof}
definition of relative homotopy between lifts.
:::

<1>2. Cellular decomposition of the cylinder pair:
<2>1. Endow the CW pair $(W, A)$ with a relative CW structure.
The relative product cell structure on $(W \times I, Y)$ has cells in bijective correspondence with the cells of $W \setminus A$:
An $n$-cell $e^n$ of $W \setminus A$ gives rise to an $(n+1)$-cell $e^n \times (0, 1)$ in $(W \times I) \setminus Y$.
::: {.proof}
product cellular decomposition with $I = [0, 1]$.
:::
<2>2. The boundary of the cell $e^n \times I$ is:
\[
\partial(e^n \times I) = (e^n \times \{0\}) \cup (\partial e^n \times I) \cup (e^n \times \{1\}) \cong S^n.
\]
::: {.proof}
boundary formula for cylinder cells.
:::

<1>3. Obstruction cochains and groups:
<2>1. Suppose $H$ has been extended to $(W \times I)^{n} \cup Y$.
To extend $H$ across an $(n+1)$-cell $e^n \times (0, 1)$, $H$ is already defined on the boundary $\partial(e^n \times I) \cong S^n$.
Since $p \circ H = g \circ \operatorname{pr}_W$ is contractible on $e^n \times I$, the map on the boundary takes values in the fiber $F$, determining an element of $\pi_n(F)$.
::: {.proof}
standard obstruction theory for extending sections of fibrations.
:::
<2>2. This defines an obstruction cocycle:
\[
c^{n+1} \in C^{n+1}(W \times I, Y; \pi_n F).
\]
::: {.proof}
assignment of boundary homotopy classes to $(n+1)$-cells.
:::
<2>3. By the suspension isomorphism for relative CW pairs:
\[
C^{n+1}(W \times I, (W \times \partial I) \cup (A \times I); \pi_n F) \cong C^n(W, A; \pi_n F),
\]
which passes to cohomology to yield:
\[
H^{n+1}(W \times I, Y; \pi_n F) \cong H^n(W, A; \pi_n F).
\]
::: {.proof}
excision and suspension isomorphism in relative cohomology.
:::

<1>4. Conclusion:
The obstruction to finding a homotopy rel $A$ between the two lifts at stage $n$ lies in $H^n(W, A; \pi_n F)$. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
