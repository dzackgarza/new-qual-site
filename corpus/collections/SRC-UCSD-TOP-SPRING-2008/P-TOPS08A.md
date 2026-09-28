---
schema: qual/card@1
id: P-TOPS08A
kind: problem
title: "Fundamental group of RP^2 # RP^2"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Connected Sum
  - Projective Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Calculate the fundamental group of $\mathbb{RP}^2 \# \mathbb{RP}^2$.
:::

::: {.solution}
<1>1. The connected sum $\mathbb{RP}^2\#\mathbb{RP}^2$ is the closed nonorientable surface of genus $2$, hence the Klein bottle $K$.
::: {.proof}
Removing an open disk from each copy of $\mathbb{RP}^2$ leaves a Möbius band. Gluing the two boundary circles gives the connected sum. This is the standard nonorientable genus-$2$ surface, which is homeomorphic to the Klein bottle.
:::

<1>2. If $c,d$ are core-circle generators of the two Möbius bands, then
$$
\pi_1(K)\cong\langle c,d\mid c^2=d^2\rangle.
$$
::: {.proof}
Each Möbius band deformation retracts to its core circle, so its fundamental group is infinite cyclic. Its boundary circle wraps twice around the core and therefore represents the square of the core generator. Van Kampen for the union of the two Möbius bands along their common boundary identifies these two boundary classes. After replacing one core generator by its inverse if necessary, the resulting relation is $c^2=d^2$.
:::

<1>3. This group is isomorphic to the standard Klein-bottle group
$$
\boxed{\pi_1(K)\cong\langle a,b\mid bab^{-1}=a^{-1}\rangle.}
$$
::: {.proof}
Set $a=cd^{-1}$ and $b=d$ in $\langle c,d\mid c^2=d^2\rangle$. Since $d^{-2}=c^{-2}$,
$$
bab^{-1}=d(cd^{-1})d^{-1}=dcd^{-2}=dcc^{-2}=dc^{-1}=(cd^{-1})^{-1}=a^{-1}.
$$
Conversely, in $\langle a,b\mid bab^{-1}=a^{-1}\rangle$ set $c=ab$ and $d=b$. Then
$$
c^2=(ab)^2=a(bab^{-1})b^2=aa^{-1}b^2=b^2=d^2.
$$
The substitutions are inverse on generators, so the presentations define isomorphic groups.
:::

<1>4. In particular, the group is not $\mathbb Z/2*\mathbb Z/2=D_\infty$.
::: {.proof}
The Klein-bottle presentation has unique normal forms $a^m b^n$ with $m,n\in\mathbb Z$: using $ba=a^{-1}b$, every word can be put in this form, and the standard deck-transformation model on $\mathbb R^2$ shows distinct pairs give distinct elements. If $(a^m b^n)^k=1$ for $k>0$, projection to the exponent of $b$ gives $kn=0$, hence $n=0$, and then $a^{km}=1$ forces $m=0$. Thus the group is torsion-free, whereas $D_\infty$ contains elements of order $2$.
:::
:::
