---
schema: qual/card@1
id: P-BERK85S-08
kind: problem
title: Discrete harmonic oscillator and convergence to the sine function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Solved the second-order recurrence using the characteristic roots
    1+ih and 1-ih, imposed the two initial values, and reduced the continuum
    limit to (1+ix/n)^n -> e^{ix}.
---

::: {.problem}
Fix $h>0$ and consider
\[
\frac{y((n+2)h)-2y((n+1)h)+y(nh)}{h^2}=-y(nh),
\qquad n=0,1,2,\dots.
\]

1. Find the general solution by exponential substitution.
2. Find the solution satisfying
   \[
   y(0)=0,
   \qquad
   y(h)=h,
   \]
   and denote it by $S_h(nh)$.
3. For fixed $x$, put $h=x/n$. Prove that
   \[
   \lim_{n\to\infty}S_{x/n}(x)=\sin x.
   \]
:::

::: {.solution}
Put
$$
u_n\coloneqq y(nh).
$$

<1>1. The difference equation is equivalent to
$$
u_{n+2}-2u_{n+1}+(1+h^2)u_n=0.
$$

::: {.proof}
Multiply the given equation by $h^2$ and move the term
$-h^2y(nh)$ to the left.
:::

<1>2. The characteristic equation of the recurrence in step <1>1 is
$$
r^2-2r+(1+h^2)=0,
$$
with distinct roots
$$
r_\pm=1\pm ih.
$$

::: {.proof}
Substituting $u_n=r^n$ into the recurrence gives
$$
r^n\left(r^2-2r+1+h^2\right)=0.
$$
Since $h>0$, the two roots $1\pm ih$ are distinct.
:::

<1>3. The general solution is
$$
\boxed{
y(nh)
=
A(1+ih)^n+B(1-ih)^n
},
$$
where $A,B\in\CC$ are arbitrary.
For real-valued solutions, the coefficients are exactly those satisfying
$B=\overline A$.

::: {.proof}
Each characteristic root from step <1>2 yields a solution, and the two
solutions are linearly independent because the roots are distinct. A
second-order recurrence is uniquely determined by $u_0$ and $u_1$, so
their span is the full complex solution space. Since the two basis
solutions are complex conjugates, their linear combination is real for
every $n$ exactly when $B=\overline A$.
:::

<1>4. The solution satisfying $y(0)=0$ and $y(h)=h$ is
$$
\boxed{
S_h(nh)
=
\frac{(1+ih)^n-(1-ih)^n}{2i}
}.
$$

::: {.proof}
Step <1>3 and $u_0=0$ give
$$
A+B=0.
$$
Thus $B=-A$. The condition $u_1=h$ then gives
$$
h
=
A\left((1+ih)-(1-ih)\right)
=
2ihA,
$$
so $A=1/(2i)$ and $B=-1/(2i)$.
:::

<1>5. For every fixed $x>0$,
$$
\lim_{n\to\infty}S_{x/n}(x)=\sin x.
$$

::: {.proof}
The standing hypothesis $h>0$ makes the substitution $h=x/n$ literal
when $x>0$. By step <1>4,
$$
S_{x/n}(x)
=
\frac{
\left(1+\frac{ix}{n}\right)^n
-
\left(1-\frac{ix}{n}\right)^n
}{2i}.
$$
Using the standard exponential limit,
$$
\left(1+\frac{ix}{n}\right)^n\longrightarrow e^{ix},
\qquad
\left(1-\frac{ix}{n}\right)^n\longrightarrow e^{-ix}.
$$
Therefore
$$
\lim_{n\to\infty}S_{x/n}(x)
=
\frac{e^{ix}-e^{-ix}}{2i}
=
\sin x.
$$
The same closed formula extends continuously to $x=0$ and, if the
recurrence is allowed for nonzero negative step size, to negative $x$ as
well.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3, <1>4, and <1>5 answer parts 1, 2, and 3 respectively.
:::
:::
