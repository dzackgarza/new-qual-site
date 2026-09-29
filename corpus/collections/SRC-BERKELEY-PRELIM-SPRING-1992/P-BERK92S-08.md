---
schema: qual/card@1
id: P-BERK92S-08
kind: problem
title: The integral $\int_{-\infty}^{\infty}\sin^3x/x^3\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Evaluate
\[
\int_{-\infty}^{\infty}\frac{\sin^3x}{x^3}\,dx.
\]
:::

::: {.solution}
Put
$$
J\coloneqq\int_0^\infty\frac{\sin^3x}{x^3}\,dx.
$$

::: pf

::: {.pf-step #s1}

The given integral is absolutely convergent and equals $2J$.

::: pf-proof

Near zero, $\sin x/x\to1$, so $\sin^3x/x^3$ extends continuously
across zero. For $\abs{x}\ge1$,
$$
\abs{\frac{\sin^3x}{x^3}}\le\frac1{\abs{x}^3},
$$
which is integrable at infinity. The integrand is even, hence the
whole-line integral is $2J$.

:::

:::

::: {.pf-step #s2}

$$
J=\frac38\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx.
$$

::: pf-proof

Integrating by parts with
$u=\sin^3x$ and $dv=x^{-3}\,dx$ gives
$$
J
=\frac32\int_0^\infty\frac{\sin^2x\cos x}{x^2}\,dx.
$$
The boundary term vanishes: as $x\downarrow0$,
$\sin^3x/x^2\to0$, and as $x\to\infty$ it is bounded by $x^{-2}$.
Using
$$
\sin^2x\cos x=\frac{\cos x-\cos3x}{4}
$$
gives the claim.

:::

:::

::: {.pf-step #s3}

$$
\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx=\pi.
$$

::: pf-proof

Another integration by parts gives
$$
\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx
=
\int_0^\infty\frac{3\sin3x-\sin x}{x}\,dx.
$$
The boundary term again vanishes: near zero,
$\cos x-\cos3x=O(x^2)$, and at infinity the numerator is bounded.
By the [[P-PRACT20-W3-24|Dirichlet integral]],
$$
\int_0^\infty\frac{\sin(ax)}x\,dx=\frac\pi2
\qquad(a>0),
$$
where the general case follows from the substitution $t=ax$. Hence
the last display equals
$$
3\frac\pi2-\frac\pi2=\pi.
$$

:::

:::

::: {.pf-step #s4}

The requested integral is $\boxed{3\pi/4}$.

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
J=\frac{3\pi}{8}.
$$
Step [](#s1){.pf-ref} therefore gives
$$
\int_{-\infty}^{\infty}\frac{\sin^3x}{x^3}\,dx
=2J
=\frac{3\pi}{4}.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} evaluates the integral.

:::

:::

:::
