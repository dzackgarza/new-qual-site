---
schema: qual/card@1
id: E-CQHYY
kind: exercise
title: Bounded functions under uniform and compact convergence topologies
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that the set $\mathcal{B}(\mathbb{R}, \mathbb{R})$ of bounded functions $f: \mathbb{R} \to \mathbb{R}$ is closed in $\mathbb{R}^{\mathbb{R}}$ in the uniform topology, but not in the topology of compact convergence.
:::

::: {.solution}
**Goal.** Show $\mathcal B(\RR,\RR)$ is closed in the uniform topology but not in the compact-convergence topology.

<1>1. $\mathcal B(\RR,\RR)$ is closed in the uniform topology.
<2>1. Let $f_n \in \mathcal B(\RR,\RR)$ converge uniformly to $f$.
::: {.proof}
take a sequence of bounded functions converging uniformly.
:::
<2>2. Each $f_n$ is bounded by some $M_n$.
::: {.proof}
definition of bounded.
:::
<2>3. Uniform convergence gives $N$ with $\sup_x |f_N(x) - f(x)| < 1$.
::: {.proof}
definition of uniform convergence.
:::
<2>4. Hence $|f(x)| \le |f_N(x)| + 1 \le M_N + 1$ for all $x$, so $f$ is bounded.
::: {.proof}
triangle inequality.
:::
<2>5. Hence $f \in \mathcal B(\RR,\RR)$, so $\mathcal B$ is closed.
::: {.proof}
the uniform limit of bounded functions is bounded.
:::

<1>2. $\mathcal B(\RR,\RR)$ is not closed in the compact-convergence topology.
<2>1. Take $f_n(x) = x$ for $|x| \le n$ and $f_n(x) = 0$ otherwise (or simply $f_n(x) = \min(|x|, n)$).
::: {.proof}
define a sequence of bounded functions.
:::
<2>2. Each $f_n$ is bounded.
::: {.proof}
$|f_n(x)| \le n$ for all $x$.
:::
<2>3. $f_n \to f$ in the compact-convergence topology, where $f(x) = x$ (unbounded).
::: {.proof}
on any compact set $K$, for $n \ge \sup_{x \in K} |x|$, we have $f_n(x) = x = f(x)$ on $K$, so $f_n \to f$ uniformly on every compact set.
:::
<2>4. $f \notin \mathcal B(\RR,\RR)$ (it is unbounded).
::: {.proof}
$f(x) = x$ is unbounded.
:::
<2>5. Hence $\mathcal B$ is not closed in the compact-convergence topology.
::: {.proof}
there is a sequence in $\mathcal B$ converging (in compact convergence) to a function outside $\mathcal B$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2 prove the two claims.
:::
:::
