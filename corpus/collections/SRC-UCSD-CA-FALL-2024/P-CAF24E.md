---
schema: qual/card@1
id: P-CAF24E
kind: problem
title: '$L^1$-bounded holomorphic functions on the disc have a locally uniform subsequence'
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Uniform Convergence
relations: []
review: draft
---

::: problem
Let $f_n : \mathbb{D} \to \mathbb{C}$ be holomorphic functions such that
\[
\int_{\mathbb{D}} |f_n|\, dx\, dy \le 1, \qquad \forall n \ge 1.
\]
Show that there exists a subsequence of $\{f_n\}$ that converges locally uniformly on $\mathbb{D}$.
:::

::: solution
Fix a compact set $K\Subset\mathbb D$. Choose $r>0$ such that
\[
B(z,r)\subset\mathbb D
\]
for every $z\in K$. Since $|f_n|$ is subharmonic, the submean inequality gives
\[
|f_n(z)|
\le \frac1{\pi r^2}
\int_{B(z,r)}|f_n(w)|\,dA(w)
\le \frac1{\pi r^2}.
\]
Thus the family $(f_n)$ is uniformly bounded on every compact subset of
$\mathbb D$. By Montel's theorem it is a normal family. Therefore every
sequence has a subsequence converging uniformly on compact subsets of
$\mathbb D$ to a holomorphic function (or, in the spherical formulation, to
$\infty$; the local bounds exclude the latter). Hence the required locally
uniformly convergent subsequence exists.
:::
