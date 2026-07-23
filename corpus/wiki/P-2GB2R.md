---
schema: qual/card@1
id: P-2GB2R
kind: problem
title: "Let"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let
\[
f_{n}(x):=\frac{x}{1+x^{n}}, \quad x \geq 0.
\]

a. Show that this sequence converges pointwise and find its limit. Is the convergence uniform on $[0, \infty)$?

b. Compute 
\[
\lim _{n \rightarrow \infty} \int_{0}^{\infty} f_{n}(x) d x
\]

\todo[inline]{Add concepts.}

:::{.solution}
\hfill
:::{.concept}
\hfill
- ?
:::


**Part a**
Claim: $f_n$ does not converge uniformly to its limit.

- Note each $f_n(x)$ is clearly continuous on $(0, \infty)$, since it is a quotient of continuous functions where the denominator is never zero.

- Note 
\[
x < 1 \implies x^n \converges{n\to\infty}\to 0\qtext{and} x>1 \implies x^n \converges{n\to\infty}\to \infty
.\]

- Thus
\[
f_n(x) = \frac{x}{1+ x^n}\converges{n\to\infty}\longrightarrow
f(x) \definedas
\begin{cases}
x, & 0 \leq x < 1 \\
\frac 1 2, & x = 1 \\
0, & x > 1 \\
\end{cases}
.\]

- If $f_n \to f$ uniformly on $[0, \infty)$, it would converge uniformly on every subset and thus uniformly on $(0, \infty)$.
  - Then $f$ would be a uniform limit of continuous functions on $(0, \infty)$ and thus continuous on $(0, \infty)$.
  - By uniqueness of limits, $f_n$ would converge to the pointwise limit $f$ above, which is not continuous at $x=1$, a contradiction.


**Part b**
- If the DCT applies, interchange the limit and integral:
    \[
    \lim_{n\to\infty }\int_0^\infty f_n(x)\, dx 
&= \int_0^\infty \lim_{n\to\infty}f_n(x) \, dx \quad\text{DCT}\\
    &=\int_0^\infty f(x) \,dx \\
    &= \int_0^1 x \,dx + \int_1^\infty 0\, dx \\
    &= {1\over 2}x^2 \evalfrom_0^1 \\
    &= {1\over 2}
    .\]

- To justify the DCT, write 
\[
\int_0^\infty f_n(x)
= \int_0^1 f_n(x) + \int_1^\infty f_n(x)
.\]

- $f_n$ restricted to $(0, 1)$ is uniformly bounded by $g_0(x) = 1$ in the first integral, since
  \[
  x \in [0, 1] \implies \frac{x}{1+x^n} < \frac{1}{1+x^n} < 1 \definedas g(x)
  \]
  so 
  \[
  \int_0^1 f_n(x)\,dx \leq \int_0^1 1 \,dx = 1 < \infty
  .\]
  Also note that $g_0\cdot \chi_{(0, 1)} \in L^1((0, \infty))$.

- The $f_n$ restricted to $(1, \infty)$ are uniformly bounded by $g_1(x) = {1\over x^{2}}$ on $[1, \infty)$, since
  \[
  x \in (1, \infty) \implies \frac{x}{1+x^n} \leq {x \over x^n} = {1 \over x^{n-1}} \leq {1\over x^2}\in L^1([1, \infty) \text{ when } n\geq 3
  ,\]
  by the $p\dash$test for integrals.

- So set $$g \definedas g_0 \cdot \chi_{(0, 1)} + g_1 \cdot \chi_{[1, \infty)},$$ then by the above arguments $g \in L^1((0, \infty))$ and $f_n \leq g$ everywhere, so the DCT applies.
:::

