---
schema: qual/card@1
id: E-HAT-4.H-4
kind: problem
title: "Dual of an iterated mapping cylinder"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Define the dual of an iterated mapping cylinder precisely, in terms of maps from $\Delta^n$, and use this to give a definition of $\nabla X$, the dual of $\Delta X$, for $X$ a complex of spaces.

::: solution
**Goal:** Define the dual of an iterated mapping cylinder via simplex maps and construct the dual $\nabla X$ of a complex of spaces $\Delta X$.

<1>1. Simplex reflection involution:
    *Proof:*
    <2>1. Let $\Delta^n = \{(t_0, t_1, \dots, t_n) \in \mathbb{R}^{n+1} : \sum_{i=0}^n t_i = 1, \; t_i \ge 0\}$ denote the standard geometric $n$-simplex with vertices $v_0, v_1, \dots, v_n$.
    <2>2. Define the order-reversing affine homeomorphism $\iota_n: \Delta^n \to \Delta^n$ by
    $$\iota_n(t_0, t_1, \dots, t_n) = (t_n, t_{n-1}, \dots, t_0),$$
    which maps the vertex $v_i$ to $v_{n-i}$ for each $0 \le i \le n$.
    <2>3. For any continuous map $\sigma: \Delta^n \to Z$, define the dual simplex map $\sigma^\vee: \Delta^n \to Z$ by precomposition:
    $$\sigma^\vee = \sigma \circ \iota_n.$$

<1>2. Dual of an iterated mapping cylinder:
    *Proof:*
    <2>1. Given a sequence of maps $X_0 \xrightarrow{f_1} X_1 \xrightarrow{f_2} \cdots \xrightarrow{f_n} X_n$, the iterated mapping cylinder $M(f_1, \dots, f_n)$ is constructed as the quotient of the disjoint union
    $$\coprod_{0 \le i_0 < i_1 < \dots < i_k \le n} \Delta^k \times X_{i_0}$$
    under the face identifications: for $(t_0, \dots, t_k) \in \Delta^k$ with $t_j = 0$, omit $t_j$ and $i_j$; if $j = 0$, replace $x \in X_{i_0}$ with $f_{i_1 i_0}(x) \in X_{i_1}$.
    <2>2. The dual iterated mapping cylinder $M^\vee(f_1, \dots, f_n)$ is defined on the same constituent spaces by reflecting each simplex parameter via $\iota_k$:
    each cell parameterization $\sigma: \Delta^k \times X_{i_0} \to M$ is replaced by $\sigma \circ (\iota_k \times \operatorname{id}_{X_{i_0}})$.
    <2>3. Under this reflection, the face operators act in reverse order: the $j$-th face map $\partial_j: \Delta^{k-1} \to \Delta^k$ satisfies $\iota_k \circ \partial_j = \partial_{k-j} \circ \iota_{k-1}$, so the induced structure maps on the dual cylinder satisfy $d_j^\vee = d_{k-j}$.

<1>3. Definition of the dual simplicial space $\nabla X$:
    *Proof:*
    <2>1. Let $\Delta X$ be a simplicial space (or complex of spaces) given by a sequence of topological spaces $X_n = (\Delta X)_n$ for $n \ge 0$ equipped with face maps $d_i: X_n \to X_{n-1}$ ($0 \le i \le n$) and degeneracy maps $s_i: X_n \to X_{n+1}$ ($0 \le i \le n$) satisfying the simplicial identities.
    <2>2. Define the dual simplicial space $\nabla X$ by:
    $$(\nabla X)_n = (\Delta X)_n \quad \text{for all } n \ge 0,$$
    with face maps $d_i^{\nabla}: (\nabla X)_n \to (\nabla X)_{n-1}$ and degeneracy maps $s_i^{\nabla}: (\nabla X)_n \to (\nabla X)_{n+1}$ defined by
    $$d_i^{\nabla} = d_{n-i}, \qquad s_i^{\nabla} = s_{n-i} \quad \text{for } 0 \le i \le n.$$
    <2>3. The dual operators satisfy the simplicial identities: for $i < j$,
    $$d_i^{\nabla} d_j^{\nabla} = d_{n-1-i} d_{n-j} = d_{n-j-1} d_{n-i} = d_{j-1}^{\nabla} d_i^{\nabla},$$
    confirming that $\nabla X$ is a well-defined simplicial space.

<1>4. Conclusion:
    *Proof:*
    The dual simplicial space $\nabla X$ reflects the indexing of simplices and face/degeneracy operators degree-by-degree via $d_i^{\nabla} = d_{n-i}$ and $s_i^{\nabla} = s_{n-i}$, providing the homotopy-theoretic dual to $\Delta X$.
:::
