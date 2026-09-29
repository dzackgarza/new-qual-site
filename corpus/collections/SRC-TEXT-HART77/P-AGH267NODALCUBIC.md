---
schema: qual/card@1
id: P-AGH267NODALCUBIC
kind: problem
title: Degree-zero Cartier classes on a nodal cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cartier Divisors
  - Singular Curves
  - Multiplicative Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read Exercise II.6.7 and Example II.6.11.4 in the Hartshorne transcription. Distinguished Cartier divisor classes from divisors and made the algebraically closed field and characteristic restriction explicit. The solution computes the normalization, the branch-value condition for local units, and the resulting multiplicative coordinate.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic different from two, and let
$$
X=V(y^2z-x^3-x^2z)\subseteq\PP_k^2.
$$
Its node is $N=[0:0:1]$, and put $O=[0:1:0]$.
Imitate Example II.6.11.4: define degree on Cartier divisor classes by moving a representative away from $N$, and show that the degree-zero class group $\operatorname{CaCl}^0(X)$ is naturally isomorphic to the multiplicative group $\GG_m$.
:::

::: {.solution}
The [[D-5PQ5W|Cartier class group]] means Cartier divisors modulo principal Cartier divisors, not the group of Cartier divisors before taking this quotient.
We construct its degree map and an explicit isomorphism $\operatorname{CaCl}^0(X)\cong k^\times$.
We then identify the associated group variety with $\GG_m$.

::: pf

