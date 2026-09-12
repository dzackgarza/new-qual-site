---
schema: qual/card@1
id: P-HGRO44
kind: problem
title: The Frobenius kernel of a sharply two-transitive action
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the cardinality request with the retained Harvard group-theory source; it makes no finiteness assumption. Defined the fixed-point-free set explicitly and retained both finite and infinite cases."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the exact finite count, uniqueness of an involution in a point stabilizer, fixed-point-free products of distinct involutions, the infinite cardinal comparison, finite subgroup closure in both parity cases, and regularity whenever K is a subgroup."
---

::: problem
Let $G$ act sharply $2$-transitively on a set $X$ with $|X|\geq2$.
Put
$$
K=\{1\}\cup\{g\in G:g\text{ fixes no point of }X\}.
$$
Prove that $|K|=|X|$. When $X$ is finite, also prove that
$K$ is a normal subgroup, the Frobenius kernel of the action.
:::

::: remark
The set $K$ is specified before any subgroup property is used.
Its cardinality statement holds without a finiteness hypothesis.
Subgroup closure is proved below when $X$ is finite; the
infinite cardinality proof does not infer closure from counting.
Whenever $K$ is a subgroup, its action is regular and the map
$k\mapsto kx$ is a bijection $K\to X$ for each $x\in X$.
:::

::: solution
Sharp double transitivity means that for any two ordered
pairs of distinct points there is exactly one group element
mapping the first pair to the second. In particular, only
the identity can fix two distinct points, and the action
is faithful. A fixed-point-free element is also called a
derangement. We use the axiom of choice for infinite cardinalities.

<1>1. If $X$ is finite of size $n\geq2$, then $|K|=n$.

::: proof
Fix distinct $x,y\in X$. Sharp double transitivity makes
$$
G\longrightarrow\{(a,b)\in X^2:a\ne b\},
\qquad g\longmapsto(gx,gy)
$$
a bijection. Thus $|G|=n(n-1)$. For each $a\in X$,
its stabilizer $G_a$ acts regularly on $X\setminus\{a\}$:
there is exactly one element taking any chosen point
of that complement to any other. Hence $|G_a|=n-1$.

No nonidentity element belongs to two different point
stabilizers, since it would fix two points. Therefore
the number of nonidentity elements having a fixed point
is exactly $n(n-2)$. Their complement in $G$ is $K$,
including the identity. Consequently
$$
|K|=n(n-1)-n(n-2)=n.
$$
This includes $n=2$, when every point stabilizer is trivial.
:::

<1>2. Each pair of distinct points has a unique swapping
involution, and each point stabilizer contains at most one involution.

::: proof
For distinct $x,y$, the unique element swapping $x,y$
has square fixing both and is not the identity. It is
therefore an involution, uniquely determined by that pair.
For fixed $x$, varying $y\ne x$ gives distinct involutions.

Suppose involutions $i,j$ fix $x$, and choose $y\ne x$.
Neither can fix $y$. Since $G_y$ is transitive on
$X\setminus\{y\}$, choose $g\in G_y$ with $g(jy)=iy$.
The involution $g^{-1}ig$ sends $y$ to $jy$ and hence
swaps $y,jy$. By uniqueness of that swap it equals $j$.
Since $j$ fixes $x$, the involution $i$ fixes $gx$.
It already fixes $x$, so $gx=x$; otherwise it would fix
two points. Now $g$ fixes both $x,y$, so $g=1$ and $i=j$.
:::

<1>3. A product of two distinct involutions is fixed-point-free.

::: proof
Let $i,j$ be involutions, and suppose $ij$ fixes $x$.
Then $jx=ix$. If this common point is $x$, both involutions
belong to $G_x$ and are equal by step <1>2. Otherwise
both swap $x$ with the same distinct point, and uniqueness
of the swap again gives $i=j$. Thus for $i\ne j$ their
product fixes no point. In particular, if $J$ is the
set of involutions and $i\in J$, then $iJ\subseteq K$.
:::

<1>4. If $X$ is infinite, then $|K|=|X|$ as well.

::: proof
We first justify the cardinal arithmetic being used.
Deleting one point from an infinite set does not change
its cardinality: choose a sequence of distinct points
starting at that point, shift along the sequence, and
fix every point outside it. This gives the required bijection.

