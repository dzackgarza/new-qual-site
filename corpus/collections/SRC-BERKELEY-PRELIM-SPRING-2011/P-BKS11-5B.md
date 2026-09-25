---
schema: qual/card@1
id: P-BKS11-5B
kind: problem
title: Wallis integrals $\int_0^\pi\sin^n x\,dx$ and the Wallis product
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared all three parts with page 5 of the retained Spring 2011 solution PDF and independently reviewed the Wallis recurrence and product argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the integration-by-parts formulas, strict monotonicity of the integrals, and a direct squeeze proof that the product converges to 2/pi.
---

::: {.problem}
(a) Evaluate $\begin{array} { r } { I ( n ) = \int _ { 0 } ^ { \pi } \sin ( x ) ^ { n } } \end{array}$ dx for n a non-negative integer.

(b) Prove that $I ( n ) > I ( n + 1 ) > 0$

(c) Evaluate the infinite product ${ \begin{array} { l } { { \frac { 1 } { 2 } } \times { \frac { 3 } { 2 } } \times { \frac { 3 } { 4 } } \times { \frac { 5 } { 4 } } \times { \frac { 5 } { 6 } } \times \cdots } \end{array} }$
:::

::: {.solution}
Write
$$
I_n\coloneqq\int_0^\pi\sin^n x\,dx.
$$

<1>1. One has
$$
I_0=\pi,
\qquad
I_1=2,
$$
and for every $n\geq2$,
$$
I_n
=
\frac{n-1}{n}I_{n-2}.
$$

::: {.proof}
The initial values are immediate. For $n\geq2$, write
$$
I_n
=
\int_0^\pi
\sin^{n-1}x\sin x\,dx.
$$
Integrate by parts with
$$
u=\sin^{n-1}x,
\qquad
dv=\sin x\,dx.
$$
The boundary term vanishes because $\sin0=\sin\pi=0$, and hence
$$
\begin{aligned}
I_n
&=
(n-1)
\int_0^\pi
\sin^{n-2}x\cos^2x\,dx\\
&=
(n-1)
\int_0^\pi
\sin^{n-2}x(1-\sin^2x)\,dx\\
&=
(n-1)(I_{n-2}-I_n).
\end{aligned}
$$
Thus
$$
nI_n=(n-1)I_{n-2},
$$
which is the stated recurrence.
:::

<1>2. For every $m\geq1$,
$$
I_{2m}
=
\pi
\prod_{k=1}^m
\frac{2k-1}{2k},
$$
and for every $m\geq0$,
$$
I_{2m+1}
=
2
\prod_{k=1}^m
\frac{2k}{2k+1}.
$$

::: {.proof}
Iterate the recurrence in step <1>1 separately through the even and odd
indices, terminating at $I_0=\pi$ and $I_1=2$, respectively.
:::

<1>3. These formulas evaluate $I_n$ for every nonnegative integer $n$.

::: {.proof}
Every nonnegative integer is either $2m$ or $2m+1$, so step <1>2 covers
all cases. This proves part (a).
:::

<1>4. For every $n\geq0$,
$$
I_n>I_{n+1}>0.
$$

::: {.proof}
On $(0,\pi)$,
$$
0<\sin x\leq1.
$$
Thus
$$
0<\sin^{n+1}x\leq\sin^n x.
$$
The inequality is strict except at the single point $x=\pi/2$.
Consequently
$$
\sin^n x-\sin^{n+1}x
$$
is continuous, nonnegative, and positive on a nonempty open subset of
$(0,\pi)$. Its integral is therefore positive:
$$
I_n-I_{n+1}>0.
$$
Also $I_{n+1}>0$ because its integrand is positive on $(0,\pi)$.
This proves part (b).
:::

<1>5. Let $P_j$ denote the product of the first $j$ displayed factors in
part (c). Then for $n\geq1$,
$$
P_{2n-1}
=
\frac{2I_{2n}}{\pi I_{2n-1}}
<
\frac2\pi
$$
and
$$
P_{2n}
=
\frac{2I_{2n}}{\pi I_{2n+1}}
>
\frac2\pi.
$$

::: {.proof}
The product has factors
$$
\frac{2k-1}{2k},
\qquad
\frac{2k+1}{2k},
\qquad
k=1,2,\ldots.
$$
Therefore
$$
\begin{aligned}
P_{2n-1}
&=
\left(
\prod_{k=1}^{n}\frac{2k-1}{2k}
\right)
\left(
\prod_{k=1}^{n-1}\frac{2k+1}{2k}
\right)\\
&=
\frac{I_{2n}/\pi}{I_{2n-1}/2}
=
\frac{2I_{2n}}{\pi I_{2n-1}},
\end{aligned}
$$
using step <1>2. Similarly,
$$
\begin{aligned}
P_{2n}
&=
\left(
\prod_{k=1}^{n}\frac{2k-1}{2k}
\right)
\left(
\prod_{k=1}^{n}\frac{2k+1}{2k}
\right)\\
&=
\frac{I_{2n}/\pi}{I_{2n+1}/2}
=
\frac{2I_{2n}}{\pi I_{2n+1}}.
\end{aligned}
$$
The inequalities now follow from step <1>4.
:::

<1>6. One has
$$
P_{2n}-P_{2n-1}\longrightarrow0.
$$

::: {.proof}
The last factor passing from $P_{2n-1}$ to $P_{2n}$ is
$$
\frac{2n+1}{2n}
=
1+\frac1{2n}.
$$
Hence
$$
P_{2n}-P_{2n-1}
=
\frac{P_{2n-1}}{2n}.
$$
By step <1>5,
$$
0<P_{2n-1}<\frac2\pi,
$$
so
$$
0
<
P_{2n}-P_{2n-1}
<
\frac{1}{\pi n}
\longrightarrow0.
$$
:::

<1>7. The infinite product in part (c) converges to
$$
\boxed{\frac2\pi}.
$$

::: {.proof}
By step <1>5,
$$
P_{2n-1}
<
\frac2\pi
<
P_{2n}.
$$
By step <1>6, the distance between the two bounding quantities tends to
$0$. Therefore both subsequences converge to $2/\pi$, and so the full
sequence of partial products converges to $2/\pi$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), step <1>4 proves part (b), and step <1>7 proves
part (c).
:::
:::
