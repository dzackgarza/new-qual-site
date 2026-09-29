---
schema: qual/card@1
id: P-AGXGATHGLOBALSEC
kind: problem
title: When global regular functions determine morphisms out of a prevariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Prevarieties
  - Global Sections
  - Morphisms of Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Gathmann 5.9 card and recorded collection context
    together with the retained Problem Set 5 native source and migration
    record. The source gives the affine-affine proposition and asks the two
    extensions but supplies no argument. Cross-checked part (a) against the
    repository proof P-AGH224HOMSPEC of the general adjunction
    Hom(X,Spec A)=Hom(A,Gamma(X,O_X)).
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read both parts. Checked that the local affine morphisms induced by a
    global k-algebra map agree on affine subopens of every overlap and hence
    glue uniquely. Checked the counterexample X=Spec k, Y=P^1: both distinct
    k-points induce the unique k-algebra map k to k because
    Gamma(P^1,O)=k.
---

::: {.problem}
There is a bijection
\[
\ts{ \text{morphisms } X \to Y }
&\stackrel{1: 1}{\leftrightarrow}
\ts{ k\dash\text{algebra morphisms } \OO_{Y}(Y) \to \OO_{X}(X) } \\
f &\mapsto f^{*}
.\]

Does this bijection hold if

a. $X$ is an arbitrary prevariety but $Y$ is still affine?

b. $Y$ is an arbitrary prevariety but $X$ is still affine?
:::

::: {.solution}
For a $k$-prevariety $Z$, write
$$
A(Z)=\Gamma(Z,\OO_Z).
$$

::: pf

::: {.pf-step #morphism-from-algebra-map}
Part (a): if
$$
Y=\Spec A
$$
is affine, every $k$-algebra homomorphism
$$
\varphi:A\longrightarrow A(X)
$$
determines a morphism
$$
\boxed{f_\varphi:X\longrightarrow Y.}
$$

::: pf-proof
Choose an affine open cover
$$
X=\bigcup_i U_i,
\qquad
U_i=\Spec B_i.
$$
Restricting global sections gives homomorphisms
$$
\varphi_i:
A
\xrightarrow{\varphi}
A(X)
\longrightarrow
A(U_i)=B_i.
$$
By the affine correspondence, each $\varphi_i$ determines a unique morphism
$$
f_i:U_i\longrightarrow\Spec A.
$$

For any $i,j$, cover $U_i\cap U_j$ by affine opens
$$
W=\Spec C.
$$
Both restrictions
$$
f_i|_W,\quad f_j|_W
$$
correspond to the same ring homomorphism
$$
A
\xrightarrow{\varphi}
A(X)
\longrightarrow
A(W)=C,
$$
because both maps are obtained by restricting the same global sections.
Thus
$$
f_i|_W=f_j|_W.
$$
Since the affine opens $W$ cover $U_i\cap U_j$, the morphisms $f_i$ and
$f_j$ agree on the whole overlap.

The $f_i$ therefore glue uniquely to a morphism
$$
f_\varphi:X\longrightarrow\Spec A.
$$
This is the construction proved in [[P-AGH224HOMSPEC]].
:::

:::

::: {.pf-step #bijection-established}
Part (a): the assignments
$$
f\longmapsto f^*
\qquad\text{and}\qquad
\varphi\longmapsto f_\varphi
$$
are inverse. Hence the displayed correspondence remains a bijection when
$X$ is arbitrary and $Y$ is affine.

::: pf-proof
Let
$$
\varphi:A\longrightarrow A(X).
$$
On every affine open $U_i=\Spec B_i$, the morphism $f_\varphi$ of step
[](#morphism-from-algebra-map){.pf-ref} restricts to the affine morphism induced by
$$
A\xrightarrow{\varphi}A(X)\longrightarrow B_i.
$$
Therefore the pullback
$$
f_\varphi^*:A\longrightarrow A(X)
$$
has, after restriction to every $U_i$, the same value as $\varphi$.
The sheaf axiom gives
$$
f_\varphi^*=\varphi.
$$

Conversely, suppose
$$
f,g:X\longrightarrow\Spec A
$$
induce the same homomorphism
$$
A\longrightarrow A(X).
$$
Their restrictions to every affine $U_i=\Spec B_i$ induce the same ring
homomorphism
$$
A\longrightarrow B_i.
$$
The affine correspondence therefore gives
$$
f|_{U_i}=g|_{U_i}
$$
for every $i$, so
$$
f=g.
$$
Thus the correspondence is both surjective and injective.
:::

:::

::: {.pf-step #no-bijection-counterexample}
Part (b):
$$
\boxed{\text{No.}}
$$
Take
$$
X=\Spec k,
\qquad
Y=\PP^1.
$$

::: pf-proof
The variety $X$ is affine, while $Y$ is a non-affine prevariety.
With homogeneous coordinates $[S:T]$, the standard affine cover
$$
D_+(T)\cong\Spec k[t],
\qquad
D_+(S)\cong\Spec k[u]
$$
of $\PP^1$ has overlap on which
$$
u=t^{-1}.
$$
Hence a global regular function on $\PP^1$ is an element of
$$
k[t]\cap k[t^{-1}]
$$
inside $k[t,t^{-1}]$, so it is constant. Therefore
$$
A(\PP^1)=k.
$$
Also
$$
A(\Spec k)=k.
$$
There is only one $k$-algebra homomorphism
$$
k\longrightarrow k,
$$
namely the identity.

On the other hand, there are at least two distinct morphisms
$$
\Spec k\longrightarrow\PP^1,
$$
for example the $k$-points
$$
[1:0]
\qquad\text{and}\qquad
[0:1].
$$
Both induce the same map
$$
k=A(\PP^1)\longrightarrow A(\Spec k)=k.
$$
Thus
$$
\Hom(X,Y)\longrightarrow
\Hom_{k\text{-alg}}\!\bigl(A(Y),A(X)\bigr)
$$
is not injective, so it cannot be a bijection.
:::

:::

::: pf-qed
Steps [](#morphism-from-algebra-map){.pf-ref} and [](#bijection-established){.pf-ref} prove that the bijection persists for arbitrary $X$ when
$Y$ is affine. Step [](#no-bijection-counterexample){.pf-ref} gives an affine $X$ and a non-affine $Y$ for which
the map is not injective, proving that the analogous statement in part (b)
fails.
:::

:::
:::
