---
schema: qual/card@1
id: P-HBECH
kind: problem
title: Compact connected surfaces of Euler characteristic $-3$, possibly with boundary
  or nonorientable
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem VII of the official UGA Spring 2009 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Applied the classification theorem for compact connected surfaces. The
    orientable equation 2-2g-b=-3 has three solutions, and the nonorientable
    equation 2-k-b=-3 has five. Orientability, genus, and boundary count
    distinguish all eight homeomorphism classes.
---

::: problem
How many surfaces are there, up to homeomorphism, which are:

- Connected,

- Compact,

- Possibly with boundary,

- Possibly nonorientable, and

- With Euler characteristic -3?

Describe one representative from each class.
:::

::: {.solution}
Write $\Sigma_{g,b}$ for the compact connected orientable surface of genus $g$ with $b$ boundary components, and write $N_{k,b}$ for the compact connected nonorientable surface of nonorientable genus $k$ with $b$ boundary components.

<1>1. The orientable surfaces with Euler characteristic $-3$ are exactly
\[
\Sigma_{0,5},
\qquad
\Sigma_{1,3},
\qquad
\Sigma_{2,1}.
\]
::: {.proof}
By the classification theorem for compact connected surfaces, every orientable example is homeomorphic to a unique $\Sigma_{g,b}$ with
\[
g\ge0,
\qquad
b\ge0,
\]
and
\[
\chi(\Sigma_{g,b})=2-2g-b.
\]
The condition $\chi=-3$ is therefore
\[
2-2g-b=-3,
\qquad\text{equivalently}\qquad
2g+b=5.
\]
Since $g,b$ are nonnegative integers, the only solutions are
\[
(g,b)=(0,5),
\qquad
(1,3),
\qquad
(2,1).
\]
:::

<1>2. The nonorientable surfaces with Euler characteristic $-3$ are exactly
\[
N_{1,4},
\quad
N_{2,3},
\quad
N_{3,2},
\quad
N_{4,1},
\quad
N_{5,0}.
\]
::: {.proof}
Again by the classification theorem, every compact connected nonorientable surface is homeomorphic to a unique $N_{k,b}$ with
\[
k\ge1,
\qquad
b\ge0,
\]
and
\[
\chi(N_{k,b})=2-k-b.
\]
Thus $\chi=-3$ is equivalent to
\[
k+b=5.
\]
The positive-integer/nonnegative-integer solutions are
\[
(k,b)=(1,4),(2,3),(3,2),(4,1),(5,0).
\]
:::

<1>3. These eight surfaces are pairwise nonhomeomorphic.
::: {.proof}
An orientable surface cannot be homeomorphic to a nonorientable one.
Within the orientable class, the classification theorem says the pair $(g,b)$ determines the homeomorphism type, and the three pairs in <1>1 are distinct.
Within the nonorientable class, the pair $(k,b)$ determines the homeomorphism type, and the five pairs in <1>2 are distinct.
Hence all eight listed surfaces are pairwise nonhomeomorphic.
:::

<1>4. Explicit representatives are:

- the sphere with five disjoint open disks removed, representing $\Sigma_{0,5}$;

- the torus with three disjoint open disks removed, representing $\Sigma_{1,3}$;

- the orientable genus-$2$ surface with one open disk removed, representing $\Sigma_{2,1}$;

- $\RP^2$ with four disjoint open disks removed, representing $N_{1,4}$;

- the Klein bottle with three disjoint open disks removed, representing $N_{2,3}$;

- the connected sum of three copies of $\RP^2$ with two open disks removed, representing $N_{3,2}$;

- the connected sum of four copies of $\RP^2$ with one open disk removed, representing $N_{4,1}$;

- the connected sum of five copies of $\RP^2$, representing $N_{5,0}$.

::: {.proof}
The standard representatives in the classification theorem realize $\Sigma_{g,b}$ by deleting $b$ open disks from the closed orientable genus-$g$ surface and realize $N_{k,b}$ by deleting $b$ open disks from the connected sum of $k$ projective planes.
The Klein bottle is $N_{2,0}$, so deleting three disks gives $N_{2,3}$.
:::

Therefore the number of homeomorphism classes is
\[
\boxed{8}.
\]
:::
