---
schema: qual/card@1
id: P-APA22G
kind: problem
title: Spectrum of the sum of all transpositions on the Specht module $S^{(4,2,1)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
Let $(S_{\lambda}, \rho_{\lambda})$ be the irreducible representation of the complex group algebra of the symmetric group $S_7$ corresponding to the partition $\lambda = (4, 2, 1)$.
Using Murphy's theorem (or otherwise), determine the spectrum of $\rho_{\lambda}(T)$, where $T$ is the sum of all transpositions.
:::


::: {.solution}
Let
\[
T=\sum_{1\le i<j\le7}(ij)\in\mathbb C[S_7].
\]
Since conjugation permutes the transpositions, $T$ is central in $\mathbb C[S_7]$. Hence, by Schur's lemma, on the irreducible module $S^{(4,2,1)}$ it acts by a scalar.

Murphy's theorem identifies $T$ with the sum of the Jucys--Murphy elements, and on a standard tableau the latter act with eigenvalues equal to the contents of the boxes containing $1,\ldots,7$. Therefore the scalar by which $T$ acts on $S^\lambda$ is the sum of the contents of all boxes of $\lambda$:
\[
\sum_{(i,j)\in\lambda}(j-i).
\]
For $\lambda=(4,2,1)$ this is
\[
(0+1+2+3)+(-1+0)+(-2)=6-1-2=3.
\]
Thus
\[
\rho_{(4,2,1)}(T)=3I.
\]
Consequently the spectrum is
\[
\boxed{\{3\}}.
\]

If algebraic multiplicity is requested, the hook-length formula gives
\[
\dim S^{(4,2,1)}
=\frac{7!}{6\cdot4\cdot2\cdot1\cdot3\cdot1\cdot1}
=\frac{5040}{144}=35.
\]
Hence the eigenvalue $3$ occurs with multiplicity $35$.
:::
