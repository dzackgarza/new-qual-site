---
schema: qual/card@1
id: P-UTQJT
kind: problem
title: "a. Prove that if $g\\in L^1(\\RR)$ then"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
a. Prove that if $g\in L^1(\RR)$ then
\[
\lim_{N\to \infty} \int _{\abs{x} \geq N} \abs{f(x)} \, dx = 0
,\]
and demonstrate that it is not necessarily the case that $f(x) \to 0$ as $\abs{x}\to \infty$.

b. Prove that if $f\in L^1([1, \infty])$ and is decreasing, then $\lim_{x\to\infty}f(x) =0$ and in fact $\lim_{x\to \infty} xf(x) = 0$.

c. If $f: [1, \infty) \to [0, \infty)$ is decreasing with $\lim_{x\to \infty} xf(x) = 0$, does this ensure that $f\in L^1([1, \infty))$?

:::{.concept}
\envlist
- Limits
- Cauchy Criterion for Integrals: $\int_a^\infty f(x) \,dx$ converges iff for every $\eps>0$ there exists an $M_0$ such that $A,B\geq M_0$ implies $\abs{\int_A^B f} < \eps$, i.e. $\abs{\int_A^B f} \converges{A\to\infty}\to 0$.
- Integrals of $L^1$ functions have vanishing tails: $\int_{N}^\infty \abs{f} \converges{N\to\infty}\too 0$.
- Mean Value Theorem for Integrals: $\int_a^b f(t)\, dt = (b-a) f(c)$ for some $c\in [a, b]$.
:::

:::{.solution title="of a"}
Stated integral equality: 

- Let $\eps > 0$
- $C_c(\RR^n) \injects L^1(\RR^n)$ is dense so choose $\theset{f_n} \to f$ with $\norm{f_n - f}_1 \to 0$.
- Since $\theset{f_n}$ are compactly supported, choose $N_0\gg 1$ such that $f_n$ is zero outside of $B_{N_0}(\vector 0)$.
- Then
\[
N\geq N_0 \implies \int_{\abs x > N} \abs{f} &= \int_{\abs x > N} \abs{f - f_n + f_n} \\
&\leq \int_{\abs x > N} \abs{f-f_n} + \int_{\abs x > N} \abs{f_n} \\
&= \int_{\abs x > N} \abs{f-f_n} \\ 
&\leq \int_{\abs x > N} \norm{f-f_n}_1 \\
&= \norm{f_n-f}_1 \qty{\int_{\abs x > N} 1} \\
&\converges{n\to\infty}\too 0 \qty{\int_{\abs x > N} 1} \\
&= 0\\
&\converges{N\to\infty}\too 0
.\]


To see that this doesn't force $f(x)\to 0$ as $\abs{x} \to \infty$:

- Take $f(x)$ to be a train of rectangles of height 1 and area $1/2^j$ centered on even integers.
- Then $$\int_{\abs x > N} \abs{f} = \sum_{j=N}^\infty 1/2^j \converges{N\to\infty}\too 0$$ as the tail of a convergent sum. 
- However $f(x) = 1$ for infinitely many even integers $x > N$, so $f(x) \not\to 0$ as $\abs{x}\to\infty$.
:::

:::{.solution title="of b"}
\envlist

:::{.proof title="Solution 1, a slight trick"}
\envlist

- Since $f$ is decreasing on $[1, \infty)$, for any $t\in [x-n, x]$ we have
\[
x-n \leq t \leq x \implies f(x) \leq f(t) \leq f(x-n)
.\]

- Integrate over $[x, 2x]$, using monotonicity of the integral:
\[
\int_x^{2x} f(x) \,dt \leq 
\int_x^{2x} f(t) \,dt \leq 
\int_x^{2x} f(x-n) \,dt \\ 
\implies 
f(x) \int_x^{2x} \,dt \leq 
\int_x^{2x} f(t) \,dt \leq 
f(x-n) \int_x^{2x} \,dt  \\
\implies xf(x) \leq \int_x^{2x} f(t) \, dt \leq xf(x-n)
.\]

- By the Cauchy Criterion for integrals, $\lim_{x\to \infty} \int_x^{2x} f(t)~dt = 0$.
- So the LHS term $xf(x) \converges{x\to\infty}\too 0$.
- Since $x>1$, $\abs{f(x)} \leq \abs{xf(x)}$ 
- Thus $f(x) \converges{x\to\infty}\too 0$ as well.

:::

:::{.proof title="Solution 2: Variation on the trick"}
\envlist

- Use mean value theorem for integrals:
\[
\int_x^{2x} f(t)\, dt = xf(c_x) \quad\text{for some $c_x \in [x, 2x]$ depending on $x$}
.\]

- Since $f$ is decreasing, 
\[
x\leq c_x \leq 2x 
&\implies f(2x)\leq f(c_x) \leq f(x) \\
&\implies 2xf(2x)\leq 2xf(c_x) \leq 2xf(x) \\
&\implies 2xf(2x)\leq 2x\int_x^{2x} f(t)\, dt \leq 2xf(x) \\
.\]

- By Cauchy Criterion, $\int_x^{2x} f \to 0$.
- So $2x f(2x) \to 0$, which by a change of variables gives $uf(u) \to 0$.
- Since $u\geq 1$, $f(u) \leq uf(u)$ so $f(u) \to 0$ as well.

:::

:::{.proof title="Solution 3: Contradiction"}
Just showing $f(x) \converges{x\to \infty}\too 0$:

- Toward a contradiction, suppose not.
- Since $f$ is decreasing, it can not diverge to $+\infty$
- If $f(x) \to -\infty$, then $f\not\in L^1(\RR)$: choose $x_0 \gg 1$ so that $t\geq x_0 \implies f(t) < -1$, then 
- Then $t\geq x_0 \implies \abs{f(t)} \geq 1$, so
 \[
\int_1^\infty \abs{f} \geq \int_{x_0}^\infty \abs{f(t) } \, dt \geq \int_{x_0}^\infty 1 =\infty
 .\]

