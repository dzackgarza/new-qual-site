---
schema: qual/card@1
id: P-AGH3114CONNPRINCIPLE
kind: problem
title: The principle of connectedness for a flat family
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Flat Families
  - Connectedness
  - Stein Factorization
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.4 in the Hartshorne source sequence and independently
    checked the connectedness-specialization argument through Stein
    factorization. The proof below makes explicit the lower semicontinuity of
    the number of geometric connected components, including its Stein-factor
    proof, and was cross-checked against Stacks Project Tag 0BUI. This avoids
    the false shortcut that connected nonreduced fibres force h^0(O)=1.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $\ts{X_t}$ be a flat family of closed subschemes of $\PP_k^n$ parametrized by an irreducible curve $T$ of finite type over $k$.
Suppose there is a nonempty open set $U \subseteq T$ such that $X_t$ is connected for all closed points $t \in U$.
Prove that $X_t$ is connected for all $t \in T$.
:::

::: {.solution}
Let
$$
\pi:\mathcal X\longrightarrow T
$$
denote the total family, so that
$$
X_t=\mathcal X\times_T\Spec\kappa(t).
$$
Because $\mathcal X$ is a closed subscheme of $\PP_k^n\times T$, the
morphism $\pi$ is projective. It is flat by hypothesis and of finite
presentation because all schemes involved are of finite type over $k$.

<1>1. For $t\in T$, let
$$
c(t)
$$
be the number of connected components of the geometric fibre
$$
\mathcal X_{\overline t}.
$$
Then $c:T\to\ZZ_{\ge0}$ is lower semicontinuous.

::: {.proof}
We give the Stein-factor argument in the form needed here.
Fix $t\in T$ and put
$$
r=c(t).
$$
Take the Stein factorization
$$
\mathcal X\xrightarrow{h}S\xrightarrow{g}T,
$$
where
$$
S=\Spec_T(\pi_*\mco_{\mathcal X}),
$$
$g$ is finite, and $h$ has geometrically connected fibres.

More explicitly, after replacing $T$ by an étale neighbourhood of $t$, the
points of the finite fibre of $S$ corresponding to the $r$ geometric
connected components of $\mathcal X_{\overline t}$ lie in pairwise disjoint
open-and-closed pieces
$$
V_1,\ldots,V_r\subseteq S.
$$
This is the standard local decomposition of a finite morphism around the
points of one fibre; see the
[Stein-factor proof of lower semicontinuity](https://stacks.math.columbia.edu/tag/0BUI).

Put
$$
\mathcal X_i=h^{-1}(V_i).
$$
Each $\mathcal X_i$ is open in $\mathcal X$, hence
$$
\mathcal X_i\longrightarrow T
$$
is flat and of finite presentation. A flat morphism locally of finite
presentation is open, so its image
$$
W_i=\pi(\mathcal X_i)
$$
is an open neighbourhood of $t$. Therefore
$$
W=W_1\cap\cdots\cap W_r
$$
is an open neighbourhood of $t$.

For every $u\in W$, each $\mathcal X_i$ meets the fibre over $u$.
Since the $V_i$ are pairwise disjoint open-and-closed subsets of $S$, these
intersections lie in distinct connected components of the geometric fibre
$\mathcal X_{\overline u}$. Hence
$$
c(u)\ge r=c(t)
$$
for all $u$ in an open neighbourhood of $t$. This is precisely lower
semicontinuity.
:::

<1>2. For every closed point $u\in U$,
$$
c(u)=1.
$$

::: {.proof}
Because $T$ is a finite-type curve over the algebraically closed field $k$,
every closed point has residue field $k$. Thus
$$
\mathcal X_{\overline u}=X_u.
$$
By hypothesis $X_u$ is connected, so it has exactly one connected component.
:::

<1>3. No point $t\in T$ can satisfy
$$
c(t)\ge2.
$$

::: {.proof}
Suppose that $c(t)\ge2$ for some $t\in T$. By lower semicontinuity from
step <1>1, there is a nonempty open neighbourhood
$$
W\subseteq T
$$
of $t$ such that
$$
c(w)\ge2
$$
for every $w\in W$.

The curve $T$ is irreducible, so any two nonempty open subsets meet.
Therefore
$$
W\cap U\ne\varnothing.
$$
Since $T$ is of finite type over a field, its closed points are dense; choose
a closed point
$$
u\in W\cap U.
$$
Then step <1>2 gives
$$
c(u)=1,
$$
whereas the defining property of $W$ gives
$$
c(u)\ge2,
$$
a contradiction.
:::

<1>4. Every fibre $X_t$ is connected.

::: {.proof}
Step <1>3 gives
$$
c(t)\le1
$$
for every $t\in T$.
The family has nonempty fibres everywhere. Indeed, $\pi$ is projective, hence
its image is closed, and it is flat of finite presentation, hence its image
is open. The image contains the nonempty open set $U$, so irreducibility of
$T$ forces
$$
\pi(\mathcal X)=T.
$$
Thus every geometric fibre is nonempty and consequently
$$
c(t)=1
$$
for all $t$.

A scheme whose geometric fibre is connected has connected ordinary fibre.
Hence every $X_t$ is connected.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 rule out the appearance of a second connected component
under specialization, and step <1>4 supplies nonemptiness and concludes that
every fibre has exactly one connected component.
:::
:::
