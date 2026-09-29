---
schema: qual/card@1
id: P-AGH3105ETALENBHD
kind: problem
title: Local freeness is detected on etale neighborhoods
classification:
  areas:
  - algebraic-geometry
  topics:
  - Etale Morphisms
  - Etale Neighborhoods
  - Locally Free Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.5 together with the flat/unramified characterization
    of étale morphisms. The proof descends a free basis across the faithfully
    flat local map on stalks and then uses coherence to spread the resulting
    stalkwise freeness to a Zariski neighborhood.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $x$ is a point of a scheme $X$, we define an **étale neighborhood** of $x$ to be an étale morphism $f: U \to X$, together with a point $x' \in U$ such that $f(x') = x$.

As an example of the use of étale neighborhoods, prove the following: if $\mcf$ is a coherent sheaf on $X$, and if every point of $X$ has an étale neighborhood $f: U \to X$ for which $f^* \mcf$ is a free $\mco_U\dash$module, then $\mcf$ is locally free on $X$.
:::

::: {.solution}
Fix a point $x\in X$. Choose an étale neighborhood
$$
f:U\longrightarrow X,
\qquad
x'\in U,
\qquad
f(x')=x,
$$
such that $f^*\mcf$ is free.

Put
$$
A=\OO_{X,x},
\qquad
B=\OO_{U,x'},
\qquad
M=\mcf_x.
$$

::: pf

::: {.pf-step #s1}

The local homomorphism $A\to B$ is faithfully flat and
$$
\mathfrak m_A B=\mathfrak m_B.
$$

::: pf-proof

An étale morphism is flat and unramified by
[[P-AGH3103ETALECHAR|Exercise III.10.3]]. Hence $A\to B$ is flat and
Hartshorne's unramified condition gives
$$
\mathfrak m_A B=\mathfrak m_B.
$$

A flat local homomorphism of local rings is faithfully flat. Indeed, if $N$ is
a nonzero $A$-module and $0\ne n\in N$, then the cyclic submodule $An$ is
isomorphic to $A/I$ for the proper ideal $I=\operatorname{Ann}(n)$. Flatness
preserves the injection $An\hookrightarrow N$, while
$$
(A/I)\tensor_A B=B/IB\ne0
$$
because $I\subseteq\mathfrak m_A$ and hence $IB\subseteq\mathfrak m_B$.
Thus $N\tensor_A B\ne0$, so tensoring with $B$ detects nonzero modules.

:::

:::

::: {.pf-step #s2}

The stalk $M=\mcf_x$ is a free $A$-module.

::: pf-proof

Since pullback commutes with stalks,
$$
(f^*\mcf)_{x'}\cong M\tensor_A B.
$$
By hypothesis this is a free $B$-module, say of rank $r$.

Let
$$
k=A/\mathfrak m_A,
\qquad
k'=B/\mathfrak m_B.
$$
Using step [](#s1){.pf-ref},
$$
(M/\mathfrak m_A M)\tensor_k k'
\cong
(M\tensor_A B)/\mathfrak m_B(M\tensor_A B)
\cong
(k')^{\oplus r}.
$$
Therefore
$$
\dim_k M/\mathfrak m_A M=r.
$$

Choose elements $m_1,\ldots,m_r\in M$ whose classes form a $k$-basis of
$M/\mathfrak m_A M$. Because $M$ is finite over the local ring $A$, Nakayama's
lemma gives a surjection
$$
\varphi:A^{\oplus r}\twoheadrightarrow M,
\qquad
e_i\longmapsto m_i.
$$

Tensor with the flat $A$-algebra $B$. We get a surjection
$$
\varphi_B:B^{\oplus r}\twoheadrightarrow M\tensor_A B.
$$
Modulo $\mathfrak m_B$, this is an isomorphism between $r$-dimensional
$k'$-vector spaces. Since the target is free of rank $r$, Nakayama's lemma
applied to a matrix for $\varphi_B$ shows that $\varphi_B$ is an isomorphism.

Let $K=\ker\varphi$. Flatness of $B/A$ gives
$$
K\tensor_A B=\ker\varphi_B=0.
$$
Faithful flatness from step [](#s1){.pf-ref} therefore gives $K=0$. Hence
$$
\boxed{M\cong A^{\oplus r}}.
$$

:::

:::

::: {.pf-step #s3}

The sheaf $\mcf$ is free on a Zariski neighborhood of $x$.

::: pf-proof

Choose the basis $m_1,\ldots,m_r$ of $\mcf_x$ from step [](#s2){.pf-ref}. After shrinking
to an open neighborhood $V$ of $x$, each $m_i$ is represented by a section of
$\mcf|_V$. These sections define a morphism
$$
\psi:\OO_V^{\oplus r}\longrightarrow\mcf|_V
$$
whose stalk at $x$ is an isomorphism.

Because $\mcf$ is coherent, the kernel and cokernel of $\psi$ are coherent.
Their stalks at $x$ vanish, so after shrinking $V$ once more both sheaves
vanish identically. Thus
$$
\psi:\OO_V^{\oplus r}\xrightarrow{\sim}\mcf|_V.
$$
Hence $\mcf$ is free on a Zariski neighborhood of $x$.

:::

:::

::: {.pf-step #s4}

The sheaf $\mcf$ is locally free on $X$.

::: pf-proof

The point $x\in X$ was arbitrary. Step [](#s3){.pf-ref} produces a Zariski neighborhood
of every point on which $\mcf$ is free. Therefore $\mcf$ is locally free.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} descend freeness from an étale stalk, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref}
spread the resulting free stalk to ordinary Zariski neighborhoods across all
of $X$.

:::

:::

:::
