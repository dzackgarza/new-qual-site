---
schema: qual/card@1
id: P-YIC3K
kind: problem
title: "Let $f$ be a continuous real-valued function on"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $f$ be a continuous real-valued function on
$[0,1]$. Prove that there exists at least one point $\xi\in[0,1]$
such that $\int_0^1 x^4 f(x)\,dx=\frac{1}{5}f(\xi)$.

:::{.proof}
*Proof.* Assume that $f$ is a continuous real-valued function on
$[0,1]$. Then, by the Intermediate Value Theorem we have that $f$
attains its maximum and minimum on $[0,1]$. That is, for some
$a,b\in[0,1]$,

$$f(a)=\min\limits_{[0,1]}f(x) \qquad \text{and} \qquad  f(b)=\max\limits_{[0,1]}f(x).$$

We now have $f(a)\leq f(x)\leq f(b)$ for all $x\in[0,1]$. This gives
$$f(a)\int_0^1 x^4dx\leq \int_0^1 x^4f(x)dx\leq f(b)\int_0^1 x^4dx.$$

By the Fundamental Theorem of Calculus we know that

$$\int_0^1x^4dx=\frac{1}{5}.$$

Thus, it follows that

$$\frac{1}{5}f(a)\leq\int_0^1 x^4f(x)dx\leq \frac{1}{5}f(b)$$ giving

$$f(a)\leq 5\int_0^1 x^4f(x)dx\leq f(b).$$

By the Intermediate Value Theorem, there exists $\xi\in[0,1]$ such
that

$$f(\xi)=5\int_0^1 x^4f(x)dx.$$

Therefore, we have that there exists $\xi\in[0,1]$ such that
$\int_0^1 x^4 f(x)dx=\frac{1}{5}f(\xi)$. ◻
:::
