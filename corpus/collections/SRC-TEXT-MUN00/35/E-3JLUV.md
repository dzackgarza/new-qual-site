---
schema: qual/card@1
id: E-3JLUV
kind: exercise
title: Bounded under every metric, bounded continuous functions, and limit point compactness
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be metrizable.
Show that the following are equivalent:

(i) $X$ is bounded under every metric that gives the topology of $X$.

(ii) Every continuous function $\phi: X \to \mathbb{R}$ is bounded.

(iii) $X$ is limit point compact.

[Hint: If $\phi: X \to \mathbb{R}$ is a continuous function, then $F(x) = x \times \phi(x)$ is an imbedding of $X$ in $X \times \mathbb{R}$. If $A$ is an infinite subset of $X$ having no limit point, let $\phi$ be a surjection of $A$ onto $\mathbb{Z}_+$.]
:::

::: solution
**Goal:** Prove the equivalence of (i) universal metric boundedness, (ii) pseudocompactness (boundedness of continuous real-valued functions), and (iii) limit point compactness for any metrizable space $X$.

<1>1. (i) $\implies$ (ii):
    *Proof:*
    <2>1. Suppose for contradiction that there exists a continuous function $\phi: X \to \mathbb{R}$ that is unbounded.
    <2>2. Let $d_0$ be an arbitrary compatible metric on $X$.
    <2>3. Define a new function $d: X \times X \to [0, \infty)$ by:
        $$d(x, y) = d_0(x, y) + |\phi(x) - \phi(y)|.$$
    <2>4. $d$ is a metric on $X$: positivity, non-degeneracy, symmetry, and the triangle inequality hold immediately from the properties of $d_0$ and the absolute value metric on $\mathbb{R}$.
    <2>5. $d$ generates the original topology of $X$: the map $F(x) = (x, \phi(x))$ is a topological embedding of $X$ into $(X, d_0) \times \mathbb{R}$ with the $\ell_1$ product metric $d((x_1, t_1), (x_2, t_2)) = d_0(x_1, x_2) + |t_1 - t_2|$.
    <2>6. Since $\phi(X)$ is unbounded in $\mathbb{R}$, $\operatorname{diam}_d(X) \ge \sup_{x, y \in X} |\phi(x) - \phi(y)| = \infty$.
    <2>7. Thus $X$ is unbounded under the compatible metric $d$, contradicting (i).
    <2>8. Therefore every continuous function $\phi: X \to \mathbb{R}$ must be bounded.

<1>2. (ii) $\implies$ (iii):
    *Proof:*
    <2>1. Suppose for contradiction that $X$ is not limit point compact.
    <2>2. There exists an infinite subset $A \subseteq X$ with no limit points in $X$.
    <2>3. Let $A_0 = \{a_1, a_2, \dots\}$ be a countably infinite subset of $A$. Since $A$ has no limit points, $A_0$ has no limit points, so $A_0$ is a closed and discrete subspace of $X$.
    <2>4. Define $f: A_0 \to \mathbb{R}$ by $f(a_n) = n$. Because $A_0$ is discrete, $f$ is continuous.
    <2>5. Since $X$ is metrizable, $X$ is normal ($T_4$).
    <2>6. By the Tietze Extension Theorem, $f$ extends to a continuous function $\phi: X \to \mathbb{R}$.
    <2>7. Since $\phi(a_n) = n$ for all $n \in \mathbb{Z}_+$, $\phi$ is unbounded on $X$, contradicting (ii).
    <2>8. Thus $X$ is limit point compact.

<1>3. (iii) $\implies$ (i):
    *Proof:*
    <2>1. For any metrizable space, limit point compactness is equivalent to compactness.
    <2>2. Let $d$ be any metric inducing the topology of $X$. Since $X$ is compact, $(X, d)$ is a compact metric space.
    <2>3. Every compact metric space is bounded: fixing $x_0 \in X$, the open cover $\{B_d(x_0, n)\}_{n=1}^\infty$ has a finite subcover, so $X \subseteq B_d(x_0, N)$, giving $\operatorname{diam}_d(X) \le 2N < \infty$.
    <2>4. Thus $X$ is bounded under $d$, establishing (i).

<1>4. Conclusion:
    The conditions (i), (ii), and (iii) are mutually equivalent. Q.E.D.
:::
