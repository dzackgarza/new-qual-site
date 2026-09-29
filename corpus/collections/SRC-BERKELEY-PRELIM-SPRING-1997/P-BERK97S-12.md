---
schema: qual/card@1
id: P-BERK97S-12
kind: problem
title: Integral of $\sin^2x/x^2$ over $\RR$
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
\int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx.
\]
:::

::: {.solution}
Put
$$
J\coloneqq\int_0^\infty\frac{\sin 2x}{x}\,dx.
$$

::: pf

::: {.pf-step #s1}

One has
$$
\int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx=2J.
$$

::: pf-proof

The original integrand is even. It is bounded near $0$, since
$\sin x/x\to1$, and it is at most $1/x^2$ for large $x$, so the improper
integral converges. For $0<\varepsilon<R$, integration by parts gives
$$
\int_\varepsilon^R\frac{\sin^2x}{x^2}\,dx
=
\left[-\frac{\sin^2x}{x}\right]_\varepsilon^R
+\int_\varepsilon^R\frac{\sin 2x}{x}\,dx.
$$
The boundary term tends to $0$ as
$\varepsilon\downarrow0$ and $R\to\infty$. Hence
$$
\int_0^\infty\frac{\sin^2x}{x^2}\,dx=J,
$$
and evenness gives the claim.

:::

:::

::: {.pf-step #s2}

For $a>0$, define
$$
J(a)\coloneqq\int_0^\infty e^{-ax}\frac{\sin 2x}{x}\,dx.
$$
Then
$$
J(a)=\frac\pi2-\arctan\frac a2.
$$

::: pf-proof

For fixed $a>0$, differentiation under the integral sign is justified on a
small neighborhood of $a$ by an integrable exponential majorant. Thus
$$
J'(a)
=-\int_0^\infty e^{-ax}\sin 2x\,dx
=-\frac{2}{a^2+4}.
$$
Therefore
$$
J(a)=C-\arctan\frac a2
$$
for a constant $C$. With the substitution $u=ax$,
$$
\abs{J(a)}
\leq
\int_0^\infty e^{-u}\frac{\abs{\sin(2u/a)}}{u}\,du
\leq\frac2a,
$$
so $J(a)\to0$ as $a\to\infty$. Since
$\arctan(a/2)\to\pi/2$, it follows that $C=\pi/2$.

:::

:::

::: {.pf-step #s3}

The undamped Dirichlet integral satisfies
$$
J=\lim_{a\downarrow0}J(a)=\frac\pi2.
$$

::: pf-proof

For $a\geq0$, let
$$
\phi_a(x)\coloneqq\frac{e^{-ax}}{x}.
$$
On $[R,\infty)$ this function is positive and decreasing to $0$.
Integration by parts against the bounded primitive $-\cos(2x)/2$ of
$\sin(2x)$ gives, uniformly for $a\geq0$,
$$
\abs{\int_R^\infty\phi_a(x)\sin 2x\,dx}
\leq\phi_a(R)
\leq\frac1R.
$$
Thus the tails of $J(a)$, including $a=0$, are uniformly small as
$R\to\infty$. On every fixed interval $[0,R]$,
$$
e^{-ax}\frac{\sin 2x}{x}
\longrightarrow
\frac{\sin 2x}{x}
$$
and the integrands are dominated by $2$. Dominated convergence on
$[0,R]$, followed by the uniform tail estimate, gives
$$
J=\lim_{a\downarrow0}J(a).
$$
Step [](#s2){.pf-ref} now yields $J=\pi/2$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{\int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx=\pi}.
$$

::: pf-proof

By step [](#s1){.pf-ref} the integral equals $2J$, and step [](#s3){.pf-ref} gives
$J=\pi/2$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested value.

:::

:::

:::
