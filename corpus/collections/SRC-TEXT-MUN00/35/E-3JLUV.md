---
schema: qual/card@1
id: E-3JLUV
kind: problem
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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S35.pdf, Exercise 35.3, page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S35.pdf, Internet Archive snapshot 20220130234235 of
    web.math.ku.dk/~moller/e02/3gt/opg/S35.pdf), checked against Munkres, Topology (2000), Section 35
    Exercise 3, printed p. 223, Theorem 35.1, Theorem 28.2 and Exercise 20.3. The three implications
    are the card's: for (i) implies (ii) Moller takes d(x,y) + |phi(x) - phi(y)|, which induces the
    same topology because the identity is a uniform-equivalence between d and d, and is unbounded;
    for (ii) implies (iii) he extends a surjection of a closed discrete infinite subset onto Z_+ by
    Tietze; for (iii) implies (i) he uses that limit point compact metrizable spaces are compact and
    that a metric on a compact space is bounded. The card writes the same three steps with the
    imbedding x -> (x, phi(x)) named. No correction to the mathematics was needed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subsections suffice, and the 21
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: an unbounded continuous function is used to build the compatible metric
    $d_0+\abs{\phi(x)-\phi(y)}$, failure of limit point compactness gives a closed discrete countable
    subset on which Tietze produces an unbounded function, and compactness of a metrizable space bounds it
    under any compatible metric because finitely many balls of integer radius cover it. Checked against
    Munkres, Topology (2000), section 35 Exercise 3. Nothing in the statement was changed.

---

::: {.exercise}

Let $X$ be metrizable.
Show that the following are equivalent:

(i) $X$ is bounded under every metric that gives the topology of $X$.

(ii) Every continuous function $\phi: X \to \RR$ is bounded.

(iii) $X$ is limit point compact.

[Hint: If $\phi: X \to \RR$ is a continuous function, then $F(x) = x \times \phi(x)$ is an imbedding of $X$ in $X \times \RR$. If $A$ is an infinite subset of $X$ having no limit point, let $\phi$ be a surjection of $A$ onto $\ZZ_+$.]
:::

::: {.solution}

If $X=\varnothing$, all three conditions hold. Assume $X\neq\varnothing$ below.

::: pf

::: pf-step
(i) $\implies$ (ii):

::: pf-proof

::: pf-step
Suppose for contradiction that there exists a continuous function $\phi: X \to \RR$ that is unbounded.

::: pf-proof
This is the negation of condition (ii).
:::

:::

::: pf-step
Let $d_0$ be an arbitrary compatible metric on $X$.

::: pf-proof
Such a metric exists because $X$ is metrizable.
:::

:::

::: pf-step
Define a new function $d: X \times X \to [0, \infty)$ by:
$$d(x, y) = d_0(x, y) + \abs{\phi(x) - \phi(y)}.$$

::: pf-proof
This is a definition: the sum of $d_0$ and the pullback of the Euclidean metric along $\phi$.
:::

:::

::: pf-step
$d$ is a metric on $X$: positivity, non-degeneracy, symmetry, and the triangle inequality hold immediately from the properties of $d_0$ and the absolute value metric on $\RR$.

::: pf-proof
Non-negativity, symmetry and the triangle inequality hold termwise, and $d(x,y)=0$ forces $d_0(x,y)=0$, hence $x=y$.
:::

:::

::: pf-step
$d$ generates the original topology of $X$: the map $F(x) = (x, \phi(x))$ is a topological embedding of $X$ into $(X, d_0) \times \RR$ with the $\ell_1$ product metric $d((x_1, t_1), (x_2, t_2)) = d_0(x_1, x_2) + \abs{t_1 - t_2}$.

::: pf-proof
$\phi$ is continuous for $d_0$, so the graph map is a homeomorphism onto its image, and $d$ is the metric pulled back from the product metric $d_0+\abs{\cdot}$ along it.
:::

:::

