---
schema: qual/card@1
id: P-HCAO21
kind: problem
title: Dual module of a zero-dimensional Gorenstein algebra
classification:
  areas:
  - algebra
  topics:
  - Gorenstein Rings
  - Hom and Duality
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both Hom expressions with the retained Harvard source; neither localness, finite k-dimension, nor an R-action on k is specified there."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the explicit adjunction and augmentation action, proved the finite-dimensional Gorenstein self-duality through minimal resolutions rather than an uncited socle criterion, and verified the infinite-dimensional counterexample. The injective-dimension definition was cross-checked against Stacks tag 0DW6."
---

::: problem
Let $R$ be a zero-dimensional Gorenstein $k$-algebra.
What can be said about the $R$-module $\operatorname{Hom}_k(R,k)$?
For the second question, assume that a $k$-algebra homomorphism
$\varepsilon:R\to k$ is specified, and let $R$ act on $k$ by
$r\cdot a=\varepsilon(r)a$.
What is
\[
\operatorname{Hom}_R\!\left(k,\operatorname{Hom}_k(R,k)\right)?
\]
:::

::: remark
A $k$-algebra structure gives a map $k\to R$, not an
$R$-module structure on $k$. The specified augmentation
$\varepsilon:R\to k$ is needed for the second question;
such a map need not exist. Also, Krull dimension zero does
not imply finite dimension over $k$. The rank-one assertion
below requires finite $k$-dimension, while the adjunction
and the computation of the displayed Hom do not.
:::

::: solution
Put $D=\operatorname{Hom}_k(R,k)$ with action
$(r\varphi)(s)=\varphi(rs)$. In general, $D$ is an
injective cogenerator. If $R$ is finite-dimensional over
$k$, the Gorenstein hypothesis gives a noncanonical
$R$-module isomorphism $D\cong R$. For every specified
augmentation, the answer to the second question is
$$
\operatorname{Hom}_R(k,D)\cong k.
$$
If $R$ is finite-dimensional and local with residue field
$k$, then $D$ is also the injective hull of that residue field.

We use the local injective-dimension definition of Gorenstein:
the ring is commutative and Noetherian, and each localization
at a maximal ideal has finite injective dimension over itself.

<1>1. For every $R$-module $M$ there is a natural isomorphism
$$
\operatorname{Hom}_R(M,D)\cong\operatorname{Hom}_k(M,k).
$$

::: proof
Send an $R$-linear map $u:M\to D$ to
$\lambda_u(m)=u(m)(1)$. Conversely, for a $k$-linear
$\lambda:M\to k$, define
$$
u_\lambda(m)(r)=\lambda(rm).
$$
For fixed $m$, this is $k$-linear in $r$. Moreover,
$u_\lambda(am)(r)=\lambda(ram)=(a u_\lambda(m))(r)$,
so $u_\lambda$ is $R$-linear. The two constructions are
inverse because
$$
u_\lambda(m)(1)=\lambda(m),\qquad
\lambda_u(rm)=u(rm)(1)=(r u(m))(1)=u(m)(r).
$$
They commute with precomposition of module maps, proving
naturality.
:::

<1>2. The module $D$ is injective and separates nonzero elements
of every $R$-module.

::: proof
For an inclusion $M\subseteq N$, any $k$-linear functional
on $M$ extends to $N$ by extending a vector-space basis
[@DF04]. Through step <1>1, this says exactly that each
$R$-linear map $M\to D$ extends to $N$. This is injectivity.
If $0\ne m\in M$, choose a $k$-linear functional with
$\lambda(m)=1$. The corresponding map satisfies
$u_\lambda(m)(1)=1$, so it does not kill $m$.
This is the asserted cogenerator property. Neither conclusion
uses the Gorenstein or dimension hypotheses.
:::

<1>3. The specified augmentation gives
$\operatorname{Hom}_R(k,D)\cong k$ explicitly.

