---
schema: qual/card@1
id: PR-VA4S3
kind: proposition
title: The Segre embedding, and why $\PP^m \times \PP^n$ is projective
slogan: 'The Segre embedding identifies $\PP^m\times\PP^n$ with the rank-one tensor locus, cut out by the $2\times2$ minors.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Segre Embedding
  - Projective Varieties
  - Products
relations:
- kind: uses
  target: D-CP2MH
review: draft
prompts:
- Is $\PP^1 \times \PP^1$ a projective variety?
- What equations cut out the Segre image?
- Show that the Segre variety is the categorical product of projective varieties $X \subseteq \PP^n$ and $Y \subseteq \PP^m$.
---

::: {.proposition}
The Segre morphism
$$
\psi\colon \PP^m_k \times_k \PP^n_k \longrightarrow \PP_k^{(m+1)(n+1)-1}, \qquad
([x_i],[y_j]) \mapsto [x_i y_j]
$$
is a closed immersion. Its image is the closed subscheme cut out by the $2\times2$ minors
$$
z_{ij} z_{kl} - z_{il} z_{kj} = 0 .
$$
Consequently, if $X\subseteq\PP_k^m$ and $Y\subseteq\PP_k^n$ are projective varieties, then $X\times_kY$ is projective and its Segre image represents their categorical product in $k$-schemes.
:::

::: {.proof}
Rescaling the homogeneous coordinates by $x_i\mapsto\lambda x_i$ and $y_j\mapsto\mu y_j$ rescales every product $x_i y_j$ by the common factor $\lambda\mu$, so $\psi$ is well defined.

Every point in the image gives a matrix $(z_{ij})=(x_i y_j)$ of rank one, hence all $2\times2$ minors vanish. Conversely, work on the projective chart $D_+(z_{i_0j_0})$. After normalizing $z_{i_0j_0}=1$, the minor equations imply
$$
z_{ij}=z_{i j_0}z_{i_0 j}
$$
for all $i,j$. Thus this chart of the determinantal locus is isomorphic to
$$
\AA^m\times\AA^n,
$$
with coordinates $z_{i j_0}$ for $i\ne i_0$ and $z_{i_0 j}$ for $j\ne j_0$, exactly the corresponding product of standard affine charts of $\PP^m\times\PP^n$. These local inverses show that $\psi$ is an isomorphism onto the closed subscheme defined by the minors.

If $X$ and $Y$ are closed in the two projective spaces, then $X\times_kY$ is closed in $\PP^m\times_k\PP^n$ by base change of closed immersions. Composing with the Segre closed immersion embeds $X\times_kY$ into projective space.
:::

::: {.remark}
For $m = n = 1$ there is one minor, and the image is the quadric surface
$$
z_{00} z_{11} - z_{01} z_{10} = 0
$$
in $\PP^3$.
The two rulings of that quadric are the images of $\theset{p} \times \PP^1$ and $\PP^1 \times \theset{q}$.

If $V$ and $W$ are vector spaces with $\PP(V)=\PP^m$ and $\PP(W)=\PP^n$, then the Segre image is the projectivized locus of decomposable tensors $v\tensor w\in V\tensor W$, equivalently the rank-one tensors.
:::
