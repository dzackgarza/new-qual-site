---
schema: qual/card@1
id: P-WESRA16-B4
kind: problem
title: 'Limits of integrals of powers of a nonnegative function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group B, problem B4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f:\RR\to[0,\infty)$ be measurable with $\operatorname{supp}f\subset[0,1]$.
Put
\[
X=\{x\in[0,1]:f(x)>1\},\qquad
Y=\{x\in[0,1]:f(x)=1\},\qquad
Z=\{x\in[0,1]:f(x)<1\}.
\]
Assuming
\[
\lim_{n\to\infty}\int_{\RR}f^n
\]
exists in $[0,\infty]$, prove that there are $\alpha,\beta,\gamma\in[0,\infty]$ such that
\[
\lim_{n\to\infty}\int_{\RR}f^n
=\alpha\lambda(X)+\beta\lambda(Y)+\gamma\lambda(Z).
\]
Determine the relevant contributions using monotone and dominated convergence.
:::

::: {.solution}

Because $\operatorname{supp}f\subseteq[0,1]$ and $X,Y,Z$ partition $[0,1]$,
$$
\int_{\RR}f^n
=\int_Xf^n+\int_Yf^n+\int_Zf^n.
$$

::: pf

::: {.pf-step #s1-1}

On $Y$,
$$
\int_Y f^n=\lambda(Y)
$$
for every $n$.


::: pf-proof

By definition, $f(x)=1$ for every $x\in Y$. Hence $f^n=1$ on $Y$, so
$$
\int_Yf^n=\int_Y1=\lambda(Y).
$$

:::

:::

::: {.pf-step #s1-2}

On $Z$,
$$
\lim_{n\to\infty}\int_Zf^n=0.
$$


::: pf-proof

For every $x\in Z$, one has $0\leq f(x)<1$, hence
$$
f(x)^n\longrightarrow0.
$$
Moreover,
$$
0\leq f(x)^n\leq1
$$
for every $x\in Z$ and every $n$. Since $Z\subseteq[0,1]$, the dominating function $\mathbf1_Z$ is integrable. The Dominated Convergence Theorem therefore gives
$$
\lim_{n\to\infty}\int_Zf^n
=\int_Z\lim_{n\to\infty}f^n
=0.
$$

:::

:::

::: {.pf-step #s1-3}

On $X$, the functions $f^n\mathbf1_X$ increase pointwise to the extended-valued function
$$
h(x)=
\begin{cases}
\infty,&x\in X,\\
0,&x\notin X.
\end{cases}
$$


::: pf-proof

If $x\in X$, then $f(x)>1$, so the sequence $f(x)^n$ is increasing and tends to $\infty$. If $x\notin X$, multiplication by $\mathbf1_X(x)$ makes every term zero. This proves the asserted monotone pointwise convergence.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\lim_{n\to\infty}\int_Xf^n
=
\begin{cases}
0,&\lambda(X)=0,\\
\infty,&\lambda(X)>0.
\end{cases}
$$


::: pf-proof

By step [](#s1-3){.pf-ref} and the Monotone Convergence Theorem,
$$
\lim_{n\to\infty}\int_Xf^n
=\int h.
$$
If $\lambda(X)=0$, then $h=0$ almost everywhere and the integral is $0$. If $\lambda(X)>0$, then for every $M>0$,
$$
h\geq M\mathbf1_X,
$$
so
$$
\int h\geq M\lambda(X).
$$
Since $M$ is arbitrary, $\int h=\infty$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\lim_{n\to\infty}\int_{\RR}f^n
=
\begin{cases}
\lambda(Y),&\lambda(X)=0,\\
\infty,&\lambda(X)>0.
\end{cases}
$$


::: pf-proof

Use the decomposition before step [](#s1-1){.pf-ref}. The $Y$-term equals $\lambda(Y)$ by step [](#s1-1){.pf-ref}, the $Z$-term tends to $0$ by step [](#s1-2){.pf-ref}, and the $X$-term has the limit computed in step [](#s1-4){.pf-ref}. Adding these three limits gives the displayed formula.

:::

:::

::: {.pf-step #s1-6}

There exist $\alpha,\beta,\gamma\in[0,\infty]$ such that
$$
\boxed{\lim_{n\to\infty}\int_{\RR}f^n
=\alpha\lambda(X)+\beta\lambda(Y)+\gamma\lambda(Z)}.
$$


::: pf-proof

Take
$$
\beta=1,
\qquad
\gamma=0,
$$
and define
$$
\alpha=
\begin{cases}
0,&\lambda(X)=0,\\
\infty,&\lambda(X)>0.
\end{cases}
$$
If $\lambda(X)=0$, the right-hand side is $\lambda(Y)$; if $\lambda(X)>0$, it is $\infty$. Step [](#s1-5){.pf-ref} shows that these are exactly the two possible values of the limit.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref} give the requested dominated- and monotone-convergence contributions, and step [](#s1-6){.pf-ref} gives the required constants.

:::

:::

:::
