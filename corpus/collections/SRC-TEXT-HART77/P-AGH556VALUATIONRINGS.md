---
schema: qual/card@1
id: P-AGH556VALUATIONRINGS
kind: problem
title: Classification of valuation rings of the function field of a surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Hartshorne V.5.6 as transcribed here, the retained Andrew Egbert
    companion argument, II.4.12 and its corrected solution, the valuation
    center criterion II.4.5, and V.5.1 on resolving a rational function by
    point blowups. The retained companion identifies the successive-center
    trichotomy but does not prove the hint's decisive assertion in case (3).
    The proof below supplies it: for f in R, resolve [f:1] by finitely many
    point blowups. Blowups away from the center of R are local
    isomorphisms, while a blowup at that center is exactly the next member
    of the valuation's center sequence. Thus some O_{X_i,x_i} is the local
    ring at the center on the resolved model. Since f lies in R, the induced
    Spec R -> P^1 lands in A^1, so f is regular at that center. Hence every
    f in R lies in the union R_0, proving R=R_0.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the complete trichotomy against II.4.12, the proper-center
    criterion, and V.5.1. Checked that a codimension-one center forces
    equality with the corresponding DVR, while a closed center lifts to the
    exceptional curve after each blowup and either becomes divisorial
    (type 2) or yields the infinite type-3 chain. In the infinite case,
    checked the local comparison with an arbitrary finite point-blowup
    resolution of [f:1]: off-center blowups leave the center local ring
    unchanged, on-center blowups advance exactly one A_i, and f in R gives
    an extension Spec R -> A^1 whose uniqueness inside P^1 forces f to be
    regular at the resolved center. Thus f lies in every A_i for i
    sufficiently large, so R=union A_i.
---

::: {.problem}
Let $X$ be a surface with function field $K$.
Show that every valuation ring $R$ of $K / k$ is one of the three kinds described in (II, Ex.
4.12).

Hint: In case (3), let $f \in R$.
Use (Ex.
5.1) to show that for all $i \gg 0$, $f \in \mathcal{O}_{X_i}$, so in fact $f \in R_0$.
:::

::: {.solution}
Under the standing hypotheses of Chapter V, $X$ is a nonsingular projective
surface over the algebraically closed field $k$. Put
$$
K=k(X).
$$

Exercise II.4.12 explicitly excludes the trivial valuation ring $K$ itself
from its three surface types. We therefore prove the assertion for
$$
R\subsetneq K;
$$
the ring $K$ is the separate trivial case.

<1>1. The valuation ring $R$ has a unique center
$$
x_0\in X.
$$

::: {.proof}
Since $X$ is projective, it is proper over $k$. The valuation-center
criterion [[P-AGH245VALCENTER|Exercise II.4.5]] says that every valuation
ring of $K/k$ has a unique center on a proper model. Equivalently, the
generic-point map
$$
\Spec K\longrightarrow X
$$
extends uniquely to
$$
\Spec R\longrightarrow X,
$$
and the image of the closed point is $x_0$.
:::

<1>2. The center $x_0$ is not the generic point of $X$.

::: {.proof}
If $x_0=\eta_X$, then domination gives
$$
\OO_{X,\eta_X}=K\subseteq R.
$$
Since already $R\subseteq K$, this would force
$$
R=K,
$$
contrary to the nontriviality assumption.
:::

Because $\dim X=2$, step <1>2 leaves two possibilities: $x_0$ is the
generic point of an irreducible curve, or $x_0$ is a closed point.

<1>3. If $x_0$ has codimension one, then
$$
\boxed{R=\OO_{X,x_0},}
$$
so $R$ is of type (1) in Exercise II.4.12.

::: {.proof}
Since $X$ is nonsingular and $x_0$ has codimension one,
$$
\OO_{X,x_0}
$$
is a one-dimensional regular local domain, hence a discrete valuation ring
with fraction field $K$.

