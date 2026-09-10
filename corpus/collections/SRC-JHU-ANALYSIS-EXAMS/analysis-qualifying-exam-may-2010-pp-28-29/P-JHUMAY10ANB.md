---
schema: qual/card@1
id: P-JHUMAY10ANB
kind: problem
title: All integral values over simple closed curves avoiding two poles
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the integrand and the simple, smooth, closed curve restriction with May 2010 problem 2 in the retained extraction; replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Computed both residues, imposed the common orientation sign on enclosed poles, and supplied explicit smooth circles realizing every listed value."
---

2. Find all possible values of

$$
\int _ { \gamma } { \frac { e ^ { \pi z } } { ( z - 1 ) ( z - i ) ^ { 2 } } } d z
$$

where γ ranges over all simple closed smooth curves contained in $\mathbb { C } \setminus \{ 1 , i \}$ . (A simple closed curve is a closed curve that does not intersect itself; i.e., it is a homeomorphic image of the circle.)

You do not need to give a proof for your answer to this problem, but show all your work.

::: solution
Set
$$
A=-\pi e^\pi,\qquad B=-\pi(\pi+1)+i\pi^2.
$$
The complete set of values is
$$
\boxed{\{0,A,-A,B,-B,A+B,-A-B\}.}
$$

<1>1. The two poles give the contributions $A$ and $B$ for positive winding number one.

::: proof
Write $F(z)=e^{\pi z}/((z-1)(z-i)^2)$. At the simple
pole $1$,
$$
\operatorname{Res}_{1}F=\frac{e^\pi}{(1-i)^2}
=\frac{i e^\pi}{2},
\qquad 2\pi i\operatorname{Res}_{1}F=A.
$$
At the double pole $i$, the derivative formula gives
$$
\begin{aligned}
\operatorname{Res}_{i}F
&=\left.\frac{d}{dz}\frac{e^{\pi z}}{z-1}\right|_{z=i}\\
&=-\frac{\pi}{i-1}+\frac1{(i-1)^2}
=\frac\pi2+\frac{i(\pi+1)}2,
\end{aligned}
$$
where $e^{\pi i}=-1$, $(i-1)^{-1}=(-1-i)/2$, and
$(i-1)^{-2}=i/2$. Multiplication by $2\pi i$ gives $B$.
These are the only poles [@SS03].
:::

<1>2. A simple closed curve allows exactly the displayed residue combinations.

::: proof
A simple closed smooth curve has index zero at every
point of its unbounded complementary component and a
common index $\varepsilon\in\{1,-1\}$ at every point
of its bounded component, according to orientation
[@SS03]. The two poles may lie outside, only $1$ may
lie inside, only $i$ may lie inside, or both may lie
inside. The residue theorem consequently gives, respectively,
$$
0,\qquad \varepsilon A,\qquad \varepsilon B,
\qquad \varepsilon(A+B).
$$
In particular a curve cannot have index $1$ at one
enclosed pole and $-1$ at the other while remaining simple.
Thus no other combination is allowed.
:::

<1>3. Every listed value is attained.

::: proof
The circle $|z|=1/4$ encloses neither pole. The circles
$|z-1|=1/4$ and $|z-i|=1/4$ enclose exactly $1$ and
$i$, respectively, because their distance is $\sqrt2$.
The circle $|z|=2$ encloses both. None passes through
a pole, and all are smooth and simple. Counterclockwise
orientation gives $0,A,B,A+B$; reversing the last three
orientations gives their negatives. This proves both
attainability and exhaustion of the stated set.
:::
:::
