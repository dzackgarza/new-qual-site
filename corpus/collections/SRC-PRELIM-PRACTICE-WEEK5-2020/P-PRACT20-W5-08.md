---
schema: qual/card@1
id: P-PRACT20-W5-08
kind: problem
title: Automorphism and inner automorphism groups
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 8).
---

::: {.problem}
Let $G$ be a group and define $\Aut(G)$ to be the set of all isomorphisms of $G$ to itself. Prove that $\Aut(G)$ is a group under the operation of functional composition. For each $g \in G$, define the map $\phi_g(x) = gxg^{-1}$ for $x \in G$ and let $\operatorname{Inn}(G) = \{\phi_g : g \in G\}$. Show that $\operatorname{Inn}(G)$ is a subgroup of $\Aut(G)$. What does $\operatorname{Inn}(G)$ look like if $G$ is abelian?
:::

::: {.solution}
<1>1. The composition of two automorphisms of $G$ is an automorphism of $G$.

::: {.proof}
Let $\alpha,\beta\in\Aut(G)$. Since both maps are bijections, their
composition $\alpha\circ\beta$ is a bijection. For $x,y\in G$,
\[
(\alpha\circ\beta)(xy)
=\alpha(\beta(xy))
=\alpha(\beta(x)\beta(y))
=\alpha(\beta(x))\alpha(\beta(y)).
\]
Thus $\alpha\circ\beta$ is a homomorphism and therefore an automorphism.
:::

<1>2. The set $\Aut(G)$ is a group under composition.

::: {.proof}
Composition of functions is associative. By step <1>1, $\Aut(G)$ is closed
under composition. The identity map
\[
\operatorname{id}_G:G\to G
\]
is an automorphism and is the identity for composition. If
$\alpha\in\Aut(G)$, its inverse function $\alpha^{-1}$ is a bijection; it is
also a homomorphism because, writing $u=\alpha(x)$ and $v=\alpha(y)$,
\[
\alpha^{-1}(uv)
=\alpha^{-1}(\alpha(x)\alpha(y))
=\alpha^{-1}(\alpha(xy))
=xy
=\alpha^{-1}(u)\alpha^{-1}(v).
\]
Hence every element has an inverse in $\Aut(G)$.
:::

<1>3. For every $g\in G$, the map
\[
\phi_g(x)=gxg^{-1}
\]
is an automorphism of $G$.

::: {.proof}
For $x,y\in G$,
\[
\phi_g(xy)
=gxyg^{-1}
=(gxg^{-1})(gyg^{-1})
=\phi_g(x)\phi_g(y).
\]
Thus $\phi_g$ is a homomorphism. Its inverse is $\phi_{g^{-1}}$, since
\[
\phi_{g^{-1}}(\phi_g(x))
=g^{-1}(gxg^{-1})g
=x.
\]
Hence $\phi_g\in\Aut(G)$.
:::

<1>4. The inner automorphisms satisfy
\[
\phi_g\circ\phi_h=\phi_{gh}
\qquad(g,h\in G).
\]

::: {.proof}
For every $x\in G$,
\[
(\phi_g\circ\phi_h)(x)
=g(hxh^{-1})g^{-1}
=(gh)x(gh)^{-1}
=\phi_{gh}(x).
\]
:::

<1>5. One has
\[
\boxed{\operatorname{Inn}(G)\le\Aut(G)}.
\]

::: {.proof}
By step <1>3, every inner automorphism belongs to $\Aut(G)$. Also
\[
\phi_e=\operatorname{id}_G.
\]
By step <1>4, the product of two inner automorphisms is inner, and
\[
\phi_g^{-1}=\phi_{g^{-1}}
\]
is inner. Hence $\operatorname{Inn}(G)$ is a subgroup.
:::

<1>6. If $G$ is abelian, then
\[
\boxed{\operatorname{Inn}(G)=\{\operatorname{id}_G\}}.
\]

::: {.proof}
If $G$ is abelian, then for all $g,x\in G$,
\[
\phi_g(x)=gxg^{-1}=xgg^{-1}=x.
\]
Thus every inner automorphism is the identity.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves that $\Aut(G)$ is a group, step <1>5 proves the subgroup
claim, and step <1>6 settles the abelian case.
:::
:::