::: proof
Apply step <1>1 to the $R$-module $k$ defined by
$\varepsilon$. Evaluation at $1\in k$ identifies
$\operatorname{Hom}_k(k,k)$ with $k$. The resulting map
is $u\mapsto u(1)(1)$. Its inverse sends $a\in k$ to
$$
u_a(c)(r)=ac\,\varepsilon(r)
\qquad(c\in k,\ r\in R).
$$
These formulas also show that the isomorphism respects
the $R$-action through $\varepsilon$. In particular the
Hom space has $k$-dimension one, independently of whether
$R$ is finite-dimensional or Gorenstein.
:::

<1>4. If $A$ is a finite-dimensional local Gorenstein
$k$-algebra, then $D_A=\operatorname{Hom}_k(A,k)\cong A$.

::: proof
Write $\mathfrak n$ for its maximal ideal and
$\kappa=A/\mathfrak n$. First, $\mathfrak n$ is nilpotent.
Its powers stabilize by finite $k$-dimension, say
$I=\mathfrak n^h=\mathfrak n I$. Choose finitely many
generators $y_1,\ldots,y_t$ of $I$. The equality gives
$y=B y$ for a matrix $B$ with entries in $\mathfrak n$.
Multiplication by the adjugate of $1-B$ shows that
$\det(1-B)$ kills all generators. This determinant is
one modulo $\mathfrak n$, hence a unit in the local ring.
Therefore $I=0$.

Construct a free resolution $F_\bullet\to D_A$ by choosing
at each stage lifts of a $\kappa$-basis of the module
modulo $\mathfrak n$. Those lifts generate: their cokernel
$C$ satisfies $C=\mathfrak n C$, and nilpotence forces
$C=\mathfrak n^hC=0$. All ranks are finite because all
kernels are finite-dimensional over $k$. The kernel of each
such minimal free cover lies in $\mathfrak n$ times the
free module, since reduction modulo $\mathfrak n$ is an
isomorphism. Thus every differential of $F_\bullet$ has
matrix entries in $\mathfrak n$. Write $F_i=A^{b_i}$.

The functor $(-)^*=\operatorname{Hom}_k(-,k)$ is exact:
linear functionals extend from subspaces. Finite-dimensional
biduality gives $D_A^*\cong A$ via $e(b)(\varphi)=\varphi(b)$. This is
$A$-linear because $(a\,e(b))(\varphi)=\varphi(ab)=e(ab)(\varphi)$.
Dualizing the resolution therefore gives
$$
0\longrightarrow A\longrightarrow D_A^{b_0}
\longrightarrow D_A^{b_1}\longrightarrow D_A^{b_2}
\longrightarrow\cdots .
$$
This is an injective resolution by step <1>2, because each
finite sum of injective modules is injective. Its differentials
still have entries in $\mathfrak n$. Applying
$\operatorname{Hom}_A(\kappa,-)$ makes all differentials
zero: the image of each map from $\kappa$ is annihilated
by $\mathfrak n$. Computing Ext with this resolution gives
$$
\operatorname{Ext}_A^i(\kappa,A)
\cong\operatorname{Hom}_A(\kappa,D_A)^{b_i}
\cong\operatorname{Hom}_k(\kappa,k)^{b_i}
$$
[@DF04, sec. 17.1]. The last vector space is nonzero whenever
$b_i>0$. Finite injective dimension of $A$ makes the Ext
groups vanish for all sufficiently large $i$. Hence $b_i=0$
for all sufficiently large $i$: the minimal free resolution
of $D_A$ is finite.

Let $d$ be its largest index with $F_d\ne0$. If $d>0$,
exactness makes $F_d\to F_{d-1}$ injective. Choose
$0\ne c\in A$ with $\mathfrak n c=0$, using the last
nonzero power of $\mathfrak n$; if $\mathfrak n=0$, take
$c=1$. For a basis vector $v\in F_d$, the vector $cv$
is nonzero, but its image is zero because the differential
has entries in $\mathfrak n$. This is a contradiction.
Thus $d=0$ and $D_A$ is free. Finally
$\dim_kD_A=\dim_kA>0$, so its free rank is exactly one.
:::

<1>5. The same rank-one assertion holds for finite-dimensional
$R$ without assuming localness.

