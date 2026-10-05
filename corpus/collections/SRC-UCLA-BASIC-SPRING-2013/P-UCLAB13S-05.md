---
schema: qual/card@1
id: P-UCLAB13S-05
kind: problem
title: Chebyshev polynomials of the second kind
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained source prints U_1=1 and U_2=2x while also indexing n from 0 and asking for U_n(cos theta)=sin((n+1)theta)/sin(theta). This card corrects the evident indexing typo to the standard U_0=1, U_1=2x.
---

::: {.problem}
Define polynomials $U_n(x)$, $n=0,1,2,\ldots$, by
\[
U_0(x)=1,\qquad U_1(x)=2x,\qquad U_{n+1}(x)=2xU_n(x)-U_{n-1}(x).
\]

(a) Prove that
\[
U_n(\cos\theta)=\frac{\sin((n+1)\theta)}{\sin\theta}.
\]

(b) Prove that
\[
\int_{-1}^1 U_m(x)U_n(x)\sqrt{1-x^2}\,dx
=
\begin{cases}
0,&m\neq n,\\
\pi/2,&m=n.
\end{cases}
\]
:::

::: {.solution}
<1>1. For
\[
n=0,
\]
one has
\[
U_0(\cos\theta)
=
1
=
\frac{\sin\theta}{\sin\theta}
\]
whenever
\[
\sin\theta\ne0.
\]

::: {.proof}
This follows from
\[
U_0(x)=1.
\]
:::

<1>2. For
\[
n=1,
\]
one has
\[
U_1(\cos\theta)
=
2\cos\theta
=
\frac{\sin(2\theta)}{\sin\theta}
\]
whenever
\[
\sin\theta\ne0.
\]

::: {.proof}
By definition,
\[
U_1(x)=2x.
\]
Using
\[
\sin(2\theta)=2\sin\theta\cos\theta,
\]
the quotient equals
\[
2\cos\theta.
\]
:::

<1>3. Suppose for some $n\ge1$ that
\[
U_n(\cos\theta)
=
\frac{\sin((n+1)\theta)}{\sin\theta}
\]
and
\[
U_{n-1}(\cos\theta)
=
\frac{\sin(n\theta)}{\sin\theta}.
\]
Then
\[
U_{n+1}(\cos\theta)
=
\frac{\sin((n+2)\theta)}{\sin\theta}.
\]

::: {.proof}
Using the recurrence,
\[
\begin{aligned}
U_{n+1}(\cos\theta)
&=
2\cos\theta\,U_n(\cos\theta)
-
U_{n-1}(\cos\theta)\\
&=
\frac{
2\cos\theta\sin((n+1)\theta)
-
\sin(n\theta)
}{
\sin\theta
}.
\end{aligned}
\]
The trigonometric identity
\[
2\cos\theta\sin((n+1)\theta)
=
\sin((n+2)\theta)
+
\sin(n\theta)
\]
reduces the numerator to
\[
\sin((n+2)\theta).
\]
:::

<1>4. Therefore
\[
\boxed{
U_n(\cos\theta)
=
\frac{\sin((n+1)\theta)}{\sin\theta}
}
\]
for every $n\ge0$ and every $\theta$ with
\[
\sin\theta\ne0.
\]

::: {.proof}
Steps <1>1--<1>3 give the induction.
At points where
\[
\sin\theta=0,
\]
the quotient has a removable singularity and the identity extends by continuity.
This proves part (a).
:::

<1>5. In the integral from part (b), make the substitution
\[
x=\cos\theta,
\qquad
0\le\theta\le\pi.
\]
Then
\[
dx=-\sin\theta\,d\theta
\]
and
\[
\sqrt{1-x^2}=\sin\theta.
\]

::: {.proof}
On
\[
[0,\pi],
\]
one has
\[
\sin\theta\ge0.
\]
Therefore
\[
\sqrt{1-\cos^2\theta}
=
|\sin\theta|
=
\sin\theta.
\]
Also,
\[
\frac{dx}{d\theta}
=
-\sin\theta.
\]
:::

<1>6. The weighted inner product becomes
\[
\int_{-1}^1
U_m(x)U_n(x)\sqrt{1-x^2}\,dx
=
\int_0^\pi
\sin((m+1)\theta)
\sin((n+1)\theta)
\,d\theta.
\]

::: {.proof}
Using step <1>5,
\[
\begin{aligned}
&\int_{-1}^1
U_m(x)U_n(x)\sqrt{1-x^2}\,dx\\
&\qquad=
\int_\pi^0
U_m(\cos\theta)
U_n(\cos\theta)
\sin\theta
(-\sin\theta)\,d\theta\\
&\qquad=
\int_0^\pi
U_m(\cos\theta)
U_n(\cos\theta)
\sin^2\theta\,d\theta.
\end{aligned}
\]
By step <1>4, for interior $\theta$,
\[
U_m(\cos\theta)\sin\theta
=
\sin((m+1)\theta)
\]
and similarly for $n$.
The endpoint values do not affect the integral.
Thus the displayed identity follows.
:::

<1>7. If
\[
m\ne n,
\]
then
\[
\int_0^\pi
\sin((m+1)\theta)
\sin((n+1)\theta)
\,d\theta
=
0.
\]

::: {.proof}
Use the product-to-sum identity
\[
\sin(a\theta)\sin(b\theta)
=
\frac12
\left[
\cos((a-b)\theta)
-
\cos((a+b)\theta)
\right].
\]
Here
\[
a=m+1,
\qquad
b=n+1.
\]
If
\[
m\ne n,
\]
then
\[
a-b\ne0
\]
and
\[
a+b>0.
\]
For every nonzero integer $k$,
\[
\int_0^\pi\cos(k\theta)\,d\theta
=
\left[
\frac{\sin(k\theta)}k
\right]_0^\pi
=0.
\]
Hence the integral vanishes.
:::

<1>8. If
\[
m=n,
\]
then
\[
\int_0^\pi
\sin^2((n+1)\theta)\,d\theta
=
\frac{\pi}{2}.
\]

::: {.proof}
Use
\[
\sin^2 u
=
\frac{1-\cos(2u)}2.
\]
Then
\[
\begin{aligned}
\int_0^\pi
\sin^2((n+1)\theta)\,d\theta
&=
\frac12
\int_0^\pi
1\,d\theta\\
&\quad-
\frac12
\int_0^\pi
\cos(2(n+1)\theta)\,d\theta\\
&=
\frac{\pi}{2},
\end{aligned}
\]
because the cosine integral is zero.
:::

<1>9. Therefore
\[
\boxed{
\int_{-1}^1 U_m(x)U_n(x)\sqrt{1-x^2}\,dx
=
\begin{cases}
0,&m\ne n,\\[1mm]
\pi/2,&m=n.
\end{cases}
}
\]

::: {.proof}
Combine step <1>6 with steps <1>7--<1>8.
This proves part (b).
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and step <1>9 proves part (b).
:::
:::
