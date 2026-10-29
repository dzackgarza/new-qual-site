---
schema: qual/card@1
id: P-UCLARA12S-06
kind: problem
title: Translates of a function with nonvanishing Fourier transform
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Suppose $f\in L^2(\RR)$ and $\widehat f(\xi)>0$ for almost every $\xi$.
Show that the set of finite linear combinations of translates of $f$ is dense in $L^2(\RR)$.
:::

::: {.solution}

For $a\in\RR$, write
$$
(\tau_a f)(x)=f(x+a),
$$
and let
$$
M\coloneqq
\overline{\operatorname{span}\{\tau_a f:a\in\RR\}}^{L^2}.
$$

::: pf

::: {.pf-step #s1-1}

It suffices to prove that $M^\perp=\{0\}$.


::: pf-proof

Since $M$ is a closed subspace of the Hilbert space $L^2(\RR)$,
$$
L^2(\RR)=M\oplus M^\perp.
$$
Thus $M=L^2(\RR)$ exactly when $M^\perp=\{0\}$.

:::

:::

::: {.pf-step #s1-2}

If $g\in M^\perp$, then the $L^1$ function
$$
h(\xi)\coloneqq
\widehat f(\xi)\overline{\widehat g(\xi)}
$$
has Fourier transform identically zero.


::: pf-proof

Because $\widehat f,\widehat g\in L^2(\RR)$ by Plancherel, Cauchy--Schwarz gives
$$
\norm h_{L^1}
\le
\norm{\widehat f}_{L^2}
\norm{\widehat g}_{L^2}
<\infty.
$$
For every $a\in\RR$, orthogonality gives
$$
0
=
\langle\tau_a f,g\rangle_{L^2}.
$$
Using Plancherel and the translation formula for the Fourier transform,
$$
\widehat{\tau_a f}(\xi)
=
e^{2\pi i a\xi}\widehat f(\xi)
$$
for the convention
$$
\widehat u(\xi)=\int_{\RR}u(x)e^{-2\pi i x\xi}\,dx.
$$
Hence
$$
0
=
\int_{\RR}
e^{2\pi i a\xi}
h(\xi)\,d\xi
$$
for every $a\in\RR$. This is the inverse Fourier transform of $h$, so the Fourier transform of $h$ vanishes identically as well.

:::

:::

::: {.pf-step #s1-3}

Every $g\in M^\perp$ is zero.


::: pf-proof

By the uniqueness theorem for the Fourier transform on $L^1(\RR)$, step [](#s1-2){.pf-ref} implies
$$
h(\xi)
=
\widehat f(\xi)\overline{\widehat g(\xi)}
=0
$$
for almost every $\xi$. By hypothesis,
$$
\widehat f(\xi)>0
$$
for almost every $\xi$, so
$$
\widehat g(\xi)=0
$$
almost everywhere. Plancherel then gives $g=0$ in $L^2(\RR)$.

:::

:::

::: {.pf-step #s1-4}

Finite linear combinations of translates of $f$ are dense in $L^2(\RR)$.


::: pf-proof

Step [](#s1-3){.pf-ref} gives $M^\perp=\{0\}$. By step [](#s1-1){.pf-ref}, $M=L^2(\RR)$, and $M$ is by definition the closure of the finite linear combinations of translates.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required density statement.

:::

:::

:::
