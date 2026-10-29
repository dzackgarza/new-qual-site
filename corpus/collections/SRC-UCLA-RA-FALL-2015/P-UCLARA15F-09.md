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
$$
\iint_{\CC} |f_j(z)|^2 e^{-|z|^2}\,dx\,dy \leq C, \quad j = 1, 2, \ldots,
$$
for some constant $C > 0$. Show that there exists a subsequence $(f_{j_k})$ and an entire function $f$ such that we have
$$
\iint_{\CC} |f_{j_k}(z) - f(z)|^2 e^{-2|z|^2}\,dx\,dy \to 0, \quad k \to \infty.
$$
:::

::: {.solution}

Assume
$$
\int_{\CC}
|f_j(z)|^2e^{-|z|^2}\,dA(z)
\le C
$$
for every $j$, where $dA=dx\,dy$.

We first obtain compactness on bounded subsets of $\CC$.

::: pf

::: {.pf-step #s1-1}

For every entire function $g$ and every $z_0\in\CC$,
$$
\boxed{
|g(z_0)|^2
\le
\frac1\pi
\int_{D(z_0,1)}
|g(z)|^2\,dA(z)}.
$$


::: pf-proof

The function $|g|^2$ is subharmonic. The subharmonic mean-value inequality on the unit disk gives the displayed estimate.

:::

:::

::: {.pf-step #s1-2}

Fix $R>0$. If
$$
|z_0|\le R
$$
and
$$
z\in D(z_0,1),
$$
then
$$
|z|\le R+1.
$$


::: pf-proof

By the triangle inequality,
$$
|z|
\le
|z-z_0|+|z_0|
<
1+R.
$$

:::

:::

::: {.pf-step #s1-3}

Hence, for $|z_0|\le R$,
$$
\int_{D(z_0,1)}
|f_j(z)|^2\,dA(z)
\le
e^{(R+1)^2}
\int_{D(z_0,1)}
|f_j(z)|^2e^{-|z|^2}\,dA(z).
$$


::: pf-proof

On the disk from step [](#s1-2){.pf-ref},
$$
e^{|z|^2}
\le
e^{(R+1)^2}.
$$
Thus
$$
|f_j(z)|^2
=
|f_j(z)|^2e^{-|z|^2}e^{|z|^2}
\le
e^{(R+1)^2}|f_j(z)|^2e^{-|z|^2}.
$$
Integrate over the disk.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
|f_j(z_0)|^2
\le
\frac{C}{\pi}e^{(R+1)^2}}
$$
for all $j$ and all $|z_0|\le R$.


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} and use the global hypothesis
$$
\int_{\CC}|f_j|^2e^{-|z|^2}\,dA\le C.
$$

:::

:::

::: pf-step

Thus the family $\{f_j\}$ is locally uniformly bounded on $\CC$.


::: pf-proof

For every closed disk $\{|z|\le R\}$, step [](#s1-4){.pf-ref} gives a bound independent of $j$.

:::

:::

::: {.pf-step #s1-6}

By Montel's theorem, there is a subsequence
$$
(f_{j_k})
$$
converging uniformly on compact subsets of $\CC$ to an entire function $f$.


::: pf-proof

A locally uniformly bounded family of holomorphic functions is normal. Choose a convergent subsequence. The locally uniform limit of holomorphic functions is holomorphic.

:::

:::

::: {.pf-step #s1-7}

In particular,
$$
\boxed{
f_{j_k}(z)\to f(z)}
$$
for every $z\in\CC$.


::: pf-proof

Pointwise convergence follows from locally uniform convergence.

:::

:::

::: {.pf-step #s1-8}

Fatou's lemma gives
$$
\boxed{
\int_{\CC}
|f(z)|^2e^{-|z|^2}\,dA(z)
\le C}.
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
|f_{j_k}(z)|^2e^{-|z|^2}
\to
|f(z)|^2e^{-|z|^2}
$$
pointwise. These functions are nonnegative, so Fatou yields
$$
\int |f|^2e^{-|z|^2}
\le
\liminf_{k\to\infty}
\int |f_{j_k}|^2e^{-|z|^2}
\le C.
$$

:::

:::

::: {.pf-step #s1-9}

For every $R>0$ and every $|z|>R$,
$$
\boxed{
e^{-2|z|^2}
\le
e^{-R^2}e^{-|z|^2}}.
$$


::: pf-proof

If $|z|>R$, then
$$
e^{-|z|^2}
\le
e^{-R^2}.
$$
Thus
$$
e^{-2|z|^2}
=
e^{-|z|^2}e^{-|z|^2}
\le
e^{-R^2}e^{-|z|^2}.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\int_{|z|>R}
|f_{j_k}(z)|^2e^{-2|z|^2}\,dA(z)
\le
Ce^{-R^2}}
$$
for every $k$.


::: pf-proof

Use step [](#s1-9){.pf-ref} and the original weighted $L^2$ bound.

:::

:::

::: {.pf-step #s1-11}

Likewise,
$$
\boxed{
\int_{|z|>R}
|f(z)|^2e^{-2|z|^2}\,dA(z)
\le
Ce^{-R^2}}.
$$


::: pf-proof

Use step [](#s1-9){.pf-ref} and the bound from step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\int_{|z|>R}
|f_{j_k}(z)-f(z)|^2e^{-2|z|^2}\,dA(z)
\le
4Ce^{-R^2}.
$$


::: pf-proof

Use
$$
|a-b|^2\le2|a|^2+2|b|^2,
$$
then apply steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref}:
$$
\begin{aligned}
\int_{|z|>R}|f_{j_k}-f|^2e^{-2|z|^2}
&\le
2\int_{|z|>R}|f_{j_k}|^2e^{-2|z|^2}\\
&\quad+
2\int_{|z|>R}|f|^2e^{-2|z|^2}\\
&\le
4Ce^{-R^2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-13}

Fix $\varepsilon>0$. Choose $R>0$ so large that
$$
\boxed{
4Ce^{-R^2}<\frac{\varepsilon}{2}}.
$$


::: pf-proof

Since
$$
e^{-R^2}\to0,
$$
such $R$ exists.

:::

:::

::: {.pf-step #s1-14}

On the closed disk
$$
\overline{D(0,R)},
$$
one has
$$
\boxed{
\sup_{|z|\le R}
|f_{j_k}(z)-f(z)|
\to0}.
$$


::: pf-proof

This is local uniform convergence from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\int_{|z|\le R}
|f_{j_k}(z)-f(z)|^2
e^{-2|z|^2}
\,dA(z)
\to0.
$$


::: pf-proof

Since
$$
e^{-2|z|^2}\le1,
$$
$$
\begin{aligned}
\int_{|z|\le R}
|f_{j_k}-f|^2e^{-2|z|^2}\,dA
&\le
\pi R^2
\left(
\sup_{|z|\le R}|f_{j_k}-f|
\right)^2,
\end{aligned}
$$
and the right-hand side tends to zero by step [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Hence there exists $K$ such that for all $k\ge K$,
$$
\boxed{
\int_{|z|\le R}
|f_{j_k}-f|^2e^{-2|z|^2}\,dA
<
\frac{\varepsilon}{2}}.
$$


::: pf-proof

Apply step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

For $k\ge K$,
$$
\int_{\CC}
|f_{j_k}-f|^2e^{-2|z|^2}\,dA
<
\varepsilon.
$$


::: pf-proof

Split the integral into $|z|\le R$ and $|z|>R$. The inside contribution is $<\varepsilon/2$ by step [](#s1-16){.pf-ref}, while the outside contribution is $<\varepsilon/2$ by steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
\int_{\CC}
|f_{j_k}(z)-f(z)|^2e^{-2|z|^2}\,dA(z)
\longrightarrow0}.
$$


::: pf-proof

Step [](#s1-17){.pf-ref} is the $\varepsilon$-definition of convergence to zero.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the subsequence and entire limit, and step [](#s1-18){.pf-ref} gives the required weighted $L^2$ convergence.

:::

:::

:::
