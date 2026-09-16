---
schema: qual/card@1
id: P-CASP12D
kind: problem
title: "Real-valued analytic functions on radii and conditions for existence"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
(i) Prove that if $f(z) = \sum_{n=0}^{\infty} a_n z^n$ is analytic on $\mathbb{D}$ and $f(z) \in \mathbb{R}$ whenever $z \in [0, 1)$, then $a_n \in \mathbb{R}$ for all $n$.

(ii) Find necessary and sufficient conditions on a constant $\omega$ with $|\omega| = 1$ for there to exist a nonconstant analytic function $f$ on $\mathbb{D}$ that is real valued on the radii $[0, 1)$ and $[0, \omega)$.
:::

::: {.solution}
(i) For real $x\in[0,1)$ we have $f(x)=\overline{f(x)}$. Thus the holomorphic
functions
\[
f(z)\quad\text{and}\quad \overline{f(\bar z)}
\]
agree on an interval with an accumulation point in the disk. By the identity
theorem they agree everywhere. Comparing Taylor coefficients gives
$a_n=\overline{a_n}$, hence $a_n\in\mathbb R$.

(ii) By (i), any such nonconstant function has a power series
$f(z)=\sum a_nz^n$ with real coefficients. Reality on the second radius says
\[
\sum a_n\omega^n r^n\in\mathbb R\qquad(0\le r<1),
\]
so every $a_n\omega^n$ is real. Since $f$ is nonconstant, some $a_n\ne0$ for
$n\ge1$, and therefore $\omega^n\in\{1,-1\}$. Thus $\omega$ must be a root of
unity.

Conversely, if $\omega$ is a root of unity, choose $n\ge1$ with
$\omega^n=1$. Then $f(z)=z^n$ is nonconstant and is real-valued on both
radii. Hence the necessary and sufficient condition is
\[
\boxed{\omega\text{ is a root of unity}.}
\]
:::
