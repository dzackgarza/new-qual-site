---
schema: qual/card@1
id: FR-GG457
kind: proof
title: Almost everywhere convergence implies convergence in measure on a set of finite measure
classification:
  areas:
  - real-analysis
  topics:
  - Egorov
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $m$ be Lebesgue measure on $\RR^d$, let $E \subseteq \RR^d$ be [[D-MDJII|Lebesgue measurable]] with $m(E) < \infty$, and let $f_k\colon E\to\RR$ for $k\geq1$ and $f\colon E\to\RR$ be [[D-DHFN4|measurable]].
If $f_k \to f$ almost everywhere on $E$, then $f_k\to f$ [[FD-D7HOH|in measure]] on $E$.
:::

::: {.proof}
Fix $\varepsilon > 0$ and $\delta > 0$.
For each $N\geq1$, define the measurable set
$$
E_N \coloneqq \theset{x \in E \suchthat \abs{f_k(x) - f(x)} < \varepsilon \text{ for all } k \ge N}.
$$
The sets $E_N$ increase with $N$, and every $x\in E$ at which $f_k(x) \to f(x)$ lies in some $E_N$, so $E\setminus\bigcup_N E_N$ is a null set.
By continuity of measure from below, $m(E_N)\to m\qty{\bigcup_N E_N} = m(E)$; since $m(E)<\infty$, it follows that $m(E \setminus E_N) = m(E)-m(E_N) \to 0$ as $N \to \infty$.
Choose $N$ with $m(E \setminus E_N) < \delta$.
For every $k \ge N$ and every $x \in E_N$ we have $\abs{f_k(x) - f(x)} < \varepsilon$, so
$$
m\qty{\theset{x \in E \suchthat \abs{f_k(x) - f(x)} \ge \varepsilon}} \le m(E \setminus E_N) < \delta
$$
for all $k \ge N$.
Since $\delta>0$ was arbitrary, $m\qty{\theset{x \in E \suchthat \abs{f_k(x) - f(x)} > \varepsilon}}\to0$ as $k\to\infty$ for every $\varepsilon>0$, which is convergence in measure.
:::
