---
schema: qual/card@1
id: P-FBGV6
kind: problem
title: "Suppose that $f: [0,1] \\to \\mathbb{R}$ is differentiable and"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
1.  
Suppose that $f: [0,1] \to \mathbb{R}$ is differentiable and
$f(0) = 0$. Assume that there is a $k > 0$ such that
$$|f'(x)| \leq k|f(x)|$$ for all $x\in [0,1]$. Prove that $f(x) = 0$
for all $x\in [0,1]$.

:::{.proof}
*Proof.* Let $0<\delta_1<1$, and fix $x_1 \in (0, \delta_1]$. Since
$f(x)$ is differentiable on all of $[0,1]$, $f(x)$ is differentiable
on all of $(0, \delta_1)$. So by the Mean Value Theorem, there
exists $x_2 \in (0, x_1)$ such that
$$f'(x_2) = \frac{f(x_1) - f(0)}{x_1-0} = \frac{f(x_1)}{x_1} .$$
Solving for $f(x_1)$, we get $f(x_1) = f'(x_2)x_1$. So by
hypothesis, $f(x_1) = f'(x_2) x_1 \leq k|f(x_2)|x_1$. Assume for
$x_1, x_2, \ldots, x_{n-1} \in (0,1)$ the following conditions are
satisfied for $j\in\{1,2,\ldots, n-1\}$. $$\begin{aligned}
x_j &\in& (0,x_{j-1}) \\
f(x_{j-1}) &=& f'(x_j)x_{j-1} \\
f(x_1) &\leq& k^{j-1}|f(x_j)|(x_{j-1} \cdots x_2x_1)
\end{aligned}$$ I now claim that this inductive process is true
for $j=n$, given that it holds for all $j \leq n$. We apply the Mean
Value Theorem to find some $x_n \in (0, x_{n-1})$ such that
$f'(x_n) = \frac{f(x_{n-1})}{x_{n-1}}$, then write
$f(x_{n-1}) = f'(x_n)x_{n-1}.$ By our inductive hypothesis, we have
$$\begin{aligned}
|f(x_1)| &\leq& k^{n-2}|f(x_{n-1})|(x_{n-2}\cdots x_2x_1) \\
&=& k^{n-2}|f'(x_n)x_{n-1}|(x_{n-2}\cdots x_2x_1)  \\
&\leq& k^{n-2}(k|f(x_n)|)(x_{n-1}x_{n-2}\cdots x_2x_1) \\
&=& k^{n-1}|f(x_n)|(x_{n-1}x_{n-2}\cdots x_2x_1).
\end{aligned}$$

Thus our claim holds by induction. Now, since $f$ is a continuous
function on the closed interval, we can apply the Extreme Value
Theorem to find some $M>0$ for which $f(x) \leq M$ for all
$x\in [0,1]$. Thus we get $$|f(x_1)| \leq k^n M (x_n \cdots x_1)
=(kx_n)(kx_{n-1})\cdots(kx_1)M$$ for all $n \in \mathbb{N}$. If
$k < \frac{1}{x_1}$, then for any $\epsilon > 0$ we can find
$N\in \mathbb{N}$ sufficiently large so that $|f(x_1)| < \epsilon$.
Otherwise, we set $\delta_1< \frac{1}{k}$ so that $kx_1< 1$. ◻
:::

