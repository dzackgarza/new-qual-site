---
schema: qual/card@1
id: P-XGHXK
kind: problem
title: A non-surjective map into $S^n$ is nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f: X \to S^n$ be a continuous map that is not surjective.
Prove that $f$ is nullhomotopic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Since $f$ is not surjective, there exists a point $p \in S^n \setminus f(X)$.

::: pf-proof
definition of non-surjectivity.
:::

:::

::: pf-step
Let $s_0 = -p \in S^n$ be the antipodal point to $p$.

::: pf-proof
definition of antipodal point on $S^n$.
:::

:::

::: {.pf-step #s3}
For all $x \in X$ and all $t \in [0, 1]$, $(1 - t)f(x) + t s_0 \neq 0$ in $\mathbb{R}^{n+1}$.

::: pf-proof

::: pf-step
Suppose $(1 - t)f(x) + t s_0 = 0$ for some $t \in [0, 1]$ and $x \in X$.

::: pf-proof
hypothesis for contradiction.
:::

:::

::: {.pf-step #s3-2}
If $t = 0$, then $f(x) = 0$, impossible since $f(x) \in S^n \implies \|f(x)\| = 1$.

::: pf-proof
norm on $S^n$.
:::

:::

::: {.pf-step #s3-3}
If $t = 1$, then $s_0 = 0$, impossible since $\|s_0\| = 1$.

::: pf-proof
norm on $S^n$.
:::

:::

::: pf-step
For $0 < t < 1$, $(1 - t)f(x) = -t s_0$.
Taking norms gives $(1 - t) = t \implies t = 1/2$.

::: pf-proof
$\|f(x)\| = \|s_0\| = 1$.
:::

:::

::: pf-step
Then $f(x) = -s_0 = -(-p) = p$.

::: pf-proof
$(1-t)f(x) = -t s_0$ with $t = 1/2$.
:::

:::

::: {.pf-step #s3-6}
But $p \notin f(X)$, so $f(x) \neq p$, a contradiction.

::: pf-proof
step [](#s1){.pf-ref}.
:::

:::

::: pf-step
Thus $(1 - t)f(x) + t s_0 \neq 0$ for all $x \in X, t \in [0, 1]$.

::: pf-proof
step [](#s3-2){.pf-ref}, step [](#s3-3){.pf-ref}, and step [](#s3-6){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s4}
Define $H: X \times [0, 1] \to S^n$ by
\[
H(x, t) = \frac{(1 - t)f(x) + t s_0}{\|(1 - t)f(x) + t s_0\|}.
\]

::: pf-proof

::: {.pf-step #s4-1}
$H$ is well-defined because the denominator is non-zero by step [](#s3){.pf-ref}.

::: pf-proof
step [](#s3){.pf-ref}.
:::

:::

::: {.pf-step #s4-2}
$H$ is continuous as a composition of continuous functions (vector addition, scalar multiplication, norm, and quotient).

::: pf-proof
continuity of linear operations and norm on $\mathbb{R}^{n+1} \setminus \{0\}$.
:::

:::

::: {.pf-step #s4-3}
For $t = 0$: $H(x, 0) = \frac{f(x)}{\|f(x)\|} = f(x)$ since $\|f(x)\| = 1$.

::: pf-proof
$f(x) \in S^n$.
:::

:::

::: {.pf-step #s4-4}
For $t = 1$: $H(x, 1) = \frac{s_0}{\|s_0\|} = s_0$ since $\|s_0\| = 1$.

::: pf-proof
$s_0 \in S^n$.
:::

:::

::: pf-step
Hence $H$ is a homotopy between $f$ and the constant map $x \mapsto s_0$.

::: pf-proof
steps [](#s4-1){.pf-ref} through [](#s4-4){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s5}
Therefore $f$ is nullhomotopic.

::: pf-proof
step [](#s4){.pf-ref}.
:::

:::

::: pf-qed
step [](#s5){.pf-ref}.
:::

:::

:::
