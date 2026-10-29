---
schema: qual/card@1
id: P-HCAX11
kind: problem
title: The punctured disk is not conformally equivalent to an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Prove that the punctured unit disk is not conformally equivalent to an annulus.
:::

::: {.solution}
Let $\DD^*=\{z:0<\abs{z}<1\}$ and $A=\{w:r<\abs{w}<R\}$ with $0<r<R<\infty$.
Suppose, for contradiction, that $f\colon\DD^*\to A$ is biholomorphic.

::: pf

::: {.pf-step #s1}

$f$ extends to a holomorphic function $\tilde f\colon\DD\to\CC$, and
$w_0\coloneqq\tilde f(0)$ satisfies $r\le\abs{w_0}\le R$.

::: pf-proof

Since $\abs{f}<R$ on $\DD^*$, the singularity at $0$ is removable by Riemann's
removable singularity theorem. By continuity, $w_0=\lim_{z\to0}f(z)$ lies in
$\overline A$.

:::

:::

::: {.pf-step #s2}

$w_0\notin A$.

::: pf-proof

If $w_0\in A$, then $w_0=f(z_1)$ for some $z_1\in\DD^*$. Choose disjoint
open disks $U\ni0$ and $V\ni z_1$ in $\DD$. The map $\tilde f$ is nonconstant,
so by the open mapping theorem $\tilde f(U)$ and $\tilde f(V)$ are open
neighborhoods of $w_0$; their intersection is an open set, hence it contains
a point other than $w_0$, of the form $f(z')=f(z'')$ with $z'\in U\setminus\{0\}$
and $z''\in V$. Since $U\cap V=\varnothing$, $z'\ne z''$, contradicting
injectivity of $f$.

:::

:::

::: {.pf-step #s3}

$w_0\notin\partial A$.

::: pf-proof

By the open mapping theorem, $\tilde f(\DD)$ is an open set containing $w_0$.
If $\abs{w_0}=r$ or $\abs{w_0}=R$, every neighborhood of $w_0$ contains points
of modulus less than $r$ or greater than $R$. But
$\tilde f(\DD)=A\cup\{w_0\}\subseteq\overline A$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} are incompatible, so no biholomorphism $\DD^*\to A$ exists.

:::

:::

:::
