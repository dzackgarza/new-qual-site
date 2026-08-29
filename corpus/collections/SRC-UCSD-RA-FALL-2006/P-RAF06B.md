---
schema: qual/card@1
id: P-RAF06B
kind: problem
title: "L^p convergence implies convergence in measure; converse with domination"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Convergence in Measure
  - Dominated Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Recall that $f_n \to f$ in measure if, for every $\varepsilon > 0$, $\mu(\{x : |f(x) - f_n(x)| \geq \varepsilon\}) \to 0$ as $n \to \infty$.
Let $1 \leq p < \infty$.

(a) Suppose $f_n \to f$ in $L^p(X, \mu)$.
Show that $f_n \to f$ in measure.

(b) Suppose $f_n \to f$ in measure and $|f_n| \leq g$ a.e. with $g \in L^p(X, \mu)$.
Show that $f \in L^p(X, \mu)$ and $f_n \to f$ in $L^p(X, \mu)$.
:::

::: {.solution}
**(a).**

<1>1. Let $\varepsilon > 0$ and define $E_n = \{x : |f(x) - f_n(x)| \ge \varepsilon\}$.
Proof: definition.

<1>2. On $E_n$, $|f - f_n|^p \ge \varepsilon^p$, so
$$\varepsilon^p \mu(E_n) \le \int_{E_n} |f - f_n|^p\,d\mu \le \int_X |f - f_n|^p\,d\mu = \|f - f_n\|_p^p.$$
Proof: Chebyshev's inequality.

<1>3. Hence $\mu(E_n) \le \varepsilon^{-p} \|f - f_n\|_p^p \to 0$ as $n \to \infty$.
Proof: <1>2 and $f_n \to f$ in $L^p$.

<1>4. Therefore $f_n \to f$ in measure.
Proof: <1>3 (for every $\varepsilon > 0$).

**(b).**

<1>1. Since $f_n \to f$ in measure, some subsequence $f_{n_k} \to f$ a.e.
Proof: convergence in measure implies a subsequence converges a.e.

<1>2. $|f_{n_k}| \le g$ a.e., so $|f| \le g$ a.e.
Proof: <1>1 and taking the pointwise limit.

<1>3. Hence $f \in L^p$ (since $g \in L^p$ and $|f| \le g$).
Proof: <1>2.

<1>4. $|f_n - f|^p \le (|f_n| + |f|)^p \le (2g)^p = 2^p g^p \in L^1$.
Proof: $|f_n| \le g$ and $|f| \le g$, so $|f_n - f| \le 2g$.

<1>5. Suppose for contradiction that $f_n \not\to f$ in $L^p$. Then there is $\varepsilon > 0$ and a subsequence $f_{n_k}$ with $\|f_{n_k} - f\|_p \ge \varepsilon$.
Proof: negate $L^p$ convergence.

<1>6. Since $f_{n_k} \to f$ in measure, a further subsequence $f_{n_{k_j}} \to f$ a.e.
Proof: convergence in measure implies a.e. convergence of a subsequence.

<1>7. $|f_{n_{k_j}} - f|^p \le 2^p g^p \in L^1$ and $|f_{n_{k_j}} - f|^p \to 0$ a.e.
Proof: <1>4 and <1>6.

<1>8. By the dominated convergence theorem, $\|f_{n_{k_j}} - f\|_p^p = \int |f_{n_{k_j}} - f|^p \to 0$.
Proof: <1>7.

<1>9. This contradicts <1>5, so $f_n \to f$ in $L^p$.
Proof: <1>8 contradicts the lower bound $\varepsilon$.

<1>10. Q.E.D.
Proof: <1>4 (a) and <1>3, <1>9 (b).
:::
