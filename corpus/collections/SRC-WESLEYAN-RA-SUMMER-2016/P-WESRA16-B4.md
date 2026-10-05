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
Let $f:\mathbb R\to[0,\infty)$ be measurable with $\operatorname{supp}f\subset[0,1]$.
Put
\[
X=\{x\in[0,1]:f(x)>1\},\qquad
Y=\{x\in[0,1]:f(x)=1\},\qquad
Z=\{x\in[0,1]:f(x)<1\}.
\]
Assuming
\[
\lim_{n\to\infty}\int_{\mathbb R}f^n
\]
exists in $[0,\infty]$, prove that there are $\alpha,\beta,\gamma\in[0,\infty]$ such that
\[
\lim_{n\to\infty}\int_{\mathbb R}f^n
=\alpha\lambda(X)+\beta\lambda(Y)+\gamma\lambda(Z).
\]
Determine the relevant contributions using monotone and dominated convergence.
:::

::: {.solution}
Because $\operatorname{supp}f\subseteq[0,1]$ and $X,Y,Z$ partition $[0,1]$,
$$
\int_{\mathbb R}f^n
=\int_Xf^n+\int_Yf^n+\int_Zf^n.
$$

<1>1. On $Y$,
$$
\int_Y f^n=\lambda(Y)
$$
for every $n$.

::: {.proof}
By definition, $f(x)=1$ for every $x\in Y$. Hence $f^n=1$ on $Y$, so
$$
\int_Yf^n=\int_Y1=\lambda(Y).
$$
:::

<1>2. On $Z$,
$$
\lim_{n\to\infty}\int_Zf^n=0.
$$

::: {.proof}
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

<1>3. On $X$, the functions $f^n\mathbf1_X$ increase pointwise to the extended-valued function
$$
h(x)=
\begin{cases}
\infty,&x\in X,\\
0,&x\notin X.
\end{cases}
$$

::: {.proof}
If $x\in X$, then $f(x)>1$, so the sequence $f(x)^n$ is increasing and tends to $\infty$. If $x\notin X$, multiplication by $\mathbf1_X(x)$ makes every term zero. This proves the asserted monotone pointwise convergence.
:::

<1>4. One has
$$
\lim_{n\to\infty}\int_Xf^n
=
\begin{cases}
0,&\lambda(X)=0,\\
\infty,&\lambda(X)>0.
\end{cases}
$$

::: {.proof}
By step <1>3 and the Monotone Convergence Theorem,
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

<1>5. Therefore
$$
\lim_{n\to\infty}\int_{\mathbb R}f^n
=
\begin{cases}
\lambda(Y),&\lambda(X)=0,\\
\infty,&\lambda(X)>0.
\end{cases}
$$

::: {.proof}
Use the decomposition before step <1>1. The $Y$-term equals $\lambda(Y)$ by step <1>1, the $Z$-term tends to $0$ by step <1>2, and the $X$-term has the limit computed in step <1>4. Adding these three limits gives the displayed formula.
:::

<1>6. There exist $\alpha,\beta,\gamma\in[0,\infty]$ such that
$$
\boxed{\lim_{n\to\infty}\int_{\mathbb R}f^n
=\alpha\lambda(X)+\beta\lambda(Y)+\gamma\lambda(Z)}.
$$

::: {.proof}
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
If $\lambda(X)=0$, the right-hand side is $\lambda(Y)$; if $\lambda(X)>0$, it is $\infty$. Step <1>5 shows that these are exactly the two possible values of the limit.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>2 and <1>4 give the requested dominated- and monotone-convergence contributions, and step <1>6 gives the required constants.
:::
:::
