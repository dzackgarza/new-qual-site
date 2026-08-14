---
schema: qual/card@1
id: P-VSKE4
kind: problem
title: "Let $\\Omega \\subset \\CC$ be a connected open subset."
classification:
  areas:
  - complex-analysis
  topics:
  - normal-families
  - montel
  - uniform-convergence
  - identity-theorem
relations: []
review: draft
---

::: {.problem title="?"}
Let $\Omega \subset \CC$ be a connected open subset.
Let $\left\{f_{n}: \Omega \rightarrow \CC\right\}_{n=1}^{\infty}$ be a sequence of holomorphic functions uniformly bounded on compact subsets of $\Omega$.
Let $f: \Omega \rightarrow \CC$ be a holomorphic function such that the set
\[
\left\{z \in \Omega \mid \lim _{n \rightarrow \infty} f_{n}(z)=f(z)\right\}
\]
has a limit point in $\Omega$.
Show that $f_{n}$ converges to $f$ uniformly on compact subsets of $\Omega$.
:::

::: {.solution}
Write $g(z) \da \lim_{n\to\infty}f_n(z)$ for the pointwise limit, then $g(z) = f(z)$ on a set with a limit point.
By the identity principle, $g\equiv f$ on $\Omega$, making $f$ the pointwise limit of the $f_n$.

By Montel, locally uniformly bounded implies normal and locally equicontinuous.
So $\ts{f_n}$ is normal, and thus has a locally uniformly convergent subsequence $\ts{f_{n_k}}$.
Since singletons $\ts{z}$ are compact, $f_{n_k}(z) \to g(z)$ pointwise, and by uniqueness of limits, $\lim_{k\to\infty } f_{n_k} = g = f$ on any compact $K \subseteq \Omega$.

It remains to show that the original sequence $\ts{f_n}$ converges locally uniformly to $f$, not just the subsequence.
Suppose not, then there exists a compact $K \subseteq \Omega$ and $\eps>0$ so that $\norm{f_n - f}_{K, \infty} > \eps$ for infinitely many $n$.
This produces a subsequence $\ts{f_{n_j}}$ with $\norm{f_{n_j} - f} > \eps$ for all $j$.
However, since $\mcf$ was normal, *every* subsequence has a locally uniformly convergent subsequence, so this has a further subsequence $f_{n_{j'}}$ uniformly converging to $f$, a contradiction.
:::
