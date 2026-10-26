---
schema: qual/card@1
id: P-UCLARA15F-09
kind: problem
title: Normal families in a Gaussian-weighted $L^2$ space of entire functions
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 9 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $(f_j)$ be a sequence of entire functions such that, writing $z = x + iy$, we have
\[
\iint_{\mathbb{C}} |f_j(z)|^2 e^{-|z|^2}\,dx\,dy \leq C, \quad j = 1, 2, \ldots,
\]
for some constant $C > 0$. Show that there exists a subsequence $(f_{j_k})$ and an entire function $f$ such that we have
\[
\iint_{\mathbb{C}} |f_{j_k}(z) - f(z)|^2 e^{-2|z|^2}\,dx\,dy \to 0, \quad k \to \infty.
\]
:::

Assume
\[
\int_{\mathbb C}
|f_j(z)|^2e^{-|z|^2}\,dA(z)
\le C
\]
for every \(j\), where \(dA=dx\,dy\).

We first obtain compactness on bounded subsets of \(\mathbb C\).

::: pf

::: pf-step

For every entire function \(g\) and every \(z_0\in\mathbb C\),
\[
\boxed{
|g(z_0)|^2
\le
\frac1\pi
\int_{D(z_0,1)}
|g(z)|^2\,dA(z)}.
\]


::: pf-proof

The function \(|g|^2\) is subharmonic. The subharmonic mean-value inequality on the unit disk gives the displayed estimate.

:::

:::

::: pf-step

Fix \(R>0\). If
\[
|z_0|\le R
\]
and
\[
z\in D(z_0,1),
\]
then
\[
|z|\le R+1.
\]


::: pf-proof

By the triangle inequality,
\[
|z|
\le
|z-z_0|+|z_0|
<
1+R.
\]

:::

:::

::: pf-step

Hence, for \(|z_0|\le R\),
\[
\int_{D(z_0,1)}
|f_j(z)|^2\,dA(z)
\le
e^{(R+1)^2}
\int_{D(z_0,1)}
|f_j(z)|^2e^{-|z|^2}\,dA(z).
\]


::: pf-proof

On the disk from step <1>2,
\[
e^{|z|^2}
\le
e^{(R+1)^2}.
\]
Thus
\[
|f_j(z)|^2
=
|f_j(z)|^2e^{-|z|^2}e^{|z|^2}
\le
e^{(R+1)^2}|f_j(z)|^2e^{-|z|^2}.
\]
Integrate over the disk.

:::

:::

::: pf-step

Therefore
\[
\boxed{
|f_j(z_0)|^2
\le
\frac{C}{\pi}e^{(R+1)^2}}
\]
for all \(j\) and all \(|z_0|\le R\).


::: pf-proof

Combine steps <1>1--<1>3 and use the global hypothesis
\[
\int_{\mathbb C}|f_j|^2e^{-|z|^2}\,dA\le C.
\]

:::

:::

::: pf-step

Thus the family \(\{f_j\}\) is locally uniformly bounded on \(\mathbb C\).


::: pf-proof

For every closed disk \(\{|z|\le R\}\), step <1>4 gives a bound independent of \(j\).

:::

:::

::: pf-step

By Montel's theorem, there is a subsequence
\[
(f_{j_k})
\]
converging uniformly on compact subsets of \(\mathbb C\) to an entire function \(f\).


::: pf-proof

A locally uniformly bounded family of holomorphic functions is normal. Choose a convergent subsequence. The locally uniform limit of holomorphic functions is holomorphic.

:::

:::

::: pf-step

In particular,
\[
\boxed{
f_{j_k}(z)\to f(z)}
\]
for every \(z\in\mathbb C\).


::: pf-proof

Pointwise convergence follows from locally uniform convergence.

:::

:::

::: pf-step

Fatou's lemma gives
\[
\boxed{
\int_{\mathbb C}
|f(z)|^2e^{-|z|^2}\,dA(z)
\le C}.
\]


::: pf-proof

By step <1>7,
\[
|f_{j_k}(z)|^2e^{-|z|^2}
\to
|f(z)|^2e^{-|z|^2}
\]
pointwise. These functions are nonnegative, so Fatou yields
\[
\int |f|^2e^{-|z|^2}
\le
\liminf_{k\to\infty}
\int |f_{j_k}|^2e^{-|z|^2}
\le C.
\]

