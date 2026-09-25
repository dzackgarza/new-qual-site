---
schema: qual/card@1
id: P-BKF87-6
kind: problem
title: Automorphisms of a direct product of finite groups of coprime order
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
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
<1>1. The subgroup $G\times\{1\}$ is characteristic in $G\times H$.

::: {.proof}
An element $(g,h)\in G\times H$ belongs to $G\times\{1\}$ if and only if its order divides $\abs G$.

Indeed, if $h=1$, then
$$
\operatorname{ord}(g,1)=\operatorname{ord}(g)
$$
divides $\abs G$ by Lagrange's theorem.

Conversely, suppose
$$
\operatorname{ord}(g,h)\mid\abs G.
$$
Then $\operatorname{ord}(h)$ divides $\operatorname{ord}(g,h)$, so it divides $\abs G$. It also divides $\abs H$. Since
$$
\gcd(\abs G,\abs H)=1,
$$
one has $\operatorname{ord}(h)=1$, hence $h=1$.

Thus $G\times\{1\}$ is characterized purely by element orders. Every automorphism preserves element orders, so every automorphism of $G\times H$ preserves $G\times\{1\}$.
:::

<1>2. The subgroup $\{1\}\times H$ is characteristic in $G\times H$.

::: {.proof}
Interchanging the roles of $G$ and $H$ in step <1>1 shows that
$$
\{1\}\times H
$$
is exactly the set of elements whose orders divide $\abs H$. Hence it too is preserved by every automorphism.
:::

<1>3. Every automorphism $\varphi$ of $G\times H$ has the form
$$
\varphi(g,h)=\bigl(\alpha(g),\beta(h)\bigr)
$$
for uniquely determined
$$
\alpha\in\operatorname{Aut}(G),
\qquad
\beta\in\operatorname{Aut}(H).
$$

::: {.proof}
By steps <1>1 and <1>2, $\varphi$ restricts to automorphisms of the two factors. Thus there are uniquely determined automorphisms $\alpha$ and $\beta$ such that
$$
\varphi(g,1)=(\alpha(g),1)
$$
and
$$
\varphi(1,h)=(1,\beta(h)).
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
(\alpha(g),1)(1,\beta(h))\\
&=
(\alpha(g),\beta(h)).
\end{aligned}
$$
:::

<1>4. The map
$$
\Psi:\operatorname{Aut}(G\times H)
\longrightarrow
\operatorname{Aut}(G)\times\operatorname{Aut}(H)
$$
that sends $\varphi$ to its two restrictions is a group isomorphism.

::: {.proof}
Step <1>3 shows that $\Psi$ is injective.

Given
$$
(\alpha,\beta)\in
\operatorname{Aut}(G)\times\operatorname{Aut}(H),
$$
the map
$$
(g,h)\longmapsto(\alpha(g),\beta(h))
$$
is an automorphism of $G\times H$, with inverse
$$
(g,h)\longmapsto(\alpha^{-1}(g),\beta^{-1}(h)).
$$
Hence $\Psi$ is surjective.

Finally, restriction commutes with composition, so $\Psi$ is a homomorphism. Therefore it is an isomorphism.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required isomorphism.
:::
:::
