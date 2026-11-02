---
schema: qual/card@1
id: P-MCG5C
kind: problem
title: Compactness and Euler characteristic of covering spaces, and coverings of even-dimensional
  $\RP^N$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Euler Characteristic
  - Cell Complexes
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    The solution was an outline: five steps whose proof blocks were single hints ("covering of compact
    is compact iff finite sheeted", "lift cell structure", "chi(RP^2k) = 1", "d divides 1"), which is
    what issue #96 flagged. Replaced by proofs, not restyled. The compactness direction that the
    outline skipped entirely is now an elementary finite-subcover argument that also fixes what the
    hint elided: a fibre is a closed discrete subset of Y, hence finite when Y is compact, which is
    the only way finiteness of the degree follows from compactness. The Euler-characteristic step now
    names its hypothesis (X finite CW, which is where the alternating sum is an integer) and derives
    the cell count of Y from the lifted cell structure. The RP conclusion now says why the base is
    finite CW: the problem's standing hypothesis makes X a CW complex, and a compact CW complex has
    finitely many cells, so chi(X) is an integer and d divides 1. A remark records that scope, since
    the printed part (c) renames only the total space and omits it. The statement is unchanged from
    the printed Problem 6 of the Spring 2009 UGA topology qualifying exam.
- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    Correction to the remark added in the preceding event, which said the problem's standing hypothesis
    is that X is a *connected* CW complex. The source assumes no such thing: it says "Let X be a
    CW-complex and pi: Y -> X be a covering space", with no connectedness and no finiteness hypothesis,
    and narrowing it that way silently strengthened the question. The remark now states the reconciliation
    instead. (a) needs no connectedness: "finite degree" is read as "every fibre is finite", a compact CW
    complex has finitely many components, and the finite-subcover argument runs on each component, so the
    step is proved for arbitrary CW X. (b) is a statement about chi, which is an integer only for
    finitely many cells, so it presupposes a finite CW complex; and a single factor d is what connectedness
    of X gives, the general form being the componentwise identity chi(Y) = sum_i d_i chi(X_i). Both are now
    said on the card. (c) assumes nothing beyond a CW base: X is connected because it is the image of the
    connected RP^N, compact by (a), and finitely cellular because it is a compact CW complex, so chi(X) is
    an integer. The proofs were changed only where this reconciliation touches them: the fibre-cardinality
    step now says "on each component", the compactness step is proved for finite fibres over an arbitrary
    compact CW base, and the multiplicativity step names both its finiteness and its single-d assumption.
    The printed statement is unchanged. Not checked here: no source beyond the extracted exam text.

- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    Correction to two necessity claims in the remark, both unsupported by the argument the remark
    itself gives. Claim one said the sheet number "is one number exactly when X is connected", and
    claim two said chi "is an integer only when there are finitely many cells". Neither is a
    consequence of the locally-constant and alternating-sum arguments stated there, and both are
    false as written. The remark now states each as a sufficient hypothesis and separates what is
    actually used. Sheet number: local constancy gives a constant d_i on each component, so a single
    d exists as soon as the d_i agree; connectedness secures that but is not necessary, and the
    general form is chi(Y) = sum_i d_i chi(X_i). Finiteness: the alternating sum of the cell counts
    is an integer whenever each count is finite and only finitely many are nonzero, which includes
    finite CW complexes but also bounded-dimension complexes of finite type with infinitely many
    cells, and the homology definition gives it whenever the integral homology is finitely generated
    in each degree and vanishes above some degree; what the argument needs is a well-defined integer
    chi(X) together with a common d. A counterexample to the printed (b) in the absence of a common d
    is now on the card: X = {p} sqcup {q} has chi(X) = 2 and the covering with one point over p and
    two over q has chi(Y) = 3, while d chi(X) is 2 or 4 for either candidate sheet number, so no d
    satisfies the conclusion. The proof steps are unchanged by this edit and remain consistent with
    it, since the finiteness they use (a compact CW complex has finitely many cells) is the
    sufficient hypothesis, not the necessity claim. Not checked here: no source beyond the extracted
    exam text; the counterexample and the two sufficient-hypothesis statements were verified by hand
    against the locally-constant and alternating-sum arguments on this card, not by a machine check.

---

::: {.problem}
Let $X$ be a CW complex and let $\pi : Y \to X$ be a covering space.

Show that $Y$ is compact iff $X$ is compact and $\pi$ has finite degree.

Assume that $\pi$ has finite degree $d$.
Show that $\chi (Y ) = d \chi (X)$.

Let $\pi :\RP^N \to X$ be a covering map.
Show that if $N$ is even, $\pi$ is a homeomorphism.

:::

::: {.remark}
The source states only "Let $X$ be a CW complex and let $\pi\colon Y\to X$ be a covering space": it assumes neither connectedness nor finiteness, and the three parts do not need more than they say, as follows.

**Connectedness is not assumed anywhere.** In (a), read "finite degree" as "every fibre is finite". A compact CW complex has finitely many components, so the sheet numbers are bounded, and the finite-subcover argument runs on each component; nothing needs the sheet number to agree between components.

**A single degree $d$ needs the sheet number to agree on all components, for which connectedness is sufficient but not necessary.** The fibre cardinality is locally constant, hence constant on each component, so $d$ is one number as soon as those componentwise values coincide. Connectedness is one way to secure that, and it is the hypothesis (b) is stated under; a disconnected base with equal sheet numbers on every component gives the same single $d$. When the values differ there is no common $d$, and the honest general form is the componentwise identity $\chi(Y)=\sum_i d_i\,\chi(X_i)$. Without a common $d$ the printed (b) has no true reading at all: for $X=\{p\}\sqcup\{q\}$, so that $\chi(X)=2$, take $Y$ to be the covering with one point over $p$ and two over $q$; then $\chi(Y)=3$, whereas $d\,\chi(X)$ is $2$ or $4$ according to which component's sheet number is called $d$, so no value of $d$ satisfies the conclusion.

**For $\chi$ to be an integer, finitely many cells is sufficient but not necessary.** $\chi$ is the alternating sum of the cell counts, which is an integer as soon as each count is finite and only finitely many of them are nonzero — in particular for a CW complex with finitely many cells, which is the hypothesis (b) is stated under, and then $Y$ has finitely many too. That hypothesis is stronger than necessary: a finite-type CW complex of bounded dimension, with infinitely many cells in all, still has an integral $\chi$ by the same alternating sum, and so does any space whose integral homology is finitely generated in each degree and vanishes above some degree, where $\chi$ is defined by the homology sum instead. What is genuinely needed for the argument below is that $\chi(X)$, and hence each $\chi(X_i)$ used, be a well-defined integer, together with a common $d$. In (c) nothing is assumed in advance: $X$ is the image of the connected $\RP^N$, so it is connected; it is compact by (a); and being a CW complex by the opening hypothesis, compactness forces finitely many cells, so $\chi(X)\in\ZZ$.
:::

::: {.solution}

::: pf

::: {.pf-step #sheet-count}
The fibre cardinality is locally constant, hence constant on each connected component of $X$; on a connected $X$ it is therefore a single $d\in\NN\cup\{\infty\}$, the degree.

::: pf-proof
Let $U$ be an evenly covered neighbourhood of $x$, so that $\pi^{-1}(U)$ is a disjoint union of open subsets each mapped homeomorphically onto $U$ by $\pi$. For $x'\in U$, each such sheet meets $\pi^{-1}(x')$ in exactly one point: the sheet is homeomorphic to $U$ over $U$, so it contains exactly one point over $x'$. Hence $\abs{\pi^{-1}(x')}=\abs{\pi^{-1}(x)}$, and $x\mapsto\abs{\pi^{-1}(x)}$ is locally constant. A locally constant function is constant on each connected component, and constant on $X$ when $X$ is connected.

