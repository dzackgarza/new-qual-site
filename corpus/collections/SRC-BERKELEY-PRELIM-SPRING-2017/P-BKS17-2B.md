---
schema: qual/card@1
id: P-BKS17-2B
kind: problem
title: A continuous function with vanishing moments on $[-1,1]$ is zero
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 13 problem 2B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 solutions. The first printed method approximates $f$ and concludes from an integral of $f^2$, which is not valid for a complex-valued function; the solution below instead approximates $\overline f$ and obtains an integral of $\abs{f}^2$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified extension from monomials to complex polynomials, complex Weierstrass approximation of $\overline f$, the $L^2$ estimate, and the continuity argument.
---

::: {.problem}
Suppose $f : [-1, 1] \to \CC$ is a continuous complex-valued function, and for all non-negative integers $n$

$$
\int_{-1}^{1} x^n f(x) \, dx = 0.
$$

Prove that $f = 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every complex polynomial $P$,
$$
\int_{-1}^1 f(x)P(x)\,dx=0.
$$


::: pf-proof

Write
$$
P(x)=\sum_{j=0}^m a_jx^j
$$
with $a_j\in\CC$. By linearity of the integral and the assumed vanishing of every moment,
$$
\int_{-1}^1 f(x)P(x)\,dx
=
\sum_{j=0}^m a_j\int_{-1}^1 x^jf(x)\,dx
=0.
$$

:::

:::

::: {.pf-step #s1-2}

For every $\varepsilon>0$, there is a complex polynomial $P$ such that
$$
\sup_{x\in[-1,1]}\abs{\overline{f(x)}-P(x)}<\varepsilon.
$$


::: pf-proof

Write $f=u+iv$ with real-valued continuous functions $u,v$. By the Weierstrass approximation theorem, there are real polynomials $A$ and $B$ satisfying
$$
\norm{u-A}_\infty<\frac{\varepsilon}{2},
\qquad
\norm{v-B}_\infty<\frac{\varepsilon}{2}.
$$
For $P\coloneqq A-iB$,
$$
\abs{\overline f-P}
=
\abs{(u-A)-i(v-B)}
\leq
\abs{u-A}+\abs{v-B}
<\varepsilon
$$
uniformly on $[-1,1]$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_{-1}^1\abs{f(x)}^2\,dx=0.
$$


::: pf-proof

Let $\varepsilon>0$ and choose $P$ as in step [](#s1-2){.pf-ref}. By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\int_{-1}^1\abs{f(x)}^2\,dx
&=\int_{-1}^1 f(x)\overline{f(x)}\,dx\\
&=\int_{-1}^1 f(x)(\overline{f(x)}-P(x))\,dx.
\end{aligned}
$$
Hence
$$
0\leq
\int_{-1}^1\abs{f(x)}^2\,dx
\leq
\varepsilon\int_{-1}^1\abs{f(x)}\,dx.
$$
The last integral is finite because $f$ is continuous on the compact interval $[-1,1]$. Since the inequality holds for every $\varepsilon>0$, the integral of $\abs{f}^2$ must be zero.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{f=0}.
$$


::: pf-proof

The function $\abs{f}^2$ is continuous and nonnegative. If $f(x_0)\neq0$ at some $x_0\in[-1,1]$, continuity would give a nontrivial interval relative to $[-1,1]$ on which $\abs{f}^2$ is bounded below by a positive constant. Its integral would then be positive, contradicting step [](#s1-3){.pf-ref}. Thus $f(x)=0$ for every $x\in[-1,1]$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the assertion.

:::

:::

:::
