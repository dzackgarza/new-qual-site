---
schema: qual/card@1
id: P-NSD6Y
kind: problem
title: $\RR^2$ is not homeomorphic to $\RR^n$ for $n>2$
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homology
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 4 of the official UGA Fall 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the punctured-space argument by comparing H_1(S^1) with H_1(S^{n-1}) for n greater than 2.
---

::: problem
Prove that $\RR^2$ is not homeomorphic to $\RR^n$ for $n > 2$.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that there is a homeomorphism
\[
h:\mathbb R^2\to\mathbb R^n
\]
with $n>2$.
::: {.proof}
We will derive a contradiction from the homology of the complements of corresponding points.
:::

<1>2. Restricting $h$ gives a homeomorphism
\[
\mathbb R^2\setminus\{0\}
\cong
\mathbb R^n\setminus\{h(0)\}.
\]
::: {.proof}
Since $h$ is bijective,
\[
h\bigl(\mathbb R^2\setminus\{0\}\bigr)
=
\mathbb R^n\setminus\{h(0)\}.
\]
The restriction of a homeomorphism to a subspace is a homeomorphism onto its image.
:::

<1>3. The punctured plane deformation retracts onto $S^1$, so
\[
H_1(\mathbb R^2\setminus\{0\};\mathbb Z)
\cong
\mathbb Z.
\]
::: {.proof}
The radial map
\[
r(x)=\frac{x}{\|x\|}
\]
is a deformation retraction of $\mathbb R^2\setminus\{0\}$ onto the unit circle $S^1$.
Homotopy invariance of singular homology therefore gives
\[
H_1(\mathbb R^2\setminus\{0\})
\cong
H_1(S^1)
\cong
\mathbb Z.
\]
:::

<1>4. The punctured $n$-space deformation retracts onto $S^{n-1}$, and for $n>2$,
\[
H_1(\mathbb R^n\setminus\{h(0)\};\mathbb Z)=0.
\]
::: {.proof}
Translation by $-h(0)$ is a homeomorphism
\[
\mathbb R^n\setminus\{h(0)\}
\cong
\mathbb R^n\setminus\{0\}.
\]
Radial deformation retraction gives
\[
\mathbb R^n\setminus\{0\}\simeq S^{n-1}.
\]
Since $n>2$, one has $n-1\ge2$, and the homology of a sphere gives
\[
H_1(S^{n-1};\mathbb Z)=0.
\]
Hence the displayed punctured-space group vanishes.
:::

<1>5. This contradicts <1>2, so
\[
\boxed{\mathbb R^2\not\cong\mathbb R^n\quad(n>2)}.
\]
::: {.proof}
Homeomorphic spaces have isomorphic homology groups.
But <1>3 and <1>4 give respectively
\[
H_1(\mathbb R^2\setminus\{0\})\cong\mathbb Z
\qquad\text{and}\qquad
H_1(\mathbb R^n\setminus\{h(0)\})=0,
\]
contradicting the homeomorphism in <1>2. Therefore no homeomorphism $\mathbb R^2\to\mathbb R^n$ exists for $n>2$.
:::
:::
