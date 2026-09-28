---
schema: qual/card@1
id: P-A4HRU
kind: problem
title: Image $pA$ and kernel $A[p]$ of multiplication by $p$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $A$ be an $R$-module (or abelian group), and let $p \in R$ be a ring element (e.g. a prime integer $p \in \mathbb{Z}$).
Define the multiplication-by-$p$ map:
$$\phi_p: A \longrightarrow A, \qquad x \longmapsto p x.$$
(1) Prove that $\phi_p$ is an $R$-module homomorphism when $p \in Z(R)$.
(2) Define the image submodule $p A \coloneqq \operatorname{im}(\phi_p)$ and the kernel submodule $A[p] \coloneqq \ker(\phi_p)$ ($p$-torsion submodule).
(3) Compute $p A$, $A/pA$, and $A[p]$ for $A = \mathbb{Z}$, $A = \mathbb{Z}/n\mathbb{Z}$, and $A = \mathbb{Q}/\mathbb{Z}$.
:::

::: {.solution}
Assume \(p\in Z(R)\). Then for \(r\in R\) and \(x\in A\),
\[
\phi_p(rx)=p(rx)=(pr)x=(rp)x=r(px)=r\phi_p(x),
\]
so \(\phi_p:x\mapsto px\) is \(R\)-linear. Its image and kernel are
\[
pA=\{px:x\in A\},\qquad
A[p]=\{x\in A:px=0\}.
\]
Hence
\[
0\longrightarrow A[p]\longrightarrow A\xrightarrow{\,p\,}A
\longrightarrow A/pA\longrightarrow0
\]
is exact, and the first isomorphism theorem gives \(A/A[p]\cong pA\).

For abelian groups and prime integer \(p\):

- If \(A=\mathbb Z\), then
  \[
  pA=p\mathbb Z,\qquad A/pA\cong\mathbb Z/p\mathbb Z,\qquad A[p]=0.
  \]

- If \(A=\mathbb Z/n\mathbb Z\) and \(d=\gcd(p,n)\), then
  \[
  |pA|=n/d,\qquad A/pA\cong\mathbb Z/d\mathbb Z,
  \qquad A[p]=\langle n/d\rangle\cong\mathbb Z/d\mathbb Z.
  \]
  Since \(p\) is prime, \(d\in\{1,p\}\).

- If \(A=\mathbb Q/\mathbb Z\), multiplication by \(p\) is surjective, so
  \[
  pA=A,\qquad A/pA=0,
  \]
  while
  \[
  A[p]=\left\{\frac{k}{p}+\mathbb Z:0\le k<p\right\}\cong\mathbb Z/p\mathbb Z.
  \]
:::
