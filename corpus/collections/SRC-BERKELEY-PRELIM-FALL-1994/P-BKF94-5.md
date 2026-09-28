---
schema: qual/card@1
id: P-BKF94-5
kind: problem
title: Solutions of a seventh-order constant-coefficient ODE
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Factored the characteristic polynomial through r^8-1; the real solution
    basis comes from the seven nontrivial eighth roots of unity, and the
    decaying subspace is exactly the three modes with negative real part.
---

::: {.problem}
(a) Find a basis for the real solution space of
\[
\sum_{n=0}^{7}\frac{d^nx}{dt^n}=0.
\]

(b) Find a basis for the subspace of solutions satisfying $x(t)\to0$ as $t\to+\infty$.
:::

::: {.solution}
Let
$$
P(r)\coloneqq\sum_{n=0}^{7}r^n.
$$

<1>1. The characteristic roots are
$$
-1,\qquad
\pm i,\qquad
e^{\pm i\pi/4},\qquad
e^{\pm3i\pi/4}.
$$

::: {.proof}
For $r\neq1$,
$$
P(r)
=
\frac{r^8-1}{r-1}.
$$
Hence the roots of $P$ are precisely the eighth roots of unity other than
$1$. They are the seven displayed numbers, and they are all simple.
:::

<1>2. A real basis of the full solution space is
$$
\begin{aligned}
&e^{-t},\\
&\cos t,\quad \sin t,\\
&e^{t/\sqrt2}\cos\frac{t}{\sqrt2},
\quad
e^{t/\sqrt2}\sin\frac{t}{\sqrt2},\\
&e^{-t/\sqrt2}\cos\frac{t}{\sqrt2},
\quad
e^{-t/\sqrt2}\sin\frac{t}{\sqrt2}.
\end{aligned}
$$

::: {.proof}
The real root $-1$ gives the solution $e^{-t}$. The conjugate roots
$\pm i$ give $\cos t$ and $\sin t$. Since
$$
e^{\pm i\pi/4}
=
\frac1{\sqrt2}\pm\frac{i}{\sqrt2},
$$
that conjugate pair gives
$$
e^{t/\sqrt2}\cos\frac{t}{\sqrt2},
\qquad
e^{t/\sqrt2}\sin\frac{t}{\sqrt2}.
$$
Likewise,
$$
e^{\pm3i\pi/4}
=
-\frac1{\sqrt2}\pm\frac{i}{\sqrt2},
$$
which gives the final two decaying functions. The seven simple
characteristic roots produce seven linearly independent solutions, equal to
the order of the differential equation, so these form a basis.
:::

<1>3. Every linear combination of
$$
e^{-t},
\qquad
e^{-t/\sqrt2}\cos\frac{t}{\sqrt2},
\qquad
e^{-t/\sqrt2}\sin\frac{t}{\sqrt2}
$$
tends to $0$ as $t\to+\infty$.

::: {.proof}
Each of the three displayed functions tends to zero because its
trigonometric factor is bounded and its exponential factor tends to zero.
The same is true for every finite linear combination.
:::

<1>4. If a solution tends to $0$ as $t\to+\infty$, then its coefficients
of
$$
e^{t/\sqrt2}\cos\frac{t}{\sqrt2},
\qquad
e^{t/\sqrt2}\sin\frac{t}{\sqrt2}
$$
in the basis of step <1>2 are both zero.

::: {.proof}
Write the growing contribution as
$$
e^{t/\sqrt2}
\left(
A\cos\frac{t}{\sqrt2}
+B\sin\frac{t}{\sqrt2}
\right).
$$
If $(A,B)\neq(0,0)$, the trigonometric factor has positive amplitude
$$
\sqrt{A^2+B^2}.
$$
There is therefore a sequence $t_j\to\infty$ along which its absolute value
equals that amplitude. Along this sequence the growing contribution has
absolute value
$$
\sqrt{A^2+B^2}\,e^{t_j/\sqrt2}\longrightarrow\infty,
$$
whereas the remaining basis contributions are bounded or tend to zero.
Thus the full solution cannot tend to zero, a contradiction.
:::

<1>5. If a solution tends to $0$ as $t\to+\infty$, then its coefficients
of $\cos t$ and $\sin t$ are both zero.

::: {.proof}
By step <1>4, the growing contribution is absent. The remaining nondecaying
part is
$$
C\cos t+D\sin t.
$$
If $(C,D)\neq(0,0)$, this function has positive amplitude
$\sqrt{C^2+D^2}$ and attains that absolute value along a sequence tending to
infinity. The other remaining terms tend to zero by step <1>3, so the full
solution cannot tend to zero. Hence $C=D=0$.
:::

<1>6. A basis for the subspace of solutions tending to zero is
$$
\boxed{
e^{-t},
\quad
e^{-t/\sqrt2}\cos\frac{t}{\sqrt2},
\quad
e^{-t/\sqrt2}\sin\frac{t}{\sqrt2}
}.
$$

::: {.proof}
Step <1>3 shows that the displayed span consists of decaying solutions.
Steps <1>4 and <1>5 show that every decaying solution has zero coefficient
on every other basis vector from step <1>2. Therefore the displayed three
functions form a basis of the decaying subspace.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 answers part (a), and step <1>6 answers part (b).
:::
:::
