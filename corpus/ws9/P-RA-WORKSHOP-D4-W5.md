---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W5
kind: problem
title: 'A liminf-limsup bound for real sequences'
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
relations: []
review: draft
---

::: {.problem title="?"}
A useful lemma: Let $\{x_n\}$ be a real sequence with $\liminf_{n\to\infty}x_n$, $\limsup_{n\to\infty}x_n\in\mathbb R$.
Show that for any $\epsilon>0$ there exists some $N\in\mathbb N$ so that
$$
\left(\liminf_{n\to\infty}x_n\right)-\epsilon<x_n<
\left(\limsup_{n\to\infty}x_n\right)+\epsilon
\qquad\text{for all }n\ge N.
$$
What does this result imply if $\limsup_{n\to\infty}x_n<L$?
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Upper bound: eventually $x_n < \limsup x_n + \epsilon$.
    Proof: let $L = \limsup x_n = \inf_N \sup_{n \ge N} x_n$ (finite by assumption). For any $\epsilon > 0$, $L + \epsilon$ is not a lower bound of the tail suprema... more precisely, $L = \inf_N S_N$ with $S_N = \sup_{n\ge N}x_n$, so there is $N_1$ with $S_{N_1} < L + \epsilon$. Then for all $n \ge N_1$, $x_n \le S_{N_1} < L + \epsilon$.
<1>2. Lower bound: eventually $x_n > \liminf x_n - \epsilon$.
    Proof: let $\ell = \liminf x_n = \sup_N \inf_{n\ge N} x_n$. For any $\epsilon > 0$, $\ell - \epsilon$ is not an upper bound of the tail infima, so there is $N_2$ with $\inf_{n\ge N_2} x_n > \ell - \epsilon$; hence for all $n \ge N_2$, $x_n > \ell - \epsilon$.
<1>3. Combine.
    Proof: with $N = \max(N_1, N_2)$, for all $n \ge N$:
    \[\ell - \epsilon < x_n < L + \epsilon.\]
<1>4. Consequence if $\limsup x_n < L$.
    Proof: taking $\epsilon = L - \limsup x_n > 0$ in <1>1 gives $x_n < \limsup x_n + \epsilon = L$ for all $n \ge N$. Hence the sequence is eventually strictly bounded above by $L$: $x_n < L$ for all large $n$. (Similarly, $\liminf x_n > \ell$ would force $x_n > \ell$ eventually.)
<1>5. Q.E.D.
:::
