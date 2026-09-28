---
schema: qual/card@1
id: P-BKS12-3A
kind: problem
title: Moments of $\exp(-x^{1/4})\sin(x^{1/4})$
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
  note: Compared the authored statement with page 1 of the retained Spring 2012 solution PDF and independently reviewed its complex-exponential moment computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the x=y^4 substitution, the complex gamma integral by repeated integration by parts, and the reality of (1-i)^(4n+4).
---

::: {.problem}
The moments of a function $f$ are the numbers $\textstyle \int _ { 0 } ^ { \infty } x ^ { n } f ( x ) d x$ for $n = 0 , 1 , 2 , \ldots$ . Find the moments of $f ( x ) = \exp ( - x ^ { 1 / 4 } ) \sin ( x ^ { 1 / 4 } )$ . (Hint: complex analysis.)
:::

::: {.solution}
For $n\geq0$, let
$$
M_n
\coloneqq
\int_0^\infty
x^n e^{-x^{1/4}}\sin(x^{1/4})\,dx.
$$

<1>1. After the substitution $x=y^4$,
$$
M_n
=
4\operatorname{Im}
\int_0^\infty
y^{4n+3}e^{-(1-i)y}\,dy.
$$

::: {.proof}
The substitution gives
$$
dx=4y^3\,dy
$$
and
$$
x^n=y^{4n}.
$$
Also
$$
e^{-y}\sin y
=
\operatorname{Im}(e^{-(1-i)y}).
$$
The integral is absolutely convergent because the modulus of the complex
integrand is
$$
4y^{4n+3}e^{-y},
$$
which is integrable on $[0,\infty)$. Hence taking the imaginary part may
be interchanged with integration.
:::

<1>2. If $m\geq0$ and $a\in\CC$ has $\operatorname{Re}(a)>0$, then
$$
\int_0^\infty y^m e^{-ay}\,dy
=
\frac{m!}{a^{m+1}}.
$$

::: {.proof}
For $m=0$,
$$
\int_0^\infty e^{-ay}\,dy
=
\left[-\frac{e^{-ay}}a\right]_0^\infty
=
\frac1a,
$$
since $\operatorname{Re}(a)>0$ implies $e^{-ay}\to0$ as
$y\to\infty$.

For $m\geq1$, integration by parts gives
$$
\begin{aligned}
\int_0^\infty y^m e^{-ay}\,dy
&=
\left[
-\frac{y^m}{a}e^{-ay}
\right]_0^\infty
+
\frac{m}{a}
\int_0^\infty y^{m-1}e^{-ay}\,dy\\
&=
\frac{m}{a}
\int_0^\infty y^{m-1}e^{-ay}\,dy.
\end{aligned}
$$
The boundary term vanishes because exponential decay dominates the
polynomial factor. Induction on $m$ yields the formula.
:::

<1>3. One has
$$
\int_0^\infty
y^{4n+3}e^{-(1-i)y}\,dy
=
\frac{(4n+3)!}{(1-i)^{4n+4}}.
$$

::: {.proof}
Apply step <1>2 with
$$
m=4n+3
$$
and
$$
a=1-i,
$$
whose real part is $1>0$.
:::

<1>4. The number in step <1>3 is real.

::: {.proof}
One has
$$
(1-i)^2=-2i
$$
and therefore
$$
(1-i)^4=-4.
$$
Hence
$$
(1-i)^{4n+4}
=
\bigl((1-i)^4\bigr)^{n+1}
=
(-4)^{n+1},
$$
which is a nonzero real number. The numerator $(4n+3)!$ is also real.
:::

<1>5. Every moment of $f$ is
$$
\boxed{M_n=0}
$$
for $n=0,1,2,\ldots$.

::: {.proof}
By step <1>1, $M_n$ is four times the imaginary part of the integral in
step <1>3. Step <1>4 shows that this integral is real, so its imaginary
part is zero.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives all requested moments.
:::
:::
