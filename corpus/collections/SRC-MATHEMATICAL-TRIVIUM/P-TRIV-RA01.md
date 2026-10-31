---
schema: qual/card@1
id: P-TRIV-RA01
kind: problem
title: Derivatives of $\log\frac{a}{x}$, $\cos\arcsin x$ and $\frac{x^2+1}{x^3+1}$
classification:
  areas: [real-analysis]
  topics:
  - Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash reads `Find f(x), if f(x)=...`; any missing derivative mark in the source prompt is unresolved and is not silently supplied.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost prime in f'(x) and separated the three functions against Real Analysis Problem 1 on page 8 of the source PDF.
---

::: {.problem}
Find $f'(x)$, if $f(x) = \log\frac{a}{x}$, $\cos\arcsin x$, $\frac{x^2+1}{x^3+1}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
f(x)=\log\frac{a}{x},
$$
one has
$$
\boxed{f'(x)=-\frac1x}
$$
wherever the logarithm is defined.


::: pf-proof

On any interval on which $a/x>0$,
$$
\log\frac{a}{x}
=
\log\abs{a}-\log\abs{x}.
$$
Therefore
$$
f'(x)=-\frac1x.
$$

:::

:::

::: {.pf-step #s1-2}

For
$$
f(x)=\cos(\arcsin x),
$$
one has
$$
\boxed{f'(x)=-\frac{x}{\sqrt{1-x^2}}}
$$
for $\abs{x}<1$.


::: pf-proof

By the chain rule,
$$
f'(x)
=
-\sin(\arcsin x)
\cdot
\frac1{\sqrt{1-x^2}}.
$$
Since
$$
\sin(\arcsin x)=x,
$$
the formula follows.

:::

:::

::: {.pf-step #s1-3}

For
$$
f(x)=\frac{x^2+1}{x^3+1},
$$
one has
$$
\boxed{
f'(x)
=
\frac{-x^4-3x^2+2x}{(x^3+1)^2}
}
$$
for $x\neq-1$.


::: pf-proof

The quotient rule gives
$$
\begin{aligned}
f'(x)
&=
\frac{
2x(x^3+1)
-
(x^2+1)3x^2
}{(x^3+1)^2}\\
&=
\frac{
2x^4+2x-3x^4-3x^2
}{(x^3+1)^2}\\
&=
\frac{-x^4-3x^2+2x}{(x^3+1)^2}.
\end{aligned}
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the three requested derivatives.

:::

:::

:::
