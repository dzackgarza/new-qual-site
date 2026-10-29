---
schema: qual/card@1
id: E-HAT-2.2-42
kind: problem
title: Finite group of homeomorphisms of graph injects into $GL_n(\ZZ)$ acting on $H_1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Graphs
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be a finite connected graph having no vertex that is the endpoint of just one edge, and suppose that $H_1(X; \ZZ)$ is free abelian of rank $n > 1$, so the group of automorphisms of $H_1(X; \ZZ)$ is $GL_n(\ZZ)$, the group of invertible $n \times n$ matrices with integer entries whose inverse matrix also has integer entries.
Show that if $G$ is a finite group of homeomorphisms of $X$, then the homomorphism $G \to GL_n(\ZZ)$ assigning to $g: X \to X$ the induced homomorphism $g_*: H_1(X; \ZZ) \to H_1(X; \ZZ)$ is injective.
Show the same result holds if the coefficient group $\ZZ$ is replaced by $\ZZ_m$ with $m > 2$.
What goes wrong when $m = 2$?
:::

::: {.solution}
Throughout, $R$ denotes $\ZZ$ or $\ZZ_m$ with $m > 2$; the only property of $R$ used is $2 \neq 0$ in $R$.
A *circle* in $X$ is a subgraph homeomorphic to $S^1$, and a *bridge* is an edge whose removal (keeping its endpoints) disconnects $X$.
For a homeomorphism $g$ of $X$, write $g_\#$ for the induced map on cellular chains.

::: pf

