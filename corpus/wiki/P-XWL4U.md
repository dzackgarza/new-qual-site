---
schema: qual/card@1
id: P-XWL4U
kind: problem
title: "Let $\\{f_k\\}$ be any sequence of functions in $L^2([0, 1])$ satisfying\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\norm{f_k}_2 ≤ M$ for all $k ∈ \NN$.
  
Prove that if $f_k \to f$ almost everywhere, then $f ∈ L^2([0, 1])$ with $\norm{f}_2 ≤ M$ and
$$
\lim _{k \rightarrow \infty} \int_{0}^{1} f_{k}(x) dx = \int_{0}^{1} f(x) d x
$$

> Hint: Try using Fatou’s Lemma to show that $\norm{f}_2 ≤ M$ and then try applying Egorov’s Theorem.

:::{.solution}
\hfill
:::{.concept}
\hfill
- Definition of $L^+$: space of measurable function $X\to [0, \infty]$.
- Fatou: For any sequence of $L^+$ functions, $\int \liminf f_n \leq \liminf \int f_n$.
- Egorov's Theorem: If $E\subseteq \RR^n$ is measurable, $m(E) > 0$, $f_k:E\to \RR$ a sequence of measurable functions where $\lim_{n\to\infty} f_n(x)$ exists and is finite a.e., then $f_n\to f$ *almost uniformly*: for every $\eps>0$ there exists a closed subset $F_\eps \subseteq E$ with $m(E\setminus F) < \eps$ and $f_n\to f$ uniformly on $F$.
:::

$L^2$ bound:

- Since $f_k \to f$ almost everywhere, $\liminf_n f_n(x) = f(x)$ a.e.
- $\norm{f_n}_2 < \infty$ implies each $f_n$ is measurable and thus $\abs{f_n}^2 \in L^+$, so we can apply Fatou:

\[
\norm{f}_2^2
&= \int \abs{f(x)}^2  \\
&= \int \liminf_n \abs{f_n(x)}^2 \\
&\underset{\text{Fatou}}\leq\liminf_n \int \abs{f_n(x)}^2 \\
&\leq \liminf_n M \\
&= M
.\]

- Thus $\norm{f}_2 \leq \sqrt{M} < \infty$ implying $f\in L^2$.

:::{.remark}
What is the "right" proof here that uses the first part?
:::
Equality of Integrals: 

- Take the sequence $\eps_n = {1\over n}$
- Apply Egorov's theorem: obtain a set $F_\eps$ such that $f_n \to f$ uniformly on $F_\eps$ and $m(I\setminus F_\eps) < \eps$. 
\[
\lim_{n\to \infty} \abs{ \int_0^1 f_n - f }
&\leq \lim_{n\to\infty} \int_0^1 \abs{f_n - f} \\
&= \lim_{n\to\infty} \qty{ \int_{F_\eps} \abs{f_n - f} + \int_{I\setminus F_\eps} \abs{f_n - f} } \\
&= \int_{F_\eps} \lim_{n\to\infty} \abs{f_n - f} + \lim_{n\to\infty} \int_{I\setminus F_\eps} \abs{f_n - f} \quad\text{by uniform convergence} \\ 
&= 0 + \lim_{n\to\infty} \int_{I\setminus F_\eps} \abs{f_n - f}
,\]

  so it suffices to show $\int_{I\setminus F_\eps} \abs{f_n - f} \converges{n\to\infty}\to 0$.

- We can obtain a bound using Holder's inequality with $p=q=2$:
\[
\int_{I\setminus F_\eps} \abs{f_n - f} 
&\leq \qty{ \int_{I\setminus F_\eps} \abs{f_n - f}^2 } \qty{ \int_{I\setminus F_\eps} \abs{1}^2  } \\
&= \qty{ \int_{I\setminus F_\eps} \abs{f_n - f}^2 } \mu(F_\eps) \\
&\leq \norm{f_n - f}_2 \mu(F_\eps) \\
&\leq \qty{ \norm{f_n}_2 + \norm{f}_2 } \mu(F_\eps) \\
&\leq 2M \cdot \mu(F_\eps)
\]
  where $M$ is now a constant not depending on $\eps$ or $n$.

- Now take a nested sequence of sets $F_{\eps}$ with $\mu(F_\eps) \to 0$ and applying continuity of measure yields the desired statement.
:::