::: pf-step
Since $\phi(X)$ is unbounded in $\RR$, $\operatorname{diam}_d(X) \ge \sup_{x, y \in X} \abs{\phi(x) - \phi(y)} = \infty$.

::: pf-proof
Since $\phi(X)$ is unbounded, for every $n$ there are points with $\abs{\phi(x)-\phi(y)}>n$, so $d(x,y)>n$.
:::

:::

::: pf-step
Thus $X$ is unbounded under the compatible metric $d$, contradicting (i).

::: pf-proof
Condition (i) says that every compatible metric makes $X$ bounded.
:::

:::

::: pf-step
Therefore every continuous function $\phi: X \to \RR$ must be bounded.

::: pf-proof
The supposition is therefore false.
:::

:::

:::

:::

::: pf-step
(ii) $\implies$ (iii):

::: pf-proof

::: pf-step
Suppose for contradiction that $X$ is not limit point compact.

::: pf-proof
This is the negation of condition (iii).
:::

:::

::: pf-step
There exists an infinite subset $A \subseteq X$ with no limit points in $X$.

::: pf-proof
This is the definition of the failure of limit point compactness.
:::

:::

::: pf-step
Let $A_0 = \{a_1, a_2, \dots\}$ be a countably infinite subset of $A$. Since $A$ has no limit points, $A_0$ has no limit points, so $A_0$ is a closed and discrete subspace of $X$.

::: pf-proof
Every infinite set contains a countably infinite subset.
:::

:::

::: pf-step
Define $f: A_0 \to \RR$ by $f(a_n) = n$. Because $A_0$ is discrete, $f$ is continuous.

::: pf-proof
A set with no limit point is closed and discrete in itself, so every function on it is continuous.
:::

:::

::: pf-step
Since $X$ is metrizable, $X$ is normal ($T_4$).

::: pf-proof
Metrizable spaces are normal.
:::

:::

::: pf-step
By the Tietze Extension Theorem, $f$ extends to a continuous function $\phi: X \to \RR$.

::: pf-proof
Tietze's theorem extends a continuous real function defined on a closed subspace, and $A_0$ is closed because it has no limit point.
:::

:::

::: pf-step
Since $\phi(a_n) = n$ for all $n \in \ZZ_+$, $\phi$ is unbounded on $X$, contradicting (ii).

::: pf-proof
The values of $\phi$ include every positive integer.
:::

:::

::: pf-step
Thus $X$ is limit point compact.

::: pf-proof
The supposition led to a contradiction.
:::

:::

:::

:::

::: pf-step
(iii) $\implies$ (i):

::: pf-proof

::: pf-step
For any metrizable space, limit point compactness is equivalent to compactness.

::: pf-proof
For metric spaces limit point compactness, sequential compactness and compactness coincide.
:::

:::

::: pf-step
Let $d$ be any metric inducing the topology of $X$. Since $X$ is compact, $(X, d)$ is a compact metric space.

::: pf-proof
Let $d$ be an arbitrary compatible metric and fix $x_0$; the balls about $x_0$ of integer radius cover $X$, and compactness extracts a finite subcover.
:::

:::

::: pf-step
Every compact metric space is bounded: fixing $x_0 \in X$, the open cover $\{B_d(x_0, n)\}_{n=1}^\infty$ has a finite subcover, so $X \subseteq B_d(x_0, N)$, giving $\operatorname{diam}_d(X) \le 2N < \infty$.

::: pf-proof
The finite subcover has some largest radius $N$, and then every point is within $N$ of $x_0$, so the diameter is at most $2N$.
:::

:::

::: pf-step
Thus $X$ is bounded under $d$, establishing (i).

::: pf-proof
The metric was arbitrary, which is condition (i).
:::

:::

:::

:::

::: pf-step
Conclusion:
The conditions (i), (ii), and (iii) are mutually equivalent. Q.E.D.

::: pf-proof
The three implications close the cycle, so the three conditions are equivalent.
:::

:::

:::

:::
