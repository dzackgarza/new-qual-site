---
schema: qual/card@1
id: P-ALGF24G
kind: problem
title: Scaled roots in a characteristic-zero splitting field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
---

::: problem
Suppose $F$ is a field of characteristic zero, $f \in F[x]$ is monic and irreducible, and $E$ is a splitting field of $f$ over $F$.
Let $X := \{\alpha \in E \mid f(\alpha) = 0\}$.

(a) Suppose $m \in \mathbb{N}$ and $\alpha \in X$.
Let $g(x) := m_{\alpha^m,F}(x)$ be the minimal polynomial of $\alpha^m$ over $F$.
Prove that $\{\beta^m \mid \beta \in X\}$ is the set of zeros of $g(x)$ in $E$.

(b) Suppose there exist $\alpha \in E$ and $r \in F$ such that $\alpha, r\alpha \in X$.
Prove that
\[
\ell_r \colon X \to X, \qquad \ell_r(\beta) = r\beta
\]
is well-defined.
Deduce that $r$ is a root of unity.

(c) Suppose $\alpha, r\alpha \in X$, $r \in F$, and the multiplicative order of $r$ is $m$.
Prove that
\[
m_{\alpha,F}(x) = m_{\alpha^m,F}(x^m);
\]
that means $f(x) = g(x^m)$.
:::
