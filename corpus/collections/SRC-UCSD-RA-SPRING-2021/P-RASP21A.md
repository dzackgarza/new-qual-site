---
schema: qual/card@1
id: P-RASP21A
kind: problem
title: "Sumset of measurable set with null set"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2021 real-analysis qualifying exam. The card had transposed the hypothesis and conclusion; the official statement assumes A+B is contained in the irrationals and asks to prove that one set is null.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $A, B \subseteq \RR$ be Lebesgue measurable and suppose
$$
\{a+b:a\in A,\ b\in B\}\subseteq\RR\setminus\QQ.
$$
Prove that either $m(A)=0$ or $m(B)=0$.
:::


::: {.solution}

The argument is the card's own: the convolution of the two indicator functions is continuous and not identically zero, so the sumset contains an interval, and every interval contains a rational. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $A,B\subseteq\RR$ be Lebesgue measurable with $\{a+b:a\in A,\ b\in B\}\subseteq\RR\setminus\QQ$.

::: pf

::: {.pf-step #bounded}
If $m(A)>0$ and $m(B)>0$ there are bounded measurable $A_{0}\subseteq A$ and $B_{0}\subseteq B$ with $0<m(A_{0})<\infty$ and $0<m(B_{0})<\infty$.

::: pf-proof
$A=\bigcup_{n}(A\cap[-n,n])$ is an increasing union, so $m(A)=\lim_{n}m(A\cap[-n,n])$; since $m(A)>0$ some $m(A\cap[-n,n])>0$, and that set is bounded with finite measure. The same for $B$.
:::

:::

::: {.pf-step #convolution}
$h(t)=m\big(A_{0}\cap(t-B_{0})\big)$ is continuous, nonnegative, and $\int_{\RR}h=m(A_{0})m(B_{0})>0$.

::: pf-proof
For $t\in\RR$,
$$
h(t)=\int_{\RR}\mathbf 1_{A_{0}}(x)\,\mathbf 1_{t-B_{0}}(x)\,dx=\int_{\RR}\mathbf 1_{A_{0}}(x)\,\mathbf 1_{B_{0}}(t-x)\,dx,
$$
which is the convolution $\mathbf 1_{A_{0}}*\mathbf 1_{B_{0}}$ at $t$. Both factors lie in $L^{1}(\RR)$, being indicators of measurable sets of finite measure, and the convolution of two $L^{1}$ functions is continuous — indeed $\abs{h(t+h)-h(t)}\le\norm{\mathbf 1_{A_{0}}}_{1}\norm{\mathbf 1_{B_{0}}(\cdot-h)-\mathbf 1_{B_{0}}}_{1}$, which tends to $0$ by continuity of translation in $L^{1}$. The function $h$ is nonnegative because the integrand is. Finally, by Tonelli,
$$
\int_{\RR}h(t)\,dt=\int_{\RR}\int_{\RR}\mathbf 1_{A_{0}}(x)\mathbf 1_{B_{0}}(t-x)\,dx\,dt=\int_{\RR}\mathbf 1_{A_{0}}(x)\Big(\int_{\RR}\mathbf 1_{B_{0}}(t-x)\,dt\Big)dx=m(A_{0})m(B_{0}),
$$
which is positive.
:::

:::

::: {.pf-step #positive-interval}
There is a nonempty open interval $I$ with $h(t)>0$ for $t\in I$.

::: pf-proof
Since $h\ge0$ and $\int h>0$, the set $\{t:h(t)>0\}$ is nonempty, so pick $t_{0}$ with $h(t_{0})>0$. By continuity of $h$ at $t_{0}$ and $h(t_{0})/2>0$ there is $\delta>0$ with $h(t)>h(t_{0})/2>0$ for $\abs{t-t_{0}}<\delta$; take $I=(t_{0}-\delta,t_{0}+\delta)$.
:::

:::

::: {.pf-step #contradiction}
$I\subseteq A+B$, hence $A+B$ meets $\QQ$, contradicting the hypothesis.

::: pf-proof
Let $t\in I$. Since $h(t)=m\big(A_{0}\cap(t-B_{0})\big)>0$, that intersection is nonempty, so there are $a\in A_{0}$ and $b\in B_{0}$ with $a=t-b$, that is $t=a+b\in A_{0}+B_{0}\subseteq A+B$. Hence $I\subseteq A+B\subseteq\RR\setminus\QQ$. But $I$ is a nonempty open interval, and the rationals are dense, so $I\cap\QQ\ne\varnothing$, giving a rational in $A+B$. That contradicts the hypothesis, so $m(A)>0$ and $m(B)>0$ cannot both hold: at least one of $A$, $B$ has measure zero.
:::

:::

:::
:::
