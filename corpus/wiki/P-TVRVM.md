---
schema: qual/card@1
id: P-TVRVM
kind: problem
title: "2. Base case: for $n=1$, we have $a_1 = 1 \\leq a_2 = \\frac{16} 3 \\leq\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
2. Base case: for $n=1$, we have $a_1 = 1 \leq a_2 = \frac{16} 3 \leq 10.$ Suppose this holds for $k < n$, then 
$$
a_{n-1} \leq a_n = \frac{a_{n-1}}{3} + 5 \implies 3a_{n-1} \leq a_{n-1} + 15 \implies a_{n-1} \leq \frac{15}{2}
$$

   and thus we have
$$
a_{n+1} = \frac{a_n}{3} + 5 = \frac{1}{3}(a_n + 15) \\ 
= \frac{1}{3}((\frac{a_{n-1}}{3} + 5) + 15) \\
= \frac{a_{n-1} + 60}{9} \\
\leq \frac{\frac{15}{2} + 60}{9} \\
= \frac{150}{18} \\
< \frac{180}{18} = 10,
$$

and $a_{n+1} \leq 10$. Moreover, note that the relation $a_{n+1} = \frac{a_n}{3} + 5$ can be rewritten as 
$$
a_n = 3a_{n+1} - 15, \\ 
a_{n-1} = 3a_n - 15.
$$ Using the inductive hypothesis $a_{n-1} \leq a_n$, we can thus write
$$
3a_n - 15 = a_{n-1} \leq a_n = 3a_{n+1} - 15,
$$

from which we get $3a_{n} - 15 \leq 3a_{n+1} - 15$ and thus $a_{n} \leq a_{n+1}$.

To compute $\lim_{n\to\infty}a_n$, perhaps there are easier ways, but we can just use generating functions. Note that the limit exists by the **Monotone Convergence Theorem**. Let $A(x) = \sum_{n=0}^\infty a_n x^n$ where $a_0 = 0$. Then applying the magic sauce, we have
$$\begin{align*}
a_n = \frac{1}{3}a_{n-1} + 5 &\implies \sum_{n=1}^\infty a_nx^n = \frac{1}{3}\sum_{n=1}^\infty a_{n-1}x^n + 5\sum_{n=1}^\infty x^n \\
&\implies A(x) - a_0 = \frac 1 3 xA(x) + 5\left( \frac 1 {1-x} - 1\right) \\
&\implies A(x)\left(1 - \frac x 3\right) = 5\left( \frac x {1-x}\right) \\
&\implies A(x) = 15\left(\frac 1 {3-x} \right)\left(\frac x {1-x} \right) \\
&\implies A(x) = \frac{15x}{(3-x)(1-x)} \\
&\implies A(x) = \frac{-\frac{45}{2}}{3-x} + \frac{\frac{15}{2}}{1-x} \\
&\implies A(x) = \frac 3 2 \left(-5 \left( \frac{1}{1-\frac x 3} \right) + 5\left( \frac 1 {1-x}\right) \right) \\
&\implies A(x) = \frac{15}{2} \sum_{n=0}^\infty \left(1 - \left( \frac 1 3\right)^n\right)x^n \\
&\implies a_n = \frac {15} 2 \left(1 - \left( \frac 1 3\right)^n\right)
\end{align*}$$

and so we find 
$$
\lim_{n\to\infty}a_n = \lim_{n\to\infty}\frac {15} 2 \left(1 - \left( \frac 1 3\right)^n\right) = \frac{15}{2}. \qed
$$

  > Alternatively: 
  $$
  a_{n+1} = \frac 1 3 a_n + 5 \implies \lim_{n\to\infty} a_{n+1} = \lim_{n\to\infty} \frac 1 3 a_n + 5 \\
  \implies L = \frac 1 3 L + 5 \implies \frac 2 3 L = 5 \implies L = \frac {15} 2
  $$

