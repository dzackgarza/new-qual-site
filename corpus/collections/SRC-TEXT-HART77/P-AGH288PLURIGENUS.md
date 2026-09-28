---
schema: qual/card@1
id: P-AGH288PLURIGENUS
kind: problem
title: Plurigenera and regular differential forms are birational invariants
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plurigenera
  - Hodge Numbers
  - Birational Invariance
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the plurigenus and h^{q,0} definitions and the requested birational invariance with the retained Hartshorne II.8.8 transcription. Checked extension across codimension two against Stacks Project Tag 0AVB. The proof extends rational maps at all codimension-one points and constructs inverse pullbacks on regular tensor forms without using resolution of singularities.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed and let $X$ be a projective nonsingular variety over $k$.
For any $n > 0$ define the **$n$th plurigenus of $X$** to be
$$
P_n = \dim_k \Gamma(X, \omega_X^{\tensor n})
.
$$
Thus in particular $P_1 = p_g$.
Also, for any $q$ with $0 \leq q \leq \dim X$, define an integer
$$
h^{q, 0} = \dim_k \Gamma(X, \Omega^q_{X/k})
\quad\text{where}\quad
\Omega^q_{X/k} = \bigwedge\nolimits^q \Omega_{X/k}
$$
is the sheaf of regular $q\dash$forms on $X$.
In particular, for $q = \dim X$ we recover the geometric genus.
The integers $h^{q,0}$ are called **Hodge numbers**.

