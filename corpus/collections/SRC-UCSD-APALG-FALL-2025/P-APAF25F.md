---
schema: qual/card@1
id: P-APAF25F
kind: problem
title: Character bound $|\chi(g)|\leq\dim V$ is sharp
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
Let $(V,\varphi)$ be a finite-dimensional complex representation of a finite group $G$, and let $\chi(g)=\operatorname{Tr}\varphi(g)$ be its character.
Prove that $|\chi(g)|\leq\dim V$ for all $g\in G$, and that the bound is sharp.
:::

::: {.solution}
Let \(d=\dim V\).

<1>1. For every \(g\in G\), all eigenvalues of \(\varphi(g)\) have modulus \(1\).
::: {.proof}
Because \(G\) is finite, \(g\) has finite order, say \(g^m=e\). Hence
\[
\varphi(g)^m=\varphi(g^m)=I.
\]
If \(\lambda\) is an eigenvalue of \(\varphi(g)\), then \(\lambda^m=1\), so \(|\lambda|=1\).
:::

<1>2. For every \(g\in G\),
\[
|\chi(g)|\le d.
\]
::: {.proof}
Over \(\mathbb C\), the characteristic polynomial of \(\varphi(g)\) splits. Let its eigenvalues, counted with algebraic multiplicity, be \(\lambda_1,\ldots,\lambda_d\). Then
\[
\chi(g)=\operatorname{Tr}\varphi(g)=\sum_{j=1}^d\lambda_j.
\]
By <1>1, \(|\lambda_j|=1\) for every \(j\). Therefore the triangle inequality gives
\[
|\chi(g)|
\le \sum_{j=1}^d|\lambda_j|
=d.
\]
:::

<1>3. The bound is sharp.
::: {.proof}
At the identity element \(e\in G\),
\[
\varphi(e)=I_V,
\]
so
\[
\chi(e)=\operatorname{Tr}(I_V)=d.
\]
Hence
\[
|\chi(e)|=d=\dim V,
\]
showing that equality can occur.
:::
:::
