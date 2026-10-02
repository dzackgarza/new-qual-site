---
schema: qual/card@1
id: P-BKS17-5A
kind: problem
title: Power series with coefficients satisfying $3a_n+4a_{n-1}-a_{n-2}=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 6 problem 5A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 generating-function solution and verified the radius from the recurrence roots.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the recurrence characteristic roots, the nonzero dominant coefficient, the Cauchy--Hadamard radius, and the generating-function identity.
---

::: {.problem}
Suppose the coefficients of the power series

$$
\sum_{n=0}^{\infty} a_n z^n
$$

are given by the recurrence relation

$$
a_0 = 1, \quad a_1 = -1, \quad 3a_n + 4a_{n-1} - a_{n-2} = 0, \quad n = 2, 3, \ldots.
$$

Find the radius of convergence of the series and the function to which it converges in its disc of convergence.
:::

::: {.solution}
Write
$$
F(z)\coloneqq\sum_{n=0}^{\infty}a_nz^n.
$$

<1>1. The characteristic roots of the recurrence are
$$
r_+=\frac{-2+\sqrt7}{3},
\qquad
r_-=\frac{-2-\sqrt7}{3},
$$
and
$$
a_n
=
\frac{\sqrt7-1}{2\sqrt7}\,r_+^n
+
\frac{\sqrt7+1}{2\sqrt7}\,r_-^n.
$$

::: {.proof}
The recurrence is equivalent to
$$
3a_n+4a_{n-1}-a_{n-2}=0,
$$
whose characteristic equation is
$$
3r^2+4r-1=0.
$$
Its two distinct roots are $r_+$ and $r_-$. Hence
$$
a_n=Ar_+^n+Br_-^n
$$
for constants $A,B$. The initial conditions give
$$
A+B=1,
\qquad
Ar_++Br_-=-1.
$$
Solving yields
$$
A=\frac{\sqrt7-1}{2\sqrt7},
\qquad
B=\frac{\sqrt7+1}{2\sqrt7}.
$$
:::

<1>2. The radius of convergence is
$$
\boxed{R=\sqrt7-2}.
$$

::: {.proof}
Since
$$
|r_-|=\frac{2+\sqrt7}{3}>|r_+|
$$
and the coefficient of $r_-^n$ in step <1>1 is nonzero,
$$
\limsup_{n\to\infty}|a_n|^{1/n}=|r_-|=\frac{2+\sqrt7}{3}.
$$
By the Cauchy--Hadamard formula,
$$
R=\frac{1}{|r_-|}
=
\frac{3}{2+\sqrt7}
=
\sqrt7-2.
$$
:::

<1>3. For $|z|<R$,
$$
(3+4z-z^2)F(z)=3+z.
$$

::: {.proof}
Inside the disk of convergence, termwise algebra is valid. One has
$$
\begin{aligned}
(3+4z-z^2)F(z)
&=
3a_0+(3a_1+4a_0)z\\
&\quad+
\sum_{n=2}^{\infty}
(3a_n+4a_{n-1}-a_{n-2})z^n.
\end{aligned}
$$
The recurrence makes the infinite sum zero, while
$$
3a_0=3,
\qquad
3a_1+4a_0=-3+4=1.
$$
Thus the product equals $3+z$.
:::

<1>4. In its disk of convergence, the series converges to
$$
\boxed{F(z)=\frac{3+z}{3+4z-z^2}}.
$$

::: {.proof}
The zeros of the denominator are $2\pm\sqrt7$. Their moduli are
$$
\sqrt7-2
\qquad\text{and}\qquad
\sqrt7+2,
$$
so the denominator is nonzero for $|z|<R=\sqrt7-2$. Dividing the identity in step <1>3 gives the stated formula throughout the disk of convergence.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2 and <1>4 give the requested radius and sum.
:::
:::
