---
schema: qual/card@1
id: P-EMAG3
kind: problem
title: Automorphisms carrying index-$n$ subgroups of $S_n$ to point stabilizers
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both parts with Groups 3 on PDF page 1; preserved automorphism rather than strengthening it to inner automorphism."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked every small-n kernel case, the exact labeled coset stabilizer, and the overgroup orbit count, including the trivial n=1 case."
---

::: problem
Let $H$ be a subgroup of $S_n$ of index $n$.
Prove:

(a) There is an isomorphism $f : S_n \to S_n$ such that $f(H)$ is the subgroup of $S_n$ stabilizing $n$.
In particular, $H$ is isomorphic to $S_{n-1}$.

(b) The only subgroups of $S_n$ containing $H$ are $S_n$ and $H$.
:::

::: solution
<1>1. The action of $S_n$ on its $n$ left cosets of $H$
is faithful.

::: proof
Left multiplication sends $xH$ to $gxH$. It is
well defined, its inverse is multiplication by
$g^{-1}$, and it respects composition. Thus it
defines a homomorphism
$\rho:S_n\to\operatorname{Sym}(S_n/H)$.
Its kernel $N$ is normal and lies in $H$: a
kernel element fixes the coset $H$ and therefore
belongs to $H$. Hence $|N|$ divides $(n-1)!$.

For $n\geq5$, every nontrivial normal subgroup
of $S_n$ contains $A_n$ [@DF04]. Such a subgroup
has order at least $n!/2>(n-1)!$, so $N=1$.
For $n=4$, the nontrivial normal subgroups have
orders $4,12,24$, none dividing $6=|H|$.
For $n=3$, they have orders $3,6$, neither
dividing $2=|H|$ [@DF04]. For $n=2$, $H$ itself
is trivial. For $n=1$, $S_1$ itself is trivial.
Thus $N=1$ in all cases.
:::

<1>2. The coset action yields the automorphism in part (a).

::: proof
Label the cosets by $1,\ldots,n$, assigning label
$n$ to $H$. The action becomes an injective
homomorphism $f:S_n\to S_n$. Since the two finite
groups have the same order, it is bijective.
Moreover $f(g)$ fixes $n$ exactly when $gH=H$,
or $g\in H$. Thus $f(H)$ is exactly the full
stabilizer $H_n$ of $n$. Restriction to the other
$n-1$ letters identifies $H_n$ with $S_{n-1}$;
the inverse extends a permutation by fixing $n$.
This proves both assertions of part (a).
:::

<1>3. There are no overgroups strictly between $H$ and $S_n$.

::: proof
For $n=1$ there is nothing to prove, and the
convention $S_0=1$ makes part (a) valid as well.
For $n\geq2$, transport a proposed overgroup
through $f$ and suppose $H_n\subsetneq J\leq S_n$.
Choose $g\in J$ with $g(n)\ne n$. The subgroup
$H_n$ acts transitively on the other $n-1$ letters,
so the orbit of $n$ under $J$ is the full set
of $n$ letters. The stabilizer of $n$ in $J$
is exactly $H_n$, because it is the full stabilizer
in $S_n$ and is contained in $J$.
Orbit-stabilizer gives $|J|=n|H_n|=n!$, so
$J=S_n$. Applying $f^{-1}$ proves part (b).
:::
:::
