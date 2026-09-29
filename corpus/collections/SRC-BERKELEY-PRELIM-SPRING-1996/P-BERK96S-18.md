---
schema: qual/card@1
id: P-BERK96S-18
kind: problem
title: Automorphisms of a direct product of finite groups of coprime orders
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified that coprime orders force both cross-factor homomorphisms to be
    trivial, so automorphisms preserve each factor and restrict
    componentwise.
---

::: {.problem}
Let $G,H$ be finite groups of relatively prime orders. Prove that
\[
\operatorname{Aut}(G\times H)
\cong
\operatorname{Aut}(G)\times\operatorname{Aut}(H).
\]
:::

::: {.solution}
Write
$$
G_0\coloneqq G\times\{1\},
\qquad
H_0\coloneqq\{1\}\times H.
$$

::: pf

::: {.pf-step #s1}

Every homomorphism $G\to H$ and every homomorphism $H\to G$ is
trivial.

::: pf-proof

Let
$$
\psi:G\longrightarrow H
$$
be a homomorphism. The order of $\im\psi$ divides $\abs{G}$ because
$\im\psi$ is a quotient of $G$, and it divides $\abs{H}$ because it is a
subgroup of $H$. Since
$$
\gcd(\abs{G},\abs{H})=1,
$$
one has $\abs{\im\psi}=1$. Thus $\psi$ is trivial. The same argument
with $G$ and $H$ interchanged proves the other assertion.

:::

:::

::: {.pf-step #s2}

Every automorphism
$$
\varphi\in\Aut(G\times H)
$$
preserves both $G_0$ and $H_0$.

::: pf-proof

For $g\in G$, write
$$
\varphi(g,1)=(\alpha(g),\beta(g)).
$$
The maps
$$
\alpha:G\to G,
\qquad
\beta:G\to H
$$
obtained by composing $\varphi|_{G_0}$ with the two projections are
homomorphisms. By step [](#s1){.pf-ref}, $\beta$ is trivial, so
$$
\varphi(g,1)=(\alpha(g),1)\in G_0.
$$
Thus $\varphi(G_0)\subseteq G_0$. The same argument gives
$$
\varphi(H_0)\subseteq H_0.
$$

Apply the same reasoning to $\varphi^{-1}$. It gives
$$
\varphi^{-1}(G_0)\subseteq G_0,
\qquad
\varphi^{-1}(H_0)\subseteq H_0.
$$
Applying $\varphi$ to these inclusions yields the reverse inclusions.
Hence
$$
\varphi(G_0)=G_0,
\qquad
\varphi(H_0)=H_0.
$$

:::

:::

::: {.pf-step #s3}

Every $\varphi\in\Aut(G\times H)$ has a unique expression
$$
\varphi(g,h)=(\alpha(g),\delta(h))
$$
with
$$
\alpha\in\Aut(G),
\qquad
\delta\in\Aut(H).
$$

::: pf-proof

By step [](#s2){.pf-ref}, the restrictions of $\varphi$ to $G_0$ and $H_0$ are
automorphisms of those factors. Thus there are unique
$$
\alpha\in\Aut(G),
\qquad
\delta\in\Aut(H)
$$
such that
$$
\varphi(g,1)=(\alpha(g),1),
\qquad
\varphi(1,h)=(1,\delta(h)).
$$
Since
$$
(g,h)=(g,1)(1,h),
$$
the homomorphism property gives
$$
\begin{aligned}
\varphi(g,h)
&=
\varphi(g,1)\varphi(1,h)\\
&=
(\alpha(g),\delta(h)).
\end{aligned}
$$
Uniqueness follows by evaluating at $(g,1)$ and $(1,h)$.

:::

:::

::: {.pf-step #s4}

The map
$$
\Phi:\Aut(G\times H)\longrightarrow\Aut(G)\times\Aut(H),
\qquad
\varphi\longmapsto(\alpha,\delta),
$$
where $(\alpha,\delta)$ is supplied by step [](#s3){.pf-ref}, is a group isomorphism.

::: pf-proof

Composition is componentwise in the formula from step [](#s3){.pf-ref}, so $\Phi$ is a
homomorphism. It is injective because that formula determines $\varphi$
uniquely. It is surjective because, for every
$$
(\alpha,\delta)\in\Aut(G)\times\Aut(H),
$$
the map
$$
(g,h)\longmapsto(\alpha(g),\delta(h))
$$
is an automorphism of $G\times H$ whose image under $\Phi$ is
$(\alpha,\delta)$.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
\Aut(G\times H)
\cong
\Aut(G)\times\Aut(H)
}.
$$

::: pf-proof

This is the isomorphism constructed in step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
