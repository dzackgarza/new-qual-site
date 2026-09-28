---
title: Elliptic curves over $\CC$
order: 5
topics:
- Elliptic Curves
- Elliptic Functions
- Complex Multiplication
---

# Elliptic curves over $\CC$

Over $\CC$, every elliptic curve $E$ is isomorphic to $\CC/\Lambda$ for a lattice $\Lambda$, unique up to homothety, and to a Legendre curve $y^2=x(x-1)(x-\lambda)$.
For $\Lambda=\ZZ+\ZZ\tau$ the $j$-invariant is $j(\tau)$, and for the Legendre curve it is $2^8(\lambda^2-\lambda+1)^3/(\lambda^2(\lambda-1)^2)$.

## The functions

[[D-CRVWEIER]]

The residues of an elliptic function sum to zero on $\CC/\Lambda$, so a nonconstant elliptic function has degree at least $2$, and $\wp$, with a double pole at $0$, has degree exactly $2$.
A holomorphic elliptic function is bounded on a fundamental parallelogram, hence constant; so two elliptic functions with the same principal parts differ by a constant, and comparing principal parts at $0$ proves $(\wp')^2=4\wp^3-g_2\wp-g_3$.

## From a lattice to a cubic

[[T-CRVUNIF]]

By the differential equation, $z\mapsto[\wp(z):\wp'(z):1]$, with $0\mapsto[0:1:0]$, maps $\CC/\Lambda$ into the cubic $y^2=4x^3-g_2x-g_3$.
The map is bijective: $\wp$ is even of degree $2$, so $\wp(z)=\wp(w)$ exactly when $w\equiv\pm z$, and $\wp'(-z)=-\wp'(z)$ separates $z$ from $-z$ unless $2z\in\Lambda$.

By Abel's theorem on the torus, the chord-and-tangent law on the cubic corresponds to addition on $\CC/\Lambda$, so the uniformization $\CC/\Lambda\to E$ is a group isomorphism.
In particular $E[n]\cong\tfrac{1}{n}\Lambda/\Lambda\cong(\ZZ/n)^2$.

## The modular function

[[T-CRVMODJ]]

Under $\Lambda\mapsto\alpha\Lambda$, both $g_2^3$ and $\Delta$ scale by $\alpha^{-12}$, so $J$ depends only on the homothety class of $\Lambda$.
The group is $\SL_2(\ZZ)$ because $\Im\qty{\tfrac{a\tau+b}{c\tau+d}}=(ad-bc)\Im\tau/\abs{c\tau+d}^2$: a matrix of determinant $-1$ sends $\HH$ to the lower half plane.

Since each $\SL_2(\ZZ)$-orbit meets the fundamental region once, $J$ is a bijection from isomorphism classes of elliptic curves over $\CC$ onto $\CC$.
The points of the fundamental region with nontrivial stabilizer in $\PSL_2(\ZZ)$ are $\tau=i$, of order $2$, and $\tau=\rho$, of order $3$; these are the curves with $j=1728$ and $j=0$, the only ones with automorphism group larger than $\{\pm1\}$.

## Complex multiplication

[[T-CRVCM]]

The endomorphism ring $R_\Lambda=\{\alpha\in\CC\st\alpha\Lambda\subseteq\Lambda\}$ lies in $\Lambda$, so it is either $\ZZ$ or an order in an imaginary quadratic field.
The order need not be maximal: $\tau=2i$ gives $\ZZ[2i]$, of conductor $2$ in $\ZZ[i]$.

[[T-CRVCMCFT]]

Nine imaginary quadratic fields have class number one, and thirteen imaginary quadratic orders have class number one; endomorphism rings of CM elliptic curves range over all orders.
The four non-maximal orders among the thirteen have discriminants $-12$, $-16$, $-27$, and $-28$.

If $j(E)$ is not an algebraic integer, then $E$ has no complex multiplication.
