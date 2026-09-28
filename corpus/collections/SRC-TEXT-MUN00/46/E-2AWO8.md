---
schema: qual/card@1
id: E-2AWO8
kind: problem
title: Uniform, compact-convergence, and pointwise topologies on $Y^X$
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Prove Theorem 46.7. Let $X$ be a space; let $(Y, d)$ be a metric space.
For the function space $Y^X$, one has the following inclusions of topologies:

$$
(\text{uniform}) \supset (\text{compact convergence}) \supset (\text{pointwise convergence}).
$$

If $X$ is compact, the first two coincide, and if $X$ is discrete, the second two coincide.
:::

::: {.solution}
For $f \in Y^X$, $\varepsilon \in (0, 1]$, and $C \subseteq X$, put
$$B_C(f, \varepsilon) = \{g \in Y^X : \sup_{x \in C} d(f(x), g(x)) < \varepsilon\}, \qquad B(f, \varepsilon) = \{g \in Y^X : \sup_{x \in X} \bar{d}(f(x), g(x)) < \varepsilon\},$$
where $\bar{d} = \min(d, 1)$. The sets $B_C(f, \varepsilon)$ with $C$ compact form a basis for the topology of compact convergence, the sets $B(f, \varepsilon)$ form a basis for the uniform topology, and the sets $B_{\{x\}}(f, \varepsilon)$ form a subbasis for the topology of pointwise convergence. If $g \in B_C(f, \varepsilon)$ and $r = \sup_{x \in C} d(f(x), g(x))$, then $B_C(g, \varepsilon - r) \subseteq B_C(f, \varepsilon)$ by the triangle inequality, and similarly for $B(f, \varepsilon)$. So to show that a set $B_C(f, \varepsilon)$ is open in a topology, it suffices to find, for every $f$ and $\varepsilon$, a neighborhood of $f$ in that topology inside $B_C(f, \varepsilon)$.

<1>1. (pointwise) $\subseteq$ (compact convergence).

::: {.proof}
For $x \in X$, the singleton $\{x\}$ is compact, so the subbasis element $B_{\{x\}}(f, \varepsilon)$ of the pointwise topology is a basis element of the topology of compact convergence.
:::

<1>2. (compact convergence) $\subseteq$ (uniform).

::: {.proof}
Let $C \subseteq X$ be compact and $\varepsilon \in (0, 1]$. If $g \in B(f, \varepsilon)$, then $\bar{d}(f(x), g(x)) < \varepsilon \le 1$ for all $x$, so $d(f(x), g(x)) = \bar{d}(f(x), g(x))$ and $\sup_{x \in C} d(f(x), g(x)) < \varepsilon$. Hence $B(f, \varepsilon) \subseteq B_C(f, \varepsilon)$.
:::

<1>3. If $X$ is compact, the uniform topology equals the topology of compact convergence.

::: {.proof}
Take $C = X$. For $\varepsilon \in (0, 1]$, the argument of step <1>2 shows $B_X(f, \varepsilon) = B(f, \varepsilon)$. So every uniform basis element is a basis element of the topology of compact convergence, and step <1>2 gives the reverse inclusion.
:::

<1>4. If $X$ is discrete, the topology of compact convergence equals the topology of pointwise convergence.

::: {.proof}
A compact subset $C$ of a discrete space is finite, say $C = \{x_1, \ldots, x_k\}$. Then
$$B_C(f, \varepsilon) = \bigcap_{i=1}^k B_{\{x_i\}}(f, \varepsilon)$$
is open in the topology of pointwise convergence. Step <1>1 gives the reverse inclusion.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the inclusions, and steps <1>3 and <1>4 the two coincidences.
:::
:::
