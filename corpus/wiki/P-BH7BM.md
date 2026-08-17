---
schema: qual/card@1
id: P-BH7BM
kind: problem
title: Orthogonal projection onto a finite orthonormal set is the best approximation; finite-dimensional subspaces of a Hilbert space are closed
classification:
  areas:
  - real-analysis
  topics:
  - hilbert-spaces
  - closure
relations: []
review: draft
solved: true
---

::: problem
Let $\mathcal H$ be a Hilbert space.

1. Let $x\in \mathcal H$ and $\theset{u_n}_{n=1}^N$ be an orthonormal set.
  Prove that the best approximation to $x$ in $\mathcal H$ by an element in $\spanof_\CC\theset{u_n}$ is given by
  $$
  \hat x \definedas \sum_{n=1}^N \inner{x}{u_n}u_n.
  $$
2. Conclude that finite dimensional subspaces of $\mathcal H$ are always closed.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $\hat x = \sum_{n=1}^N \inner{x}{u_n} u_n$ satisfies $x - \hat x \perp u_m$ for every $m$.
    Proof: $\inner{x - \hat x}{u_m} = \inner{x}{u_m} - \sum_n \inner{x}{u_n}\inner{u_n}{u_m} = \inner{x}{u_m} - \inner{x}{u_m} = 0$, using orthonormality $\inner{u_n}{u_m} = \delta_{nm}$.

<1>2. $x - \hat x \perp \spanof_\CC\theset{u_n}$.
    Proof: <1>1 gives orthogonality to each basis vector, hence to every finite linear combination.

<1>3. For every $y = \sum_n c_n u_n \in \spanof_\CC\theset{u_n}$: $\|x - y\|^2 = \|x - \hat x\|^2 + \|\hat x - y\|^2$.
    Proof: $x - y = (x - \hat x) + (\hat x - y)$ with $\hat x - y \in \spanof_\CC\theset{u_n}$ and $x - \hat x \perp \hat x - y$ (<1>2); the Pythagorean theorem applies.

<1>4. $\|x - y\| \ge \|x - \hat x\|$ for all $y \in \spanof_\CC\theset{u_n}$, with equality iff $y = \hat x$.
    Proof: <1>3 shows $\|x - y\|^2 = \|x - \hat x\|^2 + \|\hat x - y\|^2 \ge \|x - \hat x\|^2$; equality forces $\|\hat x - y\| = 0$.

<1>5. Q.E.D. (part 1).
    Proof: <1>4 says $\hat x$ is the unique best approximation to $x$ in $\spanof_\CC\theset{u_n}$.

<1>6. Part 2: a finite-dimensional subspace $V$ of $\mathcal H$ is closed.
    <2>1. Let $\theset{u_1, \ldots, u_N}$ be an orthonormal basis of $V$ (Gram–Schmidt).
        Proof: $V$ finite-dimensional admits an orthonormal basis.
    <2>2. $V = \spanof_\CC\theset{u_1,\ldots,u_N}$.
        Proof: an orthonormal set is linearly independent and spans by choice of basis.
    <2>3. If $(y_k) \subseteq V$ converges to $y \in \mathcal H$, then $y \in V$.
        Proof: write $y_k = \sum_n \inner{y_k}{u_n}u_n$ (Fourier expansion in the basis). Continuity of the inner product gives $\inner{y_k}{u_n} \to \inner{y}{u_n}$, so $y_k \to \sum_n \inner{y}{u_n} u_n$; the limit is unique, hence $y = \sum_n \inner{y}{u_n} u_n \in V$.
    <2>4. Q.E.D.
        Proof: <2>3 shows $V$ contains the limits of its convergent sequences, i.e. $V$ is closed.
:::
