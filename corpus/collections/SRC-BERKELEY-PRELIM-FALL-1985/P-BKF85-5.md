---
schema: qual/card@1
id: P-BKF85-5
kind: problem
title: Count quartic roots in the right half-plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md.
---

::: {.problem}
How many roots does
\[
z^4+3z^2+z+1
\]
have in the right half-plane?
:::

::: {.solution}
Set
$$
p(z)\coloneqq z^4+3z^2+z+1.
$$

<1>1. The polynomial $p$ has no zero on the imaginary axis.

::: {.proof}
For $y\in\RR$,
$$
p(iy)
=
y^4-3y^2+1+iy.
$$
If this were zero, its imaginary part would give $y=0$, but then its real part would be $1$. Hence $p(iy)\neq0$ for every real $y$.
:::

<1>2. Choose $R>0$ so large that every zero of $p$ lies in $\abs{z}<R$ and
$$
3R^2+R+1<R^4.
$$
Set
$$
A_R\coloneqq R^4-3R^2+1
$$
and let
$$
\alpha_R\coloneqq\arg(A_R+iR)\in(0,\pi/2).
$$
Along the diameter of the right half-disk, traversed from $iR$ to $-iR$, the change in argument of $p$ is
$$
-2\alpha_R.
$$

::: {.proof}
The displayed inequality implies $A_R>0$. By step <1>1, the path
$$
y\longmapsto p(iy)
=
y^4-3y^2+1+iy
$$
never passes through the origin.

For $y>0$ it lies in the open upper half-plane, for $y<0$ it lies in the open lower half-plane, and $p(0)=1$. Hence the principal argument is continuous along this path from $y=R$ down to $y=-R$. At the endpoints,
$$
p(iR)=A_R+iR,
\qquad
p(-iR)=A_R-iR,
$$
whose principal arguments are $\alpha_R$ and $-\alpha_R$, respectively. Thus the change is $-2\alpha_R$.
:::

<1>3. Along the semicircle
$$
z=Re^{i\theta},
\qquad
-\frac\pi2\leq\theta\leq\frac\pi2,
$$
traversed from $-iR$ to $iR$, the change in argument of $p$ is
$$
4\pi+2\alpha_R.
$$

::: {.proof}
On $\abs{z}=R$, write
$$
p(z)
=
z^4\left(
1+\frac{3z^2+z+1}{z^4}
\right).
$$
The choice of $R$ gives
$$
\left|
\frac{3z^2+z+1}{z^4}
\right|
\leq
\frac{3R^2+R+1}{R^4}
<1.
$$
Therefore the factor in parentheses lies in the open disk of radius $1$ centered at $1$, so it never vanishes and has a continuous principal argument on the semicircle.

For $z=Re^{i\theta}$, choose the continuous argument
$$
4\theta+
\arg\left(
1+\frac{3z^2+z+1}{z^4}
\right)
$$
for $p(z)$. The first term changes from $-2\pi$ to $2\pi$, contributing $4\pi$.

At $z=-iR$, the second factor is $p(-iR)/R^4$, whose argument is $-\alpha_R$; at $z=iR$ its argument is $\alpha_R$. Hence the second term contributes $2\alpha_R$. The total change is therefore $4\pi+2\alpha_R$.
:::

<1>4. The change in argument of $p$ around the positively oriented boundary of the right half-disk
$$
\{z:\operatorname{Re}z>0,\ \abs{z}<R\}
$$
is $4\pi$.

::: {.proof}
The positive orientation traverses the diameter from $iR$ to $-iR$ and then the right semicircle from $-iR$ to $iR$. Adding steps <1>2 and <1>3 gives
$$
-2\alpha_R+(4\pi+2\alpha_R)=4\pi.
$$
:::

<1>5. The polynomial $p$ has exactly two roots in the right half-plane, counted with multiplicity.

::: {.proof}
The boundary used in step <1>4 contains no zero of $p$: step <1>1 handles the diameter, while step <1>3 shows that $p$ is nonzero on the semicircle. By the argument principle, the number of zeros in the right half-disk is
$$
\frac{4\pi}{2\pi}=2.
$$
The radius $R$ was chosen larger than the modulus of every zero of $p$, so these are exactly the roots of $p$ in the entire right half-plane.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the required answer: $2$ roots.
:::
:::
