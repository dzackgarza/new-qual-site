---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-12
kind: problem
title: 'A bounded positive multiplier preserves convergence of a positive series'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - sequences-of-numbers
relations: []
review: draft
---

::: {.problem title="?"}
(January 2012 #1a) Let $\{a_n\}$, $\{b_n\}$ be bounded sequences of positive real numbers.
If $\sum b_n$ is convergent, show that $\sum a_nb_n$ is also convergent.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Bound $a_n$ uniformly.
    Proof: $\{a_n\}$ is bounded and positive, so there is $M > 0$ with $0 < a_n \le M$ for all $n$.
<1>2. Compare $\sum a_n b_n$ with $\sum b_n$.
    Proof: for every $n$, $a_n b_n \le M b_n$ (as $b_n > 0$). Since $\sum b_n$ converges and $M$ is constant, $\sum M b_n$ converges; by the comparison test, $\sum a_n b_n$ converges.
<1>3. Q.E.D.
:::
