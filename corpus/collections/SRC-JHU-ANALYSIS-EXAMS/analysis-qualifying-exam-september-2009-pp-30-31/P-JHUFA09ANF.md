---
schema: qual/card@1
id: P-JHUFA09ANF
kind: problem
title: Removability and the Taylor radius of $z\cot z$
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts of September 2009 problem 6 in the retained extraction; stated the quotient on a punctured neighborhood where it is defined rather than at every nonzero complex number."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Located all zeros of sine, distinguished tan's removable quotient points from the genuine poles at plus or minus pi, and proved both inequalities for the Taylor radius."
---

::: problem
For $0<|z|<\pi/2$, let

$$
f(z)=\frac{z}{\tan z}.
$$

a) Prove that f has a removable singularity at 0.

b) What is the radius of convergence of the power series for f centered at 0? Justify your answer.
:::

::: solution
The extension has value $f(0)=1$, and its Taylor series
at zero has radius exactly $\boxed{\pi}$.

<1>1. The quotient extends holomorphically throughout $|z|<\pi$.

::: proof
Where the original quotient is defined,
$$
f(z)=\frac{z\cos z}{\sin z}.
$$
The function $s(z)=\sin z/z$ extends holomorphically to
zero with value one by the sine power series [@SS03].
Moreover, the exponential formula for sine gives
$\sin z=0$ exactly when $e^{2iz}=1$. Writing $z=x+iy$,
the modulus of this equation forces $y=0$; its argument
then gives $x=k\pi$ for an integer $k$. Thus $s$ has
no zero in $|z|<\pi$, including zero.
The function
$$
F(z)=\frac{\cos z}{s(z)}
$$
is therefore holomorphic on this whole disk, agrees
with $f$ near zero, and has $F(0)=1$. This proves (a).
The Taylor theorem for holomorphic functions gives
convergence of its Taylor series throughout $|z|<\pi$
[@SS03], so the radius is at least $\pi$.
:::

<1>2. The genuine pole at $\pi$ prevents a larger Taylor disk.

::: proof
At $z=\pi$, the denominator $\sin z$ has a simple zero,
since $\cos\pi=-1\ne0$, whereas $z\cos z=-\pi\ne0$.
In particular,
$$
\lim_{z\to\pi}(z-\pi)\frac{z\cos z}{\sin z}=\pi\ne0.
$$
If the Taylor series at zero had radius greater than
$\pi$, its sum would be holomorphic in a neighborhood
of $\pi$ and would agree with $F$ on $|z|<\pi$.
Continuity would make it bounded as real $z\uparrow\pi$,
contradicting the nonzero limit above. Thus the radius
is at most $\pi$, and hence exactly $\pi$.

The poles of $\tan z$ at $\pm\pi/2$ do not obstruct
this Taylor series: the expression $z\cos z/\sin z$
is holomorphic and zero at those points. They are only
missing points of the unsimplified quotient, not poles
of the holomorphic germ's continuation.
:::
:::
