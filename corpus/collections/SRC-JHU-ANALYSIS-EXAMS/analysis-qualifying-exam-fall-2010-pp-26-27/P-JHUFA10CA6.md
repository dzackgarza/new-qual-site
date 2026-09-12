---
schema: qual/card@1
id: P-JHUFA10CA6
kind: problem
title: Vanishing first jets at the points $1/n$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros of Holomorphic Functions
  - Identity Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Read Fall 2010 problem 6 on PDF page 27; excluded the index one, whose point is outside the open disk, and specified the first-jet meaning of a double zero for C1 functions."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Answered also the exact-order interpretation, bounded both first partial derivatives at the accumulation point, and verified an actual quadratic local factor at every prescribed nonzero zero."
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the two complete source transcriptions and retained this proof on the correctly located Fall 2010 card. P-JHUMAY11ANN was a duplicate, not a separate May 2011 problem."
---

::: problem
Let $D=\{z\in\mathbb C:|z|<1\}$ and let $f:D\to\mathbb C$
be $C^1$ as a function of two real variables. Require
$f(1/n)=0$ and $Df(1/n)=0$ for each integer $n\geq2$,
where $Df$ denotes the real differential.

(a) Determine all holomorphic functions $f$ with this property.
[The terms “holomorphic” and “complex analytic” have the same meaning.]

(b) Give an example of a non-holomorphic $C^1$ function with this property.
(You must explain why your example has this property.)
:::

::: remark
Only $n\geq2$ gives points in the open unit disk.
The vanishing first-jet condition specifies the meaning of
"double zero" for a $C^1$ function. If exactly order two
is required, rather than vanishing to at least second order,
there are no holomorphic examples in (a): the identity
theorem forces the zero function, which has no zero of
exact order two. The example below has exact quadratic
order at every prescribed point and therefore answers (b)
under either interpretation.
:::

::: solution
<1>1. Under the first-jet interpretation, the only holomorphic function is zero.

::: proof
The distinct zeros $1/n$, $n\geq2$, accumulate at the
interior point zero of the connected disk. The identity
theorem gives $f\equiv0$ [@SS03]. This function has
zero value and differential at all points, so it does
satisfy the stated first-jet condition. The exact-order
alternative follows as explained in the remark.
:::

<1>2. A nonholomorphic example is $C^1$ even at the accumulation point.

::: proof
Define
$$
F(z)=\begin{cases}
e^{-1/|z|^2}\sin^2(\pi/z),&z\ne0,\\
0,&z=0.
\end{cases}
$$
It is smooth away from zero. For $r=|z|>0$, the exponential
formulas for sine and cosine give
$|\sin(\pi/z)|,|\cos(\pi/z)|\leq e^{\pi/r}$. Hence
$$
|F(z)|\leq e^{-1/r^2+2\pi/r},\qquad
|F_x(z)|,|F_y(z)|
\leq(2r^{-3}+2\pi r^{-2})e^{-1/r^2+2\pi/r}.
$$
For the derivative estimate, the Gaussian factor has
each first partial derivative bounded by $2r^{-3}e^{-1/r^2}$;
the holomorphic factor $\sin^2(\pi/z)$ has complex
derivative of modulus at most $2\pi r^{-2}e^{2\pi/r}$.
The product rule gives the displayed bounds.

When $r\leq1/(4\pi)$, the exponent is at most
$-1/(2r^2)$. For every fixed $k\geq0$,
$r^{-k}e^{-1/(2r^2)}\to0$; this follows, for example,
by bounding the exponential below by an arbitrarily
high power in its power series. It follows that
$F(z)=o(|z|)$ and both first partial derivatives tend
to zero. Thus $DF(0)=0$, the partial derivatives extend
continuously by zero, and $F\in C^1(D)$.
:::

<1>3. The prescribed zeros have exact quadratic order, and $F$ is not holomorphic.

::: proof
At $a=1/n$, $n\geq2$, the holomorphic function
$s(z)=\sin(\pi/z)$ has value zero and derivative
$$
s'(a)=-\pi n^2\cos(\pi n)=-\pi n^2(-1)^n\ne0.
$$
Locally write $s(z)=(z-a)h_a(z)$ with $h_a$ holomorphic
and $h_a(a)=s'(a)\ne0$. Then
$$
F(z)=(z-a)^2 u_a(z),\qquad
u_a(z)=e^{-1/|z|^2}h_a(z)^2,
$$
where $u_a$ is smooth near $a$ and $u_a(a)\ne0$.
Consequently $F(a)=0$, $DF(a)=0$, and
$F(z)/(z-a)^2\to u_a(a)\ne0$.

Finally $F(i/2)\ne0$, since $\sin(-2\pi i)=-i\sinh(2\pi)\ne0$.
If $F$ were holomorphic on $D$, the zeros accumulating
at zero would force $F\equiv0$ by step <1>1, contradicting
this value. Thus it is the required nonholomorphic example.
:::
:::
