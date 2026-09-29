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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Fall 2006 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Recall that $f_n \to f$ in measure if, for every $\varepsilon > 0$, $\mu(\{x : |f(x) - f_n(x)| \geq \varepsilon\}) \to 0$ as $n \to \infty$.
Let $1 \leq p < \infty$.

(a) Suppose $f_n \to f$ in $L^p(X, \mu)$.
Show that $f_n \to f$ in measure.

(b) Suppose $f_n \to f$ in measure and $|f_n| \leq g$ a.e. with $g \in L^p(X, \mu)$.
Show that $f \in L^p(X, \mu)$ and $f_n \to f$ in $L^p(X, \mu)$.
:::

::: {.solution}
**(a).**

::: pf

::: pf-step
Let $\varepsilon > 0$ and define $E_n = \{x : |f(x) - f_n(x)| \ge \varepsilon\}$.

::: pf-proof
definition.
:::

:::

::: {.pf-step #p1-s2}
On $E_n$, $|f - f_n|^p \ge \varepsilon^p$, so
$$\varepsilon^p \mu(E_n) \le \int_{E_n} |f - f_n|^p\,d\mu \le \int_X |f - f_n|^p\,d\mu = \|f - f_n\|_p^p.$$

::: pf-proof
Chebyshev's inequality.
:::

:::

::: {.pf-step #p1-s3}
Hence $\mu(E_n) \le \varepsilon^{-p} \|f - f_n\|_p^p \to 0$ as $n \to \infty$.

::: pf-proof
step [](#p1-s2){.pf-ref} and $f_n \to f$ in $L^p$.
:::

:::

::: {.pf-step #p1-s4}
Therefore $f_n \to f$ in measure.

::: pf-proof
step [](#p1-s3){.pf-ref} (for every $\varepsilon > 0$).
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #p2-s1}
Since $f_n \to f$ in measure, some subsequence $f_{n_k} \to f$ a.e.

::: pf-proof
convergence in measure implies a subsequence converges a.e.
:::

:::

::: {.pf-step #p2-s2}
$|f_{n_k}| \le g$ a.e., so $|f| \le g$ a.e.

::: pf-proof
step [](#p2-s1){.pf-ref} and taking the pointwise limit.
:::

:::

::: {.pf-step #p2-s3}
Hence $f \in L^p$ (since $g \in L^p$ and $|f| \le g$).

::: pf-proof
step [](#p2-s2){.pf-ref}.
:::

:::

::: {.pf-step #p2-s4}
$|f_n - f|^p \le (|f_n| + |f|)^p \le (2g)^p = 2^p g^p \in L^1$.

::: pf-proof
$|f_n| \le g$ and $|f| \le g$, so $|f_n - f| \le 2g$.
:::

:::

::: {.pf-step #p2-s5}
Suppose for contradiction that $f_n \not\to f$ in $L^p$. Then there is $\varepsilon > 0$ and a subsequence $f_{n_k}$ with $\|f_{n_k} - f\|_p \ge \varepsilon$.

::: pf-proof
negate $L^p$ convergence.
:::

:::

::: {.pf-step #p2-s6}
Since $f_{n_k} \to f$ in measure, a further subsequence $f_{n_{k_j}} \to f$ a.e.

::: pf-proof
convergence in measure implies a.e. convergence of a subsequence.
:::

:::

::: {.pf-step #p2-s7}
$|f_{n_{k_j}} - f|^p \le 2^p g^p \in L^1$ and $|f_{n_{k_j}} - f|^p \to 0$ a.e.

::: pf-proof
step [](#p2-s4){.pf-ref} and step [](#p2-s6){.pf-ref}.
:::

:::

::: {.pf-step #p2-s8}
By the dominated convergence theorem, $\|f_{n_{k_j}} - f\|_p^p = \int |f_{n_{k_j}} - f|^p \to 0$.

::: pf-proof
step [](#p2-s7){.pf-ref}.
:::

:::

::: {.pf-step #p2-s9}
This contradicts step [](#p2-s5){.pf-ref}, so $f_n \to f$ in $L^p$.

::: pf-proof
step [](#p2-s8){.pf-ref} contradicts the lower bound $\varepsilon$.
:::

:::

::: pf-qed
step [](#p1-s4){.pf-ref} (a) and step [](#p2-s3){.pf-ref}, step [](#p2-s9){.pf-ref} (b).
:::

:::
:::
