---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W2
kind: problem
title: Absolute-value Stieltjes integrability without function integrability
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
([Apo74, 7.12] c.f. [Rud76, p. 138 #3]) Give an example of a bounded function $f$ and an increasing function $\alpha$ defined on $[a,b]$ such that $\abs{f}\in\mathcal R(\alpha)$ but $f\notin\mathcal R(\alpha)$.
:::

::: {.solution}

On $[a,b]=[0,1]$ take $\alpha(x)=x$, which is increasing, and
$$
f(x)=\begin{cases}1, & x\in\QQ,\\ -1, & x\notin\QQ.\end{cases}
$$

::: pf

::: {.pf-step #abs-integrable}

$\abs{f}\in\mathcal R(\alpha)$.

::: pf-proof

$\abs{f}\equiv 1$ on $[0,1]$. A constant function is Riemann integrable, with $\int_0^1 \abs{f}\,dx=1$.

:::

:::

::: pf-step

$f\notin\mathcal R(\alpha)$, so $\boxed{f=\mathbf 1_{\QQ}-\mathbf 1_{\RR\setminus\QQ},\ \alpha(x)=x \text{ on } [0,1]}$ is the required example.

::: pf-proof

Every subinterval $[x_{i-1},x_i]$ of positive length contains both rationals and irrationals, because both sets are dense in $\RR$. So $\inf f=-1$ and $\sup f=1$ on every subinterval. For every partition $P$ we get $L(f,P)=-1$ and $U(f,P)=1$, so $U(f,P)-L(f,P)=2$. The Riemann criterion fails, and $f\notin\mathcal R(\alpha)$. The function $f$ is bounded by $1$, so with step [](#abs-integrable){.pf-ref} it has all the required properties.

:::

:::

:::

:::
