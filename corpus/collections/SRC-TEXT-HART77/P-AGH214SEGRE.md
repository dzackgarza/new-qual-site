---
schema: qual/card@1
id: P-AGH214SEGRE
kind: problem
title: The Segre embedding of $\PP^r \times \PP^s$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Segre Embedding
  - Projective Varieties
  - Homogeneous Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the Segre map and kernel hint with the retained Hartshorne I.2.14 transcription. The proof uses the full rectangular coordinate range and reconstructs both projective factors from any nonzero matrix entry, without imposing a product topology.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed and let $r,s\ge0$.
Let $\psi: \PP^r \times \PP^s \to \PP^N$ be the map sending the ordered pair $\tv{a_0 : \cdots : a_r} \times \tv{b_0 : \cdots : b_s}$ to the point with coordinates $a_i b_j$ in lexicographic order, where $N = rs + r + s$.
The map $\psi$ is well defined and injective; it is called the **Segre embedding**. Show that the image of $\psi$ is a subvariety of $\PP^N$.
:::

::: {.hint}
Let the homogeneous coordinates of $\PP^N$ be $\ts{z_{ij} \st 0 \leq i \leq r,\ 0 \leq j \leq s}$, and let $\mfa$ be the kernel of the homomorphism $k[\ts{z_{ij}}] \to k[x_0,\ldots,x_r,y_0,\ldots,y_s]$ sending $z_{ij} \mapsto x_i y_j$.
Then show $\im \psi = Z(\mfa)$.
:::

::: {.solution}
Write $T=k[z_{ij}:0\le i\le r,\ 0\le j\le s]$ and $S=k[x_0,\ldots,x_r,y_0,\ldots,y_s]$, and let $\theta:T\to S$ be the substitution in the hint.
Put $\mfa=\ker\theta$.

<1>1. The map $\psi$ is well-defined and its image is contained in $Z(\mfa)$.

::: {.proof}
For nonzero vectors $a,b$, choose indices $i,j$ with $a_i\ne0$ and $b_j\ne0$.
Then $a_ib_j\ne0$, so the matrix $(a_ib_j)$ gives a projective point.
Replacing the two vectors by $\lambda a$ and $\mu b$ multiplies the entire matrix by $\lambda\mu$, leaving that point unchanged.
This proves well-definedness.
For every $F\in\mfa$, the polynomial $F((x_iy_j)_{ij})$ is identically zero.
It therefore vanishes at every pair $a,b$, so the image satisfies all the equations of $\mfa$.
:::

<1>2. The ideal $\mfa$ is homogeneous and prime, and every point of $Z(\mfa)$ is in the image of $\psi$.

::: {.proof}
The map $\theta$ sends a homogeneous polynomial of degree $d$ to a homogeneous polynomial of degree $2d$, or to zero.
Distinct source degrees have distinct target degrees, so the kernel is homogeneous.
The quotient $T/\mfa\cong\im\theta$ is a subring of the domain $S$, hence is a domain.
Thus $\mfa$ is prime.

It contains every two-by-two minor
$$
z_{ij}z_{ab}-z_{ib}z_{aj},
$$
since both monomials have image $x_ix_ay_jy_b$.
Take a point $[c_{ij}]\in Z(\mfa)$ and choose a nonzero entry $c_{ab}$.
The minor equations give
$$
c_{ij}=\frac{c_{ib}c_{aj}}{c_{ab}}\qquad\text{for all }i,j.
$$
Set $u_i=c_{ib}$ and $v_j=c_{aj}/c_{ab}$.
These vectors are nonzero because $u_a=c_{ab}\ne0$ and $v_b=1$.
The displayed equations say $c_{ij}=u_iv_j$, so $[c_{ij}]=\psi([u],[v])$.
This proves the reverse inclusion, and hence $\im\psi=Z(\mfa)$.
:::

<1>3. The image is a projective variety, and the recovered factors are unique.

::: {.proof}
The zero set $Z(\mfa)$ is nonempty by step <1>1, since both projective factors contain points.
The homogeneous prime correspondence in [[P-AGH24CORRESPONDENCE]] therefore makes it irreducible and closed in $\PP^N$.
It is consequently a projective subvariety, as required.

If $[c_{ij}]=\psi([u],[v])$ and $c_{ab}\ne0$, then its $b$th column is a nonzero scalar multiple of $u$, and its $a$th row is a nonzero scalar multiple of $v$.
Thus those column and row determine $[u]$ and $[v]$ uniquely.
Equivalently, on this chart the inverse coordinates are $u_i/u_a=c_{ib}/c_{ab}$ and $v_j/v_b=c_{aj}/c_{ab}$.
This verifies the stated injectivity and identifies the inverse on every nonzero-entry chart.
The description also includes $r=0$ or $s=0$, when every nonzero matrix automatically has rank one.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 identify the image with the zero set from the hint, and step <1>3 proves it is a projective variety.
:::
:::
