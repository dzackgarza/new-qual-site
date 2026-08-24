---
schema: qual/card@1
id: P-STYWD
kind: problem
title: The series $\sum x^n/n!$ converges uniformly on bounded intervals but not on
  $\RR$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

Let 
\[
f(x) = \sum _{n=0}^{\infty} \frac{x^{n}}{n !}.
\]
Describe the intervals on which $f$ does and does not converge uniformly.

:::{.concept}
\envlist
- $f_N\to f$ uniformly $\iff$ $\norm{f_N - f}_\infty \to 0$.
  - Applied to sums: 
  \[
\sum_{0 \leq k\leq N} f_n \converges{u}\to \sum_{k\geq 0} f_n \iff \norm{\sum_{k\geq N+1} f_n }_{\infty} \to 0
  .\]
- An infinite sum is defined as the pointwise limit of its partial sums:
 \[
\sum_{n=0}^\infty c_n x^n \definedas \lim_{N\to \infty} \sum_{n=0}^N c_n x^n
 .\]
- Uniformly decaying terms for uniformly convergent series: if $\sum_{n=0}^\infty f_n(x)$ converges uniformly on a set $A$, then 
\[
\norm{f_n}_{\infty, A} \da \sup_{x\in A} \abs{f_n(x)} \converges{n\to\infty}\too 0
.\]
- $M\dash$test: if $f_n:A \to\CC$ with $\norm{f_n}_\infty < M_n$ and $\sum M_n < \infty$, then $\sum f_n$ converges uniformly and absolutely.
  - If the $f_n$ are continuous, the uniform limit theorem implies $\sum f_n$ is also continuous.
:::

:::{.strategy}
No real place to start, so pick the nicest place: compact intervals.
Then bounded intervals, then unbounded sets.
:::

:::{.solution}
\envlist


- Set $f_N(x) = \sum_{n=1}^N {x^n \over n!}$.
  - Then by definition, $f_N(x) \to f(x)$ pointwise on $\RR$.

- **Claim**: $f_N$ converges on compact intervals
  - For any compact interval $[-M, M]$, we have
  \[
  \norm{f_N(x) - f(x)}_\infty
  &= \sup_{x\in [-M, M] } ~\abs{\sum_{n=N+1}^\infty {x^n \over {n!}} } \\
  &\leq \sup_{x\in [-M, M] } ~\sum_{n=N+1}^\infty \abs{ {x^n \over {n!}} } \\
  &\leq \sum_{n=N+1}^\infty {M^n \over n!} \\
  &\leq \sum_{n=0}^\infty {M^n \over  {n!} } \quad\text{since all additional terms are positive} \\
  &= e^M \\
  &<\infty
  ,\]
    so $f_N \to f$ uniformly on $[-M, M]$ by the M-test.
    - Note: we've used that this power series converges to $e^x$ pointwise everywhere.

- This argument shows that $f$ converges on any bounded set.

- **Claim**:
$f_N$ does not converge uniformly on all of $\RR$.
  - Uniformly convergent sums have uniformly decaying terms:
  \[
  \sum_{n\leq N} g_n \converges{N\to\infty}\too \sum g_n \text{ uniformly on } A \implies \norm{g_n}_{\infty, A} \da \sup_{x\in A} \abs{g_n(x)} \converges{n\to\infty}\too 0
  .\]

  - Take $B_N$ a ball of radius $N$ about 0, then for $N>1$, note that $x=N$ on the boundary and so
  \[
  \norm{x^k \over k!}_{\infty, B_N} = {N^k \over k!} \converges{N\to\infty}\too \infty
  .\]
- **Conclusion**: $f_N$ converges on any bounded $A\subseteq \RR$ but not on all of $\RR$.
:::
