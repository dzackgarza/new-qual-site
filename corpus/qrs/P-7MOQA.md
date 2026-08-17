---
schema: qual/card@1
id: P-7MOQA
kind: problem
title: "Let $f, g$ be Lebesgue integrable on $\\RR$ and let $g_n(x) \\da g(x- n)$. Prove that $\\lim_{n\\to \\infty } \\norm{f + g_n}_1 = \\norm{f}_1 + \\norm{g}_1$ For $f\\in L^1(X)$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - l1
  - small-tails
  - norms
relations: []
review: draft
solved: true
---
Let $f, g$ be Lebesgue integrable on $\RR$ and let $g_n(x) \da g(x- n)$.
Prove that
\[
\lim_{n\to \infty } \norm{f + g_n}_1 = \norm{f}_1 + \norm{g}_1
.\]

:::{.concept}
\envlist

- For $f\in L^1(X)$, $\norm{f}_1 \da \int_X \abs{f(x)} \dx < \infty$.

- Small tails in $L_1$: if $f\in L^1(\RR^n)$, then for every $\eps>0$ exists some radius $R$ such that
\[
\norm{f}_{L^1(B_R^c)} < \eps
.\]

- Shift $g$ to the right far enough so that the two densities are mostly disjoint:

![Shifting density](../../assets/Real%20Analysis/UGA%20Questions%20%28no%20solutions%29/sections/figures/densities.png)

- Any integral $\int_a^b f$ can be written as $\norm{f}_1 - O(\text{err})$.

- Bounding technique: 
\[
a-\eps \leq b \leq a+\eps \implies b=a
.\]

:::

:::{.solution}
\envlist

- Fix $\eps$.
- Using small tails for $f, g \in L^1$, choose $R_1, R_2 \gg 0$ so that
\[
\int_{B_{R_1}(0)^c} \abs{f} &< \eps \\
\int_{B_{R_2}(0)^c} \abs{g} &< \eps
.\]

  - Note that this implies
  \[
  \int_{-R_1}^{R_1} \abs{f} &= \norm{f}_1 - 2\eps \\
  \int_{-R_2}^{R_2} \abs{g_N} &= \norm{g_N} - 2\eps 
  .\]

  - Also note that by translation invariance of the Lebesgue integral, $\norm{g}_1 = \norm{g_N}_1$.


- Now use $N$ to make the densities almost disjoint: choose $N\gg 1$ so that $N-R_2 > R_1$:

![Shifting density](../../assets/Real%20Analysis/UGA%20Questions%20%28no%20solutions%29/sections/figures/densities.png)

- Consider the change of variables $x\mapsto x-N$:
\[
\int_{-R_2}^{R_2} \abs{g(x)}\dx 
= \int_{N-R_2} ^{N+R_2} \abs{g(x-N)} \dx
\da \int_{N-R_2} ^{N+R_2} \abs{g_N(x)} \dx
.\]
  - Use this to conclude that
  \[
  \int_{N-R_2}^{N+R_2} \abs{g_N} = \norm{g_N} - 2\eps
  .\]

- Now split the integral in the problem statement at $R_1$:

\[
\norm{f + g_N}_1 
= \int_\RR \abs{f+g_N} 
= \int_{-\infty}^{R_1} \abs{f+ g_N}
+ \int_{R_1}^{\infty} \abs{f+ g_N}
\da I_1 + I_2
.\]

- **Idea**: from the picture, 

  - On $I_1$, $f$ is big and $g_N$ is small
  - On $I_2$, $f$ is small and $g_N$ is big

- Casework: estimate $I_1, I_2$ separately, bounding from above and below.

