---
schema: qual/card@1
id: P-APA23I
kind: problem
title: Trace of exterior powers of a normal operator and characteristic polynomial coefficients
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Multilinear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $H$ be an $n$-dimensional Hilbert space and $A \colon H \to H$ a normal linear transformation.

(a) Derive a formula for the trace of the degree $d$ exterior power $A^{\wedge d}$ as a function of the eigenvalues of $A$.

(b) Express the coefficients of the characteristic polynomial of $A$ in terms of traces of exterior powers of $A$.
:::

::: solution
**Goal:** Diagonalize $A$ and read traces on exterior powers from eigenvalues.

<1> Reduce to an eigenbasis.
    *Proof:*
    <2>1. Since $A$ is normal on finite-dimensional $H$, there is a unitary basis $\{v_1,\dots,v_n\}$ with
        $$Av_i=\lambda_i v_i,$$
        where $\lambda_i\in\CC$ are the eigenvalues of $A$.
    <2>2. Hence
        $$\det(tI-A)=\prod_{i=1}^n (t-\lambda_i).$$

<1> Compute $\operatorname{tr}(A^{\wedge d})$.
    *Proof:*
    <2>1. A basis of $H^{\wedge d}$ is $\{v_{i_1}\wedge\cdots\wedge v_{i_d}\mid 1\le i_1<\cdots<i_d\le n\}$.
    <2>2. On a basis vector,
        $$A^{\wedge d}(v_{i_1}\wedge\cdots\wedge v_{i_d})
        =(\lambda_{i_1}\cdots \lambda_{i_d})\,v_{i_1}\wedge\cdots\wedge v_{i_d}.$$
    <2>3. Therefore
        $$
        \operatorname{tr}(A^{\wedge d})
        =\sum_{1\le i_1<\cdots<i_d\le n}\lambda_{i_1}\cdots\lambda_{i_d}.
        $$

<1> Relate to the characteristic polynomial.
    *Proof:*
    <2>1. Expand
        $$\det(tI-A)=\prod_{i=1}^n (t-\lambda_i)=\sum_{d=0}^n (-1)^d e_d t^{n-d},$$
        where
        $$e_d=\sum_{1\le i_1<\cdots<i_d\le n}\lambda_{i_1}\cdots\lambda_{i_d}.$$
    <2>2. By step <1>, $e_d=\operatorname{tr}(A^{\wedge d})$.
    <2>3. Hence the coefficient of $t^{n-d}$ is $(-1)^d\operatorname{tr}(A^{\wedge d})$.

Authored by **Codex 5.3 Spark Extra High**.
:::
