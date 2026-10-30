---
schema: qual/card@1
id: P-UCLARA12S-03
kind: problem
title: 'Piecewise averages converge in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Convergence of Functions
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f\in L^1([0,1])$.
For $n\in\NN$, define
$$
f_n(x)=n\int_{k/n}^{(k+1)/n}f(y)\,dy
$$
whenever $x\in[k/n,(k+1)/n)$ and $0\le k\le n-1$.
Prove that $f_n\to f$ in $L^1([0,1])$.
:::

::: {.solution}

For each $n$, let $A_n:L^1([0,1])\to L^1([0,1])$ denote the averaging operator $A_nf=f_n$.

::: pf

::: {.pf-step #s1-1}

Each $A_n$ is an $L^1$-contraction:
$$
\boxed{\norm{A_nh}_{L^1}\le\norm h_{L^1}}
$$
for every $h\in L^1([0,1])$.


::: pf-proof

Write
$$
I_{k,n}=\left[\frac{k}{n},\frac{k+1}{n}\right).
$$
On $I_{k,n}$,
$$
A_nh(x)=n\int_{I_{k,n}}h(y)\,dy.
$$
Therefore
$$
\begin{aligned}
\norm{A_nh}_{L^1}
&=
\sum_{k=0}^{n-1}
\int_{I_{k,n}}
\abs{n\int_{I_{k,n}}h(y)\,dy}\,dx\\
&\le
\sum_{k=0}^{n-1}
\int_{I_{k,n}}\abs{h(y)}\,dy\\
&=
\norm h_{L^1}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

If $g\in C([0,1])$, then
$$
\norm{A_ng-g}_{L^1}\longrightarrow0.
$$


::: pf-proof

Let
$$
\omega_g(\delta)
\coloneqq
\sup\{\abs{g(x)-g(y)}:\abs{x-y}\le\delta\}.
$$
Uniform continuity of $g$ gives $\omega_g(\delta)\to0$ as $\delta\to0$. If $x\in I_{k,n}$, then
$$
\begin{aligned}
\abs{A_ng(x)-g(x)}
&=
\abs{n\int_{I_{k,n}}(g(y)-g(x))\,dy}\\
&\le
n\int_{I_{k,n}}\omega_g(1/n)\,dy\\
&=
\omega_g(1/n).
\end{aligned}
$$
Hence
$$
\norm{A_ng-g}_{L^1}
\le
\omega_g(1/n)
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-3}

For every $f\in L^1([0,1])$,
$$
\boxed{\norm{f_n-f}_{L^1}\longrightarrow0}.
$$


::: pf-proof

Fix $\varepsilon>0$. Since continuous functions are dense in $L^1([0,1])$, choose $g\in C([0,1])$ such that
$$
\norm{f-g}_{L^1}<\varepsilon.
$$
By step [](#s1-1){.pf-ref} and the triangle inequality,
$$
\begin{aligned}
\norm{A_nf-f}_{L^1}
&\le
\norm{A_n(f-g)}_{L^1}
+\norm{A_ng-g}_{L^1}
+\norm{g-f}_{L^1}\\
&\le
2\varepsilon+\norm{A_ng-g}_{L^1}.
\end{aligned}
$$
By step [](#s1-2){.pf-ref}, the last term tends to zero. Thus
$$
\limsup_{n\to\infty}\norm{A_nf-f}_{L^1}
\le2\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary, the limit is zero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the required $L^1$ convergence.

:::

:::

:::
