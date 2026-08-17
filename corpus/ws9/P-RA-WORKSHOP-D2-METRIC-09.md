---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-09
kind: problem
title: 'A compact set has positive distance from a disjoint closed set'
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - metric-spaces
relations: []
review: draft
---

::: {.problem title="?"}
(January 2011 #3a) Let $(X,d)$ be a metric space, $K\subset X$ be compact, and $F\subset X$ be closed.
If $K\cap F=\varnothing$, prove that there exists an $\epsilon>0$ so that $d(k,f)\ge\epsilon$ for all $k\in K$ and $f\in F$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. The function $x \mapsto d(x, F)$ is continuous.
    Proof: $|d(x,F) - d(x',F)| \le d(x,x')$ by the triangle inequality (for any $f \in F$, $d(x,f) \le d(x,x') + d(x',f)$, so $d(x,F) \le d(x,x') + d(x',F)$, and symmetrically), so it is 1-Lipschitz, hence continuous.
<1>2. $d(\cdot, F)$ attains its minimum on $K$.
    Proof: $K$ is compact and $x \mapsto d(x,F)$ is continuous (<1>1), so it attains a minimum at some $k_0 \in K$.
<1>3. The minimum is positive.
    Proof: suppose $d(k_0, F) = 0$. Then there is a sequence $(f_n)$ in $F$ with $d(k_0, f_n) \to 0$, i.e. $f_n \to k_0$. Since $F$ is closed, $k_0 \in F$, contradicting $K \cap F = \varnothing$. Hence $\epsilon := d(k_0, F) > 0$, and by minimality $d(k, F) \ge \epsilon$ for every $k \in K$, i.e. $d(k, f) \ge \epsilon$ for all $k \in K$, $f \in F$.
<1>4. Q.E.D.
:::
