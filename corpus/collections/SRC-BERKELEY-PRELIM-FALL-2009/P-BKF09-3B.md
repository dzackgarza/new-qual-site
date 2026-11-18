---
schema: qual/card@1
id: P-BKF09-3B
kind: problem
title: 'The Koebe function $z/(1-z)^2$: injectivity, Taylor series and image of the disk'
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Fall 2009
    solutions, Problem 3B, PDF pp. 5--6, the file named in the collection's provenance), now
    cited on the body. Two additions. The sheet's argument-principle sentence is replaced by
    Rouché's theorem applied on the circle of radius $\rho$, which gives the same conclusion -
    one zero of $f-a$ inside - without requiring a count of the zeros of $f$. And the
    maximality of the radius is proved, which neither the sheet nor the previous card did: for
    $r>1/4$ the point $-r'$ with $1/4<r'<r$ has modulus $r'<r$ and is not in $f(\DD)$, because
    $f(z)=-r'$ forces $r'z^2+(1-2r')z+r'=0$, whose roots have $\abs z^2=1$ when $r'>1/4$; with
    $1/4=f(3-2\sqrt2)$ attained, the answer $r=1/4$ is exact. The printed problem and the
    stated answer are unchanged.
---

::: {.problem}
Prove that the function $f(z)=\frac{z}{(1-z)^2}$ is injective on the disk $B_1(0)=\{z\in\CC\mid\abs{z}<1\}$.
Find the Taylor series about $z=0$, and determine its radius of convergence.
What is the maximal disk $B_r(0)=\{w\in\CC\mid\abs{w}<r\}$ such that $B_r(0)\subset f(B_1(0))$?
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Fall 2009 preliminary examination solutions, Problem 3B, PDF pp. 5–6** (`assets/attachments/f09solutions.pdf`, the file named in this collection's `provenance`): injectivity, the Taylor series, the radius, the bound $\abs{f(z)}\ge\rho/(1+\rho)^2$ on the circle $\abs z=\rho$, and the conclusion that every $\abs a<1/4$ is attained are that solution's. The card adds two things: the zero-count is replaced by Rouché's theorem, which is what the sheet's appeal to the argument principle amounts to, and the *maximality* of the radius $1/4$ is proved, which neither the sheet nor the previous version of this card did.

Throughout $f(z)=z/(1-z)^2$ on the unit disk $\DD=\theset{\abs z<1}$.

::: pf

::: {.pf-step #injective}
$f$ is injective on $\DD$.

::: pf-proof
Suppose $f(z_1)=f(z_2)$ with $\abs{z_i}<1$. Cross-multiplying, $z_1(1-z_2)^2=z_2(1-z_1)^2$, so
$$
z_1-z_2=z_1(1-2z_2+z_2^2)-z_2(1-2z_1+z_1^2)=z_2z_1^2-z_1z_2^2=z_1z_2(z_1-z_2).
$$
If $z_1\ne z_2$ this gives $1=z_1z_2$, whence $1=\abs{z_1}\abs{z_2}<1$, a contradiction. So $z_1=z_2$.

:::

:::

::: {.pf-step #series}
$f(z)=\sum_{n\ge1}nz^n$ for $\abs z<1$, and the radius of convergence is $1$.

::: pf-proof
$\frac1{(1-z)^2}=\frac{d}{dz}\frac1{1-z}=\sum_{n\ge0}(n+1)z^n$ for $\abs z<1$ by termwise differentiation of the geometric series, so $f(z)=z\sum_{n\ge0}(n+1)z^n=\sum_{n\ge1}nz^n$. Its radius of convergence is $\limsup_n n^{-1/n}=1$, and it cannot be larger: $f$ has a pole at $z=1$, so $f$ is not the restriction of a function holomorphic on any disk strictly containing $\DD$.

:::

:::

::: {.pf-step #circle-bound}
For $0<\rho<1$ and $\abs z=\rho$, $\abs{f(z)}\ge\rho/(1+\rho)^2$, with equality at $z=-\rho$.

::: pf-proof
$\abs{f(z)}=\abs z/\abs{1-z}^2$ and $\abs{1-z}\le1+\abs z=1+\rho$ by the triangle inequality, so $\abs{f(z)}\ge\rho/(1+\rho)^2$. At $z=-\rho$ one has $\abs{1-z}=1+\rho$ and $\abs z=\rho$, so equality holds.

:::

:::

::: {.pf-step #attained}
Every $a$ with $\abs a<1/4$ lies in $f(\DD)$.

::: pf-proof
The function $\rho\mapsto\rho/(1+\rho)^2$ increases on $(0,1)$ — its derivative is $(1-\rho)/(1+\rho)^3>0$ — and tends to $1/4$ as $\rho\to1^-$, so for $\abs a<1/4$ there is $\rho<1$ with $\abs a<\rho/(1+\rho)^2$. On the circle $\abs z=\rho$ we then have $\abs{a}<\abs{f(z)}$ by step [](#circle-bound){.pf-ref}, so by Rouché's theorem $f-a$ and $f$ have the same number of zeros in $\abs z<\rho$. $f$ has a simple zero at $0$ there, since $f(z)=z(1+2z+\cdots)$ with the bracket nonzero near $0$. So $f(z)=a$ has a solution with $\abs z<\rho<1$.

:::

:::

::: {.pf-step #maximal}
No disk $B_r(0)$ with $r>1/4$ is contained in $f(\DD)$, and $B_{1/4}(0)\subset f(\DD)$.

::: pf-proof
The containment for $r=1/4$ is step [](#attained){.pf-ref}. For maximality, let $r>1/4$ and choose $r'$ with $1/4<r'<r$; it suffices to show $-r'\notin f(\DD)$. If $f(z)=-r'$ then $z=-r'(1-z)^2$, that is
$$
r'z^2+(1-2r')z+r'=0 ,
$$
whose roots are $z=\bigl[(2r'-1)\pm\sqrt{1-4r'}\bigr]/(2r')$. Since $r'>1/4$ the discriminant is negative, the roots are complex conjugates, and each has
$$
\abs z^2=\frac{(2r'-1)^2+(4r'-1)}{4r'^2}=\frac{4r'^2-4r'+1+4r'-1}{4r'^2}=1 .
$$
So every solution of $f(z)=-r'$ has $\abs z=1$, and $-r'\notin f(\DD)$ although $\abs{-r'}=r'<r$. Hence $B_r(0)\not\subset f(\DD)$. For the record, $1/4$ itself is attained: $f(3-2\sqrt2)=1/4$ and $\abs{3-2\sqrt2}=3-2\sqrt2<1$.

:::

:::

::: {.pf-step #conclusion}
$f$ is injective on $\DD$, $f(z)=\sum_{n\ge1}nz^n$ with radius of convergence $1$, and the maximal disk contained in $f(\DD)$ is $B_{1/4}(0)$.

::: pf-proof
Steps [](#injective){.pf-ref}, [](#series){.pf-ref} and [](#maximal){.pf-ref} give the three assertions.

:::

:::

:::
:::
