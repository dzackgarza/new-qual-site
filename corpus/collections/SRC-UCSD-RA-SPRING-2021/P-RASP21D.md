---
schema: qual/card@1
id: P-RASP21D
kind: problem
title: "Boundedness of bilinear maps via weak sequential continuity"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $X, Y, Z$ be Banach spaces and $B : X \times Y \to Z$ be a map such that for any fixed $x \in X$, $B(x, \cdot) \in L(Y, Z)$ and for any fixed $y \in Y$, $B(\cdot, y) \in L(X, Z)$.
Show that there is $C$ such that $\|B(x,y)\| \leq C\|x\|\|y\|$.
:::

::: {.solution}
<1>1. Define a family of linear operators from $Y$ to $Z$: <2>1. For each $x \in X$ with $\|x\| \le 1$, define $T_x: Y \to Z$ by $T_x(y) = B(x, y)$.
::: {.proof}
definition.
:::
<2>2. By hypothesis, for each fixed $x \in X$, $B(x, \cdot) \in L(Y, Z)$, so $T_x$ is a bounded linear operator from the Banach space $Y$ to the Banach space $Z$.
::: {.proof}
hypothesis.
:::
<2>3. Consider the family of operators $\mathcal{F} = \{T_x : x \in X, \|x\| \le 1\} \subset L(Y, Z)$.
::: {.proof}
definition of $\mathcal{F}$.
:::

<1>2. Show that the family $\mathcal{F}$ is pointwise bounded on $Y$: <2>1. Fix an arbitrary $y \in Y$.
::: {.proof}
setup.
:::
<2>2. Define the linear operator $S_y: X \to Z$ by $S_y(x) = B(x, y)$.
::: {.proof}
definition.
:::
<2>3. By hypothesis, $B(\cdot, y) \in L(X, Z)$, so $S_y$ is a bounded linear operator with operator norm $\|S_y\| < \infty$.
::: {.proof}
hypothesis.
:::
<2>4. For any $x \in X$ with $\|x\| \le 1$:
\[
\|T_x(y)\| = \|B(x, y)\| = \|S_y(x)\| \le \|S_y\| \|x\| \le \|S_y\|.
\]
::: {.proof}
definition of operator norm for $S_y$.
:::
<2>5. Taking the supremum over all $T_x \in \mathcal{F}$:
\[
\sup_{T_x \in \mathcal{F}} \|T_x(y)\| = \sup_{\|x\| \le 1} \|B(x, y)\| \le \|S_y\| < \infty.
\]
::: {.proof}
<2>4.
:::

<1>3. Apply the Uniform Boundedness Principle (Banach–Steinhaus Theorem): <2>1. $Y$ is a Banach space, $Z$ is a normed space, and $\mathcal{F} \subset L(Y, Z)$ is a pointwise bounded family of bounded linear operators.
::: {.proof}
hypothesis and <1>2. <2>2. By the Uniform Boundedness Principle, $\mathcal{F}$ is uniformly bounded in operator norm:
:::
\[
C \coloneqq \sup_{T_x \in \mathcal{F}} \|T_x\|_{L(Y, Z)} = \sup_{\|x\| \le 1} \|B(x, \cdot)\|_{L(Y, Z)} < \infty.
\]
::: {.proof}
Uniform Boundedness Principle.
:::

<1>4. Deduce the joint boundedness of $B$: <2>1. Let $x \in X$ and $y \in Y$ be arbitrary non-zero vectors (for $x = 0$ or $y = 0$, bilinearity gives $B(x, y) = 0$, so $\|B(x, y)\| = 0 \le C \|x\| \|y\|$).
::: {.proof}
case distinction.
:::
<2>2. Set $u = \frac{x}{\|x\|}$, so $\|u\| = 1$.
::: {.proof}
normalization.
:::
<2>3. By bilinearity of $B$:
\[
\|B(x, y)\| = \|x\| \|B(u, y)\| = \|x\| \|T_u(y)\| \le \|x\| \|T_u\|_{L(Y, Z)} \|y\|.
\]
::: {.proof}
bilinearity and definition of operator norm.
:::
<2>4. Since $\|u\| = 1$, $\|T_u\|_{L(Y, Z)} \le C$ by <1>3.
::: {.proof}
<1>3. <2>5. Therefore $\|B(x, y)\| \le C \|x\| \|y\|$ for all $(x, y) \in X \times Y$.
:::
::: {.proof}
<2>3 and <2>4.
:::

<1>5. Conclusion: There exists a constant $C > 0$ such that $\|B(x, y)\| \le C \|x\| \|y\|$ for all $x \in X, y \in Y$.
::: {.proof}
<1>4.
:::
Q.E.D.
:::
