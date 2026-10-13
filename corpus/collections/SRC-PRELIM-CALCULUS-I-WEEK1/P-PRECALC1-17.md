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

::: {.solution}
Assume
\[
f\sim g,
\]
so
\[
\lim_{x\to\infty}\frac{f(x)}{g(x)}=1.
\]

<1>1. One necessarily has
\[
\boxed{
f^2\sim g^2}.
\]

::: {.proof}
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

<1>2. Whenever the real square roots are defined eventually, one necessarily
has
\[
\boxed{
\sqrt f\sim\sqrt g}.
\]

::: {.proof}
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

<1>3. One necessarily has
\[
\boxed{
f+g\sim2g}.
\]

::: {.proof}
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

<1>4. One necessarily has
\[
\boxed{
g\sim f}.
\]

::: {.proof}
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

<1>5. Define
\[
\boxed{
f(x)=x,
\qquad
g(x)=x-1}.
\]

::: {.proof}
These are continuous real-valued functions.
:::

<1>6. For this pair,
\[
\boxed{
f\sim g}.
\]

::: {.proof}
\[
\frac{f(x)}{g(x)}
=
\frac{x}{x-1}
=
\frac1{1-1/x}
\longrightarrow1.
\]
:::

<1>7. But
\[
\frac{e^{f(x)}}{e^{g(x)}}
=
e^{f(x)-g(x)}
=
e.
\]

::: {.proof}
For the functions in step <1>5,
\[
f(x)-g(x)
=
x-(x-1)
=
1.
\]
:::

<1>8. Therefore
\[
\boxed{
e^f\not\sim e^g}.
\]

::: {.proof}
By step <1>7,
\[
\lim_{x\to\infty}
\frac{e^{f(x)}}{e^{g(x)}}
=
e\ne1.
\]
:::

<1>9. Hence the statement that does not necessarily follow is
\[
\boxed{\text{(c) }e^f\sim e^g}.
\]

::: {.proof}
Steps <1>1--<1>4 verify the other alternatives, while steps <1>5--<1>8
give a counterexample to (c).
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 gives the required choice.
:::
:::
