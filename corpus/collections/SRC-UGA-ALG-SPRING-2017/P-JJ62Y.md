---
schema: qual/card@1
id: P-JJ62Y
kind: problem
title: Galois group of $x^5-2$ over $\QQ$ isomorphic to $\begin{pmatrix}a&b\\0&1\end{pmatrix}$ with $a\in\FF_5^\times$ and $b\in\FF_5$, and the Galois intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Matrix Groups
relations: []
review: draft
---
::: {.problem}
(a) Let $K$ denote the splitting field of $x^5 - 2$ over $\QQ$. Show that the Galois group $\operatorname{Gal}(K/\QQ)$ is isomorphic to the matrix group
$$
\operatorname{Aff}(\FF_5) = \left\{ \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} \;\middle|\; a \in \FF_5^\times, \, b \in \FF_5 \right\}.
$$

(b) Determine all intermediate fields between $K$ and $\QQ$ that are Galois over $\QQ$.
:::

::: {.solution}
Let $\alpha$ be the positive real fifth root of $2$ and let $\zeta=e^{2\pi i/5}$. Then $K=\QQ(\alpha,\zeta)$.

::: pf

::: {.pf-step #s1}

The degree of the splitting field is $[K:\QQ]=20$.

::: pf-proof

Eisenstein's criterion at $2$ makes $x^5-2$ irreducible, so $[\QQ(\alpha):\QQ]=5$. The cyclotomic polynomial $\Phi_5=x^4+x^3+x^2+x+1$ is irreducible, hence $[\QQ(\zeta):\QQ]=4$. Both degrees divide $[K:\QQ]$, so $20$ divides $[K:\QQ]$. By the tower law $[K:\QQ]\leq5\cdot4=20$. Equality follows.

:::

:::

::: {.pf-step #s2}

The map
$$
\boxed{\Psi:\operatorname{Gal}(K/\QQ)\xrightarrow{\sim}\operatorname{Aff}(\FF_5),
\quad \sigma\longmapsto\begin{pmatrix}a&b\\0&1\end{pmatrix},
\quad \sigma(\zeta)=\zeta^a,\ \sigma(\alpha)=\zeta^b\alpha}
$$
is a group isomorphism.

::: pf-proof

Every automorphism preserves $\QQ$, sends $\zeta$ to a primitive fifth root $\zeta^a$ with $a\in\FF_5^\times$, and sends $\alpha$ to one of the roots $\zeta^b\alpha$ with $b\in\FF_5$. Its values on these generators determine it, so $\Psi$ is injective into a set of $4\cdot5=20$ matrices. As $K/\QQ$ is the separable splitting field of $x^5-2$, its Galois group has order $20$ by step [](#s1){.pf-ref}; hence $\Psi$ is bijective. If $\sigma,\tau$ correspond respectively to $(a,b)$ and $(c,d)$, then
$$
(\sigma\tau)(\zeta)=\zeta^{ac},\qquad
(\sigma\tau)(\alpha)=\zeta^{b+ad}\alpha.
$$
These are precisely the entries of the matrix product, so $\Psi$ respects composition.

:::

:::

::: {.pf-step #s3}

The normal subgroups of $\operatorname{Aff}(\FF_5)$ are precisely the trivial group, the translation subgroup $T$ of order five, the subgroup $T\rtimes\{\pm1\}$ of order ten, and the whole group.

::: pf-proof

Identify the affine group with pairs $(a,b)$ acting as $u\mapsto au+b$. The homomorphism $(a,b)\mapsto a$ has kernel $T=\{(1,b)\}$ and cyclic image $\FF_5^\times$ of order four. The inverse images of its three subgroups are therefore normal, giving $T$, $T\rtimes\{\pm1\}$, and the whole group.

Conversely, let $N$ be normal and nontrivial. If $N$ contains some $(a,b)$ with $a\neq1$, then commutation with $(1,t)$ gives
$$
[(a,b),(1,t)]=(1,(a-1)t)\in N.
$$
As $a-1\neq0$, these commutators range over $T$, proving $T\subseteq N$. If no such element exists, then $N\subseteq T$, and the cyclic group $T$ of prime order five forces $N=T$. Thus every nontrivial normal subgroup contains $T$, and the quotient classification supplies exactly the stated list.

:::

:::

::: {.pf-step #s4}

The intermediate fields Galois over $\QQ$ are exactly
$$
\boxed{\QQ,\quad\QQ(\sqrt5),\quad\QQ(\zeta),\quad K}.
$$

::: pf-proof

By the Galois correspondence, such fields are the fixed fields of normal subgroups. The whole group fixes $\QQ$ and the trivial group fixes $K$. The translation subgroup $T$ fixes $\zeta$ and has index four, so its fixed field is $\QQ(\zeta)$. The subgroup $T\rtimes\{\pm1\}$ has index two and fixes $\zeta+\zeta^{-1}$. With $u=\zeta+\zeta^{-1}$, the relation $1+\zeta+\zeta^2+\zeta^3+\zeta^4=0$ gives $u^2+u-1=0$. Thus $\QQ(u)=\QQ(\sqrt5)$, which has degree two and is the fixed field. By step [](#s3){.pf-ref}, no other normal subgroup occurs.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), and step [](#s4){.pf-ref} proves part (b).

:::

:::

:::
