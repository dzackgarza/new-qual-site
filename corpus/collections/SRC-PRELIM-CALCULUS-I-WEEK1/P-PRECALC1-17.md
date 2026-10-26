---
schema: qual/card@1
id: P-PRECALC1-17
kind: problem
title: Operations preserving asymptotic equivalence $f\sim g$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For continuous functions $f,g:\mathbb R\to\mathbb R$, define the relation $\sim$ by $f\sim g$ iff
\[
\lim_{x\to\infty}\frac{f(x)}{g(x)}=1.
\]
Suppose that $f\sim g$. Which of these does NOT necessarily follow?

(a) $f^2\sim g^2$
(b) $\sqrt f\sim\sqrt g$
(c) $e^f\sim e^g$
(d) $f+g\sim 2g$
(e) $g\sim f$
:::

Assume
\[
f\sim g,
\]
so
\[
\lim_{x\to\infty}\frac{f(x)}{g(x)}=1.
\]

::: pf

::: pf-step

One necessarily has
\[
\boxed{
f^2\sim g^2}.
\]


::: pf-proof

\[
\frac{f(x)^2}{g(x)^2}
=
\left(
\frac{f(x)}{g(x)}
\right)^2
\longrightarrow
1^2
=
1.
\]

:::

:::

::: pf-step

Whenever the real square roots are defined eventually, one necessarily
has
\[
\boxed{
\sqrt f\sim\sqrt g}.
\]


::: pf-proof

On the eventual domain where the square roots are real,
\[
\frac{\sqrt{f(x)}}{\sqrt{g(x)}}
=
\sqrt{
\frac{f(x)}{g(x)}
}.
\]
Since
\[
\frac{f(x)}{g(x)}\to1
\]
and the square-root function is continuous at \(1\), the ratio tends to \(1\).

:::

:::

::: pf-step

One necessarily has
\[
\boxed{
f+g\sim2g}.
\]


::: pf-proof

\[
\frac{f(x)+g(x)}{2g(x)}
=
\frac12
\left(
\frac{f(x)}{g(x)}+1
\right)
\longrightarrow
\frac12(1+1)
=
1.
\]

:::

:::

::: pf-step

One necessarily has
\[
\boxed{
g\sim f}.
\]


::: pf-proof

Since
\[
\frac{f(x)}{g(x)}\to1,
\]
the ratio is nonzero for all sufficiently large \(x\). Hence
\[
\frac{g(x)}{f(x)}
=
\frac1{f(x)/g(x)}
\longrightarrow
1.
\]

:::

:::

::: pf-step

Define
\[
\boxed{
f(x)=x,
\qquad
g(x)=x-1}.
\]


::: pf-proof

These are continuous real-valued functions.

:::

:::

::: pf-step

For this pair,
\[
\boxed{
f\sim g}.
\]


::: pf-proof

\[
\frac{f(x)}{g(x)}
=
\frac{x}{x-1}
=
\frac1{1-1/x}
\longrightarrow1.
\]

:::

:::

::: pf-step

But
\[
\frac{e^{f(x)}}{e^{g(x)}}
=
e^{f(x)-g(x)}
=
e.
\]


::: pf-proof

For the functions in step <1>5,
\[
f(x)-g(x)
=
x-(x-1)
=
1.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
e^f\not\sim e^g}.
\]


::: pf-proof

By step <1>7,
\[
\lim_{x\to\infty}
\frac{e^{f(x)}}{e^{g(x)}}
=
e\ne1.
\]

:::

:::

::: pf-step

Hence the statement that does not necessarily follow is
\[
\boxed{\text{(c) }e^f\sim e^g}.
\]


::: pf-proof

Steps <1>1--<1>4 verify the other alternatives, while steps <1>5--<1>8
give a counterexample to (c).

:::

:::

::: pf-qed

Step <1>9 gives the required choice.

:::

:::
