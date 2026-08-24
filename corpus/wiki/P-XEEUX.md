---
schema: qual/card@1
id: P-XEEUX
kind: problem
title: Consider the function $f(x) = \frac{x}{1-x^2}$,
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Uniform Continuity
relations: []
review: draft
---

Consider the function $f(x) = \frac{x}{1-x^2}$,
$x \in (0,1)$.

1.  
By using the $\epsilon-\delta$ definition of the limit only,
prove that $f$ is continuous on $(0,1)$. (Note: You are not
allowed to trivialize the problem by using properties of
limits).

2.  
Is $f$ uniformly continuous on $(0,1)$? Justify your answer.

:::{.proof}
Fix $x\in (0,1)$ and let $\epsilon > 0$. Then we have
$$\left |f(x) - f(y) \right| 
= \left|\frac{x}{1-x^2} - \frac{y}{1-y^2}\right| 
= \left| \frac{x(1-y^2) - y(1-x^2)}{(1-x^2)(1-y^2)} \right|
= \left| \frac{x-y}{(1-x)(1+x)(1-y)(1+y)} \right|.$$
Now, choose $\delta > 0$ such that
$\delta < \min\{\frac{1}{2}(1-x)^2\epsilon, \frac{1}{2}(1-x)\}$.
When $x - \delta < y < x + \delta$, $$\begin{aligned}
|f(x) - f(y) | & = & 
\left| \frac{x-y}{(1-x)(1+x)(1-y)(1+y)} \right| \\
& \leq & \left| \frac{x-y}{(1-x)(1-y)} \right| 
\leq  \left| \frac{x-y}{(1-x)(1-(x+ \frac{1}{2}(1 - x)))} \right| \\
& = & \left| \frac{x-y}{(1-x)(1-(x+ \frac{1}{2}(1 - x)))} \right|
= \left| \frac{2}{(1-x)^2} \right||x-y| \\
& < & \epsilon.
\end{aligned}$$

As our choice of $x\in (0,1)$ was arbitrary, we conclude that
$f$ is continuous on all of $(0,1)$. ◻

:::

:::{.proof}
*Proof.* We will show that the function $f$ is not uniformly
continuous. Consider the sequence $(x_n)_{n=1}^\infty$ in
$(0,1)$ defined by $x_n = \frac{n}{n+1}$. Observe that
$$f(x_n) = \frac{\frac{n}{n+1}}{1-\left(\frac{n}{n+1}\right)^2} 
= \frac{n(n+1)}{(n+1)^2 - n^2} = \frac{n(n+1)}{[(n+1)-n][(n+1)+n]} 
= \frac{n(n+1)}{2n+1}$$ Written as
$x_n = 1 - \frac{1}{n+1}$, one can more easily see that
$(x_n)_{n=1}^\infty$ converges to $1$ in $\mathbb{R}$, hence is
Cauchy in $(0,1)$. Now, let $\delta > 0$ and choose
$N\in \mathbb{N}$ such that $|x_n - x_m| < \delta$ when
$n,m \geq N$. For $\epsilon < \frac{1}{8}$ we have

$$\begin{aligned}
\left| f(x_n) - f(x_{n+1}) \right|
&=& \left|\frac{n(n+1)}{2n+1} - \frac{(n+1)(n+2)}{2n+3} \right| 
= \left|\frac{n(n+1)(2n+3) - (n+1)(n+2)(2n+1)}{(2n+1)(2n+3)}  \right| \\ 
&=&  \left|\frac{(2n^3+5n^2+3n) - (2n^3+7n^2+7n+2)}{(2n+1)(2n+3)}  \right|
= \left|\frac{ 2n^2+4n+2 }{4n^2 + 8n + 3}  \right| \\
&\geq& \left| \frac{2n^2}{ 16n^2 } \right| =  \frac{1}{8}.\end{aligned}$$
So for any $\delta > 0$, we see that there exists two points
$x_n, x_{n+1} \in (0,1)$ such that $|x_n - x_{n+1}| < \delta$
when $n$ is sufficiently large but
$f(x_n) - f(x_{n+1}) | \not < \epsilon$. Therefore $f(x)$ is not
uniformly continuous. ◻
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (Part 1) $f$ is continuous on $(0,1)$.
    Proof: $f = p/q$ where $p(x) = x$ and $q(x) = 1 - x^2$ are continuous and $q(x) \ne 0$ on $(0,1)$; a quotient of continuous functions with nonzero denominator is continuous. (The card asks for an $\eps$--$\delta$ proof: for fixed $x_0 \in (0,1)$, $q$ is bounded away from $0$ near $x_0$ and the numerator is bounded, and
    \[
    \Big|\frac{x}{1-x^2} - \frac{x_0}{1-x_0^2}\Big| = \frac{|x - x_0|\cdot|1 + xx_0|}{(1-x^2)(1-x_0^2)},
    \]
    from which $\eps$--$\delta$ follows by keeping $x$ close to $x_0$ so $1-x^2$ stays bounded away from $0$.)
<1>2. (Part 2) $f$ is NOT uniformly continuous on $(0,1)$.
    Proof: $f$ is unbounded on $(0,1)$: as $x \to 1^-$, $f(x) = x/(1-x^2) \to +\infty$. A uniformly continuous function on a bounded interval is bounded: given $\eps = 1$, choose $\delta > 0$ with $|x-y| < \delta \Rightarrow |f(x)-f(y)| < 1$; covering $(0,1)$ by finitely many intervals of length $< \delta$ and chaining with the triangle inequality bounds $|f|$ by a constant depending only on one value of $f$. Since $f$ is unbounded, it cannot be uniformly continuous.
<1>3. Q.E.D.
:::
