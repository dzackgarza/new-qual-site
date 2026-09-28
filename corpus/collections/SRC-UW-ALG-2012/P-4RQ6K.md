---
schema: qual/card@1
id: P-4RQ6K
kind: problem
title: Kernel of a map of finitely generated free modules over a PID is a direct summand;
  the image need not be
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Free Modules
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R$ be a (commutative) principal ideal domain, let $M$ and $N$ be finitely generated free $R$-modules, and let $\varphi:M\rightarrow N$ be an $R$-module homomorphism.

- Let $K$ be the kernel of $\varphi$.
  Prove that $K$ is a direct summand of $M$.

- Let $C$ be the image of $\varphi$.
  Show by example (specifying $R$, $M$, $N$, and $\varphi$) that $C$ need not be a direct summand of $N$.
:::


::: {.solution}
<1>1. The image \(C=\operatorname{im}\varphi\) is a finitely generated free \(R\)-module.
::: {.proof}
Since \(N\) is a finitely generated free module over the PID \(R\), every submodule of \(N\) is free. Thus \(C\le N\) is free. It is finitely generated because it is the image of the finitely generated module \(M\).
:::

<1>2. The exact sequence
\[
0\longrightarrow K\longrightarrow M\overset{\varphi}{\longrightarrow} C\longrightarrow0
\]
splits.
::: {.proof}
By <1>1, \(C\) is free, hence projective. Therefore the surjection \(M\twoheadrightarrow C\) admits an \(R\)-linear section \(s:C\to M\). Consequently
\[
M=K\oplus s(C),
\]
so \(K\) is a direct summand of \(M\).
:::

<1>3. The image need not be a direct summand of \(N\).
::: {.proof}
Take
\[
R=\mathbb Z,\qquad M=N=\mathbb Z,
\qquad
\varphi:\mathbb Z\to\mathbb Z,\quad \varphi(m)=2m.
\]
Then
\[
C=\operatorname{im}\varphi=2\mathbb Z.
\]
If \(2\mathbb Z\) were a direct summand of \(\mathbb Z\), then
\[
\mathbb Z\cong 2\mathbb Z\oplus L
\]
for some subgroup \(L\). Taking the quotient by \(2\mathbb Z\) would give
\[
L\cong \mathbb Z/2\mathbb Z.
\]
But every subgroup of the torsion-free group \(\mathbb Z\) is torsion-free, so no such \(L\) exists. Hence \(2\mathbb Z\) is not a direct summand of \(\mathbb Z\).
:::
:::
