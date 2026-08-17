---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-10
kind: problem
title: 'Every positive metric sphere in an unbounded connected metric space is nonempty'
classification:
  areas:
  - real-analysis
  topics:
  - metric-spaces
  - connectedness
relations: []
review: draft
---

::: {.problem title="?"}
Let $(X,d)$ be an unbounded and connected metric space.
Prove that for each $x_0\in X$, the set $$\{x\in X:d(x,x_0)=r\}$$ is nonempty.
:::

::: remark
The source statement does not explicitly quantify or restrict $r$; the displayed wording is preserved verbatim.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. The map $f(x) = d(x, x_0)$ is continuous and its image is an interval containing $0$.
    Proof: $f$ is 1-Lipschitz (reverse triangle inequality), hence continuous; $f(x_0) = 0 \in f(X)$; and $f(X) \subseteq [0,\infty)$. Since $X$ is connected and $f$ is continuous, $f(X)$ is connected; the connected subsets of $[0,\infty)$ are intervals, so $f(X)$ is an interval containing $0$.
<1>2. $f(X)$ is unbounded above.
    Proof: if $f(X)$ were bounded above by $R$, then $d(x,x_0) \le R$ for all $x$, contradicting that $X$ is unbounded. Hence $\sup f(X) = \infty$.
<1>3. Every $r \ge 0$ is attained.
    Proof: $f(X)$ is an interval containing $0$ and unbounded above, hence $[0,\infty) \subseteq f(X)$: for every $r \ge 0$ there is $x \in X$ with $d(x,x_0) = r$. In particular the sphere $\{x : d(x,x_0) = r\}$ is nonempty for every $r \ge 0$ (in particular every $r > 0$).
<1>4. Q.E.D.
:::
