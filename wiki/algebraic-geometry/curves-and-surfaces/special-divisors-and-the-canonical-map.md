---
title: Special divisors and the canonical map
order: 10
topics:
- Special Divisors
- Canonical Map
- Gonality
---

# Special divisors and the canonical map

A divisor $D$ on a smooth projective curve $C$ of genus $g$ is special when $h^1(C,\OO_C(D))>0$, and Serre duality reads that condition as $\ell(D)>\deg D+1-g$, so a special divisor carries more sections than its degree forces ([[D-CRVSPEC]]).
Above degree $2g-2$ no divisor is special, and below it the correction term $\ell(K_C-D)$ is what Riemann--Roch leaves undetermined; Clifford's theorem bounds it from above, and beyond the trivial and the canonical divisor the bound is attained only by multiples of a hyperelliptic pencil.
The canonical system sits at the top of the special range: for a divisor of degree $2g-2$ Clifford gives $\ell(D)\le g$ with equality exactly when $D\sim K$, so $\linearsystem{K_C}$ is the unique linear system of that degree and dimension.
It is base-point free for $g\ge2$, and for $g\ge3$ the map it defines embeds $C$ exactly when $C$ carries no degree-two map to $\PP^1$.

## The index of speciality

[[D-CRVSPEC]]

Riemann--Roch for a divisor $D$ on a curve of genus $g$ is $\ell(D)-\ell(K-D)=\deg D+1-g$ [@Har77, Theorem IV.1.3], so $\ell(D)\ge\deg D+1-g$ always, with equality exactly for the nonspecial divisors.
Two consequences are used throughout: a divisor of negative degree has $\ell(D)=0$, since an effective divisor has nonnegative degree; and a divisor of degree at least $g$ has $\ell(D)\ge1$.
The canonical divisor itself is special, because $\ell(K-K)=\ell(0)=1$, and $\deg K=2g-2$ [@Har77, Example IV.1.3.3].
Speciality is a property of the divisor class, since $\ell$ depends only on $\OO_C(D)$.

## Clifford's theorem

[[T-CRVCLIFF]]

The theorem as printed in [@Har77, Theorem IV.5.4] is $\dim\linearsystem{D}\le\tfrac12\deg D$ for an effective special $D$, with equality if and only if $D=0$, or $D=K$, or $C$ is hyperelliptic and $D$ is a multiple of the unique $g^1_2$; in the form $\ell(D)\le\tfrac12\deg D+1$ the three equality cases are $D=0$, $D\sim K$, and multiples of the hyperelliptic pencil ([[T-CRVCLIFF]]).
The hypothesis that $D$ be special is not removable: a nonspecial divisor of degree $2g+2$ has $\ell(D)=g+3$, while $\tfrac12\deg D+1=g+2$, so the bound fails outside the special range.

The equality case is attained and can be computed.
On a hyperelliptic curve of genus $g\ge2$ with pencil $g^1_2$, the linear system $\linearsystem{m\,g^1_2}$ has degree $2m$ and $\ell=2m+1-g+\ell\bigl((g-1-m)g^1_2\bigr)=m+1$ for $1\le m\le g-1$, which is Clifford's bound exactly; at $m=g-1$ this is the identity $\linearsystem{K}=(g-1)g^1_2$ ([[D-CRVHYP]]).

The theorem is stated for effective divisors, and that is enough: a special divisor with $\ell(D)\ge1$ is linearly equivalent to an effective one, so the bound $\ell(D)\le\tfrac12\deg D+1$ holds for every special divisor whose linear system is nonempty ([[T-CRVCLIFF]]).
Read as a bound on the degree it says that a special $g^r_d$ has $d\ge2r$, and that a $g^r_d$ with $d\le2r-1$ is nonspecial, its dimension being then computed by Riemann--Roch alone.

## The canonical map

[[T-D8TUX]]