- Otherwise $f(x) \to L\neq 0$, some finite limit.
- If $L>0$:
  - Fix $\eps>0$, choose $x_0\gg 1$ such that $t\geq x_0 \implies L-\eps \leq f(t) \leq L$
  - Then $$\int_1^\infty f \geq \int_{x_0}^\infty f \geq \int_{x_0}^\infty \qty{L-\eps}\,dt = \infty$$
- If $L<0$:
  - Fix $\eps > 0$, choose $x_0\gg 1$ such that $t\geq x_0 \implies L \leq f(t) \leq L + \eps$.
  - Then $$\int_1^\infty f \geq \int_{x_0}^\infty f \geq \int_{x_0}^\infty \qty{L}\,dt = \infty$$

Showing $xf(x) \converges{x\to \infty}\too 0$.

- Toward a contradiction, suppose not.
- (How to show that $xf(x) \not\to + \infty$?)
- If $xf(x)\to -\infty$
  - Choose a sequence $\Gamma = \theset{\hat x_i}$ such that $x_i \to \infty$ and $x_i f(x_i) \to -\infty$.
  - Choose a subsequence $\Gamma' = \theset{x_i}$ such that $x_if(x_i) \leq -1$ for all $i$ and $x_i \leq x_{i+1}$.
  - Choose a further subsequence $S = \theset{x_i \in \Gamma' \suchthat 2x_i  < x_{i+1}}$.
  - Then since $f$ is always decreasing, for $t\geq x_0$, $\abs f$ is increasing, and $\abs{f(x_i)} \leq \abs{f(2x_i)}$, so
  \[
  \int_1^{\infty} \abs{f} \geq \int_{x_0}^\infty \abs{f} \geq \sum_{x_i \in S} \int_{x_i}^{2x_i} \abs{f(t)} \, dt \geq 
  \sum_{x_i \in S} \int_{x_i}^{2x_i} \abs{f(x_i)} &= \sum_{x_i \in S} x_i f(x_i) \to \infty
  .\]

- If $xf(x) \to L \neq 0$ for $0 < L< \infty$:
  - Fix $\eps> 0$, choose an infinite sequence $\theset{x_i}$ such that $L-\eps \leq x_i f(x_i) \leq L$ for all $i$.
\[
\int_1^\infty \abs{f} \geq \sum_S \int_{x_i}^{2x_i} \abs{f(t)}\,dt \geq \sum_S \int_{x_i}^{2x_i} f(x_i) \,dt = \sum_S x_i f(x_i) \geq \sum_S \qty{L-\eps} \to \infty
.\]
- If $xf(x) \to L \neq 0$ for $-\infty < L < 0$:
  - Fix $\eps> 0$, choose an infinite sequence $\theset{x_i}$ such that $L \leq x_i f(x_i) \leq L + \eps$ for all $i$.
\[
\int_1^\infty \abs{f} \geq \sum_S \int_{x_i}^{2x_i} \abs{f(t)}\,dt \geq \sum_S \int_{x_i}^{2x_i} f(x_i) \,dt = \sum_S x_i f(x_i) \geq \sum_S \qty{L} \to \infty
.\]

:::

:::{.proof title="Solution 4: Akos' suggestion"}
For $x\geq 1$, 
\[
\abs{xf(x)} = \abs{ \int_x^{2x} f(x) \, dt } \leq \int_x^{2x} \abs{f(x)} \, dt \leq \int_x^{2x} \abs{f(t)}\, dt \leq \int_x^{\infty} \abs{f(t)} \,dt \converges{x\to\infty}\too 0
\]
  where we've used 
  
  - Since $f$ is decreasing and $\lim_{x\to\infty}f(x) =0$ from part (a), $f$ is non-negative.
  - Since $f$ is positive and decreasing, for every $t\in[a, b]$ we have $\abs{f(a)} \leq \abs{f(t)}$.
  - By part (a), the last integral goes to zero.


:::

:::{.proof title="Solution 5: Peter's"}
\envlist

- Toward a contradiction, produce a sequence $x_i\to\infty$ with $x_i f(x_i) \to \infty$ and $x_if(x_i) > \eps > 0$, then
\[
\int f(x) \, dx 
&\geq \sum_{i=1}^\infty \int_{x_i}^{x_{i+1}} f(x) \, dx \\
&\geq \sum_{i=1}^\infty \int_{x_i}^{x_{i+1}} f(x_{i+1}) \, dx \\
&=    \sum_{i=1}^\infty f(x_{i+1}) \int_{x_i}^{x_{i+1}} \, dx \\
&\geq \sum_{i=1}^\infty (x_{i+1} - x_i) f(x_{i+1}) \\
&\geq \sum_{i=1}^\infty (x_{i+1} - x_i) {\eps \over x_{i+1}} \\
&= \eps \sum_{i=1}^\infty \qty{ 1 - {x_{i-1} \over x_i}} \to \infty
\]
  which can be ensured by passing to a subsequence where $\sum {x_{i-1} \over x_i} < \infty$.

:::


:::

:::{.solution title="of c"}
\envlist

- No: take $f(x) = {1\over x\ln x}$
- Then by a $u\dash$substitution,
  \[
  \int_0^x f = \ln\qty{\ln (x)} \converges{x\to\infty}\too \infty
  \]
  is unbounded, so $f\not\in L^1([1, \infty))$.
- But 
  \[
  xf(x) = { 1 \over \ln(x)} \converges{x\to\infty} \too 0
  .\]

:::


## Fall 2019 # 5. $\done$