The assertion that $x_0$ is the center means precisely that $R$ dominates
$\OO_{X,x_0}$. A valuation ring dominating another valuation ring of the
same fraction field is equal to it [[P-AGH2412VALEX]]. Hence
$$
R=\OO_{X,x_0}.
$$
This is the first surface construction in Exercise II.4.12.
:::

Assume from now on that $x_0$ is closed.

<1>4. As long as the center $x_i$ of $R$ on $X_i$ is closed, define
$$
X_{i+1}=\Bl_{x_i}X_i.
$$
Then $R$ has a unique center
$$
x_{i+1}\in X_{i+1},
$$
and
$$
\boxed{x_{i+1}\in E_{i+1},}
$$
where $E_{i+1}$ is the exceptional curve of
$$
X_{i+1}\longrightarrow X_i.
$$

::: {.proof}
The blowup of a nonsingular projective surface at a closed point is again a
nonsingular projective surface. Hence step <1>1 applies to every $X_i$ and
gives a unique center $x_{i+1}$ on $X_{i+1}$.

The morphism
$$
X_{i+1}\longrightarrow X_i
$$
is proper and the induced maps
$$
\Spec R\longrightarrow X_{i+1}\longrightarrow X_i
$$
and
$$
\Spec R\longrightarrow X_i
$$
agree on the generic point. By uniqueness of the center on $X_i$, the
closed point $x_{i+1}$ maps to $x_i$. Therefore
$$
x_{i+1}\in\pi_{i+1}^{-1}(x_i)=E_{i+1}.
$$
:::

<1>5. If for some $n\ge1$ the center $x_n$ is the generic point of
$E_n$, then
$$
\boxed{R=\OO_{X_n,x_n},}
$$
and $R$ is of type (2) in Exercise II.4.12.

::: {.proof}
The surface $X_n$ is nonsingular, so the local ring at the generic point of
the irreducible curve $E_n$ is a DVR:
$$
\OO_{X_n,x_n}.
$$
The valuation ring $R$ dominates this DVR because $x_n$ is its center.
As in step <1>3, domination between valuation rings of the same fraction
field forces equality.

The composite birational morphism
$$
X_n\longrightarrow X
$$
maps the exceptional curve $E_n$ to the original closed point $x_0$.
Thus $R$ is exactly the local ring at the generic point of a curve on a
birational model which is contracted to a closed point of $X$, the second
construction of Exercise II.4.12.
:::

<1>6. If no center ever becomes divisorial, then every $x_i$ is closed and
the construction gives an infinite chain
$$
X=X_0
\longleftarrow
X_1
\longleftarrow
X_2
\longleftarrow
\cdots
$$
of blowups at the successive centers of $R$. Put
$$
A_i=\OO_{X_i,x_i},
\qquad
R_0=\bigcup_{i\ge0}A_i.
$$
Then
$$
\boxed{R_0\subseteq R.}
$$

::: {.proof}
By definition of center, $R$ dominates every $A_i$, so
$$
A_i\subseteq R
$$
for all $i$. Hence their union is contained in $R$.

Moreover the transition maps are local inclusions
$$
A_i\hookrightarrow A_{i+1},
$$
because $x_{i+1}$ lies above $x_i$. Thus this is precisely the third
construction of Exercise II.4.12, except that it remains to prove the
assertion promised there:
$$
R_0=R.
$$
:::

<1>7. Let
$$
f\in R.
$$
There is an index $N$ such that, for every $i\ge N$,
$$
\boxed{f\in A_i=\OO_{X_i,x_i}.}
$$

::: {.proof}
The case $f=0$ is immediate, so assume
$$
f\in K^\times.
$$
Regard $f$ as the rational map
$$
\varphi_f:X\dashrightarrow\PP^1,
\qquad
x\longmapsto[f(x):1].
$$
Exercise V.5.1 [[P-AGH551RESOLVERATFN]] gives a finite sequence of point
blowups
$$
Y_m
\xrightarrow{g_m}
Y_{m-1}
\longrightarrow
\cdots
\longrightarrow
Y_1
\xrightarrow{g_1}
Y_0=X
$$
such that $\varphi_f$ extends to a morphism
$$
\psi:Y_m\longrightarrow\PP^1.
$$