Using the method of (8.19), show that $P_n$ and $h^{q,0}$ are birational invariants of $X$: if $X$ and $X'$ are birationally equivalent nonsingular projective varieties, then $P_n(X) = P_n(X')$ and $h^{q,0}(X) = h^{q,0}(X')$.
:::

::: {.solution}
Let $d=\dim X=\dim X'$ and let $f:X\dashrightarrow X'$ be a birational map with rational inverse $g$.
For $0\le q\le d$ and $m\ge1$, put
$$
\mathcal T_{q,m}(X)\coloneqq(\Omega^q_{X/k})^{\otimes m},
\qquad \Omega^q_{X/k}=\bigwedge^q\Omega_{X/k}.
$$
These are locally free coherent sheaves, since the varieties are nonsingular over the perfect field $k$.
The case $q=0$ uses $\Omega^0_{X/k}=\OO_X$.

<1>1. The map $f$ is represented by a morphism $f_U:U\to X'$ on an open subset $U\subseteq X$ containing every point of codimension at most one.

::: {.proof}
Fix a projective embedding $X'\hookrightarrow\PP_k^N$.
At the generic point of $X$, the rational map is represented by homogeneous coordinates $[a_0:\cdots:a_N]$ with $a_i\in K(X)$, not all zero.
Let $x$ be a codimension-one point of $X$.
The local ring $R=\OO_{X,x}$ is a DVR, with uniformizer $t$, because $X$ is regular.
Let $e$ be the minimum of the valuations of the nonzero $a_i$.
Then $t^{-e}a_i\in R$ for all $i$, and at least one of them is a unit of $R$.

These finitely many rational functions are regular on a neighborhood of $x$; after shrinking, the chosen unit is invertible there.
They define a morphism from that neighborhood to $\PP^N$.
Every homogeneous equation of $X'$ vanishes on these coordinates in the function field, and hence vanishes as a regular function on that neighborhood, since $X$ is integral.
The morphism therefore factors through $X'$ and represents $f$.
This proves that $f$ extends near every codimension-one point, as well as on its original domain containing the generic point.

Any two such local extensions agree on their overlap: they agree generically, the overlap is reduced, and $X'$ is separated, so the dense-open uniqueness result [[P-AGH242AGREEDENSE]] applies.
They glue on the union $U$ of their domains.
The closed complement contains no point of codimension zero or one, as required.
This is the codimension-one extension step in the method of [@Har10a, Theorem II.8.19].
:::

<1>2. If $W$ is a normal integral noetherian scheme, $V\subseteq W$ is open with complement of codimension at least two, and $\mathcal E$ is locally free of finite rank, then restriction is an isomorphism
$$
\Gamma(W,\mathcal E)\xrightarrow{\cong}\Gamma(V,\mathcal E|_V).
$$

::: {.proof}
Sections of a locally free sheaf on an integral scheme inject into its generic stalk, as is seen by expressing them in a local frame.
Thus restriction is injective.
Take a section on $V$ and regard it as an element of that generic stalk.
On any affine open $W_0=\Spec A$ with $\mathcal E|_{W_0}\cong\OO_{W_0}^{\oplus r}$, write its generic value as a vector in $\operatorname{Frac}(A)^r$.
Every height-one point of $W_0$ belongs to $V$, so all coordinates belong to $A_{\mathfrak p}$ for every height-one prime $\mathfrak p$ of $A$.
The [codimension-one intersection property for a normal domain](https://stacks.math.columbia.edu/tag/0AVB), applied to the rank-one free module, says
$$
A=\bigcap_{\operatorname{height}(\mathfrak p)=1}A_{\mathfrak p}
\quad\text{inside }\operatorname{Frac}(A).
$$
Hence these coordinates belong to $A$, giving a section on $W_0$.
If $A$ has dimension zero, it is a field and the same assertion is immediate.
The local extensions agree because their generic values agree and the sheaf is locally free.
They glue to a section on $W$, and its restriction is the given section by the same generic-value argument.
This proves surjectivity and uniqueness.
:::

<1>3. The birational map induces a $k$-linear map
$$
f^*:\Gamma(X',\mathcal T_{q,m}(X'))
\longrightarrow\Gamma(X,\mathcal T_{q,m}(X))
$$
for every $q,m$ in the stated ranges.

::: {.proof}
On the open $U$ from step <1>1, functoriality of [[D-4GCH6|Kähler differentials]] gives
$$
f_U^*\Omega_{X'/k}\longrightarrow\Omega_{U/k}.
$$
Taking the $q$th exterior power and then the $m$th tensor power gives
$$
f_U^*\mathcal T_{q,m}(X')\longrightarrow\mathcal T_{q,m}(U).
$$
Pullback commutes with these operations by [[P-AGH2516TENSOROPS]], part (e).
For $q=0$ the map is the ordinary structure-sheaf pullback.
Thus a global section on $X'$ pulls back to a regular tensor form on $U$.
Step <1>2 extends it uniquely over $X$.
Both operations are $k$-linear, giving the displayed map.

The result is independent of the chosen representative domain for $f$: on any two domains the constructions have the same generic value, and regular tensor forms are determined by that value.
At the generic points this map is exactly the map on tensor powers of exterior differentials induced by the field isomorphism $K(X')\xrightarrow{f^*}K(X)$.
:::

<1>4. The pullbacks associated to $f$ and $g$ are mutual inverses.

::: {.proof}
Step <1>3 applies also to $g:X'\dashrightarrow X$ because $X$ is projective and $X'$ is nonsingular.
On the function fields, the two homomorphisms are inverse.
The induced maps on differentials, exterior powers and tensor powers are consequently inverse there, by functoriality.
Hence the composites on global sections agree with the identity at the generic point.
Since each sheaf $\mathcal T_{q,m}$ is locally free on an integral scheme, equality at the generic point is equality of its global sections, as in step <1>2.
The composites are therefore the identity, giving
$$
\Gamma(X,\mathcal T_{q,m}(X))\cong
\Gamma(X',\mathcal T_{q,m}(X')).
$$
This proof uses neither resolution of indeterminacy nor a factorization into blowups, and it imposes no characteristic-zero hypothesis.
:::

<1>5. The required invariants agree:
$$
\boxed{P_n(X)=P_n(X')\ (n\ge1),\qquad
h^{q,0}(X)=h^{q,0}(X')\ (0\le q\le d).}
$$

::: {.proof}
The sheaves in question are coherent on projective schemes, so their spaces of global sections are finite-dimensional [@Har10a, Theorem III.5.2].
For $q=d$, the sheaf $\Omega^d_{X/k}$ is $\omega_X$, so step <1>4 with $m=n$ identifies the spaces defining $P_n$.
With $m=1$, the same step identifies the spaces defining $h^{q,0}$ for each $q$.
Taking dimensions proves both equalities and includes $P_1=p_g$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 construct the inverse pullbacks on regular tensor forms, and step <1>5 gives the two families of birational invariants requested in the statement.
:::
:::
