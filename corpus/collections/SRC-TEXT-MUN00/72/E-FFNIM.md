---
schema: qual/card@1
id: E-FFNIM
kind: exercise
title: Adjoining cells of dimension above two does not change the fundamental group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $X$ be a Hausdorff space; let $A$ be a closed path-connected subspace.
Suppose that $h: B^n \to X$ is a continuous map that maps $S^{n-1}$ into $A$ and maps $\operatorname{Int} B^n$ bijectively onto $X - A$.
Let $a$ be a point of $h(S^{n-1})$.
If $n > 2$, what can you say about the homomorphism of $\pi_1(A, a)$ into $\pi_1(X, a)$ induced by inclusion?
:::

::: {.solution}
<1>1. Cell attachment description:
<2>1. The space $X$ is homeomorphic to the adjunction space $A \cup_\phi B^n$ formed by attaching an $n$-cell $B^n$ to $A$ along the attaching map $\phi = h|_{S^{n-1}}: S^{n-1} \to A$.
Proof: definition of cell attachment quotient topology.

<1>2. Open cover for Seifert–van Kampen Theorem:
<2>1. Let $p = h(0) \in X \setminus A$ be the center of the attached cell.
Define the open subsets:
\[
U = X \setminus \{p\}, \qquad V = h\big(\{x \in B^n \mid \|x\| < 3/4\}\big).
\]
Proof: openness in the quotient topology.
<2>2. **Retraction of $U$ onto $A$:**
The punctured ball $B^n \setminus \{0\}$ deformation retracts radially onto the boundary $S^{n-1}$.
This radial deformation extends continuously to $X \setminus \{p\}$ by fixing $A$ pointwise, so $A$ is a deformation retract of $U$.
Thus the inclusion $A \hookrightarrow U$ induces an isomorphism:
\[
\pi_1(A, a) \cong \pi_1(U, a).
\]
Proof: homotopy invariance of fundamental group.
<2>3. **Contractibility of $V$:**
$V \cong \operatorname{Int}(B^n)$ is homeomorphic to the open Euclidean ball, which is convex and contractible.
Thus $\pi_1(V) = 0$.
Proof: contractibility of open Euclidean balls.
<2>4. **Simply-connectedness of $U \cap V$ for $n > 2$:**
The intersection $U \cap V = h(\{x \in B^n \mid 0 < \|x\| < 3/4\})$ is homeomorphic to the punctured Euclidean ball $\mathbb{R}^n \setminus \{0\}$, which deformation retracts onto the sphere $S^{n-1}$.
Since $n > 2$, the dimension $n - 1 \ge 2$, so $S^{n-1}$ is simply connected:
\[
\pi_1(U \cap V) \cong \pi_1(S^{n-1}) = 0.
\]
Proof: $\pi_1(S^k) = 0$ for all $k \ge 2$.

<1>3. Seifert–van Kampen Theorem:
<2>1. By the Seifert–van Kampen Theorem, since $U \cap V$ is path-connected:
\[
\pi_1(X, a) \cong \pi_1(U, a) *_{\pi_1(U \cap V)} \pi_1(V) \cong \pi_1(A, a) *_0 0 \cong \pi_1(A, a).
\]
Proof: Seifert–van Kampen Theorem with trivial amalgamating subgroup.
<2>2. The isomorphism $\pi_1(A, a) \xrightarrow{\sim} \pi_1(X, a)$ is precisely the homomorphism $i_*$ induced by the inclusion map $i: A \hookrightarrow X$.
Proof: inclusion factorization $A \hookrightarrow U \hookrightarrow X$.

<1>4. Conclusion:
For $n > 2$, the inclusion-induced map $i_*: \pi_1(A, a) \to \pi_1(X, a)$ is an isomorphism. Q.E.D.
Proof: <1>2 and <1>3.
:::
