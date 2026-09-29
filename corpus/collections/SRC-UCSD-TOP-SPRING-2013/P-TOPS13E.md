---
schema: qual/card@1
id: P-TOPS13E
kind: problem
title: "No antipodal-preserving map from R^3 minus origin to R^2"
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Prove by contradiction that there does not exist a continuous map $f : \mathbb{R}^3 \setminus \{0\} \to \mathbb{R}^2$ with the property that $f(x) \neq f(-x)$ for all $x \in \mathbb{R}^3 \setminus \{0\}$.

Hint: Define $g : \mathbb{R}^3 \setminus \{0\} \to S^1$ by
$$
g(x) = \frac{f(x) - f(-x)}{|f(x) - f(-x)|},
$$
which satisfies $g(-x) = -g(x)$.
Define the loop $\eta : I \to \mathbb{R}^3 \setminus \{0\}$ by $\eta(s) = (\cos(2\pi s), \sin(2\pi s), 0)$ and consider the loop $h = g \circ \eta$ in $S^1$.
:::

::: {.solution}

::: pf

::: {.pf-step #assume-f-exists}
Suppose for contradiction that such an $f$ exists.

::: pf-proof
assume the contrary.
:::

:::

::: {.pf-step #define-g}
Define $g(x) = \frac{f(x) - f(-x)}{|f(x) - f(-x)|} \in S^1$, which is continuous and satisfies $g(-x) = -g(x)$.

::: pf-proof
$f(x) \neq f(-x)$ so the denominator is nonzero; and $g(-x) = \frac{f(-x) - f(x)}{|f(-x)-f(x)|} = -g(x)$.
:::

:::

::: {.pf-step #define-eta-and-h}
Let $\eta(s) = (\cos 2\pi s, \sin 2\pi s, 0)$ and $h = g \circ \eta: S^1 \to S^1$.

::: pf-proof
definition.
:::

:::

::: {.pf-step #h-nullhomotopic}
$h$ is nullhomotopic.

::: pf-proof
The loop $\eta$ contracts to the north pole inside $\RR^3\setminus\{0\}$ via
$$
H(s,t)=(1-t)\eta(s)+t(0,0,1).
$$
Indeed
$$
\|H(s,t)\|^2=(1-t)^2+t^2>0
$$
for every $t\in[0,1]$, so this homotopy never meets the origin. Therefore $\eta$ is nullhomotopic, and so is $h=g\circ\eta$.
:::

:::

::: {.pf-step #h-has-degree-zero}
Hence $h$ has degree $0$.

::: pf-proof
a nullhomotopic map $S^1 \to S^1$ has degree $0$.
:::

:::

::: {.pf-step #h-has-odd-degree}
But $h$ has odd degree.

::: pf-proof

::: pf-step
$h(s + 1/2) = g(\eta(s + 1/2)) = g(-\eta(s)) = -g(\eta(s)) = -h(s)$.

::: pf-proof
$\eta(s + 1/2) = -\eta(s)$ and $g(-x) = -g(x)$.
:::

:::

::: pf-step
A map $h:S^1\to S^1$ with $h(s+1/2)=-h(s)$ has odd degree.

::: pf-proof
Write $S^1=\RR/\ZZ$ and choose a lift $\widetilde h:\RR\to\RR$ of $h$. There is an integer $d=\deg h$ such that
$$
\widetilde h(s+1)=\widetilde h(s)+d.
$$
The equivariance relation implies
$$
\widetilde h(s+1/2)-\widetilde h(s)-1/2\in\ZZ.
$$
The left side is continuous in $s$ and integer-valued, hence is a constant integer $k$. Applying this relation twice gives
$$
\widetilde h(s+1)=\widetilde h(s)+1+2k.
$$
Thus $d=1+2k$ is odd.
:::

:::

:::

:::

::: {.pf-step #contradiction-step}
Contradiction.

::: pf-proof
Step [](#h-has-degree-zero){.pf-ref} says $\deg h = 0$ but step [](#h-has-odd-degree){.pf-ref} says $\deg h$ is odd.
:::

:::

::: {.pf-step #no-such-f-exists}
Hence no such $f$ exists.

::: pf-proof
Steps [](#assume-f-exists){.pf-ref}, [](#define-g){.pf-ref}, [](#define-eta-and-h){.pf-ref}, [](#h-nullhomotopic){.pf-ref}, [](#h-has-degree-zero){.pf-ref}, [](#h-has-odd-degree){.pf-ref} and [](#contradiction-step){.pf-ref}.
:::

:::

::: pf-qed
Step [](#no-such-f-exists){.pf-ref}.
:::

:::

:::
