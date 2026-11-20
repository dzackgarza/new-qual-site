---
schema: qual/card@1
id: E-HAT-3.C-15
kind: problem
title: Pontryagin ring from polynomial cohomology
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 15; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read and checked line by line; nothing needed repair. The rank-one conclusion on
    $A^{nd}$ follows from $A\otimes\QQ\cong\QQ[\alpha]$ together with the hypothesis that $A$ is free
    in each degree, and $d$ is even because $\alpha^2\ne0$ in a graded-commutative ring. With
    $a_n=q_n\alpha^n$ and $a_ia_j=m_{ij}a_{i+j}$ one gets $m_{ij}=q_iq_j/q_{i+j}$, and the recursion
    $q_{n+1}=q_1q_n/m_{1,n}$ determines the $q_n$ from the $m_{ij}$ up to the rescaling
    $\alpha\mapsto c\alpha$, so the rational coproduct is pinned by the integral ring. Two points
    worth recording as correct rather than automatic: $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$
    because $d$ is the least positive degree, so there are no decomposable terms of degree $d$; and
    cocommutativity is read off that displayed formula, not from the H-space being homotopy
    commutative, which is not assumed. Torsion-freeness of $A\otimes A$ is what carries the rational
    computation back to $\ZZ$, and it is used twice, once for the coproduct and once for
    commutativity and associativity of the Pontryagin product.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 15 of §3.C, printed p. 292. Correct throughout. $A\otimes\QQ=\QQ[\alpha]$
    with $A$ free in each degree gives $A_{nd}$ of rank one and nothing else in positive degrees,
    and $d$ even because $\alpha^2\ne0$ in a graded-commutative ring. With $a_n=q_n\alpha^n$ and
    $a_ia_j=m_{ij}a_{i+j}$ one has $m_{ij}=q_iq_j/q_{i+j}$, so the $q_n$ are determined by the
    integral ring up to rescaling $\alpha$; $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$ because
    $d$ is the least positive degree, so no decomposables occur, and multiplicativity of $\Delta$
    gives $\Delta(a_n)=\sum_i\binom ni(q_n/q_iq_{n-i})a_i\otimes a_{n-i}$. $A\otimes A$ is free, hence
    torsionfree, so the rational coproduct determines the integral one; the coproduct formula is
    cocommutative and coassociative as an identity on the generator, which is where those two Hopf
    axioms come from without assuming the H-space multiplication is homotopy commutative or
    associative; dualizing gives the Pontryagin product, $H_*$ being degreewise finite free.
    Nothing changed. Not claimed: a published solution, and no certificate.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, each carrying a `pf-proof`, and the closing summary sentence is kept
    outside the proof. The arguments are the ones the two reviews recorded as correct, now
    distributed over the steps; nothing is strengthened. Cited by number only: the Künneth
    isomorphism for free finitely generated graded pieces, and the universal coefficient
    theorem over $\ZZ$ in the form that cohomology is dual to homology when the groups are free.
    Checked: that $A$ is a domain because $A\to A\otimes\QQ$ is injective into $\QQ[\alpha]$;
    that $m_{ij}\ne0$; that $q_{n+1}=q_1q_n/m_{1,n}$ determines the $q_n$ from the integral
    constants up to rescaling $\alpha$; that only the degrees $0$ and $d$ contribute to
    $\Delta(\alpha)$; and that the twist carries the sign $+1$ because $d$ is even.
---

::: {.problem}
Suppose that $X$ is a path-connected H-space such that $H^*(X; \ZZ)$ is free and finitely generated in each dimension, and $H^*(X; \QQ)$ is a polynomial ring $\QQ[\alpha]$.
Show that the Pontryagin ring $H_*(X; \ZZ)$ is commutative and associative, with a structure uniquely determined by the ring $H^*(X; \ZZ)$.
:::

::: {.solution}

Put $A=H^*(X;\ZZ)$, with $\alpha$ of degree $d$.

::: pf

::: pf-step
Each graded piece of $A$ is free of finite rank, and $A\otimes\QQ\cong\QQ[\alpha]$.

::: pf-proof
The first clause is the hypothesis, and tensoring a free graded abelian group of finite rank with $\QQ$ gives a rational vector space of the same rank in each degree. The hypothesis on the rational cohomology is that this graded ring is the polynomial ring on one generator $\alpha$ of degree $d$, so $A\otimes\QQ$ is $\QQ$ in degrees $nd$ and $0$ in the other positive degrees.
:::

:::

::: pf-step
The degree $d$ is even; $A^{nd}$ has rank one for every $n\ge0$, and every other positive-degree group vanishes.

::: pf-proof
By step 1 the dimension of $(A^k\otimes\QQ)$ equals the rank of the free group $A^k$, so the rank of $A^k$ is $1$ when $k=nd$ and $0$ otherwise. For the parity: $A$ is graded-commutative, so $\alpha^2=(-1)^{d\cdot d}\alpha^2=(-1)^d\alpha^2$; and $\alpha^2\ne0$, because $\alpha^2=0$ would make $\QQ[\alpha]$ spanned by $1$ and $\alpha$ over $\QQ$, a finite-dimensional algebra, whereas a polynomial ring in one variable is infinite-dimensional. Hence $(-1)^d=1$ and $d$ is even.
:::

:::

::: pf-step
Choosing a generator $a_n$ of $A^{nd}$ with $a_0=1$, the integral ring determines integers $m_{ij}\ne0$ by $a_ia_j=m_{ij}a_{i+j}$; after tensoring with $\QQ$, writing $a_n=q_n\alpha^n$ with $q_n\in\QQ^\times$, one has $m_{ij}=q_iq_j/q_{i+j}$, so the $q_n$ are determined by $A$ up to the rescaling $\alpha\mapsto c\alpha$.

