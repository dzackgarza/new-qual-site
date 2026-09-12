---
schema: qual/card@1
id: P-RAF06E
kind: problem
title: "Laplace transform operator: Schur's test bound on L^p and L^2"
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Schur Test
  - Laplace Transform
  - Holder Inequality
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Fall 2006 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the legacy proof, which contained an unresolved exponent mismatch, by a complete Minkowski/change-of-variables derivation of the stated constant.
---

::: problem
Consider the linear operator
$$
(Tf)(y) := \int_0^\infty e^{-xy} f(x) \, dx, \quad y > 0.
$$

(a) Let $1 < p < \infty$, $\frac{1}{p} + \frac{1}{q} = 1$, and show that for nonnegative measurable functions $f, g : (0, \infty) \to [0, \infty)$,
$$
\int_0^\infty \int_0^\infty e^{-xy} f(x) g(y) \, dx \, dy \leq C_p \left(\int_0^\infty f(x)^p x^{p-2} \, dx\right)^{1/p} \left(\int_0^\infty g(y)^q \, dy\right)^{1/q},
$$
where
$$
C_p := \int_0^\infty e^{-z} z^{(1-p)/p} \, dz.
$$

(b) Show that the operator $T$ is bounded on $L^2((0, \infty))$ and $\|Tf\|_2 \leq C_2 \|f\|_2$, where $C_2$ is the constant in (a) with $p = 2$.
:::

::: solution
<1>1. Regard the double integral as the pairing of $Tf$ with $g$.
::: proof
For nonnegative measurable $f$ and $g$, Tonelli's theorem gives
\[
\int_0^\infty\int_0^\infty e^{-xy}f(x)g(y)\,dx\,dy
=\int_0^\infty (Tf)(y)g(y)\,dy.
\]
Hence Hölder's inequality will prove part (a) once we show
\[
\|Tf\|_{L^p(dy)}
\le C_p\left(\int_0^\infty f(x)^p x^{p-2}\,dx\right)^{1/p}.
\]
:::

<1>2. Rewrite $Tf$ by the change of variables $z=xy$.
::: proof
For $y>0$,
\[
(Tf)(y)
=\int_0^\infty e^{-xy}f(x)\,dx
=\int_0^\infty e^{-z}y^{-1}f(z/y)\,dz.
\]
Minkowski's integral inequality therefore yields
\[
\|Tf\|_p
\le
\int_0^\infty e^{-z}
\left(\int_0^\infty y^{-p}f(z/y)^p\,dy\right)^{1/p}dz.
\]
:::

<1>3. Compute the inner $L^p$ norm exactly.
::: proof
For fixed $z>0$, put $x=z/y$. Then $y=z/x$ and $dy=z x^{-2}\,dx$ after reversing the limits. Thus
\[
\begin{aligned}
\int_0^\infty y^{-p}f(z/y)^p\,dy
&=\int_0^\infty (x/z)^p f(x)^p\,z x^{-2}\,dx\\
&=z^{1-p}\int_0^\infty f(x)^p x^{p-2}\,dx.
\end{aligned}
\]
Consequently
\[
\left(\int_0^\infty y^{-p}f(z/y)^p\,dy\right)^{1/p}
=z^{(1-p)/p}
\left(\int_0^\infty f(x)^p x^{p-2}\,dx\right)^{1/p}.
\]
Substitution into Step 2 gives
\[
\|Tf\|_p
\le
\left(\int_0^\infty e^{-z}z^{(1-p)/p}\,dz\right)
\left(\int_0^\infty f(x)^p x^{p-2}\,dx\right)^{1/p}.
\]
The first factor is exactly $C_p$ (equivalently $C_p=\Gamma(1/p)$). Therefore
\[
\boxed{
\|Tf\|_p
\le C_p
\left(\int_0^\infty f(x)^p x^{p-2}\,dx\right)^{1/p}.}
\]
:::

<1>4. Complete part (a).
::: proof
Let $q$ be conjugate to $p$. By Step 1, Hölder's inequality, and Step 3,
\[
\begin{aligned}
\int_0^\infty\int_0^\infty e^{-xy}f(x)g(y)\,dx\,dy
&=\int_0^\infty (Tf)(y)g(y)\,dy\\
&\le \|Tf\|_p\|g\|_q\\
&\le C_p
\left(\int_0^\infty f(x)^p x^{p-2}\,dx\right)^{1/p}
\left(\int_0^\infty g(y)^q\,dy\right)^{1/q}.
\end{aligned}
\]
This is the desired inequality.
:::

<1>5. Deduce the $L^2$ estimate in part (b).
::: proof
For $p=2$, the weight is $x^{p-2}=1$. Step 3 gives, initially for nonnegative $f$,
\[
\|Tf\|_2\le C_2\|f\|_2,
\qquad
C_2=\int_0^\infty e^{-z}z^{-1/2}\,dz=\sqrt\pi.
\]
For an arbitrary complex-valued $f$,
\[
|Tf(y)|\le T(|f|)(y),
\]
so the same estimate follows:
\[
\boxed{\|Tf\|_2\le C_2\|f\|_2.}
\]
Thus $T$ extends to a bounded operator on $L^2((0,\infty))$ with operator norm at most $C_2$.
:::
:::