::: {.pf-step #s1}
The normalization of $X$ is $\PP_k^1$, with parameter $t=y/x$ and map
$$
\nu([u:v])=[v(u^2-v^2):u(u^2-v^2):v^3].
$$
The two points over $N$ are $t=1,-1$, and $\nu(\infty)=O$.

::: pf-proof
On $z=1$ the equation is $y^2=x^2(x+1)$, and the parametrization is
$$
x=t^2-1,\qquad y=t(t^2-1).
$$
It has rational inverse $t=y/x$ wherever $x\ne0$.
The affine coordinate ring embeds under this substitution: write an element as $p(x)+yq(x)$ and separate the even and odd powers of $t$ in its image to see that a zero image forces $p=q=0$.
These formulas homogenize to the stated map, whose three coordinates have no common zero.
They send precisely $t=\pm1$ to $N$ and send $\infty$ to $O$.

On the affine chart, put $A=k[t^2-1,t(t^2-1)]\subseteq k[t]$.
The parameter $t$ is integral over $A$, satisfying $t^2-(x+1)=0$, and $\operatorname{Frac}(A)=k(t)$.
Thus $k[t]$ is a finite normal birational extension of $A$, and is its integral closure: any element of $k(t)$ integral over $A$ is also integral over $k[t]$, so belongs to $k[t]$.
Near $O$, use $u=1$ and $w=v/u$; on the chart $y\ne0$ the map is
$$
x/y=w,\qquad z/y=\frac{w^3}{1-w^2},
$$
and has regular inverse $w=x/y$ near $O$.
This proves the [[D-QJ5M9|normalization]] assertion and gives
$$
U\coloneqq X\setminus\{N\}\cong\PP_k^1\setminus\{1,-1\}.
$$
The affine partial derivatives show that $N$ is the only singular point: a singular affine point must have $y=0$ and $x\in\{0,-1\}$, but the $x$-derivative is nonzero at $(-1,0)$.
The point $O$ is smooth since the $z$-derivative there is $1$.
At $N$ the tangent cone is $(y-x)(y+x)$, with distinct factors, so it is a node.
:::

:::

::: {.pf-step #s2}
A rational function $f\in k(t)$ is a unit at $N$ if and only if it is regular and nonzero at $t=\pm1$ and $f(1)=f(-1)$.

::: pf-proof
For the affine ring of step [](#s1){.pf-ref},
$$
A=k+(t^2-1)k[t]=\{a(t)\in k[t]:a(1)=a(-1)\}.
$$
To see the first equality, every $(t^2-1)t^{2j}$ equals $x(x+1)^j$ and every $(t^2-1)t^{2j+1}$ equals $y(x+1)^j$, so all multiples of $t^2-1$ belong to $A$.
Conversely, the two generators vanish at both $1$ and $-1$.
For the second equality, subtract the common value from a polynomial and divide by the two relatively prime factors $t-1,t+1$.

The maximal ideal of $N$ consists of the elements with common value zero.
Consequently every element of $\OO_{X,N}$ is regular at both branch points and has equal values there; a unit has nonzero common value.

Conversely, write a rational function regular at both points as $f=p(t)/q(t)$ with $q(1)q(-1)\ne0$.
The denominator $q(t)q(-t)$ belongs to $A$ and has nonzero common value at the two points.
If $f(1)=f(-1)$, the numerator $p(t)q(-t)$ also has equal values there and therefore belongs to $A$.
Thus
$$
f=\frac{p(t)q(-t)}{q(t)q(-t)}\in\OO_{X,N}.
$$
If the common value is nonzero, the same argument applies to $1/f$, proving the unit criterion.
:::

:::

::: {.pf-step #s3}
Every Cartier class has a representative supported on $U$, and the sum of its point coefficients defines a degree homomorphism $\operatorname{CaCl}(X)\to\ZZ$.

::: pf-proof
For a Cartier divisor $D$, choose its rational local equation $f$ on a neighborhood of $N$.
Subtracting the principal Cartier divisor of $f$ makes its local equation $1$ there.
Since $U$ is smooth, the resulting divisor is a finite sum $\sum_P n_P[P]$ of points of $U$.
Conversely, each point of $U$ defines a Cartier divisor on $X$, with local equation $1$ near $N$.

Two such divisors represent the same Cartier class precisely when their difference is the divisor on $U$ of a rational function that is a unit at $N$.
By step [](#s2){.pf-ref}, this function has no zero or pole at either point over $N$.
Its divisor on $\PP^1$ is therefore supported on $U$ and has total degree zero.
It follows that $\sum_P n_P$ depends only on the Cartier class and is additive.
This degree map is surjective since $[O]$ has degree one.
Its kernel is the stated group $\operatorname{CaCl}^0(X)$, as in [@Har10a, Example II.6.11.4].
:::

:::

::: {.pf-step #s4}
Taking the ratio of the two branch values gives an isomorphism $\Phi:\operatorname{CaCl}^0(X)\to k^\times$.

::: pf-proof
Represent a degree-zero Cartier class by a divisor $D$ supported on $U$ and regard $D$ as a divisor on $\PP^1$.
There is a rational function $F_D$ with $\operatorname{div}_{\PP^1}(F_D)=D$.
Explicitly, if the coefficients at finite parameters $a$ are $n_a$, take
$$
F_D(t)=\prod_{a\in k\setminus\{1,-1\}}(t-a)^{n_a};
$$
the coefficient at $\infty$ is $-\sum_a n_a$ because $D$ has degree zero.
All but finitely many exponents vanish.
There is no zero or pole at $\pm1$, so define
$$
\Phi(\operatorname{cl}D)=\frac{F_D(1)}{F_D(-1)}\in k^\times.
$$

Changing $F_D$ multiplies it by a nonzero constant, which does not change the ratio: a rational function on $\PP^1$ with zero divisor is constant by factoring its numerator and denominator.
Changing $D$ by the divisor of a unit at $N$ also leaves the ratio unchanged, by step [](#s2){.pf-ref}.
Multiplication of the functions proves that $\Phi$ is a homomorphism.
If $\Phi(\operatorname{cl}D)=1$, then $F_D$ has equal nonzero branch values and is a unit at $N$ by step [](#s2){.pf-ref}.
Thus $D$ is principal as a Cartier divisor on $X$, proving injectivity.

For the point $P_a=\nu(a)$, where $a\in k\setminus\{1,-1\}$, take $D=[P_a]-[O]$ and $F_D=t-a$.
Then
$$
\Phi(\operatorname{cl}([P_a]-[O]))=\frac{1-a}{-1-a}=\frac{a-1}{a+1}.
$$
Every $\lambda\in k^\times\setminus\{1\}$ is obtained by taking $a=(1+\lambda)/(1-\lambda)$, which is neither $1$ nor $-1$ since $\lambda\ne0$ and $\operatorname{char}k\ne2$.
The value $1$ is obtained from the zero class, represented by $[O]-[O]$.
This proves surjectivity and the group isomorphism.
:::

:::

::: {.pf-step #s5}
The multiplicative coordinate realizes the isomorphism as one of group varieties.

::: pf-proof
The map $P\mapsto\operatorname{cl}([P]-[O])$ from $U(k)$ to $\operatorname{CaCl}^0(X)$ is a bijection by step [](#s4){.pf-ref}: its composite with $\Phi$ is
$$
\boxed{\lambda=\frac{t-1}{t+1},\qquad \lambda(O)=1}.
$$
This is a fractional linear isomorphism $\PP^1\setminus\{1,-1\}\to\GG_m$, not merely a bijection of points.
Its inverse in homogeneous coordinates is
$$
\lambda\longmapsto[u:v]=[1+\lambda:1-\lambda],
$$
followed by $\nu$.
The formulas are regular on their domains, including $\lambda=1$, which maps to $O$.
They transport multiplication on $\GG_m$ to the group law induced by Cartier classes on $U$.
In particular, the group law and inversion on $U$ are morphisms, and $\operatorname{CaCl}^0(X)$, realized by $U$ as in Example II.6.11.4, is the group variety $\GG_m$.
:::

:::

::: pf-qed
Step [](#s3){.pf-ref} constructs the degree-zero Cartier class group, step [](#s4){.pf-ref} gives its branch-ratio isomorphism with $k^\times$, and step [](#s5){.pf-ref} gives the corresponding isomorphism of group varieties.
:::

:::
:::

::: {.remark}
The distinction between divisors and divisor classes is essential: the relation imposed in step [](#s3){.pf-ref} is precisely the quotient by principal Cartier divisors.
The two branches must also be distinct; in characteristic two the tangent cone is a repeated line, so this equation does not define a nodal cubic.
Interchanging the two branches replaces $\lambda$ by $\lambda^{-1}$.
:::
