---
schema: qual/card@1
id: P-JHUMAY11ANM
kind: problem
title: Residues on a twice-traversed limaçon
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
  note: "Read Fall 2010 problem 5 on PDF page 27; checked all three summands, the signed polar radius and the double traversal."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Computed each winding number by polynomial root counts rather than loop sketches, excluded every pole from the curve, and retained the nonzero contribution at one half."
---

5. Let $\gamma$ be the closed curve in the complex plane that is given in polar coordinates by $r = 2 + 3$ cos θ, $0 \leq \theta \leq 4 \pi$ , oriented in the direction of increasing θ. Let

$$
f ( z ) = \frac { e ^ { z } } { 2 z - 1 } + \frac { \sin ( 2 z ) } { ( z - 2 ) ^ { 2 } } + \frac { \cos ( 5 z ) } { ( z + 5 i ) ^ { 3 } } .
$$

Calculate $\int _ { \gamma } f ( z ) d z$

[Recall that in polar coordinates, $( - r , \theta )$ and $( r , \theta + \pi )$ give the same point in the plane.]

::: solution
The integral equals
$$
\boxed{4\pi i e^{1/2}+8\pi i\cos4}.
$$

<1>1. Each winding number is twice a quadratic root count.

::: proof
With $w=e^{i\theta}$, the actual complex parametrization is
$$
\gamma(\theta)=(2+3\cos\theta)e^{i\theta}
=P(w),\qquad P(w)=\frac32w^2+2w+\frac32.
$$
This identity remains valid when the polar radius is negative.
As $\theta$ increases from zero to $4\pi$, $w$ traverses
the unit circle counterclockwise twice. If $a$ is not on
$\gamma$, substitution and the argument principle give
$$
\operatorname{Ind}(\gamma,a)
=\frac2{2\pi i}\int_{|w|=1}\frac{P'(w)}{P(w)-a}\,dw
=2N_a,
$$
where $N_a$ counts the zeros of $P-a$ in $|w|<1$, with
multiplicity [@SS03]. The next step verifies the required
boundary nonvanishing for all three poles.
:::

<1>2. The winding numbers about $1/2$, $2$, and $-5i$ are $4$, $2$, and $0$.

::: proof
For $a=1/2$, the zeros of $P-a$ are
$$
w=\frac{-2\pm i\sqrt2}{3}.
$$
Both have squared modulus $6/9<1$, so $N_{1/2}=2$.
For $a=2$, the zeros are
$$
w=\frac{-2\pm\sqrt7}{3}.
$$
Since $2<\sqrt7<3$, the plus root lies in $(0,1/3)$,
whereas the minus root is less than $-4/3$.
Hence $N_2=1$, and neither root is on the unit circle.

For $a=-5i$, on $|w|=1$ one has
$$
\left|\frac32w^2+2w\right|\leq\frac72
<\left|\frac32+5i\right|=\frac{\sqrt{109}}2.
$$
Rouché's theorem gives $N_{-5i}=0$, by comparison with
the nonzero constant $3/2+5i$, and the strict inequality
also excludes boundary zeros [@SS03]. Step <1>1 now gives
the three asserted indices and shows that the integration
curve passes through none of the poles.
:::

<1>3. The indexed residue sum gives the answer.

::: proof
The three possible poles of $f$ are precisely $1/2$, $2$
and $-5i$. The residues at the two points with nonzero
winding number are
$$
\operatorname{Res}_{1/2}f=\frac{e^{1/2}}2,
\qquad
\operatorname{Res}_{2}f
=\left.\frac{d}{dz}\sin(2z)\right|_{z=2}=2\cos4.
$$
The remaining summands are holomorphic at each of these
respective points. The winding-number form of the residue
theorem applies to this closed smooth curve, without a
simple-curve assumption [@SS03]. Therefore
$$
\int_\gamma f(z)\,dz
=2\pi i\left(4\frac{e^{1/2}}2+2(2\cos4)
+0\operatorname{Res}_{-5i}f\right)
=4\pi i e^{1/2}+8\pi i\cos4.
$$
:::
:::
