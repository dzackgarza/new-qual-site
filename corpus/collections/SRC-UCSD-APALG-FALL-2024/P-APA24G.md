---
schema: qual/card@1
id: P-APA24G
kind: problem
title: Averaging operator is the orthogonal projection onto $G$-invariants
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/FA24_202_Applied_Algebra_Qual.pdf,
    problem 7: for a finite-dimensional unitary representation (V, phi) of a
    finite group G, to state the definition of V^G and prove that the average of
    the images of g over G is the orthogonal projection onto V^G. The card
    agrees.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Every step is correct. Reindexing the sum along multiplication by h shows
    that the image of P is pointwise fixed, so it lies in V^G; P fixes V^G
    because the average of |G| copies of an invariant vector is that vector;
    hence P is idempotent with image exactly V^G, since invariants are their own
    images. Unitarity gives phi(g)^* = phi(g)^{-1}, and inversion permutes G, so
    P is self-adjoint. A self-adjoint idempotent is the orthogonal projection
    onto its image: the image is closed, and pairing an image vector with a
    kernel vector gives zero after moving P across the inner product. Nothing
    was changed.
---

::: {.problem}
Let $(V, \varphi)$ be a finite-dimensional unitary representation of a finite group $G$.
State the definition of the space $V^G$ of $G$-invariant vectors in $V$, and prove that
$$
P = \frac{1}{\cardinality{G}} \sum_{g \in G} \varphi(g)
$$
is the orthogonal projection of $V$ onto $V^G$.
:::

::: {.solution}

The invariant subspace is
$$
V^G:=\{v\in V:\varphi(g)v=v\text{ for every }g\in G\}.
$$
Define
$$
P:=\frac1{\cardinality{G}}\sum_{g\in G}\varphi(g).
$$

::: pf

::: {.pf-step #image-in-invariants}
The image of $P$ is contained in $V^G$.

::: pf-proof
Let $v\in V$ and $h\in G$. Then
$$
\varphi(h)Pv
=\frac1{\cardinality{G}}\sum_{g\in G}\varphi(hg)v.
$$
As $g$ runs through $G$, so does $hg$. Hence
$$
\varphi(h)Pv
=\frac1{\cardinality{G}}\sum_{k\in G}\varphi(k)v
=Pv.
$$
Thus $Pv\in V^G$.
:::

:::

::: {.pf-step #identity-on-invariants}
The operator $P$ acts as the identity on $V^G$.

::: pf-proof
If $v\in V^G$, then $\varphi(g)v=v$ for every $g\in G$. Therefore
$$
Pv=\frac1{\cardinality{G}}\sum_{g\in G}v=v.
$$
:::

:::

::: {.pf-step #p-idempotent-with-image-vg}
Consequently $P^2=P$ and $\operatorname{im}P=V^G$.

::: pf-proof
By step [](#image-in-invariants){.pf-ref}, $Pv\in V^G$ for every $v$, and by step [](#identity-on-invariants){.pf-ref}, $P$ is the identity on $V^G$. Hence
$$
P^2v=P(Pv)=Pv.
$$
Thus $P^2=P$. Also step [](#image-in-invariants){.pf-ref} gives $\operatorname{im}P\subseteq V^G$, while step [](#identity-on-invariants){.pf-ref} gives $V^G\subseteq\operatorname{im}P$, because $v=Pv$ for every invariant $v$.
:::

:::

::: {.pf-step #p-self-adjoint}
The operator $P$ is self-adjoint.

::: pf-proof
Because the representation is unitary,
$$
\varphi(g)^*=\varphi(g)^{-1}=\varphi(g^{-1}).
$$
Therefore
$$
P^*
=\frac1{\cardinality{G}}\sum_{g\in G}\varphi(g)^*
=\frac1{\cardinality{G}}\sum_{g\in G}\varphi(g^{-1}).
$$
Inversion permutes the elements of $G$, so the final sum equals $P$.
:::

:::

::: pf-step
Hence $P$ is the orthogonal projection of $V$ onto $V^G$.

::: pf-proof
By step [](#p-idempotent-with-image-vg){.pf-ref}, $P$ is an idempotent with image $V^G$, and by step [](#p-self-adjoint){.pf-ref} it is self-adjoint. A self-adjoint idempotent is the orthogonal projection onto its image. Explicitly, if $u=Px\in\operatorname{im}P$ and $w\in\ker P$, then
$$
\langle u,w\rangle
=\langle Px,w\rangle
=\langle x,Pw\rangle
=0.
$$
Thus $\operatorname{im}P\perp\ker P$, so $P$ is precisely the orthogonal projection onto $V^G$.
:::

:::

:::

:::
