---
schema: qual/card@1
id: P-LOXDS
kind: problem
title: Uncountable $E\subset[0,1]$ is uncountable on both sides of some $t$
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Show that if $E\subset [0, 1]$ is uncountable, then there is some $t\in \RR$ such that $E\intersect (-\infty ,t)$ and $E\intersect (t, \infty)$ are also uncountable.
:::

::: {.solution}
Let
$$
\begin{aligned}
S_- &\definedas \theset{ t\in \RR \st E \intersect (- \infty, t) \text{ is countable}}, \\
S_+ &\definedas \theset{ s\in \RR \st E \intersect (s, \infty) \text{ is countable}}.
\end{aligned}
$$

::: pf

::: {.pf-step #a-finite}
$a \definedas \sup S_-$ and $b \definedas \inf S_+$ are real numbers with $0\le a\le 1$ and $0\le b\le 1$.

::: pf-proof
Since $E\subset[0,1]$, every $t\le 0$ lies in $S_-$, and no $t>1$ does, because then $E\intersect(-\infty,t)=E$ is uncountable. The argument for $S_+$ is symmetric.
:::

:::

::: {.pf-step #a-countable}
$E\intersect(-\infty,a)$ and $E\intersect(b,\infty)$ are countable.

::: pf-proof
$S_-$ is downward closed: if $s\in S_-$ and $s'<s$, then $E\intersect(-\infty,s')\subseteq E\intersect(-\infty,s)$. So $a-1/n\in S_-$ for every $n\geq1$, and $E\intersect(-\infty,a)=\Union_{n\ge1}E\intersect(-\infty,a-1/n)$ is a countable union of countable sets. The argument for $b$ is symmetric.
:::

:::

::: {.pf-step #a-less-b}
$a<b$.

::: pf-proof
If $b\le a$, then every $x\in E$ satisfies $x<a$, $x=a$, or $x>a\ge b$, so $E\subseteq \bigl(E\intersect(-\infty,a)\bigr)\cup\theset{a}\cup\bigl(E\intersect(b,\infty)\bigr)$, which is countable by step [](#a-countable){.pf-ref}. This contradicts the uncountability of $E$.
:::

:::

::: pf-step
Every $t\in(a,b)$ has $E\intersect(-\infty,t)$ and $E\intersect(t,\infty)$ uncountable.

::: pf-proof
The interval is nonempty by step [](#a-less-b){.pf-ref}. Since $t>a=\sup S_-$, $t\notin S_-$; since $t<b=\inf S_+$, $t\notin S_+$.
:::

:::

:::
:::
