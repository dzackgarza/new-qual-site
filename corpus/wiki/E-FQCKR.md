---
schema: qual/card@1
id: E-FQCKR
kind: exercise
title: "Extended Liouville theorem"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Extended Liouville theorem"}
Let $f$ be an entire function. Assume that for some $k \in \mathbb{N}$, and sufficiently large $|z|$, we have that $|f(z)| \leq A+B|z|^{k}$. Prove that $f$ is a polynomal of degree at most $k$.

#complex/exercise/completed

:::

:::{.solution}
By induction on $k$, suppose that if $f$ is degree $k-1$ with $\abs{f} \leq A + B\abs{z}^{k-1}$ outside of a large enough disc.
Let $f$ be degree $k$, and consider
\[
g(z) \da 
\begin{cases}
f'(0) & z=0 
\\
{f(z) - f(0) \over z-0} & z=0.
\end{cases}
.\]
Then outside of a large enough disc,
\[
\abs{g} \sim {A+B\abs{z}^k \over \abs{z}} \leq_{\sim} B\abs{z}^{k-1}
,\]
and moreover by the MMP $g$ is bounded inside such a disc.
So $g$ is a polynomial of degree at most $k-1$ by hypothesis, making $f$ degree at most $k$.
:::

