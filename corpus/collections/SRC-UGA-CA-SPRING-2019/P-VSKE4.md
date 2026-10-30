---
schema: qual/card@1
id: P-VSKE4
kind: problem
title: Locally bounded holomorphic functions converging on a set with a limit point
  converge uniformly on compacta
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Montel
  - Uniform Convergence
  - Identity Theorem
relations: []
review: draft
---

::: {.problem}
Let $\Omega \subset \CC$ be a connected open subset.
Let $\left\{f_{n}: \Omega \rightarrow \CC\right\}_{n=1}^{\infty}$ be a sequence of holomorphic functions uniformly bounded on compact subsets of $\Omega$.
Let $f: \Omega \rightarrow \CC$ be a holomorphic function such that the set
$$
\left\{z \in \Omega \mid \lim _{n \rightarrow \infty} f_{n}(z)=f(z)\right\}
$$
has a limit point in $\Omega$.
Show that $f_{n}$ converges to $f$ uniformly on compact subsets of $\Omega$.
:::

::: {.solution}
Let $A$ be the set where $f_n\to f$ pointwise; by hypothesis it has a limit point in $\Omega$.

::: pf

::: {.pf-step #sub}
Every subsequence of $(f_n)$ has a further subsequence that converges to $f$ uniformly on compact subsets of $\Omega$.

::: pf-proof
By Montel's theorem, a family of holomorphic functions that is uniformly bounded on compact subsets is normal. So a given subsequence has a further subsequence converging uniformly on compact subsets to some $h$, which is holomorphic by Weierstrass's theorem. On $A$ the pointwise limit of this subsequence is $f$, so $h=f$ on $A$. Since $\Omega$ is connected and $A$ has a limit point in $\Omega$, the identity theorem gives $h=f$.
:::

:::

::: pf-step
$f_n\to f$ uniformly on compact subsets of $\Omega$.

::: pf-proof
If not, there are a compact $K\subseteq\Omega$, an $\varepsilon>0$ and a subsequence $(f_{n_j})$ with $\sup_K\abs{f_{n_j}-f}\ge\varepsilon$ for all $j$. No further subsequence of $(f_{n_j})$ converges to $f$ uniformly on $K$, which contradicts step [](#sub){.pf-ref}.
:::

:::

:::

:::
