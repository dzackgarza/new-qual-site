---
schema: qual/card@1
id: P-B6S3M
kind: problem
title: "Let $(X, \\mathcal B, \\mu)$ be a measure space with $\\mu(X) = 1$ and $\\{B_n\\}_{n=1}^\\infty$ be a sequence of $\\mathcal B$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - borel-cantelli
  - measure-theory
relations: []
review: draft
solved: true
---
Let $(X, \mathcal B, \mu)$ be a measure space with $\mu(X) = 1$ and $\{B_n\}_{n=1}^\infty$ be a sequence of $\mathcal B$-measurable subsets of $X$, and
$$
B \definedas \theset{x\in X \suchthat x\in B_n \text{ for infinitely many } n}.
$$

a. Argue that $B$ is also a $\mathcal{B} \dash$measurable subset of $X$.

b. Prove that if $\sum_{n=1}^\infty \mu(B_n) < \infty$ then $\mu(B)= 0$.

c. Prove that if  $\sum_{n=1}^\infty \mu(B_n) = \infty$ **and** the sequence of set complements $\theset{B_n^c}_{n=1}^\infty$ satisfies
$$
\mu\left(\bigcap_{n=k}^{K} B_{n}^{c}\right)=\prod_{n=k}^{K}\left(1-\mu\left(B_{n}\right)\right)
$$
for all positive integers $k$ and $K$ with $k < K$, then $\mu(B) = 1$.

> Hint: Use the fact that $1 - x ≤ e^{-x}$ for all $x$.

:::{.concept}
\envlist
- Borel-Cantelli: for a sequence of sets $X_n$, 
\[
\theset{x \suchthat x\in X_n \text{ for infinitely many $n$} } 
&= \Intersect_{N\geq 1} \Union_{n\geq N} X_n = \limsup_n X_n
\\
\theset{x \suchthat x\in X_n \text{ for all but finitely many $n$} }
&= \Union_{N\geq 1} \Intersect_{n\geq N} X_n = \liminf X_n
.\]

- Properties of logs and exponentials:
\[
\prod_n e^{x_n} = e^{\Sigma_n x_n} \quad\text{and} \quad \sum_n \log(x_n) = \log\left(\prod_n x_n\right)
.\]

- Tails of convergent sums vanish.
-  Continuity of measure: $B_n \searrow B$ and $\mu(B_0)<\infty$ implies $\lim_n \mu(B_n) = \mu(B)$, and $B_n\nearrow B \implies \lim_n \mu(B_n) = \mu(B)$.

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- The Borel $\sigma\dash$algebra is closed under countable unions/intersections/complements, 
- $B = \limsup_n B_n = \intersect_{N\geq 1} \union_{n\geq N} B_n$ is an intersection of unions of measurable sets.

:::

:::{.proof title="of b"}
\envlist

- Tails of convergent sums vanish, so 
\[
\sum_{n\geq N} \mu(B_n) \mapsvia{N\to\infty} 0
.\] 
- Also,
\[
B_M \definedas \Intersect_{N = 1}^M \Union_{n\geq N} B_n \decreasesto B 
.\]
- A computation:
\[
\mu(B) 
&\da \mu\left(\Intersect_{N\geq 1} \Union_{n\geq N} B_n\right) \\
&\leq \mu\left( \Union_{n\geq N} B_n \right) && \forall N \\
&\leq \sum_{n\geq N} \mu(B_n) && \forall N \\
&\converges{N\to\infty}\too 0
,\]
  where we've used that we're intersecting over fewer sets and this can only increase measure.

:::

:::{.proof title="of c"}
\envlist

- Since $\mu(X) = 1$, in order to show $\mu(B) = 1$ it suffices to show $\mu(X\sm B) = 0$.
- A computation:
\[
\mu(B^c) 
&= \mu\qty{
\qty{
\Intersect _{N=1}^\infty \Union_{n=N}^\infty B_n
}^c
}\\
&= \mu\qty{
\Union _{N=1}^\infty \Intersect_{n=N}^\infty B_n^c
} \\
&\leq \sum_{N=1}^\infty 
\mu\qty{
\Intersect_{n=N}^\infty B_n^c
} \\
&=
\sum_{N=1}^\infty \lim_{K\to\infty} \mu\qty{ \Intersect _{n=N}^K B_n^c } && \text{continuity of measure from above} \\
&=
\sum_{N=1}^\infty \lim_{K\to\infty}  \prod_{n=N}^K \qty{1 - \mu(B_n)} && \text{by assumption} \\
&\leq 
\sum_{N=1}^\infty \lim_{K\to\infty}  \prod_{n=N}^K e^{-\mu(B_n)} && \text{by hint} \\
&=
\sum_{N=1}^\infty \lim_{K\to\infty}  e^{-\sum_{n=N}^K \mu(B_n)}  \\
&=
\sum_{N=1}^\infty  e^{-\lim_{K\to\infty} \sum_{n=N}^K \mu(B_n)} && \text{by continuity of } f(x) = e^x \\
&=
\sum_{N=1}^\infty  e^{-\sum_{n=N}^\infty \mu(B_n)}  \\
&=
\sum_{N=1}^\infty 0 \\
&= 0
.\]

- Here we've used that every tail of a divergent sum is divergent:
if $\sum_{n=1}^\infty a_n \to \infty$ then for every $N$, the tail $\sum_{n=N}^\infty a_n \to \infty$ as well.
- We've also use that if $b_n\to \infty$ then $e^{-b_n} \to 0$.

:::

:::

