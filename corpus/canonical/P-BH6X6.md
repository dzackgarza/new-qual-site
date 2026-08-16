---
schema: qual/card@1
id: P-BH6X6
kind: problem
title: Define Prove that $m(E) = 0$.
classification:
  areas:
  - real-analysis
  topics:
  - borel-cantelli
relations: []
review: draft
---

::: problem
Define
$$
E:=\left\{x \in \mathbb{R}:\left|x-\frac{p}{q}\right|<q^{-3} \text { for infinitely many } p, q \in \mathbb{N}\right\}.
$$

Prove that $m(E) = 0$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

It suffices to show that for every bounded interval $[N, N+1]$ with $N \in \ZZ$, the measure $m(E \cap [N, N+1]) = 0$, since $E = \bigcup_{N \in \ZZ} (E \cap [N, N+1])$.

Fix $N \in \ZZ$, and consider $x \in E \cap [N, N+1]$.
For each pair $(p, q) \in \NN \times \NN$, let $I_{p,q} = \left(\frac{p}{q} - \frac{1}{q^3}, \frac{p}{q} + \frac{1}{q^3}\right)$, which has length $m(I_{p,q}) = \frac{2}{q^3}$.

If $I_{p,q} \cap [N, N+1] \neq \emptyset$, then:
$$
N - \frac{1}{q^3} < \frac{p}{q} < N + 1 + \frac{1}{q^3} \implies qN - \frac{1}{q^2} < p < q(N+1) + \frac{1}{q^2}.
$$
Thus, for each fixed $q \in \NN$, the number of integers $p$ for which $I_{p,q}$ intersects $[N, N+1]$ is at most $q + 3$.

Now compute the sum of the measures of all such intervals:
$$
\sum_{q=1}^\infty \sum_{p: I_{p,q} \cap [N, N+1] \neq \emptyset} m(I_{p,q}) \leq \sum_{q=1}^\infty (q + 3) \cdot \frac{2}{q^3} = 2 \sum_{q=1}^\infty \frac{1}{q^2} + 6 \sum_{q=1}^\infty \frac{1}{q^3} < \infty.
$$

Since $E \cap [N, N+1] \subseteq \limsup_{q \to \infty} \bigcup_p I_{p,q}$, by the **Borel-Cantelli lemma**, the set of points belonging to infinitely many such intervals has measure zero:
$$
m(E \cap [N, N+1]) = 0.
$$
Since $\RR = \bigcup_{N \in \ZZ} [N, N+1]$, by countable additivity $m(E) = 0$.
:::