- $I_1$ upper bound:
  \[
  I_1 
  &\da \int_{-\infty}^{R_1} \abs{f + g_N} \\
  &\leq \int_{-\infty}^{R_1} \abs{f} + \abs{g_N} \\
  &= \int_{-\infty}^{R_1} \abs{f} + \int_{-\infty}^{R_1} \abs{g_N} \\
  &\leq \int_{-\infty}^{R_1} \abs{f} + \int_{-\infty}^{\color{green} N - R_2} \abs{g_N} && R_1 < N-R_2 \\
  &= \norm{f}_1 - \int_{R_1}^{\infty} \abs{f} + \int_{-\infty}^{N - R_2} \abs{g_N} \\
  &\leq \norm{f}_1 - \int_{R_1}^{\infty} \abs{f} + \eps \\
  &\leq \norm{f}_1 + \eps
  .\]
  
  - In the last step we've used that we're subtracting off a positive number, so forgetting it only makes things larger.
  
  - We've also used monotonicity of the Lebesgue integral: if $A\leq B$, then $(c, A) \subseteq (c, B)$ and $\int_{c}^A \abs f \leq \int_c^B \abs{f}$ since $\abs f$ is positive.

- $I_1$ lower bound:
\[
I_1 
&\da \int_{-\infty}^{R_1} \abs{f + g_N} \\
&\geq \int_{-\infty}^{R_1} \abs{f} - \abs{g_N} \\
&= \int_{-\infty}^{R_1} \abs{f} - \int_{-\infty}^{R_1} \abs{g_N} \\
&\geq \int_{-\infty}^{R_1} \abs{f} - \int_{-\infty}^{\color{green} N-R_2} \abs{g_N} && R_1 < N-R_2 \\
&= \norm{f}_1 - \int_{R_1}^{ \infty } \abs f - \int_{- \infty }^{N-R_2} \abs {g_N} \\
&\geq \norm{f}_1 - \eps - \eps \\
&= \norm{f}_1 - 2\eps
.\]

  - Now we've used that the integral with $g_N$ comes in with a negative sign, so extending the range of integration only makes things *smaller*.
  We've also used the $\eps$ bound on both $f$ and $g_N$ here, and both are tail estimates.

- Taken together we conclude
\[
\norm{f}_1 - 2\eps
\leq I_1
\leq \norm{f}_1 && \eps\to 0 \implies  I_1 = \norm{f}_1
.\]


- $I_2$ lower bound:
\[
I_2 
&\da \int_{R_1}^{\infty} \abs{f + g_N} \\
&\leq \int_{R_1}^{\infty} \abs{f} + \int_{R_1}^{\infty} {g_N} \\
&\leq \int_{R_1}^{\infty} \abs{f} + \norm{g_N}_1 - \int_{-\infty}^{R_1} \abs{g_N} \\
&\leq \eps + \norm{g_N}_1 - \int_{-\infty}^{R_1} \abs{g_N} \\
&\leq \eps + \norm{g_N}_1 \\
&= \eps + \norm{g}_1 
.\]

  - Here we've again thrown away negative terms, only increasing the bound, and used the tail estimate on $f$.

- $I_2$ upper bound:

\[
I_2 
&\da \int_{R_1}^{\infty} \abs{f + g_N} \\
&= \int_{R_1}^{\infty} \abs{g_N + f} \\
&\geq \int_{R_1}^{\infty} \abs{g_N} - \int_{R_1}^{\infty} \abs{f} \\
&=  \norm{g_N} - \int_{-\infty}^{R_1} \abs{g_N} - \int_{R_1}^{\infty} \abs{f} \\
&\geq  \norm{g_N} - 2\eps
.\]

  - Here we've swapped the order under the absolute value, and used the tail estimates on both $g$ and $f$.

- Taken together:
\[
\norm{g}_1 - \eps \leq I_2 \leq \norm{g}_1 + 2\eps 
.\]

- Note that we have two inequalities:
\[
\norm{f}_1 - 2\eps &\leq \int_{-\infty}^{R_1} \abs{f -g_N} \leq \norm{f}_1 + \eps \\
\norm{g}_1 - 2\eps &\leq \int^{\infty}_{R_1} \abs{f -g_N} \leq \norm{g}_1 + \eps 
.\]

- Add these to obtain
\[
\norm{f}_1 + \norm{g}_1 - 4\eps \leq I_1 + I_2 \da \norm{f - g_N}_1 \leq \norm{f} + \norm{g}_1 + 2\eps
.\]

- Check that as $N\to \infty$ as $\eps\to 0$ to yield the result.

:::
