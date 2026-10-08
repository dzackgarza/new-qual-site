---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W4
kind: problem
title: Pointwise and uniform convergence of $x^n$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Functions
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find the pointwise limit of the sequence of functions $\{f_n\}$ given by $f_n(x)=x^n$ on $[0,1]$.
Is the convergence of $f_n$ to $f$ uniform?
([KRD10, 8.6.A]) Why is $$B=\{f\in C([0,1]):\|f\|_\infty\le1\}$$ not compact?
:::

::: {.solution}
<1>1. The pointwise limit is
\[
\boxed{f(x)=\begin{cases}0,&0\leq x<1,\\1,&x=1.\end{cases}}
\]

::: {.proof}
For each fixed $x\in[0,1)$, the geometric sequence $x^n$ tends to zero. At $x=1$, one has $x^n=1$ for every positive integer $n$.
:::

<1>2. The convergence $f_n\to f$ is not uniform on $[0,1]$.

::: {.proof}
For every positive integer $n$, step <1>1 gives
\[
\|f_n-f\|_\infty
=\sup_{0\leq x<1}x^n=1.
\]
Indeed $x^n<1$ for $x<1$, while $x^n\to1$ as $x\to1^-$ for fixed $n$. Thus the supremum norms do not tend to zero.
:::

<1>3. The sequence $(f_n)$ in $B$ has no subsequence converging in the supremum norm.

::: {.proof}
Each $f_n$ is continuous with $\|f_n\|_\infty=1$, so $f_n\in B$. Every subsequence $(f_{n_k})$ converges pointwise to the function $f$ from step <1>1, since $n_k\to\infty$. If a subsequence converged in supremum norm to a function $g\in C([0,1])$, then it would converge pointwise to $g$, forcing $g=f$. But $f$ is discontinuous at $1$, contradicting continuity of $g$.
:::

<1>4. The set $B$ is not compact in the supremum-norm topology.

::: {.proof}
The supremum norm makes $C([0,1])$ a metric space. Compact metric spaces are sequentially compact, whereas step <1>3 supplies a sequence in $B$ without a convergent subsequence in $B$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 identifies the pointwise limit, step <1>2 rules out uniform convergence, and step <1>4 establishes noncompactness of $B$.
:::
:::
