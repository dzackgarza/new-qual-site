---
schema: qual/card@1
id: P-KVE3S
kind: problem
title: "Show that the space $C^1([a, b])$ is a Banach space when equipped with\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - function-spaces
  - norms
  - completeness
relations: []
review: draft
solved: true
---
Show that the space $C^1([a, b])$ is a Banach space when equipped with the norm
\[
\|f\|:=\sup _{x \in[a, b]}|f(x)|+\sup _{x \in[a, b]}\left|f^{\prime}(x)\right|.
\]

:::{.concept}
- See 
<https://math.stackexchange.com/questions/507263/prove-that-c1a-b-with-the-c1-norm-is-a-banach-space/>
:::

:::{.solution}
\envlist

- Denote this norm $\norm{\wait}_u$

- Let $f_n$ be a Cauchy sequence in this space, so $\norm{f_n}_u < \infty$ for every $n$ and $\norm{f_j - f_k}_u \converges{j, k\to\infty}\to 0$.

and define a candidate limit: for each $x\in I$, set \[f(x) \definedas \lim_{n\to\infty} f_n(x).\]

- Note that 
\[ 
\norm{f_n}_\infty &\leq \norm{f_n}_u < \infty \\
\norm{f_n'}_\infty &\leq \norm{f_n}_u < \infty
.\]

  - Thus both $f_n, f_n'$ are Cauchy sequences in $C^0([a, b], \norm{\wait}_\infty)$, which is a Banach space, so they converge.

- So 
  - $f_n \to f$ uniformly (by uniqueness of limits), 
  - $f_n' \to g$ uniformly for some $g$, and
  - $f, g\in C^0([a, b])$.

- Claim: $g = f'$
  - For any fixed $a\in I$, we have
  \[
  f_n(x) - f_n(a) \quad &\converges{u}\to f(x) - f(a) \\
  \int_a^x f'_n  \quad &\converges{u}\to \int_a^x  g
  .\]
  - By the FTC, the left-hand sides are equal.
  - By uniqueness of limits so are the right-hand sides, so $f' = g$.

- Claim: the limit $f$ is an element in this space.
  - Since $f, f'\in C^0([a, b])$, they are bounded, and so $\norm{f}_u < \infty$. 

- Claim: $\norm{f_n - f}_u \converges{n\to\infty}\to 0$

- Thus the Cauchy sequence $\theset{f_n}$ converges to a function $f$ in the $u\dash$norm where $f$ is an element of this space, making it complete.
:::

