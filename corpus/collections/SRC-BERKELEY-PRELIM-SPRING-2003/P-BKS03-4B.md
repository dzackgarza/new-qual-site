---
schema: qual/card@1
id: P-BKS03-4B
kind: problem
title: A nonabelian simple group embeds normally in its automorphism group
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose $G$ is a nonabelian simple group and $A=\operatorname{Aut}(G)$.
Show that $A$ contains a normal subgroup isomorphic to $G$.
:::

::: {.solution}
For $g$ in $G$, let $c_g:G\to G$ be the inner automorphism $c_g(h)=ghg^{-1}$. Then it is easy to check that $g\mapsto c_g$ defines a homomorphism $G\to A$. It is nontrivial since $G$ is nonabelian, and thus an injection since $G$ is simple.
Let $B$ be the image, so $B\cong G$. If $\alpha\in A$ and $g,h\in G$, then

$$
\alpha(c_g(h))=\alpha(ghg^{-1})=\alpha(g)\alpha(h)\alpha(g)^{-1}=c_{\alpha(g)}(\alpha(h)),
$$

so $\alpha\circ c_g=c_{\alpha(g)}\circ\alpha$ in $A$. Thus $\alpha\circ c_g\circ\alpha^{-1}=c_{\alpha(g)}$, so $B$ is normal in $G$.
:::