:::

:::

::: pf-step

For every \(R>0\) and every \(|z|>R\),
\[
\boxed{
e^{-2|z|^2}
\le
e^{-R^2}e^{-|z|^2}}.
\]


::: pf-proof

If \(|z|>R\), then
\[
e^{-|z|^2}
\le
e^{-R^2}.
\]
Thus
\[
e^{-2|z|^2}
=
e^{-|z|^2}e^{-|z|^2}
\le
e^{-R^2}e^{-|z|^2}.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\int_{|z|>R}
|f_{j_k}(z)|^2e^{-2|z|^2}\,dA(z)
\le
Ce^{-R^2}}
\]
for every \(k\).


::: pf-proof

Use step <1>9 and the original weighted \(L^2\) bound.

:::

:::

::: pf-step

Likewise,
\[
\boxed{
\int_{|z|>R}
|f(z)|^2e^{-2|z|^2}\,dA(z)
\le
Ce^{-R^2}}.
\]


::: pf-proof

Use step <1>9 and the bound from step <1>8.

:::

:::

::: pf-step

Therefore
\[
\int_{|z|>R}
|f_{j_k}(z)-f(z)|^2e^{-2|z|^2}\,dA(z)
\le
4Ce^{-R^2}.
\]


::: pf-proof

Use
\[
|a-b|^2\le2|a|^2+2|b|^2,
\]
then apply steps <1>10--<1>11:
\[
\begin{aligned}
\int_{|z|>R}|f_{j_k}-f|^2e^{-2|z|^2}
&\le
2\int_{|z|>R}|f_{j_k}|^2e^{-2|z|^2}\\
&\quad+
2\int_{|z|>R}|f|^2e^{-2|z|^2}\\
&\le
4Ce^{-R^2}.
\end{aligned}
\]

:::

:::

::: pf-step

Fix \(\varepsilon>0\). Choose \(R>0\) so large that
\[
\boxed{
4Ce^{-R^2}<\frac{\varepsilon}{2}}.
\]


::: pf-proof

Since
\[
e^{-R^2}\to0,
\]
such \(R\) exists.

:::

:::

::: pf-step

On the closed disk
\[
\overline{D(0,R)},
\]
one has
\[
\boxed{
\sup_{|z|\le R}
|f_{j_k}(z)-f(z)|
\to0}.
\]


::: pf-proof

This is local uniform convergence from step <1>6.

:::

:::

::: pf-step

Therefore
\[
\int_{|z|\le R}
|f_{j_k}(z)-f(z)|^2
e^{-2|z|^2}
\,dA(z)
\to0.
\]


::: pf-proof

Since
\[
e^{-2|z|^2}\le1,
\]
\[
\begin{aligned}
\int_{|z|\le R}
|f_{j_k}-f|^2e^{-2|z|^2}\,dA
&\le
\pi R^2
\left(
\sup_{|z|\le R}|f_{j_k}-f|
\right)^2,
\end{aligned}
\]
and the right-hand side tends to zero by step <1>14.

:::

:::

::: pf-step

Hence there exists \(K\) such that for all \(k\ge K\),
\[
\boxed{
\int_{|z|\le R}
|f_{j_k}-f|^2e^{-2|z|^2}\,dA
<
\frac{\varepsilon}{2}}.
\]


::: pf-proof

Apply step <1>15.

:::

:::

::: pf-step

For \(k\ge K\),
\[
\int_{\mathbb C}
|f_{j_k}-f|^2e^{-2|z|^2}\,dA
<
\varepsilon.
\]


::: pf-proof

Split the integral into \(|z|\le R\) and \(|z|>R\). The inside contribution is \(<\varepsilon/2\) by step <1>16, while the outside contribution is \(<\varepsilon/2\) by steps <1>12--<1>13.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\int_{\mathbb C}
|f_{j_k}(z)-f(z)|^2e^{-2|z|^2}\,dA(z)
\longrightarrow0}.
\]


::: pf-proof

Step <1>17 is the \(\varepsilon\)-definition of convergence to zero.

:::

:::

::: pf-qed

Step <1>6 gives the subsequence and entire limit, and step <1>18 gives the required weighted \(L^2\) convergence.

:::

:::