::: pf-proof
$a_ia_j$ lies in $A^{(i+j)d}$, which has rank one with generator $a_{i+j}$ by step 2, so $a_ia_j=m_{ij}a_{i+j}$ for a unique integer $m_{ij}$. It is nonzero because $A$ is a domain: $A$ is torsion-free, being free, so $A\to A\otimes\QQ$ is injective, and $A\otimes\QQ\cong\QQ[\alpha]$ is a domain. Tensoring the relation with $\QQ$ and substituting $a_n=q_n\alpha^n$ gives $q_iq_j\alpha^{i+j}=m_{ij}q_{i+j}\alpha^{i+j}$, hence $m_{ij}=q_iq_j/q_{i+j}$. Reading this with $i=1$ gives $q_{n+1}=q_1q_n/m_{1,n}$, and $q_0=1$, so all $q_n$ are determined by $q_1$ and the $m_{ij}$; replacing $\alpha$ by $c\alpha$ replaces every $q_n$ by $c^{-n}q_n$ and leaves the $m_{ij}$, being integral, unchanged.
:::

:::

::: pf-step
The coproduct $\Delta$ induced by the H-space multiplication satisfies $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$ and hence, being an algebra homomorphism,
$$
\Delta(\alpha^n)=\sum_{i=0}^n\binom ni\alpha^i\otimes\alpha^{n-i}.
$$

::: pf-proof
$\Delta$ is the map on cohomology induced by the multiplication $X\times X\to X$, using the Künneth isomorphism $H^*(X\times X)\cong H^*(X)\otimes H^*(X)$, which holds integrally because each graded piece of $H^*(X)$ is free of finite rank; it is a homomorphism of graded rings, so $\Delta(1)=1\otimes1$. The degree-$d$ part of $A\otimes A$ splits as the sum of $A^i\otimes A^{d-i}$ over $i$; for $0<i<d$ the group $A^i$ vanishes by step 2, so only $i=0$ and $i=d$ contribute, giving $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$. Applying the ring homomorphism property to the $n$-th power and using that $A\otimes A$ is graded-commutative with $d$ even, so that $\alpha\otimes1$ and $1\otimes\alpha$ commute, gives the binomial expansion.
:::

:::

::: pf-step
Therefore
$$
\Delta(a_n)=\sum_{i=0}^n\binom ni\frac{q_n}{q_iq_{n-i}}a_i\otimes a_{n-i},
$$
whose coefficients are determined by the integral ring; since $A\otimes A$ is torsion-free, the integral coproduct is determined by its rationalisation, hence by $A$.

::: pf-proof
In $A\otimes\QQ$ we have $a_n=q_n\alpha^n$, so step 4 gives $\Delta(a_n)=q_n\sum_i\binom ni\alpha^i\otimes\alpha^{n-i}$, and replacing $\alpha^i$ by $a_i/q_i$ and $\alpha^{n-i}$ by $a_{n-i}/q_{n-i}$ gives the displayed formula. The classes $a_i\otimes a_{n-i}$ form a $\ZZ$-basis of the degree-$nd$ part of $A\otimes A$ by step 2 and the freeness, so the coefficients $\binom ni q_n/(q_iq_{n-i})$, which step 3 determines from $A$, determine $\Delta(a_n)$; and $A\otimes A$ is free, hence torsion-free, so two integral classes with the same image in $(A\otimes A)\otimes\QQ$ are equal. Since the $a_n$ generate $A$ as a ring and $\Delta$ is a ring homomorphism, $\Delta$ is determined on all of $A$.
:::

:::

::: pf-step
The Pontryagin product on $H_*(X;\ZZ)$ is dual to $\Delta$, and its structure constants are therefore determined by $H^*(X;\ZZ)$.

::: pf-proof
Each $H^k(X;\ZZ)$ is free of finite rank, so the natural map from cohomology to the dual of homology is an isomorphism in each degree (universal coefficients over $\ZZ$ with the $\Ext$ term vanishing). The Pontryagin product is the composite $H_*(X)\otimes H_*(X)\to H_*(X\times X)\to H_*(X)$ of the homology cross product with the map induced by the multiplication, and under the duality its adjoint is $\Delta$; hence the matrix of the product in the bases dual to the $a_n$ is the transpose of the matrix of $\Delta$, which step 5 determines from $A$.
:::

:::

::: pf-step
The Pontryagin product is commutative and associative.

::: pf-proof
Both $(\Delta\otimes1)\Delta$ and $(1\otimes\Delta)\Delta$ are ring homomorphisms $A\to A\otimes A\otimes A$ and both send $\alpha$ to $\alpha\otimes1\otimes1+1\otimes\alpha\otimes1+1\otimes1\otimes\alpha$ by step 4, so they agree after tensoring with $\QQ$; $A\otimes A\otimes A$ is free, hence torsion-free, so they agree integrally, which is coassociativity. Likewise $\Delta$ and $\tau\Delta$, where $\tau$ is the graded twist, agree after tensoring with $\QQ$ because $\tau(\alpha^i\otimes\alpha^{n-i})=\alpha^{n-i}\otimes\alpha^i$ with sign $+1$ ($d$ even) and $\binom ni=\binom n{n-i}$, so they agree integrally, which is cocommutativity. Dualising by step 6 turns coassociativity into associativity and cocommutativity into commutativity of the Pontryagin product.
:::

:::

:::

Hence $H_*(X;\ZZ)$ is a commutative associative ring whose multiplication is uniquely determined by the ring $H^*(X;\ZZ)$.

:::
