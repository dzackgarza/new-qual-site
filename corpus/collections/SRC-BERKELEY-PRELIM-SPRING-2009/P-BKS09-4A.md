---
schema: qual/card@1
id: P-BKS09-4A
kind: problem
title: Counting commuting tuples in a finite group via conjugation orbits
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed the Burnside-lemma argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the conjugation action and the fixed-point count identifying commuting (n+1)-tuples.
---

::: {.problem}
Let G be a finite group, and for each positive integer n, let

$$
X _ { n } = \{ ( g _ { 1 } , . . . , g _ { n } ) : g _ { i } g _ { j } = g _ { j } g _ { i } \forall i , j \} .
$$

Show that the formula

$$
h \cdot ( g _ { 1 } , \ldots , g _ { n } ) = ( h g _ { 1 } h ^ { - 1 } , \ldots , h g _ { n } h ^ { - 1 } ) ,
$$

defines an action of $G$ on $X _ { n }$ , and that $| X _ { n + 1 } | = | G | \cdot | X _ { n } / G |$ for all n, where $X _ { n } / G$ denotes the set of G-orbits in $X _ { n }$
:::

::: {.solution}
For $h\in G$, write
$$
X_n^h\coloneqq
\{x\in X_n:h\cdot x=x\}
$$
for the fixed-point set of $h$.

<1>1. Simultaneous conjugation preserves $X_n$.

::: {.proof}
Let $(g_1,\ldots,g_n)\in X_n$ and $h\in G$. For every $i,j$,
$$
\begin{aligned}
(hg_ih^{-1})(hg_jh^{-1})
&=h(g_ig_j)h^{-1}\\
&=h(g_jg_i)h^{-1}\\
&=(hg_jh^{-1})(hg_ih^{-1}).
\end{aligned}
$$
Thus the conjugated tuple again has pairwise commuting coordinates and lies
in $X_n$.
:::

<1>2. The displayed formula defines an action of $G$ on $X_n$.

::: {.proof}
Step <1>1 shows that the formula is well-defined on $X_n$. The identity
element acts trivially. For $h,k\in G$ and $(g_1,\ldots,g_n)\in X_n$,
coordinatewise conjugation gives
$$
h\cdot\bigl(k\cdot(g_1,\ldots,g_n)\bigr)
=
(hk)\cdot(g_1,\ldots,g_n).
$$
These are precisely the two action axioms.
:::

<1>3. For each $h\in G$, the elements of $X_n^h$ are exactly the pairwise
commuting $n$-tuples whose entries all commute with $h$.

::: {.proof}
For $(g_1,\ldots,g_n)\in X_n$,
$$
h\cdot(g_1,\ldots,g_n)=(g_1,\ldots,g_n)
$$
if and only if
$$
hg_ih^{-1}=g_i
$$
for every $i$, equivalently $hg_i=g_ih$ for every $i$.
:::

<1>4. One has
$$
\abs{X_{n+1}}
=
\sum_{h\in G}\abs{X_n^h}.
$$

::: {.proof}
Partition $X_{n+1}$ according to its last coordinate $h$. For fixed
$h\in G$, a tuple
$$
(g_1,\ldots,g_n,h)
$$
belongs to $X_{n+1}$ exactly when $(g_1,\ldots,g_n)\in X_n$ and every
$g_i$ commutes with $h$. By step <1>3, the possible first $n$ coordinates
are exactly the elements of $X_n^h$. Thus the fiber with last coordinate
$h$ has cardinality $\abs{X_n^h}$, and summing over $h$ gives the formula.
:::

<1>5. One has
$$
\abs{X_{n+1}}
=
\boxed{\abs G\,\abs{X_n/G}}.
$$

::: {.proof}
Burnside's lemma applied to the action in step <1>2 gives
$$
\abs{X_n/G}
=
\frac{1}{\abs G}
\sum_{h\in G}\abs{X_n^h}.
$$
Multiplying by $\abs G$ and applying step <1>4 yields the stated identity.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves the action assertion, and step <1>5 proves the required
counting identity.
:::
:::