For $g\ge2$ the canonical system has no base points [@Har77, Lemma IV.5.1], so it defines a morphism $\varphi_K\colon C\to\PP^{g-1}$, and $\ell(K)=g$ gives the dimension of the target.
The morphism is very ample if and only if $C$ is not hyperelliptic [@Har77, Proposition IV.5.2], so for a nonhyperelliptic curve of genus $g\ge3$ it is a closed embedding whose image has degree $\deg K=2g-2$, the canonical model of $C$.
In genus $0$ the system $\linearsystem{K}$ is empty and in genus $1$ it consists of the single divisor $K\sim0$, so the canonical map is defined and interesting only from genus $2$ on.

The proof of very ampleness is a separation count, and it is the reason the hyperelliptic pencil is the only obstruction.
For $K$ to be very ample one needs $\ell(K-p-q)=g-2$ for every pair of points, including $p=q$, equivalently $\dim\linearsystem{K-p-q}=g-3$; Riemann--Roch gives $\ell(K-p-q)=g-3+\ell(p+q)$, so the condition is $\ell(p+q)=1$, and a pair with $\ell(p+q)=2$ spans a $g^1_2$ [@Har77, Proposition IV.5.2], so the canonical map is an embedding exactly when no such pair exists ([[T-D8TUX]]).
The same criterion gives the general statement used on curves: a divisor $D$ of degree at least $2g+1$ is very ample [@Har77, Corollary IV.3.2].

## Hyperelliptic curves

[[D-CRVHYP]]

A hyperelliptic curve of genus $g\ge2$ has exactly one $g^1_2$, and its canonical morphism factors as the degree-two map to $\PP^1$ followed by the $(g-1)$-uple embedding, with image a rational normal curve of degree $g-1$ [@Har77, Proposition IV.5.3].
So the canonical image of a hyperelliptic curve is a rational normal curve of degree $g-1$ in $\PP^{g-1}$, and the canonical map is the degree-two map $C\to\PP^1$ followed by the $(g-1)$-uple embedding: it is two-to-one onto that rational normal curve and is not an embedding, so the image is not a model of $C$; what the canonical map records is the genus and the quotient by the hyperelliptic involution.
Every curve of genus $2$ is hyperelliptic, since $\linearsystem{K}$ is then itself a $g^1_2$ [@Har77, §IV.5], so all genus-two curves have the same canonical image, a rational normal curve of degree $1$.

The upshot for classification is that for $g\ge3$ a curve is determined by its canonical model unless it is hyperelliptic, and in the hyperelliptic case the canonical map sees only the quotient by the involution ([[D-CRVHYP]]).

## Gonality

[[D-CRVGON]]

