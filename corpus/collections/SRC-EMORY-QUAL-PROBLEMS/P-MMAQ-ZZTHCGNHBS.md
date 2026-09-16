---
schema: qual/card@1
id: P-MMAQ-ZZTHCGNHBS
kind: problem
title: Classification of groups of orders $15$ and $30$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both complete classification requests with Groups 7 on PDF page 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the Sylow proof at order 15, the regular-action sign character giving the normal subgroup of index two, all four conjugation actions, and the distinct center orders."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Groups (7) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAG7, whose solution repeats this semidirect-product classification."
---

::: {.problem}
Classify all groups of order $15$ and of order $30$.
:::

::: {.solution}
The only group of order $15$ is $C_{15}$. The groups
of order $30$, up to isomorphism, are
$$
C_{30},\qquad C_3\times D_{10},\qquad
C_5\times D_6,\qquad D_{30},
$$
where $D_{2m}$ denotes the dihedral group of order $2m$.

<1>1. Every group of order $15$ is cyclic.

::: {.proof}
Sylow's theorems give $n_5\mid3$, $n_5\equiv1\pmod5$,
and $n_3\mid5$, $n_3\equiv1\pmod3$ [@DF04].
Thus $n_5=n_3=1$. The respective Sylow subgroups
$Q,P$ are normal and have trivial intersection.
Their commutators lie in that intersection, so they
commute elementwise. Multiplication $P\times Q\to G$
is an injective homomorphism: $xy=1$ forces
$x=y^{-1}\in P\cap Q$. Both sides have order $15$,
so it is an isomorphism. Each prime-order factor is
cyclic, and a pair of generators has order $15$.
:::

<1>2. Every group $G$ of order $30$ is a semidirect
product $C_{15}\rtimes C_2$.

::: {.proof}
Let $\lambda:G\to\operatorname{Sym}(G)$ be the action
by left multiplication and put
$\varepsilon=\operatorname{sgn}\circ\lambda:G\to\{1,-1\}$.
This is a homomorphism [@DF04]. Cauchy's theorem
provides $t\in G$ of order two. Left multiplication
by $t$ has no fixed point, since $tx=x$ would imply
$t=1$. Thus its cycle decomposition consists of
fifteen transpositions and $\varepsilon(t)=(-1)^{15}=-1$.
The sign character is onto, so its kernel $N$ is
normal of order $15$. Step <1>1 makes $N$ cyclic.

Since $t\notin N$ and $[G:N]=2$, every element has
a unique form $a^i t^e$, where $a$ generates $N$,
$i\in\mathbb Z/15\mathbb Z$, and $e\in\{0,1\}$.
This is the asserted semidirect product.
:::

<1>3. Exactly four conjugation actions can occur.

::: {.proof}
Write $tat^{-1}=a^u$ for a unit $u$ modulo $15$.
The equation $t^2=1$ forces $u^2\equiv1\pmod{15}$.
Modulo each of $3$ and $5$, the product
$(u-1)(u+1)$ vanishes in a field, so $u=1$ or $-1$.
The Chinese remainder theorem gives exactly four
solutions modulo $15$, namely $u=1,4,11,14$ [@DF04].

The multiplication in the coordinates of step <1>2 is
$$
(i,e)(j,f)=(i+u^e j,e+f),
$$
with the coordinates reduced modulo $15$ and $2$.
For each of the four values this defines a group:
associativity follows from $u^{e+f}=u^e u^f$,
the identity is $(0,0)$, and the inverse of $(i,e)$
is $(-u^{-e}i,-e)$. Hence each action exists and
determines the group up to isomorphism.

Under $C_{15}\cong C_3\times C_5$, the respective
actions are trivial on both factors, inversion on
the $C_5$ factor only, inversion on the $C_3$ factor
only, and inversion on both. These give the four
groups displayed at the start, in the same order.
:::

<1>4. The four groups of order $30$ are pairwise nonisomorphic.

::: {.proof}
For $u=1$ the group is abelian and its center has
order $30$. For $u\ne1$, every element outside $N$
acts on $N$ by the same nontrivial automorphism
$a\mapsto a^u$, so none is central. An element
$a^i\in N$ is central exactly when it commutes with
$t$, equivalently $(u-1)i\equiv0\pmod{15}$.

For $u=4$, this holds precisely when $5\mid i$,
giving center order three. For $u=11$, it holds
precisely when $3\mid i$, giving center order five.
For $u=14$, the integer $13$ is coprime to $15$,
so only $i=0$ qualifies, giving center order one.
The distinct center orders $30,3,5,1$ distinguish
all four groups. Steps <1>1–<1>3 prove exhaustiveness.
:::
:::
