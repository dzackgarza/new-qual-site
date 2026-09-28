---
schema: qual/card@1
id: E-HAT-3.C-3
kind: problem
title: "Path-components of homotopy-associative H-spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that in a homotopy-associative H-space whose set of path-components is a group with respect to the multiplication induced by the H-space structure, all the path-components must be homotopy equivalent.
[Homotopy-associative means associative up to homotopy.]
:::

::: {.solution}
Let $X_0$ be the path-component of the identity $e$, and let $X_a$ be any other path-component. Choose $x\in X_a$. Since the set of path-components is a group under multiplication, choose $y$ in the inverse component $X_{a^{-1}}$.

Left multiplication by $x$ defines a map
\[
L_x:X_0\to X_a,
\qquad z\mapsto\mu(x,z),
\]
and left multiplication by $y$ defines
\[
L_y:X_a\to X_0.
\]
By homotopy associativity,
\[
L_yL_x(z)=\mu(y,\mu(x,z))
\simeq \mu(\mu(y,x),z)=L_{yx}(z).
\]
The point $\mu(y,x)$ lies in the identity component $X_0$, so choose a path in $X_0$ from $\mu(y,x)$ to $e$. Multiplication along this path gives a homotopy
\[
L_{yx}\simeq L_e\simeq\operatorname{id}_{X_0}.
\]
Similarly,
\[
L_xL_y\simeq L_{xy}\simeq\operatorname{id}_{X_a}.
\]
Therefore $L_x:X_0\to X_a$ is a homotopy equivalence. Since $X_a$ was arbitrary, all path-components are homotopy equivalent.
:::
