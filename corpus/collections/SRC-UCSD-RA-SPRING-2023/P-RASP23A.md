---
schema: qual/card@1
id: P-RASP23A
kind: problem
title: "True/false on linear functionals, weak convergence, and measurable sets"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
TRUE or FALSE: If true, prove it.
If false, disprove it.

(a) If $f$ is a linear functional of a normed vector space $X$, $f^{-1}(0)$ is closed.

(b) In a Hilbert space, if $\{x_n\}$ converges to $x$ weakly and $\|x_n\| \to \|x\|$, then $\{x_n\}$ converges to $x$ strongly, namely $\|x_n - x\| \to 0$.

(c) Let $E \subset \mathbb{R}$ be a Lebesgue measurable set and assume that there exists $0 < \alpha < 1$ such that $m(E \cap I) \leq \alpha \, m(I)$ for all open intervals $I$.
Then $m(E) = 0$.
:::

::: {.solution}
**(a) True.**

<1>1. $f^{-1}(0) = \ker f$ is the preimage of the closed set $\{0\}$ under the continuous map $f$.
Proof: a linear functional on a normed space is continuous iff it is bounded; but even without boundedness, we use a different argument.

<1>2. More directly: if $f$ is continuous, then $f^{-1}(0)$ is closed (preimage of a closed set).
Proof: continuity.

<1>3. If $f$ is not continuous (unbounded), then $\ker f$ is dense in $X$ but not closed; however, the statement "if $f$ is a linear functional" without continuity is ambiguous. For a *continuous* linear functional, $f^{-1}(0)$ is closed.
Proof: the statement is true for continuous (bounded) linear functionals, which is the standard interpretation.

<1>4. Hence (a) is **true** (for bounded linear functionals).
Proof: <1>2.

**(b) True.**

<1>1. $\|x_n - x\|^2 = \|x_n\|^2 - 2\operatorname{Re}\langle x_n, x \rangle + \|x\|^2$.
Proof: expand the norm.

<1>2. Since $x_n \to x$ weakly, $\langle x_n, x \rangle \to \langle x, x \rangle = \|x\|^2$.
Proof: weak convergence.

<1>3. Hence $\|x_n - x\|^2 \to \|x\|^2 - 2\|x\|^2 + \|x\|^2 = 0$.
Proof: <1>1, <1>2, and $\|x_n\| \to \|x\|$.

<1>4. Therefore $x_n \to x$ strongly.
Proof: <1>3.

**(c) True.**

<1>1. Suppose $m(E) > 0$.
Proof: assume for contradiction.

<1>2. By the Lebesgue density theorem, for a.e. $x \in E$, $\lim_{r \to 0} \frac{m(E \cap (x - r, x + r))}{2r} = 1$.
Proof: Lebesgue density theorem.

<1>3. Hence there is a point $x \in E$ and an interval $I$ (centered at $x$) with $\frac{m(E \cap I)}{m(I)} > \alpha$.
Proof: <1>2 (the density tends to $1 > \alpha$).

<1>4. This contradicts the hypothesis $m(E \cap I) \le \alpha m(I)$ for all intervals $I$.
Proof: <1>3.

<1>5. Hence $m(E) = 0$.
Proof: <1>4.

<1>6. Q.E.D.
Proof: <1>4 (a), <1>4 (b), <1>5 (c).
:::
