---
schema: qual/card@1
id: D-SSGKC
kind: definition
title: Quadratic forms in coordinates
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Bilinear Forms
  - Diagonalization
relations:
- kind: related-to
  target: D-NRRIT
review: draft
---

::: {.definition}
Let $k$ be a field with $\characteristic k\neq 2$ and $n\geq 1$.
A \dfn{quadratic form} in $n$ variables over $k$ is a homogeneous polynomial of degree $2$ in $x_1,\ldots,x_n$; it can be written uniquely as
$$
q(x_1, \ldots, x_n) = \sum_{i} a_{ii}x_i^2 + \sum_{i < j} 2a_{ij}x_ix_j = X^t A X, \qquad X = (x_1,\ldots,x_n)^t,
$$
where $A = (a_{ij})\in\Mat_{n\times n}(k)$ is symmetric, $a_{ji}=a_{ij}$.
The matrix $A$ is the \dfn{matrix of the form}.
:::

::: {.remark}
The coefficient of $x_ix_j$ for $i<j$ is written $2a_{ij}$ so that $X^tAX$ holds with $A$ symmetric: the off-diagonal entries $a_{ij}$ and $a_{ji}$ each contribute $a_{ij}x_ix_j$.
:::

::: {.proposition}
Let $k=\RR$ and let $q(X)=X^tAX$ with $A$ real symmetric.
There is an orthogonal matrix $P$ such that the change of variables $X = PX'$ gives
$$
q = \sum_{i=1}^n \lambda_i {x_i'}^2,
$$
where $\lambda_1,\ldots,\lambda_n$ are the eigenvalues of $A$.
:::

::: {.proof}
By the spectral theorem there is an orthogonal $P$ with $P^tAP=P^{-1}AP=\diag(\lambda_1,\ldots,\lambda_n)$, and $q(PX')=X'^t(P^tAP)X'$.
:::

::: {.definition}
Let $q$ be a real quadratic form with symmetric matrix $A$, nondegenerate in the sense that $\det A\neq 0$.
The \dfn{signature} of $q$ is the pair $(p,m)$, where $p$ and $m$ are the numbers of positive and negative coefficients $\lambda_i$ in a diagonalization $q=\sum_i\lambda_i{x_i'}^2$ obtained by an invertible change of variables.
:::

::: {.theorem title="Sylvester's law of inertia"}
For a nondegenerate real quadratic form, the numbers $p$ and $m$ do not depend on the invertible change of variables that diagonalizes it.
:::

::: {.example}
For a nondegenerate real quadratic form $q$ and $c>0$, the signature determines the level set $\theset{q = c}$ up to an invertible linear change of variables.
In two variables, signature $(2,0)$ gives an ellipse, $(1,1)$ a hyperbola, and $(0,2)$ the empty set.
In three variables, signature $(3,0)$ gives an ellipsoid, $(2,1)$ a hyperboloid of one sheet, $(1,2)$ a hyperboloid of two sheets, and $(0,3)$ the empty set.
:::

::: {.concept}
See Artin, *Algebra*, §8.7, (8.7.2)-(8.7.3), pp. 245-247; the signature and Sylvester's law are at §8.4, p. 240.
The basis-free formulation, as a function $q$ with $q(\lambda x) = \lambda^2 q(x)$ whose polarization is bilinear, is the related card of the same title.
:::
