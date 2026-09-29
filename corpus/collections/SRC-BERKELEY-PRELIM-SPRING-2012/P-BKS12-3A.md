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

::: pf

::: {.pf-step #substitution-form}
After the substitution $x=y^4$,
$$
M_n
=
4\operatorname{Im}
\int_0^\infty
y^{4n+3}e^{-(1-i)y}\,dy.
$$

::: pf-proof
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

:::

::: {.pf-step #gamma-formula}
If $m\geq0$ and $a\in\CC$ has $\operatorname{Re}(a)>0$, then
$$
\int_0^\infty y^m e^{-ay}\,dy
=
\frac{m!}{a^{m+1}}.
$$

::: pf-proof
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

:::

::: {.pf-step #integral-value}
One has
$$
\int_0^\infty
y^{4n+3}e^{-(1-i)y}\,dy
=
\frac{(4n+3)!}{(1-i)^{4n+4}}.
$$

::: pf-proof
Apply step [](#gamma-formula){.pf-ref} with
$$
m=4n+3
$$
and
$$
a=1-i,
$$
whose real part is $1>0$.
:::

:::

::: {.pf-step #value-real}
The number in step [](#integral-value){.pf-ref} is real.

::: pf-proof
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

:::

::: {.pf-step #moment-zero}
Every moment of $f$ is
$$
\boxed{M_n=0}
$$
for $n=0,1,2,\ldots$.

::: pf-proof
By step [](#substitution-form){.pf-ref}, $M_n$ is four times the imaginary part of the integral in
step [](#integral-value){.pf-ref}. Step [](#value-real){.pf-ref} shows that this integral is real, so its imaginary
part is zero.
:::

:::

::: pf-qed
Step [](#moment-zero){.pf-ref} gives all requested moments.
:::

:::

:::