For each $j$, let $y_j$ be the unique center of $R$ on $Y_j$. We compare the
local rings at these centers with the sequence
$$
A_0\subset A_1\subset A_2\subset\cdots.
$$

Suppose the point blown up by
$$
g_j:Y_j\longrightarrow Y_{j-1}
$$
is not $y_{j-1}$. Then $g_j$ is an isomorphism on a neighbourhood of
$y_{j-1}$, and therefore
$$
\OO_{Y_j,y_j}\cong\OO_{Y_{j-1},y_{j-1}}.
$$

Suppose instead that $g_j$ blows up $y_{j-1}$. Under any identification
$$
\OO_{Y_{j-1},y_{j-1}}\cong A_i
$$
already obtained, this is the blowup at the center $x_i$ of $R$. The center
$y_j$ selected by $R$ on that blowup is therefore the same infinitely near
point as $x_{i+1}$, and
$$
\OO_{Y_j,y_j}\cong A_{i+1}.
$$

Starting from
$$
\OO_{Y_0,y_0}=\OO_{X,x_0}=A_0
$$
and proceeding through the finite sequence of blowups, we obtain some
$N\le m$ with
$$
\OO_{Y_m,y_m}\cong A_N
$$
inside the common function field $K$.

It remains to see that $f$ is regular at $y_m$. Because
$$
f\in R,
$$
the $k$-algebra map
$$
k[t]\longrightarrow R,
\qquad
t\longmapsto f,
$$
defines a morphism
$$
\Spec R\longrightarrow\AA^1\subset\PP^1
$$
whose restriction to $\Spec K$ is the rational map $[f:1]$.

On the other hand, the center morphism
$$
\Spec R\longrightarrow Y_m
$$
followed by $\psi$ gives another extension to $\PP^1$ of the same
generic-point map. Since $\PP^1$ is separated, the two extensions agree.
Consequently
$$
\psi(y_m)\in\AA^1,
$$
and the affine coordinate $t$ pulls back near $y_m$ to the rational function
$f$. Hence
$$
f\in\OO_{Y_m,y_m}=A_N.
$$
Since
$$
A_N\subseteq A_{N+1}\subseteq A_{N+2}\subseteq\cdots,
$$
the same element belongs to $A_i$ for every $i\ge N$, exactly as asserted
in the hint.
:::

<1>8. In the infinite closed-center case,
$$
\boxed{R=R_0=\bigcup_{i\ge0}\OO_{X_i,x_i}.}
$$
Thus $R$ is of type (3) in Exercise II.4.12.

::: {.proof}
Step <1>6 gives
$$
R_0\subseteq R.
$$
Conversely, step <1>7 shows that every element
$$
f\in R
$$
belongs to some $A_N$, hence to $R_0$. Therefore
$$
R\subseteq R_0.
$$
The two inclusions give equality.

In particular, the local union $R_0$ in the third construction is itself a
valuation ring; no additional dominating valuation ring is needed. This is
the assertion deferred from Exercise II.4.12 to the present exercise.
:::

<1>9. Every nontrivial valuation ring of $K/k$ is one of the three kinds
from Exercise II.4.12.

::: {.proof}
By steps <1>1--<1>2, its center on $X$ is either divisorial or closed.
The divisorial case is type (1) by step <1>3.

Starting from a closed center, step <1>4 gives successive centers on point
blowups. If one of them becomes the generic point of the exceptional curve,
step <1>5 gives type (2). If this never happens, every center remains closed
and steps <1>6--<1>8 give type (3).

These alternatives exhaust all possibilities for points on the exceptional
curve of a nonsingular surface.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 give the first two valuation types from their centers on
successive smooth models. Steps <1>6--<1>8 prove the infinite-center case
and the essential equality $R=R_0$ using Exercise V.5.1. Step <1>9 assembles
the exhaustive trichotomy, with the trivial valuation ring $K$ separately
excluded exactly as in Exercise II.4.12.
:::
:::
