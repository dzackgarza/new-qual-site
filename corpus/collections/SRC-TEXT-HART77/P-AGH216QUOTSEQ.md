---
schema: qual/card@1
id: P-AGH216QUOTSEQ
kind: problem
title: A subsheaf gives a short exact sequence with its quotient sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Quotient Sheaves
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise II.1.6 together with the immediately preceding definitions of subsheaf, quotient sheaf, image, surjectivity, and exactness in Hartshorne II.1. The proof uses the stalk description of the quotient sheaf and the stalkwise criterion for exactness.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
(a) Let $\mcf'$ be a subsheaf of a sheaf $\mcf$.
Show that the natural map of $\mcf$ to the quotient sheaf $\mcf/\mcf'$ is surjective and has kernel $\mcf'$.
Thus there is an exact sequence
\[
0 \to \mcf' \to \mcf \to \mcf/\mcf' \to 0.
\]

(b) Conversely, if
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is an exact sequence, show that $\mcf'$ is isomorphic to a subsheaf of $\mcf$, and that $\mcf''$ is isomorphic to the quotient of $\mcf$ by this subsheaf.
:::

::: {.solution}
Let
$$
q:\mcf\longrightarrow\mcf/\mcf'
$$
denote the natural morphism to the quotient sheaf, defined as the sheafification of the presheaf quotient
$$
U\longmapsto\mcf(U)/\mcf'(U).
$$

::: pf

::: {.pf-step #stalk-of-quotient-sheaf}
For every $x\in X$, the stalk of the quotient sheaf is canonically
$$
(\mcf/\mcf')_x\cong\mcf_x/\mcf'_x,
$$
and the induced stalk map $q_x$ is the ordinary quotient homomorphism.

::: pf-proof
Taking a stalk is a filtered colimit over neighborhoods of $x$.
Filtered colimits of abelian groups commute with cokernels, so
$$
\left(\varinjlim_{x\in U}\mcf(U)\right)
\Big/
\left(\varinjlim_{x\in U}\mcf'(U)\right)
\cong
\varinjlim_{x\in U}\bigl(\mcf(U)/\mcf'(U)\bigr).
$$
Sheafification does not change stalks.
Hence the stalk of the quotient sheaf is exactly $\mcf_x/\mcf'_x$, and $q_x$ is induced by the quotient maps on sections.
:::

:::

::: {.pf-step #q-surjective-kernel-fprime}
The natural morphism $q:\mcf\to\mcf/\mcf'$ is surjective and has kernel $\mcf'$.

::: pf-proof
By step [](#stalk-of-quotient-sheaf){.pf-ref}, for every $x\in X$ the map
$$
q_x:\mcf_x\longrightarrow\mcf_x/\mcf'_x
$$
is surjective and has kernel $\mcf'_x$.
A morphism of sheaves is surjective exactly when all its stalk maps are surjective, so $q$ is surjective.

The kernel sheaf of $q$ has stalk
$$
(\ker q)_x=\ker(q_x)=\mcf'_x.
$$
The inclusion $\mcf'\hookrightarrow\mcf$ therefore identifies $\mcf'$ with $\ker q$, since a morphism of sheaves inducing an isomorphism on every stalk is an isomorphism.
Thus
$$
\boxed{0\longrightarrow\mcf'\longrightarrow\mcf\longrightarrow\mcf/\mcf'\longrightarrow0}
$$
is exact, proving part (a).
:::

:::

::: {.pf-step #i-identifies-fprime-subsheaf}
In an exact sequence
$$
0\longrightarrow\mcf'\xrightarrow{i}\mcf\xrightarrow{p}\mcf''\longrightarrow0,
$$
the morphism $i$ identifies $\mcf'$ with a subsheaf of $\mcf$.

::: pf-proof
Exactness at $\mcf'$ says that $i$ is injective.
Equivalently, every stalk map
$$
i_x:\mcf'_x\longrightarrow\mcf_x
$$
is injective.
The image sheaf $\operatorname{im}i$ is, by definition, a subsheaf of $\mcf$.
The induced morphism
$$
\mcf'\longrightarrow\operatorname{im}i
$$
is an isomorphism on every stalk, hence an isomorphism of sheaves.
Thus we may identify $\mcf'$ with the subsheaf $\operatorname{im}i\subseteq\mcf$.
:::

:::

::: {.pf-step #quotient-iso-fdoubleprime}
With the identification of step [](#i-identifies-fprime-subsheaf){.pf-ref}, there is a canonical isomorphism
$$
\boxed{\mcf/\mcf'\cong\mcf''}.
$$

::: pf-proof
Exactness at $\mcf$ gives
$$
\ker p=\operatorname{im}i=\mcf'.
$$
Therefore $p$ kills the subsheaf $\mcf'$ and induces a unique morphism
$$
\bar p:\mcf/\mcf'\longrightarrow\mcf''.
$$
On the stalk at $x$, this is the homomorphism
$$
\bar p_x:\mcf_x/\mcf'_x\longrightarrow\mcf''_x
$$
induced by $p_x$.
The stalk sequence
$$
0\longrightarrow\mcf'_x\longrightarrow\mcf_x\longrightarrow\mcf''_x\longrightarrow0
$$
is exact, so the ordinary first isomorphism theorem gives
$$
\mcf_x/\mcf'_x\cong\mcf''_x.
$$
Thus $\bar p$ is an isomorphism on every stalk and hence an isomorphism of sheaves.
This proves part (b).
:::

:::

::: pf-qed
Steps [](#stalk-of-quotient-sheaf){.pf-ref} and [](#q-surjective-kernel-fprime){.pf-ref} prove part (a), and steps [](#i-identifies-fprime-subsheaf){.pf-ref} and [](#quotient-iso-fdoubleprime){.pf-ref} prove part (b).
:::

:::

:::
