---
schema: qual/card@1
id: P-UCLARA14F-06
kind: problem
title: Separable dual implies separable Banach space
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Separability
  - Banach Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 6 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $X$ be a Banach space and $X^*$ its dual space. Suppose $X^*$ is separable (i.e. has a countable dense set); show that $X$ is separable. (You should assume the Axiom of Choice.)
:::

::: {.solution}

If $X=\{0\}$, then $X$ is trivially separable. Assume henceforth that
$X\ne\{0\}$.

::: pf

::: pf-step

Choose a countable dense set
$$
\{\varphi_1,\varphi_2,\ldots\}\subseteq X^*.
$$
For each $n$, choose $x_n\in X$ with
$$
\norm{x_n}=1
$$
and
$$
\boxed{
\abs{\varphi_n(x_n)}
\ge
\frac12\norm{\varphi_n}}.
$$


::: pf-proof

Separability of $X^*$ gives the countable dense family. By the definition of
the operator norm,
$$
\norm{\varphi_n}
=
\sup_{\norm{x}\le1}\abs{\varphi_n(x)}.
$$
If $\varphi_n\ne0$, there exists a unit vector $x_n$ satisfying the displayed
inequality. If $\varphi_n=0$, choose any unit vector. The Axiom of Choice
allows these choices to be made simultaneously.

:::

:::

::: {.pf-step #s1-2}

Let
$$
M
=
\overline{\operatorname{span}}\{x_1,x_2,\ldots\}.
$$
Then
$$
\boxed{M=X}.
$$


::: pf-proof

Suppose instead that $M\ne X$. Choose
$$
y\in X\setminus M.
$$
By the Hahn--Banach separation theorem, there exists
$$
\varphi\in X^*
$$
such that
$$
\varphi\restrict_M=0
\qquad\text{and}\qquad
\varphi(y)\ne0.
$$
In particular,
$$
\varphi\ne0.
$$

Since $\{\varphi_n\}$ is dense in $X^*$, choose a subsequence
$$
\varphi_{n_k}\to\varphi
$$
in operator norm. Because $x_{n_k}\in M$,
$$
\varphi(x_{n_k})=0.
$$
Hence
$$
\begin{aligned}
\frac12\norm{\varphi_{n_k}}
&\le
\abs{\varphi_{n_k}(x_{n_k})}\\
&=
\abs{(\varphi_{n_k}-\varphi)(x_{n_k})}\\
&\le
\norm{\varphi_{n_k}-\varphi}
\norm{x_{n_k}}\\
&=
\norm{\varphi_{n_k}-\varphi}.
\end{aligned}
$$
Therefore
$$
\norm{\varphi_{n_k}}\to0.
$$
But also
$$
\varphi_{n_k}\to\varphi
$$
in norm, so continuity of the norm gives
$$
\norm{\varphi}=0,
$$
contradicting $\varphi\ne0$. Thus $M=X$.

:::

:::

::: {.pf-step #s1-3}

The linear span of the countable set $\{x_n\}$ has a countable dense
subset.


::: pf-proof

If $X$ is a real Banach space, let
$$
D
=
\left\{
\sum_{j=1}^m q_jx_{n_j}
:
m\in\NN,\quad
q_j\in\QQ,\quad
n_j\in\NN
\right\}.
$$
This set is countable because it is a countable union of finite products of
countable sets.

Every finite real linear combination of the $x_n$ can be approximated
arbitrarily well by replacing its real coefficients by rational numbers, so
$D$ is dense in
$$
\operatorname{span}\{x_n\}.
$$

If $X$ is complex, use coefficients in
$$
\QQ+i\QQ
$$
instead; the same argument applies.

:::

:::

::: {.pf-step #s1-4}

The Banach space $X$ is separable.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\overline{\operatorname{span}}\{x_n\}=X.
$$
By step [](#s1-3){.pf-ref}, the span contains a countable dense subset $D$. Therefore
$$
\overline D=X,
$$
so $X$ is separable.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
