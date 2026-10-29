---
schema: qual/card@1
id: T-CRVCMCFT
kind: theorem
title: For a CM curve, $j$ is an algebraic integer and $K(j)/K$ is abelian of degree $h(R)$
slogan: 'Complex multiplication turns $j$ into a class-field generator: $K(j)/K$ has Galois group $\Pic(R)$, and $j\in\ZZ$ exactly when $h(R)=1$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Complex Multiplication
  - Number Theory
relations:
- kind: uses
  target: T-CRVCM
- kind: related-to
  target: T-CRVMODJ
review: draft
prompts:
- What is the arithmetic nature of $j$ for a curve with complex multiplication?
- Which field does $j$ generate over $K$, and what is its Galois group?
- When is $j$ a rational integer, and how many such curves are there?
- Why is the count thirteen and not nine?
---

::: {.theorem title="Complex multiplication and class field theory"}
Let $E/\CC$ have complex multiplication by the order $R$ of discriminant $D$ in the imaginary quadratic field $K$, and let
$$
h(R)\coloneqq\abs{\Pic(R)}
$$
be the class number of that order.
Then:

- $j(E)$ is an algebraic integer;

- $[K(j(E)) : K] = h(R)$, and $K(j(E))/K$ is abelian, with
  $$
  \Gal\bigl(K(j(E))/K\bigr)\cong\Pic(R);
  $$

- $j(E) \in \ZZ$ if and only if $h(R) = 1$.

There are exactly thirteen orders with $h(R) = 1$, so exactly thirteen values of $j$ arise this way, namely those of discriminant
$$
D \in \theset{ -3,\ -4,\ -7,\ -8,\ -11,\ -12,\ -16,\ -19,\ -27,\ -28,\ -43,\ -67,\ -163 } .
$$
:::

::: {.remark title="Thirteen orders, nine fields"}
The two counts refer to different objects: fields versus orders.

**Nine** is the number of imaginary quadratic *fields* of class number one: $d_K \in \theset{-3,-4,-7,-8,-11,-19,-43,-67,-163}$.
That is the Baker--Heegner--Stark theorem, and it is a statement about maximal orders only.

**Thirteen** is the number of imaginary quadratic *orders* of class number one, and an order need not be maximal.
Beyond the nine maximal ones there are four more, each a non-maximal order of conductor $f$ inside a field already on the list:
$$
D = -12 \ (f=2 \text{ in } \QQ(\sqrt{-3})), \quad
-16 \ (f=2 \text{ in } \QQ(i)), \quad
-27 \ (f=3 \text{ in } \QQ(\sqrt{-3})), \quad
-28 \ (f=2 \text{ in } \QQ(\sqrt{-7})) .
$$
Endomorphism rings of elliptic curves range over all orders, not just maximal ones, so the relevant count for CM $j$-invariants is thirteen.
The $\tau = 2i$ curve is exactly the $D = -16$ entry, and its $j$-invariant is the rational integer $66^3 = 287496$.
For example, $D=-4$ gives $j=1728$, $D=-3$ gives $j=0$, and $D=-163$ gives $j=-640320^3$, which explains the near-integrality of $e^{\pi\sqrt{163}}$.
:::

::: {.remark}
Complex multiplication is read off from a lattice parameter $\tau$ ([[T-CRVCM]]), but recovering $\tau$ from an algebraic equation is a transcendental computation.
The theorem gives an arithmetic test on $j$ itself: every CM $j$-invariant is an algebraic integer, so a transcendental or non-integral value of $j$ rules out complex multiplication.
For the Legendre curve
$$
y^2=x(x-1)(x-3),
$$
one has
$$
j=\frac{2^6\cdot7^3}{3^2},
$$
which is not an algebraic integer; hence this elliptic curve does not have complex multiplication.

By the Galois statement, $K(j)$ is the ring class field of $R$, and for $R = \OO_K$ it is the Hilbert class field, the maximal unramified abelian extension of $K$.
Thus singular moduli generate the ring class fields of imaginary quadratic orders. Obtaining arbitrary abelian extensions of $K$ requires additional special values, for example Weber-function values at torsion points; the $j$-invariant alone does not generate every abelian extension of $K$.
The isomorphism $\Gal \iso \Pic(R)$ is induced by the action of the class group on lattices --- a class $[\mathfrak{a}]$ sends $\CC/\Lambda$ to $\CC/\mathfrak{a}^{-1}\Lambda$, which is another curve with the same $R$, and this action is simply transitive on the isomorphism classes.
That is also why $j$ has exactly $h(R)$ conjugates: they are the $j$-invariants of the $h(R)$ curves in one orbit.
:::
