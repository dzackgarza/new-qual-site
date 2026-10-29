---
schema: qual/card@1
id: P-TOP-WORKSHOP-QPH-C1
kind: problem
title: Presentation complex and universal cover for the cyclic group of order two
classification:
  areas: [topology]
  topics: [Covering Spaces, Cell Complexes, Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the first covering-space problem in assets/attachments/QualProblemsHomotopy_extracted.md; malformed MinerU presentation brackets were normalized to standard notation.
---

::: {.problem}
Let
\[
G=\langle x\mid x^2\rangle.
\]
Find the presentation complex $X_G$, identify it as a familiar space, and then find its universal cover $\widetilde X_G$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The presentation complex $X_G$ has one $0$-cell, one $1$-cell, and one $2$-cell.


::: pf-proof

For a presentation
\[
\langle x_1,\dots,x_m\mid r_1,\dots,r_k\rangle,
\]
the presentation complex is formed from one $0$-cell, one oriented $1$-cell for each generator, and one $2$-cell for each relator.

Here there is one generator $x$ and one relator $x^2$. Thus $X_G$ has one cell in each of dimensions $0,1,2$ and no higher-dimensional cells.

:::

:::

::: {.pf-step #s1-2}

The $1$-skeleton of $X_G$ is a circle.


::: pf-proof

The single $1$-cell has both endpoints attached to the unique $0$-cell. Therefore the $1$-skeleton is
\[
S^1.
\]
The oriented loop represented by that circle is the generator $x$.

:::

:::

::: {.pf-step #s1-3}

The attaching map of the $2$-cell is the degree-$2$ map
\[
S^1\to S^1,
\qquad
z\longmapsto z^2.
\]


::: pf-proof

The relator is
\[
x^2.
\]
Traversing the boundary circle of the $2$-cell according to this word means going twice around the unique $1$-cell in its positive orientation. Hence the attaching map has degree $2$.

:::

:::

::: {.pf-step #s1-4}

The resulting CW complex is homeomorphic to the real projective plane:
\[
\boxed{
X_G\cong\RP^2.
}
\]


::: pf-proof

A standard CW decomposition of $\RP^2$ has one cell in each dimension $0,1,2$. Its $1$-skeleton is
\[
\RP^1\cong S^1,
\]
and the $2$-cell is attached along the quotient map
\[
S^1\to\RP^1,
\]
which has degree $2$ after identifying
\[
\RP^1\cong S^1.
\]
Thus its CW attaching data agree exactly with steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}, so the presentation complex is homeomorphic to $\RP^2$.

:::

:::

::: {.pf-step #s1-5}

The quotient map
\[
p:S^2\to\RP^2,
\qquad
p(v)=[v],
\]
is a two-sheeted covering map.


::: pf-proof

The real projective plane is the quotient of the sphere by the antipodal relation
\[
v\sim -v.
\]
Each projective line therefore has exactly two representatives on $S^2$, namely $v$ and $-v$.

For sufficiently small open disks $U\subset S^2$ disjoint from their antipodal images $-U$, the quotient map restricts to homeomorphisms
\[
U\xrightarrow{\cong}p(U),
\qquad
-U\xrightarrow{\cong}p(U).
\]
Hence every point of $\RP^2$ has an evenly covered neighborhood, so $p$ is a two-sheeted covering.

:::

:::

::: {.pf-step #s1-6}

The sphere $S^2$ is simply connected.


::: pf-proof

One has
\[
\pi_1(S^2)=0.
\]
Equivalently, every loop on the $2$-sphere is null-homotopic.

:::

:::

::: {.pf-step #s1-7}

Therefore the covering in step [](#s1-5){.pf-ref} is the universal cover, and
\[
\boxed{
\widetilde X_G\cong S^2.
}
\]


::: pf-proof

By step [](#s1-4){.pf-ref},
\[
X_G\cong\RP^2.
\]
Step [](#s1-5){.pf-ref} gives a covering
\[
S^2\to X_G,
\]
and step [](#s1-6){.pf-ref} says the covering space $S^2$ is simply connected. A connected simply connected covering is universal.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the presentation complex and step [](#s1-7){.pf-ref} identifies its universal cover.

:::

:::

:::