::: proof
There are only finitely many maximal ideals
$\mathfrak m_1,\ldots,\mathfrak m_t$. Indeed, the Chinese
remainder theorem gives a surjection to the product of
the residue fields at any finite set of distinct maximal
ideals [@DF04]. Counting $k$-dimensions bounds the size of
that set by $\dim_kR$, so the full set is finite.
Put $J=\bigcap_i\mathfrak m_i$. Its powers stabilize.
The determinant argument in step <1>4 applies to
$J^h=J J^h$: a determinant congruent to one modulo $J$
is a unit, because it belongs to no maximal ideal.
It follows that $J^h=0$ for some $h\geq1$.

The ideals $\mathfrak m_i^h$ are pairwise comaximal:
if $a+b=1$ with $a\in\mathfrak m_i$, $b\in\mathfrak m_j$,
expanding $(a+b)^{2h-1}$ puts every term in one of those
two powers. Since intersections of pairwise comaximal ideals
equal their products, the Chinese remainder theorem yields
$$
R\cong\prod_{i=1}^t A_i,
\qquad A_i=R/\mathfrak m_i^h,
$$
with kernel $\prod_i\mathfrak m_i^h=J^h=0$.
Each $A_i$ is local: a maximal ideal containing
$\mathfrak m_i^h$ contains $\mathfrak m_i$ and must equal it.
The product decomposition identifies $A_i$ with
$R_{\mathfrak m_i}$; localizing inverts the idempotent
of the $i$th factor and kills the other factors.
Thus every $A_i$ is Gorenstein by the hypothesis on $R$.

The finite product is also a finite direct sum as a
$k$-vector space. Dualizing gives the componentwise
$R$-module decomposition
$$
D\cong\bigoplus_{i=1}^t\operatorname{Hom}_k(A_i,k)
\cong\bigoplus_{i=1}^t A_i\cong R,
$$
where the middle isomorphism is step <1>4. These
isomorphisms require choices of generators of the dual
modules; no canonical generator is asserted.
:::

<1>6. In the finite-dimensional local case with residue field
$k$, $D$ is the injective hull of $k$.

::: proof
Let $\mathfrak m=\ker\varepsilon$. Embed $k$ in $D$ by
$a\mapsto a\varepsilon$. Step <1>3 says that the submodule
annihilated by $\mathfrak m$ is exactly $k\varepsilon$:
such elements are the values at $1$ of maps $k\to D$.
For any nonzero submodule $N\subseteq D$, choose the largest
$j$ for which $\mathfrak m^jN\ne0$. It exists because
$\mathfrak m$ is nilpotent, as proved in step <1>4.
Then $0\ne\mathfrak m^jN\subseteq N\cap k\varepsilon$.
Thus the embedding is essential: every nonzero submodule
of $D$ meets its image. Since $D$ is injective, this is
an injective hull, by the definition of an injective hull.
:::

<1>7. Finite $k$-dimension and the augmentation cannot be
silently inferred from the original dimension hypothesis.

::: proof
Take $k=\mathbb F_2$ and $R=k(t)$ with $t$ transcendental.
This is a field, hence has Krull dimension zero. It is
Gorenstein: as a module over itself it is injective,
because linear maps from subspaces extend by a basis.
The field $k(t)$ is countably infinite. It has a countably
infinite basis over $k$: a finite basis would give a finite
set, while any basis is a subset of the countable set $R$.
The elements of $D$ correspond to arbitrary assignments of
zero or one on that basis, so $|D|=2^{\aleph_0}$.
Thus $D$ and $R$ do not even have the same cardinality,
and in particular $D\not\cong R$ as $R$-modules.

There is no $k$-algebra map $k(t)\to k$. Such a map would
send $t$ to some $a\in k$ and send the invertible element
$t-a$ to zero, impossible for a unital homomorphism.
Hence the second Hom expression is not defined without
additional action data. With the action specified in the
question, step <1>3 always computes it, and steps <1>4–<1>6
give the full finite-dimensional interpretation.
:::
:::
