---
schema: qual/card@1
id: P-CAF11C
kind: problem
title: "Schwarz-Pick type inequality for analytic functions mapping into the left half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f \in H(\DD)$ be nonconstant such that $f(\DD) \subset \{z \in \CC : \operatorname{Re} z < 0\}$ and $f(0) = -1$.
Prove that for any $z \in \DD$, $$\frac{1 - \abs{z}}{1 + \abs{z}} \leq \abs{f(z)} \leq \frac{1 + \abs{z}}{1 - \abs{z}}.$$
:::

::: {.solution}
The Möbius map
$$
\Phi(w)=\frac{w+1}{w-1}
$$
maps the left half-plane conformally onto $\DD$ and sends $-1$ to $0$.
Thus
$$
g=\Phi\circ f:\DD\to\DD
$$
is holomorphic and satisfies $g(0)=0$. Schwarz's lemma gives
$$
\abs{g(z)}\le \abs{z}.
$$
Solving for $f$ yields
$$
f(z)=\frac{g(z)+1}{g(z)-1}.
$$
Therefore, writing $r=\abs{z}$,
$$
\abs{f(z)}=\frac{\abs{1+g(z)}}{\abs{1-g(z)}}
\le \frac{1+\abs{g(z)}}{1-\abs{g(z)}}
\le \frac{1+r}{1-r}.
$$
Likewise,
$$
\abs{f(z)}
\ge \frac{1-\abs{g(z)}}{1+\abs{g(z)}}
\ge \frac{1-r}{1+r}.
$$
This is the required pair of inequalities.
:::
