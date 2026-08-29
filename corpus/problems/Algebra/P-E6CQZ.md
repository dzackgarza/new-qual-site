---
schema: qual/card@1
id: P-E6CQZ
kind: problem
title: Stabilizers for $\SL_2(\RR)$ acting on $\RR^2$ and by Möbius transformations
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Matrix Groups
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Consider $\SL_2(R)$ acting on $\RR^2$ by matrix multiplication.
What is the stabiliser of a point?
Does it depend which point?
Do you know what sort of subgroup this is?
What if $\SL_2(R)$ acts by Möbius transformations instead?
:::

::: {.solution}
<1>1. For the linear action on $\mathbb{R}^2$, the stabilizer of $0$ is all of $\SL_2(\mathbb{R})$.
Proof: every matrix fixes the origin.

<1>2. For a nonzero point $v \neq 0$, the stabilizer is $\{A \in \SL_2(\mathbb{R}) : Av = v\}$, the matrices with $v$ as an eigenvector of eigenvalue $1$.
Proof: definition of stabilizer.

<1>3. The stabilizer of a nonzero point is conjugate to the subgroup $\left\{\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} : t \in \mathbb{R}\right\}$ (the unipotent upper-triangular matrices).
Proof: by a change of basis sending $v$ to $(1, 0)$, the stabilizer becomes the matrices fixing $(1,0)$, which are exactly $\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$.

<1>4. Hence the stabilizer depends on the point: it is $\SL_2(\mathbb{R})$ at $0$ and a unipotent subgroup (isomorphic to $(\mathbb{R}, +)$) at any nonzero point.
Proof: <1>1 and <1>3.

<1>5. For the Möbius action on the upper half-plane $\mathbb{H}$ (or $\mathbb{R} \cup \{\infty\}$), $\SL_2(\mathbb{R})$ acts by $z \mapsto \frac{az + b}{cz + d}$.
Proof: the Möbius action.

<1>6. The stabilizer of $i \in \mathbb{H}$ is $\operatorname{SO}(2)$ (the rotation matrices $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$).
Proof: the matrices fixing $i$ are those with $\frac{ai + b}{ci + d} = i$, which are exactly the rotations.

<1>7. The stabilizer of any point of $\mathbb{H}$ is conjugate to $\operatorname{SO}(2)$ (the action is transitive).
Proof: <1>6 and transitivity of the Möbius action on $\mathbb{H}$.

<1>8. Hence for the Möbius action, the stabilizer is always a compact subgroup isomorphic to $\operatorname{SO}(2) \cong S^1$ (independent of the point, up to conjugacy).
Proof: <1>7.

<1>9. Q.E.D.
Proof: <1>4 and <1>8.
:::
