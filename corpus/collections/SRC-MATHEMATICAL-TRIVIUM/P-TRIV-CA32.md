---
schema: qual/card@1
id: P-TRIV-CA32
kind: problem
title: Integral representation and functional equation of the Riemann zeta function
classification:
  areas: [complex-analysis]
  topics:
  - Riemann Zeta Function
  - Analytic Continuation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The analytic-continuation step explicitly asks for the contour in Figure 5. Flash preserves only the image placeholder/caption, so that figure-dependent contour data remain unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the missing-figure note with a description of Figure 5 and removed glyph residue, against Complex Analysis Problem 32 on pages 17-18 of the source PDF.
---

::: {.problem}
Riemann's zeta function is defined as $\zeta(z) = \sum_{n=1}^\infty n^{-z}$.

- For which values of $z$ does this converge?

- Show that the zeta function admits the integral representation
  $$
  \zeta(z) = \frac{1}{\Gamma(z)} \int_0^\infty \frac{t^{z-1}}{e^t - 1}\,\mathrm{d}t
  $$
  **hint:** the relation $\sum_{m=1}^\infty e^{-mt} = \frac{e^{-t}}{1 - e^{-t}}$ might prove useful.

- Now we take the contour of figure 5.
  Since we want to allow non integer values of $z$, there is a branch cut along the positive real axis.
  What is $\frac{1}{\Gamma(z)} \int_0^\infty \frac{t^{z-1}}{e^t - 1}\,\mathrm{d}t$ along this contour?

- For $z < 0$ we can deform the contour by sending the radius of the circle $D$ to infinity; the price to pay is that, to compute $I$, we have to evaluate an infinite number of poles, but this can be done.
  By comparing this result to what you did in the previous step, you should find that
  $$
  \zeta(z) = \zeta(1-z)\, \frac{e^{3\pi i z/2} - e^{\pi i z/2}}{e^{2\pi i z} - 1}\, \frac{(2\pi)^z}{\Gamma(z)}.
  $$

- Using the formula you just found, show that $\zeta(-1) = -\frac{1}{12}$.
  Notice that this doesn't mean that $1 + 2 + 3 + 4 + \ldots = -\frac{1}{12}$, since that $\zeta(z) = \sum_{n=1}^\infty n^{-z}$ is valid only for $z > 1$.
  On a side note, this is the reason why string theory (without supersymmetry) needs 26 spacetime dimensions.

Figure 5 of the source (contour for problem 32) shows, with the cut line along the positive real axis, a contour that comes in from $+\infty$ along a line $A$ just above the cut, goes counterclockwise around the origin along a small circle $D$ of radius $\varepsilon$, and returns to $+\infty$ along a line $B$ just below the cut.
:::

::: {.remark}
The source uses $I$ in the fourth part without defining it; it presumably denotes the contour integral of the third part.
:::

::: {.solution}

Write
$$
s=\sigma+i\tau
$$
for the zeta parameter.

::: pf

