---
schema: qual/card@1
id: P-AGH292CONTRACT
kind: problem
title: A morphism contracting a subvariety contracts the whole space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Proper Morphisms
  - Rigidity
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the contraction statement with the retained Hartshorne II.9.2 transcription and expanded its reference to the hypotheses of II.9.1. Checked Krull intersection against Stacks Project Tag 00IP. The proof derives constancy on any open neighborhood of Y from the formal-function calculation, then proves that the given morphism is constant on all of projective space.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Use the result of (Ex. 9.1) to prove the following geometric result.
Let $k$ be algebraically closed, let $Y\subseteq X=\PP_k^n$ be a connected nonsingular closed subvariety of positive dimension, and let $f:X\to Z$ be a morphism of $k$-varieties.
Suppose that $f(Y)$ is a single closed point $P \in Z$.
Then $f(X) = P$ also.
:::

::: {.solution}
Let $\mathcal I$ be the ideal sheaf of $Y$ in $X$ and let $\hat X$ be the [[D-SCHFORMAL|formal completion]] along $Y$.
By [[P-AGH291FORMALREG]], the constants map identifies $\Gamma(\hat X,\OO_{\hat X})$ with $k$.

::: pf

::: {.pf-step #s1}

For every open neighborhood $U$ of $Y$ in $X$, the restriction homomorphism
$$
\Gamma(U,\OO_X)\longrightarrow\Gamma(\hat X,\OO_{\hat X})
$$
is injective.

::: pf-proof

The completion of $U$ along $Y$ is canonically $\hat X$, since the ideal quotients on the common underlying space $Y$ are unchanged after restricting to a neighborhood of $Y$.
Reduction modulo each $\mathcal I^r$ therefore defines the stated homomorphism to the inverse-limit section ring.

Suppose $a\in\Gamma(U,\OO_X)$ maps to zero.
Choose a point $y\in Y$, which is possible by the positive-dimensional hypothesis.
The germ $a_y$ lies in $(\mathcal I_y)^r$ for every $r\ge1$, since its restriction to every infinitesimal neighborhood is zero.
The ring $\OO_{X,y}$ is noetherian and local, and $\mathcal I_y$ is a proper ideal.
Thus [Krull's intersection theorem](https://stacks.math.columbia.edu/tag/00IP) gives
$$
\bigcap_{r\ge1}(\mathcal I_y)^r=0,
$$
so $a_y=0$.
The section $a$ is then zero on some nonempty open neighborhood of $y$ in $U$.
Since $U$ is integral, a regular function is determined by its generic value; hence $a=0$ on $U$.
This proves injectivity without assuming that $U$ is affine.

:::

:::

::: {.pf-step #s2}

Every regular function on an open neighborhood $U$ of $Y$ is constant.

::: pf-proof

By step [](#s1){.pf-ref} and the formal-function calculation, there is an injective $k$-algebra map $\Gamma(U,\OO_X)\to k$ that is the identity on constants.
For any $a$ in its source, let $c\in k$ be its image.
Then $a-c$ has image zero, so injectivity gives $a=c$.
Consequently $\Gamma(U,\OO_X)=k$ via the constants map.

:::

:::

::: {.pf-step #s3}

The morphism $f$ is constant with value $P$ on a dense open neighborhood of $Y$.

::: pf-proof

Choose an affine open $V=\Spec B\subseteq Z$ containing $P$ and set $U=f^{-1}(V)$.
The hypothesis $f(Y)=P$ implies $Y\subseteq U$.
Thus $U$ is nonempty and dense in the integral scheme $X$.
Step [](#s2){.pf-ref} identifies the global-functions map of $f|_U$ with a $k$-algebra homomorphism
$$
B\longrightarrow\Gamma(U,\OO_U)=k.
$$
It defines a $k$-point $Q\in V$, and $f|_U$ is the composite $U\to\Spec k\xrightarrow{Q}V$.
Indeed, this composite and $f|_U$ have identical maps on coordinate rings on every affine open of $U$, so they agree as morphisms.
As $U$ contains $Y$ and $f(Y)=P$, the point $Q$ must be $P$.
The closed point $P$ is $k$-rational because $k$ is algebraically closed.

:::

:::

::: pf-qed

The fibre $f^{-1}(P)$ is closed in $X$ and contains the dense open $U$ from step [](#s3){.pf-ref}.
It therefore has underlying set all of $X$, proving $f(X)=\{P\}$.
In fact the morphism itself is the constant morphism to $P$: it agrees with that morphism on $U$, the source is reduced, and the target variety is separated, so [[P-AGH242AGREEDENSE]] applies.

:::

:::

:::
