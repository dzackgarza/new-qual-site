---
schema: qual/card@1
id: P-AGH35COMPLHYP
kind: problem
title: The complement of a hypersurface in $\PP^n$ is affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Varieties
  - Hypersurfaces
  - Veronese Embedding
relations:
- kind: uses
  target: P-AGH212DUPLE
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and hint with Hartshorne I.3.5. The proof realizes the degree-d equation as a hyperplane equation after the d-uple embedding and identifies the complement as a closed subvariety of affine N-space.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the hyperplane-section identity, the complement calculation, and the affineness argument against published solutions.'
---

::: {.problem}
By abuse of language, a variety **is affine** if it is isomorphic to an affine variety.
If $H \subseteq \PP^n$ is any hypersurface, show that $\PP^n \sm H$ is affine.
:::

::: {.hint}
Let $H$ have degree $d$, consider the $d$-uple embedding of $\PP^n$ in $\PP^N$, and use that $\PP^N$ minus a hyperplane is affine.
:::

::: {.solution}
Let $H=Z(f)$, where $f\in k[x_0,\ldots,x_n]$ is a nonzero homogeneous polynomial of degree $d$.
Let
$$
\rho_d:\PP^n\longrightarrow\PP^N
$$
be the $d$-uple embedding, and write $Y=\rho_d(\PP^n)$.

<1>1. There is a hyperplane $K\subseteq\PP^N$ such that
$$
\rho_d(H)=Y\cap K.
$$

::: {.proof}
Index the homogeneous coordinates $y_0,\ldots,y_N$ of $\PP^N$ by the degree-$d$ monomials $M_0,\ldots,M_N$ in $x_0,\ldots,x_n$.
Since these monomials form a basis of the degree-$d$ homogeneous polynomials, write
$$
f=\sum_{i=0}^N c_iM_i.
$$
Let $L=\sum_i c_i y_i$ and put $K=Z(L)$.
For every $P\in\PP^n$,
$$
L(\rho_d(P))=\sum_i c_iM_i(P)=f(P).
$$
Hence $P\in H$ exactly when $\rho_d(P)\in K$, which proves the displayed identity.
:::

<1>2. The complement $Y\setminus(Y\cap K)$ is an affine variety.

::: {.proof}
The image $Y$ is closed in $\PP^N$ by [[P-AGH212DUPLE]].
A projective linear change of coordinates carries $K$ to a coordinate hyperplane, whose complement is the standard affine chart $\AA^N$.
Therefore $\PP^N\setminus K$ is affine.

Now
$$
Y\setminus(Y\cap K)=Y\cap(\PP^N\setminus K).
$$
Because $Y$ is closed in $\PP^N$, this intersection is closed in the affine variety $\PP^N\setminus K$.
A closed subvariety of an affine variety is affine, so the displayed complement is affine.
:::

<1>3. Q.E.D.

::: {.proof}
By [[P-AGH34DUPLEISO]], $\rho_d$ is an isomorphism $\PP^n\cong Y$.
Step <1>1 shows that it restricts to an isomorphism
$$
\PP^n\setminus H
\cong
Y\setminus(Y\cap K),
$$
and step <1>2 shows that the target is affine.
Hence $\PP^n\setminus H$ is affine.
:::
:::
