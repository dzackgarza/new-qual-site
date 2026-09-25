---
schema: qual/card@1
id: P-BKS13-3B
kind: problem
title: Fourier series solution of $f''+kf=g$
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
  note: >-
    Compared the authored statement with the retained Spring 2013 exam and
    solution PDFs. The source solution divides its constant term by k even
    though the statement permits k=0.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the Fourier-coefficient identities by integration
    by parts, the k=0 solvability condition, and uniform absolute convergence.
---

::: {.problem}
Let g be 2π-periodic, continuous on $[ - \pi , \pi ]$ and have Fourier series

$$
{ \frac { a _ { 0 } } { 2 } } + \sum _ { n = 1 } ^ { \infty } ( a _ { n } \cos n x + b _ { n } \sin n x ) .
$$

Let f be 2π-periodic and satisfy the differential equation

$$
f ^ { \prime \prime } ( x ) + k f ( x ) = g ( x )
$$

where $k \neq n ^ { 2 } , n = 1 , 2 , 3 , . . . .$ Find the Fourier series of f and prove that it converges everywhere.
:::

::: {.solution}
Write the Fourier coefficients of $f$ as
$$
A_0,\ A_n,\ B_n
\qquad
(n\geq1),
$$
so formally
$$
f(x)
\sim
\frac{A_0}{2}
+
\sum_{n=1}^{\infty}
\bigl(A_n\cos nx+B_n\sin nx\bigr).
$$

<1>1. The constant Fourier coefficient of $f''$ is zero.

::: {.proof}
Since $f$ is $2\pi$-periodic and satisfies a classical second-order
differential equation with continuous right-hand side, $f'$ is also
$2\pi$-periodic. Hence
$$
\int_{-\pi}^{\pi}f''(x)\,dx
=
f'(\pi)-f'(-\pi)
=
0.
$$
:::

<1>2. For every $n\geq1$, the cosine and sine Fourier coefficients of
$f''$ are respectively
$$
-n^2A_n
\qquad\text{and}\qquad
-n^2B_n.
$$

::: {.proof}
Integrate by parts twice. Periodicity of $f$ and $f'$ makes all boundary
terms vanish. Thus
$$
\frac1\pi
\int_{-\pi}^{\pi}
f''(x)\cos(nx)\,dx
=
-n^2A_n,
$$
and similarly
$$
\frac1\pi
\int_{-\pi}^{\pi}
f''(x)\sin(nx)\,dx
=
-n^2B_n.
$$
:::

<1>3. For every $n\geq1$,
$$
\boxed{
A_n=\frac{a_n}{k-n^2},
\qquad
B_n=\frac{b_n}{k-n^2}
}.
$$

::: {.proof}
Take the $n$th cosine and sine Fourier coefficients of
$$
f''+kf=g.
$$
By step <1>2,
$$
(k-n^2)A_n=a_n
$$
and
$$
(k-n^2)B_n=b_n.
$$
The hypothesis excludes $k=n^2$ for every $n\geq1$, so division is
legitimate.
:::

<1>4. If $k\neq0$, then
$$
A_0=\frac{a_0}{k}.
$$

::: {.proof}
Taking constant Fourier coefficients in the differential equation and
using step <1>1 gives
$$
k\frac{A_0}{2}
=
\frac{a_0}{2}.
$$
Divide by $k$.
:::

<1>5. If $k=0$, then necessarily
$$
a_0=0,
$$
while $A_0$ is not determined by the equation.

::: {.proof}
For $k=0$, the constant-coefficient identity from step <1>4 before
division becomes
$$
0=\frac{a_0}{2},
$$
so $a_0=0$. Adding a constant to any $2\pi$-periodic solution of
$$
f''=g
$$
produces another solution, so the constant Fourier coefficient is free.
:::

<1>6. The Fourier coefficients $a_n,b_n$ of the continuous function $g$
are uniformly bounded in $n$.

::: {.proof}
Let
$$
M_g
\coloneqq
\max_{x\in[-\pi,\pi]}\abs{g(x)}.
$$
Then, for $n\geq1$,
$$
\abs{a_n}
\leq
\frac1\pi\int_{-\pi}^{\pi}\abs{g(x)}\,dx
\leq
2M_g,
$$
and the same estimate holds for $b_n$.
:::

<1>7. The series of nonconstant terms
$$
\sum_{n=1}^{\infty}
\left(
\frac{a_n}{k-n^2}\cos nx
+
\frac{b_n}{k-n^2}\sin nx
\right)
$$
converges absolutely and uniformly in $x$.

::: {.proof}
Because $k$ is fixed, there is $N$ such that for all $n\geq N$,
$$
\abs{k-n^2}
\geq
\frac{n^2}{2}.
$$
By step <1>6, for such $n$ the absolute value of the $n$th summand is at
most
$$
\frac{4M_g}{n^2}
+
\frac{4M_g}{n^2}
=
\frac{8M_g}{n^2}.
$$
The series
$$
\sum_{n=N}^{\infty}\frac1{n^2}
$$
converges, so the Weierstrass M-test gives absolute uniform convergence.
The finitely many initial terms do not affect convergence.
:::

<1>8. If $k\neq0$, the Fourier series of $f$ is
$$
\boxed{
\frac{a_0}{2k}
+
\sum_{n=1}^{\infty}
\left(
\frac{a_n}{k-n^2}\cos nx
+
\frac{b_n}{k-n^2}\sin nx
\right)
}.
$$

::: {.proof}
Combine steps <1>3 and <1>4.
:::

<1>9. If $k=0$, then $a_0=0$ and the Fourier series of $f$ is
$$
\boxed{
\frac{A_0}{2}
-
\sum_{n=1}^{\infty}
\left(
\frac{a_n}{n^2}\cos nx
+
\frac{b_n}{n^2}\sin nx
\right)
},
$$
where $A_0$ is the constant Fourier coefficient of the particular
solution $f$.

::: {.proof}
Combine steps <1>3 and <1>5.
:::

<1>10. In both cases the displayed Fourier series converges everywhere
to $f$.

::: {.proof}
Step <1>7 gives uniform absolute convergence of the nonconstant part.
Moreover $f$ is $C^2$ and $2\pi$-periodic, so the standard Fourier
convergence theorem applies: its Fourier series converges at every point
to $f(x)$. Hence the series identified in steps <1>8 and <1>9 converge
everywhere to the given solution.
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>8--<1>10 give the Fourier series and its everywhere convergence
for every value of $k$ allowed by the stated hypotheses.
:::
:::
