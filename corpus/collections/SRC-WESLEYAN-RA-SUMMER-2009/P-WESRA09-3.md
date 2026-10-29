---
schema: qual/card@1
id: P-WESRA09-3
kind: problem
title: 'Four measure and Banach-space problems'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Solve the following.

(a) If $(\Omega,\mathcal A,\mu)$ is a measure space with $\mu(\Omega)<\infty$ and $A_n\in\mathcal A$, prove
$$
\limsup_{n\to\infty}\mu(A_n)\le \mu(\limsup_{n\to\infty}A_n).
$$

(b) A content on a ring is subadditive.
Assuming this, prove that a premeasure is $\sigma$-subadditive.

(c) Prove that the inverse of a bijective linear map $f:X\to Y$ is linear.
If $X,Y$ are normed and $f$ is continuous, state when a course theorem implies that $f^{-1}$ is continuous, and explain why.

(d) In $C([-1,2],\RR)$ with the uniform norm, determine the uniform closure of
$$
\left\{x\mapsto\sum_{n=0}^N a_nx^{3n+1}:N\ge0,\ a_n\in\RR\right\}.
$$
:::

::: {.solution}

For part (d), write
$$
\mathcal S
=\left\{x\mapsto\sum_{n=0}^N a_nx^{3n+1}:N\ge0,\ a_n\in\RR\right\}
\subset C([-1,2],\RR).
$$

::: pf

::: {.pf-step #s1-1}

In part (a),
$$
\limsup_{n\to\infty}\mu(A_n)
\le \mu\!\left(\limsup_{n\to\infty}A_n\right).
$$


::: pf-proof

For $m\ge1$, set
$$
B_m=\bigcup_{n\ge m}A_n.
$$
Then $(B_m)$ is decreasing,
$$
\bigcap_{m=1}^\infty B_m=\limsup_{n\to\infty}A_n,
$$
and $\mu(B_1)\le\mu(\Omega)<\infty$. Continuity from above therefore gives
$$
\mu(B_m)\longrightarrow
\mu\!\left(\limsup_{n\to\infty}A_n\right).
$$
For every $n\ge m$, $A_n\subseteq B_m$, so
$$
\sup_{n\ge m}\mu(A_n)\le\mu(B_m).
$$
Letting $m\to\infty$ proves the desired inequality.

:::

:::

::: pf-step

In part (b), every premeasure $\mu$ on a ring $\mathcal R$ is $\sigma$-subadditive: if $A_n\in\mathcal R$ and $A=\bigcup_{n=1}^\infty A_n\in\mathcal R$, then
$$
\boxed{\mu(A)\le\sum_{n=1}^\infty\mu(A_n)}.
$$


::: pf-proof

Define
$$
C_1=A_1,
\qquad
C_n=A_n\setminus\bigcup_{k<n}A_k\quad(n\ge2).
$$
Because $\mathcal R$ is a ring, every $C_n$ lies in $\mathcal R$. The sets $C_n$ are pairwise disjoint, $C_n\subseteq A_n$, and $\bigcup_n C_n=A$. Hence countable additivity of the premeasure and monotonicity give
$$
\mu(A)=\sum_{n=1}^\infty\mu(C_n)
\le\sum_{n=1}^\infty\mu(A_n).
$$

:::

:::

::: pf-step

In part (c), if $f:X\to Y$ is a bijective linear map, then $\boxed{f^{-1}:Y\to X\text{ is linear}}$.


::: pf-proof

Let $y_1=f(x_1)$ and $y_2=f(x_2)$, and let $a,b$ be scalars. By linearity and bijectivity of $f$,
$$
\begin{aligned}
f^{-1}(ay_1+by_2)
&=f^{-1}\!\bigl(af(x_1)+bf(x_2)\bigr)\\
&=f^{-1}\!\bigl(f(ax_1+bx_2)\bigr)\\
&=ax_1+bx_2\\
&=af^{-1}(y_1)+bf^{-1}(y_2).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

If, in addition, $X$ and $Y$ are Banach spaces and $f$ is continuous, then $\boxed{f^{-1}\text{ is continuous}}$.


::: pf-proof

The map $f$ is a continuous linear bijection between Banach spaces. The [[T-FO27T|bounded inverse theorem]] therefore gives continuity of $f^{-1}$.

:::

:::

::: {.pf-step #s1-5}

Every function in the uniform closure $\overline{\mathcal S}^{\|\cdot\|_\infty}$ vanishes at $0$.


::: pf-proof

Every $s\in\mathcal S$ satisfies $s(0)=0$. Evaluation at $0$ is continuous in the uniform norm, since
$$
|u(0)-v(0)|\le\|u-v\|_\infty.
$$
Therefore every uniform limit of functions in $\mathcal S$ also vanishes at $0$.

:::

:::

::: {.pf-step #s1-6}

Every $g\in C([-1,2],\RR)$ with $g(0)=0$ belongs to $\overline{\mathcal S}^{\|\cdot\|_\infty}$.


::: pf-proof

Fix $\varepsilon>0$. By the [[T-3QNBQ|Weierstrass approximation theorem]], choose a real polynomial $p$ such that
$$
\|g-p\|_\infty<\frac{\varepsilon}{4}.
$$
Since $g(0)=0$, one has $|p(0)|<\varepsilon/4$. Thus
$$
r(x)=p(x)-p(0)
$$
satisfies $r(0)=0$ and
$$
\|g-r\|_\infty<\frac{\varepsilon}{2}.
$$
Write $r(x)=xh(x)$ for a real polynomial $h$. The function
$$
H(t)=h(t^{1/3}),\qquad -1\le t\le8,
$$
is continuous. Applying Weierstrass again, choose a real polynomial $q$ such that
$$
\sup_{-1\le t\le8}|H(t)-q(t)|<\frac{\varepsilon}{4}.
$$
Then $xq(x^3)\in\mathcal S$, and for $x\in[-1,2]$,
$$
\begin{aligned}
|r(x)-xq(x^3)|
&=|x|\,|h(x)-q(x^3)|\\
&=|x|\,|H(x^3)-q(x^3)|\\
&<2\cdot\frac{\varepsilon}{4}
=\frac{\varepsilon}{2}.
\end{aligned}
$$
Hence
$$
\|g-xq(x^3)\|_\infty<\varepsilon.
$$
Since $\varepsilon$ was arbitrary, $g\in\overline{\mathcal S}^{\|\cdot\|_\infty}$.

:::

:::

::: {.pf-step #s1-7}

The answer to part (d) is
$$
\boxed{
\overline{\mathcal S}^{\|\cdot\|_\infty}
=\{g\in C([-1,2],\RR):g(0)=0\}}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives one inclusion and step [](#s1-6){.pf-ref} gives the reverse inclusion.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} solve parts (a)--(c), and step [](#s1-7){.pf-ref} gives the uniform closure requested in part (d).

:::

:::

:::