The gonality of $C$ is the least $d$ for which $C$ carries a $g^1_d$, equivalently the least degree of a nonconstant morphism $C\to\PP^1$ ([[D-CRVGON]]).
Gonality $1$ forces $C\cong\PP^1$; gonality $2$ is hyperellipticity for $g\ge2$, and a genus-one curve also has gonality $2$.
A divisor with $\ell(D)=2$ produces a pencil: subtracting the base divisor from $\linearsystem{D}$ gives a base-point-free $g^1_{d'}$ with $d'\le\deg D$, so a special divisor of dimension one of degree $d$ forces gonality at most $d$.

That the set of such $d$ is nonempty needs no Brill--Noether theory: for a point $P$ the divisor $(g+1)P$ has $\ell\ge2$ by Riemann--Roch [@Har77, Theorem IV.1.3], so every smooth projective curve of genus $g$ has a $g^1_{g+1}$ and a nonconstant map to $\PP^1$ ([[D-CRVGON]]).
The sharper bound is Brill--Noether theory, stated with its own hypotheses over $\CC$ on [[D-CRVBRILLNOETHER]]: the number $\rho(g,1,d)=2d-g-2$ is nonnegative at $d=\lfloor (g+3)/2\rfloor$, so every curve of genus $g$ has a $g^1_d$ there, while a general curve has none below it and its gonality is exactly $\lfloor (g+3)/2\rfloor$.
For $g=3$ and $g=4$ the bound is $3$, so every nonhyperelliptic curve of genus $3$ or $4$ over $\CC$ is trigonal: on a smooth plane quartic the system $\abs{K-p}$ is a $g^1_3$ for each point $p$ [@Har77, Example IV.5.2.1], and a nonhyperelliptic curve of genus $4$ lies on a quadric whose rulings cut $g^1_3$'s, one of them when the quadric is a cone [@Har77, Example IV.5.2.2] ([[D-CRVGON]], [[FE-CRVLOWG]]).

## Low-genus canonical models

[[FE-CRVLOWG]]

In genus $3$ the canonical model of a nonhyperelliptic curve is a plane quartic, and conversely every smooth plane quartic has $\omega_C\cong\OO_C(1)$ and so is a canonical curve [@Har77, Example IV.5.2.1].
In genus $4$ the canonical model is a sextic curve in $\PP^3$, it lies on a unique irreducible quadric surface $Q$, and it is the complete intersection of $Q$ with an irreducible cubic surface [@Har77, Example IV.5.2.2].
When $Q$ is smooth it is $\PP^1\times\PP^1$ and the two rulings cut two $g^1_3$'s on $C$; when $Q$ is a quadric cone only the ruling of the cone survives, and $C$ has one $g^1_3$ ([[FE-CRVLOWG]]).

## Complete intersections are never hyperelliptic

[[PR-CRVHYPCI]]

If $C\subseteq\PP^n$ is a smooth complete intersection of hypersurfaces of degrees $d_1,\ldots,d_{n-1}$ and $g\ge2$, adjunction gives $\omega_C\cong\OO_C(a)$ with $a=\sum d_i-n-1$ and $2g-2=a\prod d_i$, so $a\ge1$ and $\omega_C$ is the restriction of a very ample line bundle, hence very ample [@Har77, Proposition II.8.20].
A hyperelliptic curve has a canonical map of degree $2$, so $C$ is not hyperelliptic ([[PR-CRVHYPCI]], [[D-CRVHYP]]).

The converse restricts sharply which canonical curves are complete intersections: for $C$ canonically embedded in $\PP^{g-1}$ as a complete intersection, $\omega_C\cong\OO_C(1)$ forces $\sum_{i=1}^{g-2}d_i=g+1$ with every $d_i\ge2$, hence $g\le5$, and the possible multidegrees are $(4)$ in $g=3$, $(2,3)$ in $g=4$, and $(2,2,2)$ in $g=5$ ([[PR-CRVHYPCI]]).

## Brill--Noether theory

[[D-CRVBRILLNOETHER]]

The Brill--Noether number $\rho(g,r,d)=g-(r+1)(g-d+r)$ is the expected dimension of the locus of $g^r_d$'s. Work over $\CC$, with $d\ge1$ and $r\ge0$. When $\rho\ge0$, every smooth projective curve $C$ of genus $g$ has nonempty $G^r_d(C)$ and $W^r_d(C)$; every component of $G^r_d(C)$ has dimension at least $\rho$, and the same holds for $W^r_d(C)$ when $r\ge d-g$ (Arbarello--Cornalba--Griffiths--Harris, *Geometry of Algebraic Curves, Volume I*, Chapter V, Existence Theorem (1.1)).
For a general $C$, $G^r_d(C)$ and $W^r_d(C)$ are empty when $\rho<0$; when $\rho\ge0$, $G^r_d(C)$ is reduced of pure dimension $\rho$, and $\dim W^r_d(C)=\rho$ (Arbarello--Cornalba--Griffiths--Harris, *Geometry of Algebraic Curves, Volume I*, Chapter V, Dimension Theorem (1.5)).
On a general curve $W^r_d\setminus W^{r+1}_d$ is smooth of dimension $\rho$ when $\rho\ge0$ (Gieseker--Petri) ([[D-CRVBRILLNOETHER]]).
Clifford's theorem is the reverse inequality in the case where $\rho$ is not the whole story: a special $g^r_d$ satisfies $d\ge2r$, with equality only for the trivial series, the canonical series, or a multiple of the hyperelliptic pencil, and $\linearsystem{K}$ itself is the case $r=g-1$, $d=2g-2$, $\rho=0$.
