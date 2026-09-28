---
schema: qual/card@1
id: P-CH37V
kind: problem
title: Equidistribution of $n\alpha\bmod 1$ for continuous functions and for interval
  indicators
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Integrals
relations: []
review: draft
---

::: {.problem}
Let $\mathbb{R}/\mathbb{Z}$ denote the torus (whose elements we write as cosets) and fix an irrational $\alpha>0$.

a. Show that $$\lim_{N\to\infty} \frac{1}{N}\sum_{n=0}^{N-1} f(n\alpha+\mathbb{Z}) = \int_0^1 f(x+\mathbb{Z})\,dx$$ for all continuous functions $f:\mathbb{R}/\mathbb{Z}\to\mathbb{R}$.

b. Show that the conclusion is also true when $f$ is the characteristic function of a closed interval.
:::

::: {.solution}
(a) Define $A_N(f) = \frac1N\sum_{n=0}^{N-1} f(n\alpha+\mathbb{Z})$ and $I(f)=\int_0^1 f(x+\mathbb{Z})\,dx$.
First we prove $A_N(f)\to I(f)$ when $f$ is a trigonometric polynomial.
By linearity, it suffices to take $f(x)=e^{2\pi ikx}$ for some $k\in\mathbb{Z}$.
If $k=0$ then $f \equiv 1$, so $A_N(f) = \frac1N\sum_{n=0}^{N-1} 1 = 1$ and $I(f) = \int_0^1 1\,dx = 1$, hence both sides equal $1$; so assume $k\ne0$.
Then we have $$A_N(f) = \frac1N\sum_{n=0}^{N-1}(e^{2\pi ik\alpha})^n = \frac1N\frac{1-e^{2\pi ik\alpha N}}{1-e^{2\pi ik\alpha}} \to 0 \quad \text{as } N\to\infty$$ $$I(f) = \int_0^1 e^{2\pi ikx}\,dx = 0.$$ Hence $A_N(P)\to I(P)$ for every trigonometric polynomial $P$.
Now for general $f\in C(\mathbb{R}/\mathbb{Z})$, fix $\epsilon>0$ and, by the Stone--Weierstrass theorem, let $P$ be a trigonometric polynomial with $||f-P||_{L^\infty}<\epsilon$.
Then we have $$|A_N(f)-I(f)| \le |A_N(f)-A_N(P)|+|A_N(P)-I(P)|+|I(P)-I(f)|$$ $$\le 2\epsilon+|A_N(P)-I(P)|.$$ Letting $N\to\infty$ gives $\limsup_{N\to\infty}|A_N(f)-I(f)|\le2\epsilon$; since $\epsilon>0$ is arbitrary, $A_N(f)\to I(f)$.
$\square$

(b) Let $f=\chi_{[a,b]}$.
Let $g_k$ and $h_k$ be sequences of continuous functions satisfying $0\le g_k\le f\le h_k\le1$ for all $k$, and $g_k$ and $h_k$ both converge almost everywhere to $f$ as $k\to\infty$.
Such sequences exist when $a<b$ and $b-a<1$ (if $a=b$ take $g_k=0$; if $b-a\ge1$ then $f\equiv1$ on the torus). For all sufficiently large $k$, let $g_k$ be the continuous function that is $1$ on $[a+\frac1k, b-\frac1k]$, $0$ outside $[a,b]$, and linear on $[a,a+\frac1k]$ and $[b-\frac1k,b]$, and let $h_k$ be the continuous function that is $1$ on $[a,b]$, $0$ outside $[a-\frac1k, b+\frac1k]$, and linear on $[a-\frac1k,a]$ and $[b,b+\frac1k]$; then $g_k\to f$ at every point except $a,b$, and $h_k\to f$ everywhere.
Then for each $N$ and $k$ we have $$A_N(g_k) \le A_N(f) \le A_N(h_k), \quad I(g_k) \le I(f) \le I(h_k).$$ For $k$ fixed, take $N\to\infty$.
Since $g_k$ and $h_k$ are continuous, this implies that $$I(g_k) \le \liminf_{N\to\infty} A_N(f) \le \limsup_{N\to\infty} A_N(f) \le I(h_k).$$ Since everything is dominated by 1 and we have pointwise convergence almost everywhere, by the dominated convergence theorem we can take $k\to\infty$ and get $$I(f) \le \liminf_{N\to\infty} A_N(f) \le \limsup_{N\to\infty} A_N(f) \le I(f),$$ so $\lim_{N\to\infty}A_N(f)=I(f)$.
$\square$
:::
