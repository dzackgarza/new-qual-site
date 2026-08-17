---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-11
kind: problem
title: 'Divergence is preserved by the transform a_n to a_n/(β+a_n)'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
relations: []
review: draft
---

::: {.problem title="?"}
(June 2008 #4b) Assume $\beta>0$, $a_n>0$, $n=1,2,\ldots$, and the series $\sum a_n$ is divergent.
Show that
$$
\sum\frac{a_n}{\beta+a_n}
$$
is also divergent.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Split the terms according to whether $a_n \le \beta$.
    Proof: for each $n$, either $a_n > \beta$ or $a_n \le \beta$.
<1>2. If infinitely many $a_n > \beta$, the transformed series diverges trivially.
    Proof: for $a_n > \beta$, $\frac{a_n}{\beta + a_n} > \frac{\beta}{\beta + \beta} = \frac12$ (the map $t \mapsto \frac{t}{\beta+t}$ is increasing), so infinitely many terms of the transformed series are $> 1/2$; its terms do not tend to $0$, so it diverges.
<1>3. If only finitely many $a_n > \beta$, compare with $\sum a_n$.
    Proof: for all large $n$, $a_n \le \beta$, so
    \[\frac{a_n}{\beta + a_n} \ge \frac{a_n}{\beta + \beta} = \frac{a_n}{2\beta}.\]
    Since $\sum a_n$ diverges, $\sum \frac{a_n}{2\beta}$ diverges, and by comparison $\sum \frac{a_n}{\beta + a_n}$ diverges.
<1>4. Q.E.D.
    Proof: in both cases the transformed series diverges.
:::
