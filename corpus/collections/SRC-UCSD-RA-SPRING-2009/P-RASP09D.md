---
schema: qual/card@1
id: P-RASP09D
kind: problem
title: "Principal value of 1/(x1 + x2) defines a distribution on R^2"
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
  - Principal Value
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Spring 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Show that on $\mathbb{R}^2$ (with coordinates $(x_1, x_2)$),
$$
\left\langle \operatorname{PV}\left(\frac{x_1 + x_2}{|x|^3}\right), \varphi \right\rangle = \lim_{\varepsilon \to 0} \int_{|x| > \varepsilon} \varphi(x) \frac{x_1 + x_2}{|x|^3} \, dm, \quad \varphi \in C_c^\infty(\mathbb{R}^2),
$$
exists and defines a distribution on $\mathbb{R}^2$.
:::


::: solution
<1>1. Use oddness of the kernel to expose cancellation.
::: proof
Set
\[
K(x):=\frac{x_1+x_2}{|x|^3},
\qquad x\ne0.
\]
Then
\[
K(-x)=-K(x).
\]
For $\varepsilon>0$, the domain $\{|x|>\varepsilon\}$ is symmetric under $x\mapsto -x$. Therefore, after the change of variables $x\mapsto -x$,
\[
\begin{aligned}
I_\varepsilon(\varphi)
&:=\int_{|x|>\varepsilon}\varphi(x)K(x)\,dx\\
&=\frac12\int_{|x|>\varepsilon}
\bigl(\varphi(x)-\varphi(-x)\bigr)K(x)\,dx.
\end{aligned}
\]
:::

<1>2. Show that the symmetrized integrand is absolutely integrable near the origin.
::: proof
Fix $R>0$ so that $\operatorname{supp}\varphi\subset B(0,R)$. For $|x|\le R$,
\[
|\varphi(x)-\varphi(-x)|
\le 2|x|\sup_{|y|\le R}|\nabla\varphi(y)|.
\]
Also
\[
|K(x)|
\le \frac{|x_1|+|x_2|}{|x|^3}
\le \frac{\sqrt2}{|x|^2}.
\]
Hence
\[
\left|
\bigl(\varphi(x)-\varphi(-x)\bigr)K(x)
\right|
\le
\frac{2\sqrt2}{|x|}
\sup_{|y|\le R}|\nabla\varphi(y)|.
\]
The function $|x|^{-1}$ is locally integrable on $\mathbb R^2$, because in polar coordinates
\[
\int_{|x|<R}\frac{dx}{|x|}
=2\pi R<\infty.
\]
Thus the symmetrized integrand is absolutely integrable near $0$; away from $0$ it is integrable because $\varphi$ has compact support.
:::

<1>3. Pass to the principal-value limit.
::: proof
By Step 2 and dominated convergence,
\[
\lim_{\varepsilon\downarrow0}I_\varepsilon(\varphi)
=rac12\int_{\mathbb R^2}
\bigl(\varphi(x)-\varphi(-x)\bigr)K(x)\,dx.
\]
Therefore the principal value exists for every test function $\varphi$.
:::

<1>4. Verify continuity on the test-function space.
::: proof
Let $L\subset\mathbb R^2$ be compact, and suppose $\operatorname{supp}\varphi\subset L$. Choose $R$ with
\[
L\cup(-L)\subset B(0,R).
\]
Using the estimate from Step 2,
\[
\begin{aligned}
|\langle \operatorname{PV}(K),\varphi\rangle|
&\le \frac12\int_{B(0,R)}
\frac{2\sqrt2}{|x|}
\sup_{B(0,R)}|\nabla\varphi|\,dx\\
&\le C_R\sup_{B(0,R)}|\nabla\varphi|.
\end{aligned}
\]
Thus the functional is continuous on every fixed compact-support test-function space. It is linear by construction, so
\[
\boxed{
\operatorname{PV}\!\left(\frac{x_1+x_2}{|x|^3}\right)
\in\mathcal D'(\mathbb R^2).}
\]
:::
:::
