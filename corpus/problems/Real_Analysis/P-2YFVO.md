---
schema: qual/card@1
id: P-2YFVO
kind: problem
title: Support, uniform continuity, vanishing at infinity, and derivatives of convolutions
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - Differentiation
  - Continuity
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
(a) Show that if $f, g$ are continuous and compactly supported, then so is $f\ast g$.

(b) Show that if $f\in L^1$ and $g$ is bounded, then  $f\ast g$ is bounded and uniformly continuous.

(c) If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

(d) Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

(i) $f, g\in L^1$ are both bounded.

(ii) $f, g\in L^1$ with just $g$ bounded.

(iii) $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

(iv) $f\in L^1$ and $g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

(e) Show that if $f\in L^1$ and $g$ is bounded and differentiable with every $\dd{g}{x_i}$ bounded, then $$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$$
:::

::: {.solution}
Write $\norm{\cdot}$ for the Euclidean norm on $\RR^n$ and $e_i$ for the $i$th standard basis vector.

::: pf

::: {.pf-step #support}

If $f$ and $g$ are compactly supported, then $\supp(f\ast g)\subseteq\supp f+\supp g$, which is compact.

::: pf-proof

The set $\supp f+\supp g$ is the image of the compact set $\supp f\times\supp g$ under the continuous map $(a,b)\mapsto a+b$, so it is compact and hence closed.
If $x\notin\supp f+\supp g$, then $(x-\supp g)\cap\supp f=\emptyset$, so $f(x-y)g(y)=0$ for every $y$ and $f\ast g(x)=0$.
So $\theset{f\ast g\ne0}$ lies in the closed set $\supp f+\supp g$, and so does its closure $\supp(f\ast g)$.

:::

:::

::: pf-step

(a) If $f,g$ are continuous and compactly supported, then $f\ast g$ is continuous and compactly supported.

::: pf-proof

For all $x,h$,
$$
\abs{f\ast g(x+h)-f\ast g(x)}
\le\int\abs{f(x+h-y)-f(x-y)}\,\abs{g(y)}\,dy
\le\norm{g}_1\sup_z\abs{f(z+h)-f(z)}.
$$
A continuous function with compact support is uniformly continuous, so the right side tends to $0$ as $h\to0$, uniformly in $x$.
Compact support is step [](#support){.pf-ref}.

:::

:::

::: {.pf-step #bounded-uc}

(b) If $f\in L^1$ and $\abs{g}\le M$ almost everywhere, then $\abs{f\ast g}\le M\norm{f}_1$ and $f\ast g$ is uniformly continuous.

::: pf-proof

::: {.pf-step #translate}

For $h\in\RR^n$ let $\tau_hf(y)\coloneqq f(y-h)$. Then $\abs{f\ast g(x)}\le M\norm{f}_1$ and $\abs{f\ast g(x+h)-f\ast g(x)}\le M\norm{\tau_{-h}f-f}_1$ for all $x,h$.

::: pf-proof

$\abs{f\ast g(x)}\le\int\abs{f(x-y)}\,\abs{g(y)}\,dy\le M\norm{f}_1$.
Also $f\ast g(x+h)-f\ast g(x)=\int\big(f(x+h-y)-f(x-y)\big)g(y)\,dy$, and the change of variables $u=x-y$ bounds its absolute value by $M\int\abs{f(u+h)-f(u)}\,du=M\norm{\tau_{-h}f-f}_1$.

:::

:::

::: {.pf-step #l1-translation}

$\lim_{h\to0}\norm{\tau_hf-f}_1=0$.

::: pf-proof

For a continuous $\varphi$ with compact support the claim holds by uniform continuity of $\varphi$ and dominated convergence on a fixed compact set.
Given $\eps>0$, density of $C_c(\RR^n)$ in $L^1(\RR^n)$ gives such a $\varphi$ with $\norm{f-\varphi}_1<\eps/3$.
Since $\norm{\tau_h(f-\varphi)}_1=\norm{f-\varphi}_1$, we get $\norm{\tau_hf-f}_1\le\norm{\tau_h(f-\varphi)}_1+\norm{\tau_h\varphi-\varphi}_1+\norm{\varphi-f}_1<\eps$ for $\norm{h}$ small.

:::

:::

::: pf-step

$f\ast g$ is bounded and uniformly continuous.

::: pf-proof

Boundedness is step [](#translate){.pf-ref}.
Given $\eps>0$, step [](#l1-translation){.pf-ref} gives $\delta>0$ with $\norm{\tau_{-h}f-f}_1<\eps/M$ for $\norm{h}<\delta$, and then step [](#translate){.pf-ref} gives $\abs{f\ast g(x+h)-f\ast g(x)}<\eps$ for all $x$ and all $\norm{h}<\delta$.

:::

:::

:::

:::

::: pf-step

(c) Yes: if $f$ and $g$ are compactly supported, then $f\ast g$ is $\boxed{\text{compactly supported}}$.

::: pf-proof

The argument of step [](#support){.pf-ref} uses no continuity.

:::

:::

::: pf-step

(d) Under each of the four assumptions, $f\ast g$ vanishes at infinity.

::: pf-proof

::: {.pf-step #both-bounded}

(i) If $f,g\in L^1$ are both bounded, then $f\ast g$ vanishes at infinity.

::: pf-proof

Split $f\ast g(x)$ at $\norm{y}=\norm{x}/2$.
On $\theset{\norm{y}\le\norm{x}/2}$ we have $\norm{x-y}\ge\norm{x}/2$, so the substitution $z=x-y$ gives
$$
\abs{\int_{\norm{y}\le\norm{x}/2}f(x-y)g(y)\,dy}\le\norm{g}_\infty\int_{\norm{z}\ge\norm{x}/2}\abs{f(z)}\,dz.
$$
On the complement,
$$
\abs{\int_{\norm{y}>\norm{x}/2}f(x-y)g(y)\,dy}\le\norm{f}_\infty\int_{\norm{y}>\norm{x}/2}\abs{g(y)}\,dy.
$$
Both tail integrals of $L^1$ functions tend to $0$ as $\norm{x}\to\infty$ by dominated convergence.

:::

:::

::: pf-step

(ii) If $f,g\in L^1$ and $g$ is bounded, then $f\ast g$ vanishes at infinity.

::: pf-proof

For $M>0$ write $f=f_M+r_M$ with $f_M=f\chi_{\theset{\abs{f}\le M}}$.
Then $\norm{r_M}_1=\int_{\theset{\abs{f}>M}}\abs{f}\to0$ as $M\to\infty$ by dominated convergence, and $\norm{r_M\ast g}_\infty\le\norm{r_M}_1\norm{g}_\infty$.
The function $f_M$ is bounded and in $L^1$, so $f_M\ast g$ vanishes at infinity by step [](#both-bounded){.pf-ref}.
Given $\eps>0$, choose $M$ with $\norm{r_M\ast g}_\infty<\eps/2$, then $R$ with $\abs{f_M\ast g(x)}<\eps/2$ for $\norm{x}>R$; for such $x$, $\abs{f\ast g(x)}<\eps$.

:::

:::

::: pf-step

(iii) If $f,g$ are smooth and compactly supported, then $f\ast g$ is smooth and vanishes at infinity.

::: pf-proof

Every $D^\alpha g$ is bounded, so step [](#derivative){.pf-ref} applied repeatedly gives $D^\alpha(f\ast g)=f\ast D^\alpha g$, which is continuous by step [](#bounded-uc){.pf-ref}.
By step [](#support){.pf-ref}, $f\ast g$ is zero outside a compact set.

:::

:::

::: pf-step

(iv) If $f\in L^1$ and $g$ is smooth and compactly supported, then $f\ast g$ is smooth and vanishes at infinity.

::: pf-proof

Smoothness follows from step [](#derivative){.pf-ref} and step [](#bounded-uc){.pf-ref} as in (iii).
Choose $R$ with $\supp g\subseteq\theset{\norm{y}\le R}$.
For $\norm{x}\ge2R$ and $\norm{y}\le R$, $\norm{x-y}\ge\norm{x}/2$, so
$$
\abs{f\ast g(x)}\le\norm{g}_\infty\int_{\norm{y}\le R}\abs{f(x-y)}\,dy\le\norm{g}_\infty\int_{\norm{u}\ge\norm{x}/2}\abs{f(u)}\,du,
$$
which tends to $0$ as $\norm{x}\to\infty$ because $f\in L^1$.

:::

:::

:::

:::

::: {.pf-step #derivative}

(e) If $f\in L^1$ and $g$ is bounded and differentiable with $\dd{g}{x_i}$ bounded, then $\dd{}{x_i}(f\ast g)=f\ast\dd{g}{x_i}$.

::: pf-proof

For $h\ne0$, the change of variables $y\mapsto y+he_i$ gives
$$
\frac{(f\ast g)(x+he_i)-(f\ast g)(x)}{h}=\int f(x-y)\,\frac{g(y+he_i)-g(y)}{h}\,dy.
$$
As $h\to0$ the integrand converges pointwise to $f(x-y)\dd{g}{y_i}(y)$, by differentiability of $g$ in the direction $e_i$.
By the mean value theorem applied to $t\mapsto g(y+te_i)$, the integrand is bounded by $\abs{f(x-y)}\sup_z\abs{\dd{g}{z_i}(z)}$, which is integrable in $y$ because $f\in L^1$.
Dominated convergence lets $h\to0$ pass under the integral.

:::

:::

:::

:::
