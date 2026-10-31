---
schema: qual/card@1
id: P-PRACT20-W6-02
kind: problem
title: The nested radical $\sqrt{x+\sqrt{x+\sqrt{x+\cdots}}}$
classification:
  areas:
  - prelim
  topics:
  - Sequences
  - Monotone Convergence
relations: []
review: draft
---

::: {.problem}
Fix $x > 0$. Give a rigorous meaning to $\sqrt{x + \sqrt{x + \sqrt{x + \cdots}}}$ by proving that the sequence
$$
a_{0} = \sqrt{x}, \quad a_{n} = \sqrt{x + a_{n-1}}, \quad n = 1, 2, 3, \dots
$$
converges and finding the limit.
What happens as $x \searrow 0$?
:::

::: {.solution}
Let $L=\frac{1+\sqrt{1+4x}}{2}$. We prove that $(a_n)$ is increasing and bounded above by $L$, so it converges by the monotone convergence theorem.

First, $a_1=\sqrt{x+\sqrt x}\geq\sqrt x=a_0$. If $a_n\geq a_{n-1}$ for some $n$, then

$$
x+a_n\geq x+a_{n-1}\implies\sqrt{x+a_n}\geq\sqrt{x+a_{n-1}}\implies a_{n+1}\geq a_n.
$$

By induction, $(a_n)$ is increasing.

Next, $a_0=\sqrt x=\frac{\sqrt{4x}}{2}\leq L$. Note that

$$
L^2=\frac{1+2\sqrt{1+4x}+1+4x}{4}=x+L.
$$

If $a_n\leq L$ for some $n$, then

$$
a_{n+1}=\sqrt{x+a_n}\leq\sqrt{x+L}=\sqrt{L^2}=L.
$$

By induction, $(a_n)$ is bounded above by $L$.

Hence $a_n\to a$ for some $a\in\RR$. Taking the limit on both sides of $a_{n+1}^2=x+a_n$ gives

$$
a^2=x+a\implies a^2-a-x=0\implies a=\frac{1\pm\sqrt{1+4x}}{2}.
$$

Every $a_n$ is at least $a_0=\sqrt x>0$, so $a>0$, and the negative root is excluded. Thus for $x>0$,

$$
\sqrt{x+\sqrt{x+\sqrt{x+\cdots}}}=\frac{1+\sqrt{1+4x}}{2}.
$$

As $x\searrow0$ this value tends to $1$. If instead $x=0$, then $a_n=0$ for all $n$ and the limit is $0$. So the value of the nested radical is not continuous at $x=0$.
:::
