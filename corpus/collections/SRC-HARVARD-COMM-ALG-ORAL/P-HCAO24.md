---
schema: qual/card@1
id: P-HCAO24
kind: problem
title: Define the Hilbert function
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Define the Hilbert function of a graded ring.
:::

::: {.solution}
<1>1. Setting and assumptions: <2>1. Let $S = \bigoplus_{d \ge 0} S_d$ be a standard graded commutative ring where $S_0 = k$ is a field (or more generally an Artinian ring) and $S = k[x_1, \dots, x_n]$ is finitely generated as an $S_0$-algebra by elements of degree 1 ($\deg(x_i) = 1$). Proof: standard setup for graded commutative algebra.
<2>2. Under these assumptions, each graded piece $S_d$ is a finite-dimensional $k$-vector space (or an $S_0$-module of finite length $\ell_{S_0}(S_d) < \infty$). Proof: $S_d$ is spanned as a $k$-vector space by all monomials of total degree $d$ in $x_1, \dots, x_n$, of which there are finitely many $\binom{d+n-1}{n-1}$.

<1>2. Definition of the Hilbert function: <2>1. The **Hilbert function** of the graded ring $S$ is the arithmetic function:
\[
\operatorname{HF}_S: \mathbb{Z}_{\ge 0} \to \mathbb{Z}_{\ge 0}, \quad d \mapsto \operatorname{HF}_S(d) = \dim_k(S_d) \quad \big(\text{or } \ell_{S_0}(S_d)\big).
\]
Proof: definition of Hilbert function.
<2>2. More generally, for any finitely generated graded $S$-module $M = \bigoplus_{d \in \mathbb{Z}} M_d$, each $M_d$ has finite length, and the Hilbert function of $M$ is $\operatorname{HF}_M(d) = \ell_{S_0}(M_d)$.
Proof: definition of module Hilbert function.

<1>3. Hilbert–Serre Theorem and the Hilbert Polynomial: <2>1. The generating series of the Hilbert function is the **Hilbert series** (Hilbert–Poincaré series):
\[
\operatorname{HS}_S(t) = \sum_{d=0}^\infty \operatorname{HF}_S(d) \, t^d.
\]
Proof: formal power series definition.
<2>2. By the Hilbert–Serre Theorem, the series can be written as a rational function $\operatorname{HS}_S(t) = \frac{P(t)}{(1-t)^s}$ for some polynomial $P(t) \in \mathbb{Z}[t]$.
Consequently, for all sufficiently large $d \gg 0$, $\operatorname{HF}_S(d)$ agrees with a polynomial $\operatorname{HP}_S(d) \in \mathbb{Q}[d]$ (the **Hilbert polynomial**), whose degree is $\dim(S) - 1$.
Proof: Hilbert–Serre Theorem.

<1>4. Conclusion: The Hilbert function of $S$ is $\operatorname{HF}_S(d) = \dim_k(S_d)$ (the dimension of the $d$-th graded component as a $k$-vector space).
Q.E.D. Proof: <1>1 and <1>2.
:::
