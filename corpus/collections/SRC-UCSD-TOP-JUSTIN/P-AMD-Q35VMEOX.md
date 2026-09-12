---
schema: qual/card@1
id: P-AMD-Q35VMEOX
kind: problem
title: $H_*(G)$ is an algebra, with $G$ acting through $\pi_0(G)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Algebras
  - Group Actions
relations: []
review: draft
---

::: {.problem}
Let $G$ be a topological group.
Show that $H_*(G)$ is an algebra.
Show that $G\actson H_*(G)$, which factors through the homomorphism $G \into \pi_0(G)$ yielding a trivial action if $G$ is path-connected.
:::

::: {.solution}
<1>1. Let $m:G\times G\to G$ be multiplication and $e\in G$ the identity. Define the Pontryagin product
$$
\star:H_p(G)\otimes H_q(G)\longrightarrow H_{p+q}(G)
$$
by
$$
a\star b=m_*(a\times b),
$$
where $a\times b$ is the homology cross product.
::: {.proof}
The cross product sends $H_p(G)\otimes H_q(G)$ naturally to $H_{p+q}(G\times G)$, and multiplication then induces a map back to $H_{p+q}(G)$.
:::

<1>2. This product makes $H_*(G)$ a graded algebra, with unit the class $[e]\in H_0(G)$.
::: {.proof}
Associativity follows from associativity of the group multiplication together with naturality and associativity of the homology cross product:
$$
m\circ(m\times\operatorname{id})=m\circ(\operatorname{id}\times m).
$$
The inclusion of the identity element is a two-sided unit for $m$, so its degree-zero homology class is a two-sided unit for $\star$.
:::

<1>3. The topological group $G$ acts on itself by left translations
$$
L_g(x)=gx,
$$
and hence acts on homology by
$$
g\cdot a=(L_g)_*(a).
$$
::: {.proof}
Since $L_{gh}=L_g\circ L_h$ and $L_e=\operatorname{id}$, functoriality of homology gives a genuine group action on $H_*(G)$.
:::

<1>4. If $g$ and $h$ lie in the same path component of $G$, then $(L_g)_*=(L_h)_*$.
::: {.proof}
Choose a path $\gamma:I\to G$ from $g$ to $h$. Then
$$
H(x,t)=\gamma(t)x
$$
defines a homotopy from $L_g$ to $L_h$. Homotopic maps induce the same map on homology.
:::

<1>5. Thus the action factors through the component group $\pi_0(G)$; if $G$ is path-connected, the action is trivial.
::: {.proof}
By <1>4 the action depends only on the path component of $g$, so it factors through $G\to\pi_0(G)$. If $G$ is path-connected, every $g$ lies in the component of $e$, so $(L_g)_*=(L_e)_*=\operatorname{id}$.
:::
:::
