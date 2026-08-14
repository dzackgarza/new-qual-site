---
schema: qual/card@1
id: P-EDU3Q
kind: problem
title: "Prove that the sequence $\\left(1+\\frac{z}{n}\\right)^{n}$ converges uniformly to $e^{z}$ on compact\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - sequences-of-functions
  - entire-functions
  - complex-logarithm
relations: []
review: draft
---
:::{.problem title="?"}
Prove that the sequence $\left(1+\frac{z}{n}\right)^{n}$ converges uniformly to $e^{z}$ on compact subsets of $\mathbb{C}$. 

> Hint: $e^{n \log w_{n}}=w_{n}^{n}$ and $e^{z}$ is uniform continuous on compact subsets of $\mathbb{C}$.

:::

:::{.solution}

Let $K$ be compact, where $z\in K\implies \abs{z} \leq R$ for some constant $R$. For the remainder of the problem, we only work in $K$.

:::{.claim}
$f_n(z) \da n\log(1 + {z\over n}) \to z$ uniformly.
:::

:::{.claim}
$f_n$ are uniformly bounded on $K$.
:::


:::{.claim}
$e^z$ is uniformly continuous on $K$.
:::


:::{.claim}
If $g_n\to g$ uniformly and $F$ is uniformly continuous, then $F \circ g_n \to F\circ g$ uniformly.
:::


Why these claims imply the result:

If $f_n(z)\to z$ uniformly, both are uniformly bounded, and $e^z$ is uniformly continuous, then $e^{f(z)}\to e^z$ uniformly.


:::{.proof title="Of first claim"}
We'll first show that for $w$ in a neighborhood of zero avoiding 1, there exists a constant $C$ such that
\[
\abs{ 1 - {\log(1+w) \over w} } \leq C\abs{w}
.\]
This follows from estimating the series expansion about $w=0$:
\[
\abs{ 1 - {\log(1+w) \over w} }
&= \abs{w\inv\sum_{k\geq 1} { (-w)^k \over k} } \\
&= \abs{\sum_{k\geq 2} {(-w)^{k-1} \over k} } \\
&\leq {\sum_{k\geq 2} {\abs{w}^{k-1} \over k} } \\
&= {\sum_{k\geq 1} {\abs{w}^{k} \over k+1} } \\
&\leq {\sum_{k\geq 1} {\abs{w}^{k} \over 2} } \\
&= {1\over 2}\qty{{1\over 1 - \abs w} - 1 } \\
&= {1\over 2}\abs{2} \qty{1\over 1 - \abs w} \\
&\leq C \abs{w}
,\]
using that ${1\over 1-x}$ is bounded in compact sets avoiding $x=1$.

We can now apply the $M\dash$test:
\[
\abs{n\log\qty{ 1 + {z\over n} } - z } 
&= \abs{z}\cdot \abs{
{{ \log\qty{1 + {z\over n}} \over {z\over n}} - 1}
} \\
&\leq \abs{z} \cdot C\abs{z\over n} \\
&\leq M\cdot C\qty{M\over n} \\
&= {CM^2 \over n}\\
&\convergesto{n\to\infty}0
.\]


:::


:::