For completeness, an infinite cardinal $\kappa$ satisfies
$|\kappa\times\kappa|=\kappa$. Prove this by transfinite
induction on infinite cardinals. Regard $\kappa$ as its
initial ordinal and order pairs $(\alpha,\beta)$ first by
$\max(\alpha,\beta)$ and then lexicographically. This is
a well-order. The predecessors of a pair with maximum
$\gamma$ lie in $(\gamma+1)^2$. The cardinal of
$\gamma+1$ is less than $\kappa$; its square is still
less than $\kappa$ by induction, or by finite arithmetic
when it is finite. Thus each predecessor set has cardinal
less than $\kappa$. The order type of the pairs is at
most $\kappa$, since otherwise the pair at position
$\kappa$ would have $\kappa$ predecessors. This proves
the upper bound, and $\alpha\mapsto(\alpha,0)$ gives
the reverse bound.

Now fix $x\in X$ and an involution $i$, which exists by
step <1>2. The swaps of $x$ with each $y\ne x$ give an
injection $X\setminus\{x\}\to J$. Multiplication by $i$
is injective on $J$ and takes it into $K$ by step <1>3.
The ordered-pair map in step <1>1 is a bijection even
when $X$ is infinite. We therefore have
$$
|X|=|X\setminus\{x\}|\leq |J|=|iJ|
\leq |K|\leq |G|\leq |X^2|=|X|.
$$
Both bounds coincide, proving the claim without any
subtraction of infinite cardinals.
:::

<1>5. When $X$ is finite, the set $K$ is a normal subgroup.

::: proof
The set is closed under inverses, because an element
and its inverse have the same fixed points. It is
preserved by conjugation, because conjugation carries
fixed points to fixed points. It remains to prove
closure under multiplication.

Suppose first that $n=|X|$ is even. An involution is a
product of disjoint transpositions and fixed points.
Its number of fixed points has the same parity as $n$
and is at most one, so it has none. For any $x$, the
map $J\to X\setminus\{x\}$, $j\mapsto jx$, is bijective:
its inverse sends $y$ to the unique swap of $x,y$.
Hence $|J|=n-1$. Step <1>1 says that there are exactly
$n-1$ derangements, so $K=\{1\}\cup J$. A product
of distinct involutions belongs to $K$ by step <1>3,
and a square of an involution is one. Thus $K$ is closed.

Suppose instead that $n$ is odd. Every involution has
exactly one fixed point by the same parity argument.
There is an involution fixing each point: conjugate
any involution by an element taking its fixed point
to the desired point. Step <1>2 gives uniqueness.
Consequently $|J|=n$. For a fixed $i\in J$, the subset
$iJ\subseteq K$ has $n$ elements and hence equals $K$
by step <1>1. If $a=ij$ and $b=ik$ belong to $K$,
with $j,k\in J$, then
$$
ab=ijik=(iji)k.
$$
The element $iji$ is an involution, so this product
is either one or a derangement by step <1>3. Therefore
$ab\in K$. Closure follows in both parity cases.

Thus $K$ is a subgroup, and its conjugation invariance
makes it normal. This proves the finite Frobenius-kernel
assertion without invoking a general kernel theorem.
:::

<1>6. Whenever $K$ is a subgroup, it acts regularly on $X$.

::: proof
The set $K$ is conjugation invariant as above, so such
a subgroup is normal. Steps <1>1 and <1>4 imply
$|K|=|X|\geq2$, hence $K$ contains a nonidentity element.
For fixed $x$, the orbit $Kx$ contains a point other
than $x$, since every nonidentity element of $K$ is
fixed-point-free. Normality makes this orbit invariant
under $G_x$: for $h\in G_x$ and $k\in K$,
$h(kx)=(hkh^{-1})x\in Kx$.
Since $G_x$ is transitive on $X\setminus\{x\}$,
the orbit $Kx$ must be all of $X$.

If $kx=k'x$ for $k,k'\in K$, then $(k')^{-1}k\in K$
fixes $x$, forcing $(k')^{-1}k=1$. Thus the orbit map
$K\to X$ is both surjective and injective, which is
regularity and gives the stated bijection.
:::
:::
