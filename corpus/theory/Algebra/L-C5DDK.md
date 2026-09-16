---
schema: qual/card@1
id: L-C5DDK
kind: lemma
title: A linear operator over an algebraically closed field has an eigenvector in every nonzero invariant subspace
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
---

::: {.lemma}
Let $k$ be an algebraically closed field, let $V$ be a finite-dimensional $k$-vector space, and let $A\colon V\to V$ be $k$-linear.
If $W\subseteq V$ is a nonzero subspace with $A(W)\subseteq W$, then $W$ contains an eigenvector of $A$.
:::

::: {.proof}
The restriction $A|_W\colon W\to W$ is a linear operator on a nonzero finite-dimensional space, so its characteristic polynomial has positive degree and has a root $\lambda\in k$.
Then $A|_W-\lambda\id_W$ is not injective, and a nonzero $w\in W$ with $Aw=\lambda w$ is an eigenvector of $A$.
:::

::: {.example}
The finite-dimensionality of $V$ is used: multiplication by $x$ on $V=W=k[x]$ has no eigenvector, since $xf=\lambda f$ has no nonzero solution $f\in k[x]$ by comparing degrees.
:::
