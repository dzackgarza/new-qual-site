---
schema: qual/card@1
id: P-JHUSP01CAE
kind: problem
title: A nonconstant annulus map of constant boundary modulus has at least two zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros of Holomorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the annulus, nonconstancy, boundary modulus five and two-zero conclusion with Spring 2001 Complex Analysis question 5; made the boundary-value hypothesis explicit as continuity on the closed annulus."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Normalized to a proper disk map, proved every disk value has the same multiplicity count as zero, and ruled out degree one because it would biholomorphically identify the annulus with the simply connected disk."
---

::: {.problem}
Let $f$ be holomorphic on $A=\{1<|z|<2\}$ and continuous on its closure.
Assume that $f$ is nonconstant and $|f|=5$ on both boundary circles.
Show that $f$ has at least two zeros in $A$, counted with multiplicity.
:::


::: {.solution}
Set $F=f/5$.

<1>1. The normalized map sends the annulus properly into the unit disk.
::: {.proof}
The function $F$ is holomorphic on $A$, continuous on $\overline A$, and has
$|F|=1$ on both boundary circles. By the maximum modulus principle,
$|F|\le1$ on $A$. Since $F$ is nonconstant, it cannot attain modulus one at an
interior point, so
$$
|F(z)|<1\qquad(z\in A).
$$
Thus $F:A\to\Delta$.

Continuity and the boundary condition imply that for every $0<\rho<1$ there is
a collar of each boundary circle on which $|F|>\rho$. Hence the inverse image
under $F$ of the compact disk $\{|w|\le\rho\}$ lies in a compact subannulus.
It is closed there, so it is compact. Therefore $F:A\to\Delta$ is proper.
In particular its zeros form a finite set; let $N$ be their total multiplicity.
:::

<1>2. Every value $w\in\Delta$ has exactly $N$ preimages counted with multiplicity.
::: {.proof}
Fix $w\in\Delta$. Choose $\rho$ with $|w|<\rho<1$. By the boundary continuity
from step <1>1, choose radii $1<r_1<r_2<2$ so that every zero of $F$ lies in
$r_1<|z|<r_2$ and
$$
|F(z)|>\rho>|w|
$$
on both circles $|z|=r_1,r_2$.

For $0\le t\le1$, the function $F-tw$ has no zero on these two circles.
The argument-principle count of its zeros in the subannulus is therefore
constant in $t$: the boundary integral
$$
\frac1{2\pi i}\int_{\partial A_{r_1,r_2}}
\frac{F'(z)}{F(z)-tw}\,dz
$$
depends continuously on $t$ and takes integer values. At $t=0$ it equals $N$;
at $t=1$ it counts the solutions of $F(z)=w$, with multiplicity. No solution
lies in the omitted boundary collars because there $|F|>\rho>|w|$. Hence every
$w\in\Delta$ has exactly $N$ preimages counted with multiplicity.
:::

<1>3. The degree $N$ cannot be zero or one.
::: {.proof}
Choose any $z_0\in A$ and put $w_0=F(z_0)\in\Delta$. Step <1>2 shows that
$w_0$ has exactly $N$ preimages counted with multiplicity, and it has at least
the preimage $z_0$. Thus $N\ge1$.

Suppose $N=1$. Then step <1>2 says every $w\in\Delta$ has exactly one preimage,
and that preimage has multiplicity one. Consequently $F$ is bijective and has
nonzero derivative everywhere. The holomorphic inverse function theorem gives
a holomorphic local inverse at every point, so the set-theoretic inverse
$F^{-1}:\Delta\to A$ is holomorphic. Thus $F$ would be a biholomorphism.

But a biholomorphism is a homeomorphism and therefore preserves simple
connectedness. The unit disk is simply connected, whereas the annulus is not:
the loop $t\mapsto(3/2)e^{2\pi it}$ has winding number one about zero and cannot
be contracted inside $A$. This contradiction rules out $N=1$.
Therefore $N\ge2$, so $f$ has at least two zeros in the annulus, counted with
multiplicity.
:::
:::
