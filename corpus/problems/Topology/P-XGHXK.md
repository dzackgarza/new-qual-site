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

::: problem
Let $f: X \to S^n$ be a continuous map that is not surjective.
Prove that $f$ is nullhomotopic.
:::

::: {.solution}
<1>1. Since $f$ is not surjective, there exists a point $p \in S^n \setminus f(X)$.
Proof: definition of non-surjectivity.

<1>2. Let $s_0 = -p \in S^n$ be the antipodal point to $p$.
Proof: definition of antipodal point on $S^n$.

<1>3. For all $x \in X$ and all $t \in [0, 1]$, $(1 - t)f(x) + t s_0 \neq 0$ in $\mathbb{R}^{n+1}$.
<2>1. Suppose $(1 - t)f(x) + t s_0 = 0$ for some $t \in [0, 1]$ and $x \in X$.
Proof: hypothesis for contradiction.
<2>2. If $t = 0$, then $f(x) = 0$, impossible since $f(x) \in S^n \implies \|f(x)\| = 1$.
Proof: norm on $S^n$.
<2>3. If $t = 1$, then $s_0 = 0$, impossible since $\|s_0\| = 1$.
Proof: norm on $S^n$.
<2>4. For $0 < t < 1$, $(1 - t)f(x) = -t s_0$.
Taking norms gives $(1 - t) = t \implies t = 1/2$.
Proof: $\|f(x)\| = \|s_0\| = 1$.
<2>5. Then $f(x) = -s_0 = -(-p) = p$.
Proof: $(1-t)f(x) = -t s_0$ with $t = 1/2$.
<2>6. But $p \notin f(X)$, so $f(x) \neq p$, a contradiction.
Proof: <1>1. <2>7. Thus $(1 - t)f(x) + t s_0 \neq 0$ for all $x \in X, t \in [0, 1]$.
Proof: <2>2, <2>3, and <2>6.

<1>4. Define $H: X \times [0, 1] \to S^n$ by
\[
H(x, t) = \frac{(1 - t)f(x) + t s_0}{\|(1 - t)f(x) + t s_0\|}.
\]
<2>1. $H$ is well-defined because the denominator is non-zero by <1>3. Proof: <1>3. <2>2. $H$ is continuous as a composition of continuous functions (vector addition, scalar multiplication, norm, and quotient).
Proof: continuity of linear operations and norm on $\mathbb{R}^{n+1} \setminus \{0\}$.
<2>3. For $t = 0$: $H(x, 0) = \frac{f(x)}{\|f(x)\|} = f(x)$ since $\|f(x)\| = 1$.
Proof: $f(x) \in S^n$.
<2>4. For $t = 1$: $H(x, 1) = \frac{s_0}{\|s_0\|} = s_0$ since $\|s_0\| = 1$.
Proof: $s_0 \in S^n$.
<2>5. Hence $H$ is a homotopy between $f$ and the constant map $x \mapsto s_0$.
Proof: <2>1–<2>4.

<1>5. Therefore $f$ is nullhomotopic.
Proof: <1>4.

<1>6. Q.E.D. Proof: <1>5.
:::