::: {.pf-step #graph}
$X$ has a graph structure whose vertex set $V$ is nonempty, in which every vertex has valence at least $3$, and which every homeomorphism of $X$ preserves: it permutes $V$ and permutes the edges.

::: pf-proof
Let $V$ be the set of points of $X$ having no open neighbourhood homeomorphic to $\RR$.
In the given structure a point interior to an edge, or a vertex of valence $2$, has such a neighbourhood, while a vertex of valence $k \ge 3$ does not, since deleting it disconnects every small connected neighbourhood into at least $3$ components, whereas deleting a point of an interval leaves $2$.
There are no vertices of valence $1$ by hypothesis, and none of valence $0$ because $X$ is connected with $n > 1$.
So $V$ is the set of vertices of valence at least $3$.
If $V$ were empty, $X$ would be a compact connected $1$-manifold, hence a circle, with $H_1 \cong \ZZ$, contradicting $n > 1$.
Each component of $X \setminus V$ is a union of open edges and valence-$2$ vertices; it is not a circle, since a circle component would be both open and compact, hence a component of $X$, contradicting $V \ne \emptyset$.
So each component of $X \setminus V$ is an open arc whose closure adds endpoints in $V$, and these arcs are the edges of a graph structure on $X$ with vertex set $V$.
A homeomorphism preserves $V$, because $V$ is defined topologically, and therefore permutes the components of $X \setminus V$, which are the edges.
:::

:::

::: {.pf-step #chains}
For a homeomorphism $g$ of $X$, $H_1(X; R)$ is the group $Z_1$ of cellular $1$-cycles with coefficients in $R$, and $g_*$ is the restriction of $g_\#$, which sends each oriented edge $e$ to $\pm g(e)$, with sign $+$ exactly when $g$ carries the orientation of $e$ to that of $g(e)$.

::: pf-proof
Use the structure of step [](#graph){.pf-ref}.
The cellular chain complex is $0 \to C_1 \to C_0 \to 0$ with no $2$-cells, so $H_1(X;R) = \ker \partial = Z_1$.
By step [](#graph){.pf-ref}, $g$ is a cellular map carrying each closed edge homeomorphically onto a closed edge, so the cellular chain map has the stated form, and cellular homology computes $g_*$ by naturality.
:::

:::

::: {.pf-step #circles}
If $g_* = \id$ on $H_1(X;R)$, then $g$ maps every circle $C$ onto itself, preserving its orientation.

::: pf-proof
Orient $C$ and let $z_C \in Z_1$ be the sum of the edges of $C$, each with sign $\pm 1$ according to whether its orientation agrees with that of $C$.
By step [](#chains){.pf-ref}, $g_\# z_C = \pm z_{g(C)}$, with sign $+$ exactly when $g \colon C \to g(C)$ preserves orientation.
Since $g_\# z_C = z_C$ and the coefficients $\pm 1$ are nonzero in $R$, the supports agree, so $g(C) = C$.
If $g$ reversed the orientation of $C$, then $z_C = -z_C$, so $2 z_C = 0$, which is false because $2 \neq 0$ in $R$.
:::

:::

::: {.pf-step #tree}
A finite connected graph with at least one edge, in which at most one vertex has valence at most $1$, contains a circle.

::: pf-proof
A loop is a circle, and two edges with the same endpoints form a circle.
Otherwise a graph without circles is a tree, and a finite tree with at least one edge has at least two vertices of valence $1$.
:::

:::

::: {.pf-step #bridges}
If $g$ maps every circle onto itself, then $g$ maps every bridge $f$ onto itself and fixes both of its endpoints.

::: pf-proof

::: {.pf-step #bridge-sides}
Each component of $X \setminus \operatorname{int} f$ contains a circle.

::: pf-proof
Let $K$ be a component and $w$ the endpoint of $f$ in $K$.
Every vertex of $K$ other than $w$ has valence at least $3$ in $K$, and $w$ has valence at least $2$ in $K$ by step [](#graph){.pf-ref}; in particular $K$ has an edge.
Step [](#tree){.pf-ref} gives a circle in $K$.
:::

:::

::: {.pf-step #partition}
Distinct bridges $f \neq f'$ induce distinct unordered partitions of the set of circles by the components of $X \setminus \operatorname{int} f$ and of $X \setminus \operatorname{int} f'$.

::: pf-proof
Let $K_1, K_2$ be the components of $X \setminus \operatorname{int} f$, with $f' \subset K_2$.
Removing $\operatorname{int} f'$ splits $K_2$ into a part $M$ containing the endpoint $w_2$ of $f$ and a part $N$; the components of $X \setminus \operatorname{int} f'$ are $K_1 \cup f \cup M$ and $N$.
The partitions are $\{\mathrm{Circ}(K_1), \mathrm{Circ}(M) \cup \mathrm{Circ}(N)\}$ and $\{\mathrm{Circ}(K_1) \cup \mathrm{Circ}(M), \mathrm{Circ}(N)\}$, where $\mathrm{Circ}$ is the set of circles in a subgraph.
By step [](#bridge-sides){.pf-ref}, $\mathrm{Circ}(K_1)$ and $\mathrm{Circ}(N)$ are nonempty and disjoint, so the partitions agree only if $\mathrm{Circ}(M) = \emptyset$.
But in $M$ every vertex has valence at least $3$, except the endpoints of $f$ and $f'$ lying in $M$, which lose one edge each.
If these endpoints are distinct, $M$ has an edge and no vertex of valence at most $1$; if they coincide, at most one vertex has valence at most $1$, and $M$ has an edge since that vertex has valence at least $3$ in $X$.
Step [](#tree){.pf-ref} gives a circle in $M$, so the partitions differ.
:::

:::

::: pf-step
$g(f) = f$, and $g$ fixes both endpoints of $f$.

::: pf-proof
The edge $g(f)$ is a bridge, and its partition of the circles is the image under $g$ of the partition of $f$.
Since $g$ fixes every circle, the two partitions coincide, so $g(f) = f$ by step [](#partition){.pf-ref}.
The homeomorphism $g$ permutes the components $K_1, K_2$ of $X \setminus \operatorname{int} f$; $K_1$ contains a circle by step [](#bridge-sides){.pf-ref}, which $g$ fixes, so $g(K_1) = K_1$ and $g$ fixes the endpoint of $f$ in $K_1$, and likewise the one in $K_2$.
:::

:::

:::

:::

::: {.pf-step #circle-vertices}
If $g$ maps every circle onto itself preserving its orientation, then $g$ fixes every vertex and every edge of every circle, preserving the orientation of each edge.

::: pf-proof

::: {.pf-step #fixed-vertex}
Every circle $C$ contains a vertex fixed by $g$.

::: pf-proof
Choose a vertex $w$ of $C$; by step [](#graph){.pf-ref} it has valence at least $3$, so some edge $f$ at $w$ is not in $C$.
If $f$ is a bridge, $g(w) = w$ by step [](#bridges){.pf-ref}.
Otherwise $f$ lies on a circle $C''$: remove $\operatorname{int} f$, join the endpoints of $f$ by a path in the remaining connected graph, and add $f$.
Traverse $C''$ from $w$ along $f$ until the first vertex $q$ of $C$.
If $q = w$, then $C \cap C'' = \{w\}$; both circles are $g$-invariant, so $g(w) = w$.
If $q \neq w$, the traversed path $P$ meets $C$ only in $w$ and $q$.
Let $A$ be one of the two arcs of $C$ from $w$ to $q$; then $D = P \cup A$ is a circle with $C \cap D = A$.
Both $C$ and $D$ are $g$-invariant, so $g(A) = A$.
Since $g$ preserves the orientation of $C$, it maps the arc $A$ to itself preserving the orientation $A$ inherits from $C$, so it fixes the initial point $w$ of $A$.
:::

:::

::: pf-step
$g$ fixes every vertex and every edge of $C$, preserving edge orientations.

::: pf-proof
List the vertices of $C$ in cyclic order as $v_0, \dots, v_{L-1}$ with $v_0$ fixed by step [](#fixed-vertex){.pf-ref}.
An orientation-preserving cellular homeomorphism of $C$ sends $v_i$ to $v_{i+k}$ (indices mod $L$) for a fixed $k$, and $g(v_0) = v_0$ forces $k = 0$.
Each edge from $v_i$ to $v_{i+1}$ along the orientation therefore goes to itself, with orientation preserved.
:::

:::

:::

:::

::: {.pf-step #identity}
If $g$ has finite order and $g_* = \id$ on $H_1(X; R)$, then $g = \id_X$.

::: pf-proof

::: pf-step
$g$ fixes every vertex and maps every edge to itself preserving its orientation.

::: pf-proof
Every edge $e$ is a bridge or lies on a circle: if $e$ is not a bridge, a path joining its endpoints in $X \setminus \operatorname{int} e$ together with $e$ is a circle.
Steps [](#circles){.pf-ref}, [](#bridges){.pf-ref} and [](#circle-vertices){.pf-ref} give the claim for the edges, and every vertex is an endpoint of an edge.
:::

:::

::: pf-step
$g = \id_X$.

::: pf-proof
Let $e$ be an edge with characteristic map $\varphi \colon [0,1] \to \overline{e}$, a homeomorphism from $(0,1)$ onto the open edge.
Then $h = \varphi^{-1} g \varphi$ is a homeomorphism of $(0,1)$, increasing because $g$ preserves the orientation of $e$, and $h^k = \id$ where $k$ is the order of $g$.
If $h(t) > t$ for some $t$, then applying the increasing map $h$ repeatedly gives $h^k(t) > \dots > h(t) > t$, a contradiction; likewise $h(t) < t$ is impossible.
So $h = \id$, and $g$ is the identity on every edge and every vertex.
:::

:::

:::

:::

::: pf-step
The homomorphisms $G \to GL_n(\ZZ)$ and $G \to \operatorname{Aut} H_1(X;\ZZ_m)$ for $m > 2$ are injective.

::: pf-proof
Every element of the finite group $G$ has finite order, so step [](#identity){.pf-ref} with $R = \ZZ$ and with $R = \ZZ_m$ shows that the kernel is trivial.
:::

:::

::: pf-step
For $m = 2$ the homomorphism $G \to GL_n(\ZZ_2)$ can fail to be injective, because a homeomorphism can reverse the orientation of every circle it preserves and $-1 = 1$ in $\ZZ_2$, so step [](#circles){.pf-ref} fails.

::: pf-proof
Let $X \subset \RR^2$ be the unit circle together with the segment $[-1,1] \times \{0\}$: a theta graph with vertices $(\pm 1, 0)$ and three edges, so $n = 3 - 2 + 1 = 2$, and no vertex has valence $1$.
Let $g(x,y) = (-x,y)$ and $G = \{\id, g\}$.
Orient each edge from $(-1,0)$ to $(1,0)$; $g$ maps each edge to itself reversing its orientation, so $g_\# = -\id$ on $C_1$ and $g_* = -\id$ on $H_1(X;\ZZ) \cong \ZZ^2$.
On $H_1(X;\ZZ_2) = Z_1(X;\ZZ_2)$, $g_* = -\id = \id$, although $g \neq \id$.
:::

:::

:::

:::
