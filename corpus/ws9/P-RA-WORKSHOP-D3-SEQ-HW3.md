---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW3
kind: problem
title: 'Conditional convergence with divergent square series prevents absolute convergence (warm-up)'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
relations: []
review: draft
---

::: {.problem title="?"}
(January 2003 #1) Let $\{a_k\}$ be a sequence of real numbers such that the series $\sum_{k=1}^{\infty}a_k$ converges and $\sum_{k=1}^{\infty}a_k^2$ diverges.
Prove that $\sum_{k=1}^{\infty}a_k$ does not converge absolutely.
(See also June 2010 #3a where you are instead told that $\sum_{k=1}^{\infty}a_ka_{k+1}$ diverges and asked to show the same result.
Compare this to June 2009 #3a and January 2005 #1b.)
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Suppose, toward a contradiction, that $\sum |a_k|$ converges.
<1>2. Then $|a_k| \le 1$ eventually.
    Proof: convergence of $\sum |a_k|$ forces $|a_k| \to 0$, so for all large $k$, $|a_k| \le 1$, hence $a_k^2 \le |a_k|$.
<1>3. $\sum a_k^2$ converges, contradiction.
    Proof: for all large $k$, $0 \le a_k^2 \le |a_k|$; by comparison with the convergent series $\sum |a_k|$, the series $\sum a_k^2$ converges — contradicting the hypothesis that it diverges.
<1>4. Q.E.D.
    Proof: hence $\sum a_k$ does not converge absolutely.
:::