::: {.pf-step #s1-1}

The Dirichlet series
$$
\sum_{n=1}^{\infty}n^{-s}
$$
converges absolutely when
$$
\sigma>1.
$$


::: pf-proof

Since
$$
\abs{n^{-s}}
=
n^{-\sigma},
$$
absolute convergence is exactly convergence of the $p$-series
$$
\sum_{n=1}^{\infty}n^{-\sigma},
$$
which occurs for $\sigma>1$.

:::

:::

::: {.pf-step #s1-2}

The same series diverges when
$$
\sigma\leq1.
$$


::: pf-proof

If $\sigma\leq0$, then
$$
\abs{n^{-s}}=n^{-\sigma}
$$
does not tend to $0$.

Now assume
$$
0<\sigma\leq1.
$$
Choose $\delta>0$ so small that
$$
\abs{\tau}\log(1+\delta)<\frac\pi3.
$$
For $N<n\leq(1+\delta)N$, the arguments of the complex numbers $n^{-s}$
differ from that of $N^{-s}$ by less than $\pi/3$. Projecting the block sum
onto the direction of $N^{-s}$ therefore gives
$$
\abs{
\sum_{N<n\leq(1+\delta)N}
n^{-s}
}
\geq
\frac12
\sum_{N<n\leq(1+\delta)N}
n^{-\sigma}.
$$
The right side is bounded below by a positive constant times
$$
N^{1-\sigma}.
$$
For $\sigma<1$ it grows, and for $\sigma=1$ it stays bounded away from
$0$. Hence these tails do not tend to $0$, violating the Cauchy criterion.

:::

:::

::: {.pf-step #s1-3}

Therefore the defining Dirichlet series converges exactly in the
half-plane
$$
\boxed{\operatorname{Re}s>1}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For $t>0$,
$$
\frac1{e^t-1}
=
\sum_{m=1}^{\infty}e^{-mt}.
$$


::: pf-proof

Since $e^{-t}\in(0,1)$,
$$
\sum_{m=1}^{\infty}e^{-mt}
=
\frac{e^{-t}}{1-e^{-t}}
=
\frac1{e^t-1}.
$$

:::

:::

::: {.pf-step #s1-5}

If $\operatorname{Re}s>1$, then
$$
\int_0^\infty
\frac{t^{s-1}}{e^t-1}
\,dt
=
\Gamma(s)\zeta(s).
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\frac{t^{s-1}}{e^t-1}
=
\sum_{m=1}^{\infty}
t^{s-1}e^{-mt}.
$$
For $\sigma>1$ this series is absolutely integrable, so sum and integral may
be interchanged:
$$
\begin{aligned}
\int_0^\infty
\frac{t^{s-1}}{e^t-1}
\,dt
&=
\sum_{m=1}^{\infty}
\int_0^\infty
t^{s-1}e^{-mt}
\,dt.
\end{aligned}
$$
With $u=mt$,
$$
\int_0^\infty
t^{s-1}e^{-mt}
\,dt
=
m^{-s}\Gamma(s).
$$
Summing gives the result.

:::

:::

::: {.pf-step #s1-6}

Hence, for $\operatorname{Re}s>1$,
$$
\boxed{
\zeta(s)
=
\frac1{\Gamma(s)}
\int_0^\infty
\frac{t^{s-1}}{e^t-1}
\,dt.
}
$$


::: pf-proof

Divide step [](#s1-5){.pf-ref} by $\Gamma(s)$.

:::

:::

::: {.pf-step #s1-7}

On the slit plane
$$
\CC\setminus[0,\infty),
$$
use the branch
$$
w^{s-1}
=
\exp((s-1)\Log w),
\qquad
0<\arg w<2\pi,
$$
and define the Hankel contour integral
$$
I(s)
=
\int_H
\frac{w^{s-1}}{e^w-1}
\,dw,
$$
where $H$ is the contour described in the problem.


::: pf-proof

This fixes the branch used on the two sides of the positive-real-axis cut.
The upper side has argument $0$, while the lower side has argument $2\pi$.

:::

:::

::: {.pf-step #s1-8}

For $\operatorname{Re}s>1$,
$$
I(s)
=
(e^{2\pi i s}-1)
\int_0^\infty
\frac{t^{s-1}}{e^t-1}
\,dt.
$$


::: pf-proof

On the upper side of the cut, the contour runs from $+\infty$ to the small
circle and
$$
w^{s-1}=t^{s-1},
$$
so its contribution is
$$
-\int_\varepsilon^R
\frac{t^{s-1}}{e^t-1}
\,dt.
$$

On the lower side, the contour runs from the small circle back toward
$+\infty$, and
$$
w^{s-1}
=
e^{2\pi i(s-1)}t^{s-1}
=
e^{2\pi i s}t^{s-1}.
$$
Thus its contribution is
$$
e^{2\pi i s}
\int_\varepsilon^R
\frac{t^{s-1}}{e^t-1}
\,dt.
$$

Near $w=0$,
$$
e^w-1\sim w,
$$
so the integrand has size $O(\abs{w}^{\sigma-2})$. The small-circle contribution
is therefore $O(\varepsilon^{\sigma-1})$, which tends to $0$ because
$\sigma>1$. Letting $R\to\infty$ and $\varepsilon\to0^+$ gives the
formula.

:::

:::

::: {.pf-step #s1-9}

Hence for $\operatorname{Re}s>1$,
$$
\boxed{
I(s)
=
(e^{2\pi i s}-1)
\Gamma(s)\zeta(s).
}
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} and [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

The contour formula in step [](#s1-9){.pf-ref} provides the analytic continuation
mechanism for $\zeta$.


::: pf-proof

Away from the zeros of
$$
(e^{2\pi i s}-1)\Gamma(s),
$$
define
$$
\widetilde\zeta(s)
=
\frac{I(s)}
{(e^{2\pi i s}-1)\Gamma(s)}.
$$
For $\operatorname{Re}s>1$, step [](#s1-9){.pf-ref} shows that
$$
\widetilde\zeta(s)=\zeta(s).
$$
Thus this quotient continues the original Dirichlet-series function wherever
the quotient is holomorphic, with removable singularities filled by analytic
continuation.

:::

:::

::: {.pf-step #s1-11}

Suppose $\operatorname{Re}s<0$. The poles of
$$
\frac{w^{s-1}}{e^w-1}
$$
away from the branch point at $0$ are
$$
w=2\pi i n,
\qquad
n\in\ZZ\setminus\{0\},
$$
and the residue at such a pole is
$$
(2\pi i n)^{s-1}.
$$


::: pf-proof

The zeros of $e^w-1$ occur at $w=2\pi i n$. For $n\neq0$ these zeros are
simple because
$$
\frac{d}{dw}(e^w-1)
=
e^w
=1
$$
there. Hence the residue is the numerator evaluated at the pole.

:::

:::

::: {.pf-step #s1-12}

Expanding the small circle in the Hankel contour to infinity gives
$$
I(s)
=
-2\pi i
\sum_{n\in\ZZ\setminus\{0\}}
(2\pi i n)^{s-1}.
$$


::: pf-proof

For $\sigma<0$, the large-circle contribution tends to zero: the factor
$w^{s-1}$ has size $O(R^{\sigma-1})$, so after multiplication by the arc
length the left-half-plane contribution is $O(R^\sigma)$, while the
right-half-plane part has additional exponential decay from $e^w-1$.

As the inner circle expands, it crosses all poles $2\pi i n$, $n\neq0$.
With the orientation inherited from the Hankel contour, the residue theorem
contributes the negative of $2\pi i$ times the sum of the crossed residues.
The residue series is absolutely convergent because
$$
\sum_{n\neq0}\abs{n}^{\sigma-1}
$$
converges when $\sigma<0$.

:::

:::

::: {.pf-step #s1-13}

For $\operatorname{Re}s<0$,
$$
\sum_{n\in\ZZ\setminus\{0\}}
(2\pi i n)^{s-1}
=
i(2\pi)^{s-1}
\left(
e^{3\pi i s/2}
-
e^{\pi i s/2}
\right)
\zeta(1-s).
$$


::: pf-proof

Split the sum into $n>0$ and $n<0$. On the branch
$0<\arg w<2\pi$,
$$
(2\pi i n)^{s-1}
=
(2\pi n)^{s-1}
e^{i\pi(s-1)/2}
$$
for $n>0$, while
$$
(-2\pi i n)^{s-1}
=
(2\pi n)^{s-1}
e^{3\pi i(s-1)/2}.
$$
Therefore
$$
\begin{aligned}
\sum_{n\neq0}(2\pi i n)^{s-1}
&=
(2\pi)^{s-1}
\left[
e^{i\pi(s-1)/2}
+
e^{3\pi i(s-1)/2}
\right]
\sum_{n=1}^{\infty}n^{s-1}.
\end{aligned}
$$
Since
$$
\sum_{n=1}^{\infty}n^{s-1}
=
\zeta(1-s)
$$
and
$$
e^{i\pi(s-1)/2}
+
e^{3\pi i(s-1)/2}
=
i
\left(
e^{3\pi i s/2}
-
e^{\pi i s/2}
\right),
$$
the result follows.

:::

:::

::: {.pf-step #s1-14}

Hence for $\operatorname{Re}s<0$,
$$
I(s)
=
(2\pi)^s
\left(
e^{3\pi i s/2}
-
e^{\pi i s/2}
\right)
\zeta(1-s).
$$


::: pf-proof

Substitute step [](#s1-13){.pf-ref} into step [](#s1-12){.pf-ref} and use
$$
-2\pi i\cdot i(2\pi)^{s-1}
=(2\pi)^s.
$$

:::

:::

::: {.pf-step #s1-15}

Comparing steps [](#s1-9){.pf-ref} and [](#s1-14){.pf-ref} gives
$$
\boxed{
\zeta(s)
=
\zeta(1-s)
\frac{
e^{3\pi i s/2}
-
e^{\pi i s/2}
}{
e^{2\pi i s}-1
}
\frac{(2\pi)^s}{\Gamma(s)}.
}
$$


::: pf-proof

By step [](#s1-10){.pf-ref}, the analytic continuation of $\zeta$ is defined from the same
Hankel integral by
$$
\widetilde\zeta(s)
=
\frac{I(s)}
{(e^{2\pi i s}-1)\Gamma(s)}.
$$
For $\operatorname{Re}s<0$, substitute the residue evaluation from step
[](#s1-14){.pf-ref}:
$$
\widetilde\zeta(s)
=
\zeta(1-s)
\frac{
e^{3\pi i s/2}
-
e^{\pi i s/2}
}{
e^{2\pi i s}-1
}
\frac{(2\pi)^s}{\Gamma(s)}.
$$
Since $\widetilde\zeta$ agrees with the original zeta function on
$\operatorname{Re}s>1$, it is the analytic continuation denoted again by
$\zeta(s)$.

:::

:::

::: {.pf-step #s1-16}

The exponential quotient simplifies to
$$
\frac{
e^{3\pi i s/2}
-
e^{\pi i s/2}
}{
e^{2\pi i s}-1
}
=
\frac1{2\cos(\pi s/2)}.
$$


::: pf-proof

Factor
$$
e^{3\pi i s/2}
-
e^{\pi i s/2}
=
e^{\pi i s/2}(e^{\pi i s}-1)
$$
and
$$
e^{2\pi i s}-1
=
(e^{\pi i s}-1)(e^{\pi i s}+1).
$$
Then use
$$
e^{\pi i s}+1
=
2e^{\pi i s/2}
\cos\left(\frac{\pi s}{2}\right).
$$

:::

:::

::: {.pf-step #s1-17}

The functional equation is equivalently
$$
\boxed{
\zeta(s)
=
2^s\pi^{s-1}
\sin\left(\frac{\pi s}{2}\right)
\Gamma(1-s)
\zeta(1-s).
}
$$


::: pf-proof

By step [](#s1-16){.pf-ref}, step [](#s1-15){.pf-ref} becomes
$$
\zeta(s)
=
\zeta(1-s)
\frac{(2\pi)^s}{
2\cos(\pi s/2)\Gamma(s)
}.
$$
Euler's reflection formula gives
$$
\frac1{\Gamma(s)}
=
\Gamma(1-s)
\frac{\sin\pi s}{\pi}.
$$
Using
$$
\sin\pi s
=
2\sin\left(\frac{\pi s}{2}\right)
\cos\left(\frac{\pi s}{2}\right)
$$
yields the displayed form.

:::

:::

::: {.pf-step #s1-18}

Substituting $s=-1$ gives
$$
\zeta(-1)
=
2^{-1}\pi^{-2}
\sin\left(-\frac\pi2\right)
\Gamma(2)
\zeta(2).
$$


::: pf-proof

The right-hand side of step [](#s1-17){.pf-ref} is regular at $s=-1$, so direct
substitution is valid.

:::

:::

::: {.pf-step #s1-19}

Therefore
$$
\boxed{
\zeta(-1)
=
-\frac1{12}.
}
$$


::: pf-proof

Use
$$
\sin\left(-\frac\pi2\right)=-1,
\qquad
\Gamma(2)=1,
\qquad
\zeta(2)=\frac{\pi^2}{6}.
$$
Then
$$
\zeta(-1)
=
\frac1{2\pi^2}
(-1)
\frac{\pi^2}{6}
=
-\frac1{12}.
$$

:::

:::

::: {.pf-step #s1-20}

The value $-1/12$ is an analytic-continuation value, not the ordinary
sum of $1+2+3+\cdots$.


::: pf-proof

By step [](#s1-3){.pf-ref}, the Dirichlet series defining $\zeta(s)$ converges only for
$\operatorname{Re}s>1$. At $s=-1$ it becomes
$$
1+2+3+\cdots,
$$
which diverges. The value in step [](#s1-19){.pf-ref} belongs to the meromorphic
continuation.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} answer the convergence and integral-representation parts.
Steps [](#s1-7){.pf-ref} through [](#s1-17){.pf-ref} construct the contour continuation and functional equation.
Steps [](#s1-18){.pf-ref} through [](#s1-20){.pf-ref} compute and interpret $\zeta(-1)$.

:::

:::

:::