:::

:::

::: {.pf-step #fibre-finite}
If $Y$ is compact then every fibre $\pi^{-1}(x)$ is finite.

::: pf-proof
The fibre is closed: it is the preimage of the point $x$, and points of the CW complex $X$ are closed. It is discrete in its subspace topology: every $y\in\pi^{-1}(x)$ has an evenly covered neighbourhood whose sheet through $y$ meets $\pi^{-1}(x)$ only in $y$. Now let $F=\pi^{-1}(x)$. Each $\{y\}$ with $y\in F$ is open in $F$, so there are open $V_y\subseteq Y$ with $V_y\cap F=\{y\}$, and $Y\setminus F$ is open because $F$ is closed. The sets $Y\setminus F$ and the $V_y$ cover $Y$, so by compactness finitely many of them cover $Y$; a finite such subcover uses finitely many $V_y$, and those $y$ exhaust $F$.

:::

:::

::: {.pf-step #base-compact}
If $Y$ is compact then $X$ is compact.

::: pf-proof
The map $\pi$ is continuous and surjective, so $X=\pi(Y)$ is a continuous image of a compact space.

:::

:::

::: {.pf-step #total-compact}
If $X$ is compact and every fibre is finite then $Y$ is compact.

::: pf-proof
A compact CW complex has finitely many cells, hence finitely many components, so write them $X_1,\dots,X_m$. On each $X_j$ the fibre cardinality is a finite constant $d_j$ by step [](#sheet-count){.pf-ref} and the hypothesis, and it suffices to cover each $\pi^{-1}(X_j)$ by finitely many members of a given cover of $Y$.

So let $\mathcal{U}$ be an open cover of $Y$ and work in one component $X_j$, putting $d=d_j$. Fix $x\in X_j$ and write $\pi^{-1}(x)=\{y_1,\dots,y_d\}$. For each $i$ choose $U_i\in\mathcal{U}$ with $y_i\in U_i$, and an evenly covered neighbourhood $V_i$ of $x$ with sheet $S_i$ through $y_i$. Then $\pi(S_i\cap U_i)$ is an open neighbourhood of $x$ inside $V_i$, because $\pi$ maps $S_i$ homeomorphically onto the open set $V_i$; put $W_i=\pi(S_i\cap U_i)$ and $W=\bigcap_i W_i$, an open neighbourhood of $x$. Over $W$ the sheet through $y_i$ is $S_i\cap\pi^{-1}(W)$, and it lies in $U_i$: if $z\in S_i$ has $\pi(z)\in W\subseteq\pi(S_i\cap U_i)$ then $z$, being the unique point of $S_i$ over $\pi(z)$, lies in $S_i\cap U_i$. These $d$ sheets cover $\pi^{-1}(W)$. The sets $W$, one for each $x$, cover the compact $X_j$, so finitely many of them cover $X_j$, and the finitely many sets $U_i$ used for those points cover $\pi^{-1}(X_j)$ and lie in $\mathcal{U}$. Doing this for the finitely many components covers $Y$ by finitely many members of $\mathcal{U}$.

:::

:::

::: {.pf-step #compactness}
$Y$ is compact if and only if $X$ is compact and every fibre is finite; when $X$ is connected, "every fibre is finite" is "$d<\infty$".

::: pf-proof
If $Y$ is compact then $X$ is compact by step [](#base-compact){.pf-ref} and every fibre is finite by step [](#fibre-finite){.pf-ref}. Conversely if $X$ is compact and every fibre is finite then $Y$ is compact by step [](#total-compact){.pf-ref}.

:::

:::

::: {.pf-step #lifted-cells}
Let $X$ be a finite CW complex and $d$ finite. Then $Y$ is a finite CW complex, and the number of $k$-cells of $Y$ is $d$ times the number of $k$-cells of $X$, for every $k$.

::: pf-proof
Take a cell $e\subseteq X$ with characteristic map $\Phi\colon D^k\to X$. Since $D^k$ is compact and connected and $X$ is evenly covered over the interior of $e$, the preimage $\pi^{-1}(e)$ is a disjoint union of $d$ open sets, each mapping homeomorphically onto $e$; their closures are obtained by adjoining the lifts of the attaching sphere, and the composites $D^k\to\pi^{-1}(e)\to e\subseteq X$ serve as characteristic maps. The lifted cells cover $Y$, and their intersections are the lifted skeleta, so this is a CW structure on $Y$. Counting, $c_k(Y)=d\,c_k(X)$ for every $k$, and both are finite because $X$ has finitely many cells.

:::

:::

::: {.pf-step #chi-multiplicative}
If $X$ is a finite CW complex and the sheet number is the same $d$ on every component, then $\chi(Y)=d\,\chi(X)$; without the last clause the same proof gives $\chi(Y)=\sum_i d_i\,\chi(X_i)$ over the components.

::: pf-proof
By step [](#lifted-cells){.pf-ref},
$$
\chi(Y)=\sum_k(-1)^k c_k(Y)=\sum_k(-1)^k d\,c_k(X)=d\sum_k(-1)^k c_k(X)=d\,\chi(X),
$$
both sums being finite.

:::

:::

::: {.pf-step #rp-chi}
$\chi(\RP^N)=1$ when $N$ is even, and $\chi(\RP^N)=0$ when $N$ is odd.

::: pf-proof
The standard CW structure on $\RP^N$ has exactly one cell in each dimension $0,\dots,N$, so $c_k=1$ for $k\le N$ and $c_k=0$ otherwise. Hence $\chi(\RP^N)=\sum_{k=0}^N(-1)^k$, which is $1$ for even $N$ and $0$ for odd $N$.

:::

:::

::: {.pf-step #finite-base}
Let $\pi\colon\RP^N\to X$ be a covering with $X$ a CW complex and $N$ even. Then $X$ is connected, compact, and a finite CW complex, so $\chi(X)$ is an integer.

::: pf-proof
$\RP^N$ is connected, so its continuous image $X$ is connected, which is what makes the degree of $\pi$ a single number. It is compact, so $X$ is compact by step [](#base-compact){.pf-ref}. A compact CW complex has finitely many cells: if $X$ had infinitely many, it would be the union of a strictly increasing sequence of finite subcomplexes, each closed and proper, and a compact subset of a CW complex lies in a finite subcomplex, so no strictly increasing sequence can exhaust it. Hence $X$ is a finite CW complex and $\chi(X)$ is an integer.

:::

:::

::: {.pf-step #degree-one}
Let $\pi\colon\RP^N\to X$ be a covering with $X$ a CW complex and $N$ even. Then $d=1$.

::: pf-proof
By steps [](#compactness){.pf-ref}, [](#finite-base){.pf-ref} and [](#chi-multiplicative){.pf-ref},
$$
1=\chi(\RP^N)=d\,\chi(X)
$$
with $d$ a positive integer and $\chi(X)$ an integer, by step [](#rp-chi){.pf-ref}. A positive integer dividing $1$ is $1$, so $d=1$.

:::

:::

::: {.pf-step #homeomorphism}
A covering $\pi\colon Y\to X$ of finite degree $1$ is a homeomorphism.

::: pf-proof
Every fibre is a single point, so $\pi$ is a bijection; it is continuous by hypothesis and a local homeomorphism, hence open, because a local homeomorphism carries open sets to open sets. A continuous open bijection is a homeomorphism.

:::

:::

::: pf-qed
Part (a) is step [](#compactness){.pf-ref}: compactness of $Y$ is equivalent to compactness of $X$ together with finiteness of the degree, with compactness of $X$ coming from the continuous surjection and finiteness of the degree from the fibres being closed discrete subsets of the compact $Y$. Part (b) is step [](#chi-multiplicative){.pf-ref}: for a finite CW complex the lifted cell structure has $d$ times as many cells in every dimension, so the alternating sums differ by the factor $d$. Part (c) is steps [](#degree-one){.pf-ref} and [](#homeomorphism){.pf-ref}: for even $N$ the compactness of $\RP^N$ forces the base to be a finite CW complex, its Euler characteristic is then an integer, and $1=\chi(\RP^N)=d\,\chi(X)$ forces $d=1$, so $\pi$ is a bijective local homeomorphism and therefore a homeomorphism.

:::

:::

:::
