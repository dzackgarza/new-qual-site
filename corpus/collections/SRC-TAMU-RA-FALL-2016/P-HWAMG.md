---
schema: qual/card@1
id: P-HWAMG
kind: problem
title: The discontinuity set of a real function is $F_\sigma$; no function is continuous
  exactly on $\mathbb{Q}$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(a) Let $f$ be a real valued function on the unit interval $[0,1]$.
Prove that the set of points at which $f$ is discontinuous is a countable union of closed subsets.

(b) Prove that there is no real valued function on $[0,1]$ that is continuous at all rational points but discontinuous at all irrational points.
:::

::: {.solution}
<1>1. Part (a): The discontinuity set is $F_\sigma$:
<2>1. For a function $f: [0, 1] \to \mathbb{R}$, define the oscillation of $f$ at $x \in [0, 1]$ by:
\[
\omega_f(x) = \inf_{r > 0} \operatorname{diam} f(B_r(x) \cap [0, 1]) = \inf_{r > 0} \sup \big\{|f(y) - f(z)| : y, z \in B_r(x) \cap [0, 1]\big\}.
\]
Proof: definition of oscillation.
<2>2. $f$ is continuous at $x$ if and only if $\omega_f(x) = 0$.
Thus the set of discontinuity points $D$ is:
\[
D = \{x \in [0, 1] \mid \omega_f(x) > 0\} = \bigcup_{n=1}^\infty F_n, \quad \text{where } F_n = \left\{x \in [0, 1] \;\middle|\; \omega_f(x) \ge \frac{1}{n}\right\}.
\]
Proof: $\omega_f(x) > 0 \iff \exists n \ge 1 \text{ with } \omega_f(x) \ge 1/n$.
<2>3. We show each $F_n$ is closed by showing its complement $U_n = [0, 1] \setminus F_n = \{x \in [0, 1] \mid \omega_f(x) < 1/n\}$ is open in $[0, 1]$:
If $x \in U_n$, there exists $r > 0$ such that $\operatorname{diam} f(B_r(x) \cap [0, 1]) < 1/n$.
For any $y \in B_{r/2}(x) \cap [0, 1]$, $B_{r/2}(y) \subseteq B_r(x)$, so:
\[
\omega_f(y) \le \operatorname{diam} f(B_{r/2}(y) \cap [0, 1]) \le \operatorname{diam} f(B_r(x) \cap [0, 1]) < \frac{1}{n}.
\]
Thus $B_{r/2}(x) \cap [0, 1] \subseteq U_n$, so $U_n$ is open in $[0, 1]$.
Proof: triangle inequality for metric balls.
<2>4. Since each $F_n$ is closed, $D = \bigcup_{n=1}^\infty F_n$ is a countable union of closed subsets ($F_\sigma$ set).
Proof: definition of $F_\sigma$.

<1>2. Part (b): Non-existence of a function continuous exactly on $\mathbb{Q} \cap [0, 1]$:
<2>1. By Part (a), the set of continuity points $C = [0, 1] \setminus D = \bigcap_{n=1}^\infty U_n$ of any function $f$ must be a $G_\delta$ set (countable intersection of open sets).
Proof: complement of an $F_\sigma$ set is $G_\delta$.
<2>2. Suppose for contradiction that there exists $f: [0, 1] \to \mathbb{R}$ whose set of continuity points is $C = \mathbb{Q} \cap [0, 1]$.
Then $\mathbb{Q} \cap [0, 1] = \bigcap_{n=1}^\infty V_n$ for open sets $V_n \subseteq [0, 1]$.
Proof: assumption for contradiction.
<2>3. Since $\mathbb{Q} \cap [0, 1] \subseteq V_n$ and $\mathbb{Q} \cap [0, 1]$ is dense in $[0, 1]$, each open set $V_n$ is dense in $[0, 1]$.
Proof: a superset of a dense set is dense.
<2>4. Enumerate the countable set $\mathbb{Q} \cap [0, 1] = \{q_1, q_2, q_3, \dots\}$.
For each $k \ge 1$, $W_k = [0, 1] \setminus \{q_k\}$ is open and dense in $[0, 1]$.
Proof: singletons have empty interior in $[0, 1]$.
<2>5. Since $[0, 1]$ is a complete metric space, the Baire Category Theorem implies that the countable intersection of dense open subsets:
\[
\left( \bigcap_{n=1}^\infty V_n \right) \cap \left( \bigcap_{k=1}^\infty W_k \right) = (\mathbb{Q} \cap [0, 1]) \cap \big([0, 1] \setminus (\mathbb{Q} \cap [0, 1])\big) = \emptyset
\]
must be dense in $[0, 1]$, and in particular non-empty.
This contradicts the fact that the intersection is empty.
Proof: Baire Category Theorem on complete metric spaces.

<1>3. Conclusion:
The discontinuity set is $F_\sigma$, and no function can be continuous precisely on the rationals in $[0, 1]$. Q.E.D.
Proof: <1>1 and <1>2.
:::
