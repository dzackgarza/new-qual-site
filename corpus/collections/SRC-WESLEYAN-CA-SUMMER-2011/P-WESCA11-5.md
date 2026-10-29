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
\gamma:[a,b]\to\CC
\]
be the given differentiable curve.

::: pf

::: {.pf-step #s1-1}

The contour integral of \(f\) along \(\gamma\) is defined by
\[
\boxed{
\int_\gamma f(z)\,dz
:=
\int_a^b
f(\gamma(t))\,\gamma'(t)\,dt}.
\]


::: pf-proof

This is the standard definition of integration of a complex-valued function
against the complex differential along a parametrized curve.

:::

:::

::: {.pf-step #s1-2}

If
\[
\gamma(t)=x(t)+iy(t),
\]
then
\[
\gamma'(t)=x'(t)+iy'(t).
\]


::: pf-proof

Differentiate real and imaginary parts componentwise.

:::

:::

::: pf-step

Hence
\[
\boxed{
\int_\gamma f(z)\,dz
=
\int_a^b
f(x(t)+iy(t))
\bigl(x'(t)+iy'(t)\bigr)\,dt}.
\]


::: pf-proof

Substitute step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

If
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


::: pf-proof

Expand
\[
(u+iv)(x'+iy')
=
(ux'-vy')
+
i(vx'+uy').
\]

:::

:::

::: pf-step

The integral is unchanged under an orientation-preserving \(C^1\)
reparametrization.


::: pf-proof

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

:::

::: pf-step

Reversing orientation changes the sign:
\[
\boxed{
\int_{\gamma^{-1}}f(z)\,dz
=
-\int_\gamma f(z)\,dz}.
\]


::: pf-proof

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
and substitution into step [](#s1-1){.pf-ref} gives the negative integral.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested definition.

:::

:::

:::
