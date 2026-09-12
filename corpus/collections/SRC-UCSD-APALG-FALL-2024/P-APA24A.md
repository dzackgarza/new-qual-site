---
schema: qual/card@1
id: P-APA24A
kind: problem
title: Dimension formula for the sum of two subspaces
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let $X$ be a finite-dimensional vector space over a scalar field, and let $Y, Z \subseteq X$ be two subspaces.
For simplicity, you may further assume $Y \cap Z \neq \{0\}$ and $Y \not\subseteq Z$ and $Z \not\subseteq Y$.
Prove
\[
\dim(Y + Z) = \dim(Y) + \dim(Z) - \dim(Y \cap Z),
\]
where $Y + Z = \{ y + z \mid y \in Y,\ z \in Z \}$.
:::

::: {.solution}
Let
\[
u_1,\ldots,u_r
\]
be a basis of $Y\cap Z$. Extend it to bases
\[
u_1,\ldots,u_r,y_1,\ldots,y_p
\]
of $Y$ and
\[
u_1,\ldots,u_r,z_1,\ldots,z_q
\]
of $Z$.

<1>1. The list
\[
u_1,\ldots,u_r,y_1,\ldots,y_p,z_1,\ldots,z_q
\]
spans $Y+Z$.
::: {.proof}
Every $w\in Y+Z$ has the form $w=y+z$ with $y\in Y$ and $z\in Z$.
Expand $y$ in the chosen basis of $Y$ and $z$ in the chosen basis of $Z$. Their sum is therefore a linear combination of the displayed vectors.
:::

<1>2. The displayed list is linearly independent.
::: {.proof}
Suppose
\[
\sum_{i=1}^r a_i u_i+\sum_{j=1}^p b_jy_j+\sum_{k=1}^q c_kz_k=0.
\]
Then
\[
\sum_{j=1}^p b_jy_j
=-\left(\sum_{i=1}^r a_i u_i+\sum_{k=1}^q c_kz_k\right).
\]
The left side lies in $Y$, while the right side lies in $Z$, so their common value lies in $Y\cap Z$.
Hence
\[
\sum_{j=1}^p b_jy_j\in\operatorname{span}(u_1,\ldots,u_r).
\]
Because
\[
u_1,\ldots,u_r,y_1,\ldots,y_p
\]
is a basis of $Y$, it follows that every $b_j=0$. The original relation then becomes
\[
\sum_i a_i u_i+\sum_k c_k z_k=0,
\]
and since
\[
u_1,\ldots,u_r,z_1,\ldots,z_q
\]
is a basis of $Z$, all $a_i$ and $c_k$ are also zero.
:::

<1>3. Therefore
\[
\dim(Y+Z)=\dim Y+\dim Z-\dim(Y\cap Z).
\]
::: {.proof}
By <1>1 and <1>2, the displayed list is a basis of $Y+Z$, so
\[
\dim(Y+Z)=r+p+q.
\]
Also
\[
\dim Y=r+p,
\qquad
\dim Z=r+q,
\qquad
\dim(Y\cap Z)=r.
\]
Hence
\[
\dim Y+\dim Z-\dim(Y\cap Z)
=(r+p)+(r+q)-r=r+p+q,
\]
which equals $\dim(Y+Z)$.
:::
:::
