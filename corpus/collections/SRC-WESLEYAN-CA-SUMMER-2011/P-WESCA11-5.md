---
schema: qual/card@1
id: P-WESCA11-5
kind: problem
title: 'Define a contour integral along a differentiable curve'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $\gamma$ be a differentiable curve in the complex plane and let $f$ be continuous on the trace of $\gamma$.
Define
\[
\int_\gamma f(z)\,dz.
\]
:::

::: {.solution}
Let
\[
\gamma:[a,b]\to\mathbb C
\]
be the given differentiable curve.

<1>1. The contour integral of \(f\) along \(\gamma\) is defined by
\[
\boxed{
\int_\gamma f(z)\,dz
:=
\int_a^b
f(\gamma(t))\,\gamma'(t)\,dt}.
\]

::: {.proof}
This is the standard definition of integration of a complex-valued function
against the complex differential along a parametrized curve.
:::

<1>2. If
\[
\gamma(t)=x(t)+iy(t),
\]
then
\[
\gamma'(t)=x'(t)+iy'(t).
\]

::: {.proof}
Differentiate real and imaginary parts componentwise.
:::

<1>3. Hence
\[
\boxed{
\int_\gamma f(z)\,dz
=
\int_a^b
f(x(t)+iy(t))
\bigl(x'(t)+iy'(t)\bigr)\,dt}.
\]

::: {.proof}
Substitute step <1>2 into step <1>1.
:::

<1>4. If
\[
f=u+iv,
\]
then
\[
\begin{aligned}
\int_\gamma f(z)\,dz
={}&
\int_a^b
\bigl(
u(\gamma(t))x'(t)-v(\gamma(t))y'(t)
\bigr)\,dt\\
&+
i\int_a^b
\bigl(
v(\gamma(t))x'(t)+u(\gamma(t))y'(t)
\bigr)\,dt.
\end{aligned}
\]

::: {.proof}
Expand
\[
(u+iv)(x'+iy')
=
(ux'-vy')
+
i(vx'+uy').
\]
:::

<1>5. The integral is unchanged under an orientation-preserving \(C^1\)
reparametrization.

::: {.proof}
Let
\[
\phi:[c,d]\to[a,b]
\]
be an increasing \(C^1\) bijection and let
\[
\widetilde\gamma=\gamma\circ\phi.
\]
Then
\[
\widetilde\gamma'(s)
=
\gamma'(\phi(s))\phi'(s).
\]
Thus
\[
\begin{aligned}
\int_{\widetilde\gamma}f(z)\,dz
&=
\int_c^d
f(\gamma(\phi(s)))
\gamma'(\phi(s))
\phi'(s)\,ds\\
&=
\int_a^b
f(\gamma(t))\gamma'(t)\,dt
\end{aligned}
\]
by the real change-of-variables formula.
:::

<1>6. Reversing orientation changes the sign:
\[
\boxed{
\int_{\gamma^{-1}}f(z)\,dz
=
-\int_\gamma f(z)\,dz}.
\]

::: {.proof}
Take
\[
\gamma^{-1}(t)
=
\gamma(a+b-t).
\]
Its derivative is
\[
-\gamma'(a+b-t),
\]
and substitution into step <1>1 gives the negative integral.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 is the requested definition.
:::
:::
