---
schema: qual/card@1
id: P-CASP17G
kind: problem
title: 'Order, rank and genus of the entire function $\cos\sqrt z$'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Order
  - Genus
  - Weierstrass Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, with the definitions stated and the two asymptotic claims proved. The prose said "z_k is asymptotic to k^2, so the exponent of convergence is 1/2", "the canonical product has rank 0 and genus 0", and "log M(r) is asymptotic to sqrt r" without argument; the card now defines order, exponent of convergence, rank and genus, proves the sum over 1/|z_k| converges (so the rank is 0) and that the exponent of convergence is 1/2, and proves the order is 1/2 from both sides: the upper bound from |cos w| <= e^{|w|} and the lower bound from |f(-r)| = cosh(sqrt r) >= e^{sqrt r}/2. The product identity is Euler's cosine product with w^2 = z, and the card says why substituting is legitimate (the identity theorem applied to the agreement on z >= 0). The final step states plainly what is and is not claimed: the order is not the rank. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the answers order 1/2, rank 0, genus 0 are correct.
---

::: {.problem}
Show that the function $f(z) = \cos(\sqrt{z})$ is entire.
Determine the order, rank and genus of $f$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

The definitions used are the standard ones for an entire function $f$ with zeros $z_1,z_2,\dots$ repeated by multiplicity and maximum modulus $M(r)=\max_{\abs{z}\le r}\abs{f(z)}$: the order is $\rho=\limsup_{r\to\infty}\frac{\log\log M(r)}{\log r}$; the exponent of convergence of the zeros is $\lambda=\inf\{\alpha>0:\sum_k\abs{z_k}^{-\alpha}<\infty\}$; the rank is the least integer $p\ge0$ with $\sum_k\abs{z_k}^{-(p+1)}<\infty$; and the genus of $f$ is $\max(p,\deg P)$ when $f=e^P\prod_kE_p(z/z_k)$ is the Hadamard factorization by a canonical product of genus $p$.

::: pf

::: {.pf-step #entire}
$\cos(\sqrt z)$ is entire.

::: pf-proof
The power series of $\cos$ in the variable $w=\sqrt z$ is $\sum_k\frac{(-1)^kw^{2k}}{(2k)!}=\sum_k\frac{(-1)^kz^k}{(2k)!}$, which converges for every $z$ since $\frac1{(2k)!}$ decays faster than any power: the radius of convergence is $\lim_k\frac{(2k+2)!}{(2k)!}=\infty$. So the displayed series defines an entire function $f$ with $f(w^2)=\cos w$ for all $w$.
:::

:::

::: {.pf-step #zeros}
The zeros of $f$ are $z_k=\pi^2\left(k+\frac12\right)^2$, $k=0,1,2,\dots$, each simple.

::: pf-proof
$f(w^2)=\cos w$, so $f(z)=0$ for $z=w^2$ exactly when $\cos w=0$, that is $w=\pi\left(k+\frac12\right)$ for some integer $k$; and every $z$ with $\sqrt z=w$ gives the same $z$ for $w$ and $-w$, which is why $k\ge0$ enumerates each zero once. So the zeros are $\pi^2(k+\frac12)^2$. For simplicity, note $f'(z)=-\sin(\sqrt z)/(2\sqrt z)$ for $z\ne0$ (from $f(w^2)=\cos w$ by the chain rule, $2wf'(w^2)=-\sin w$), and at $z_k$,
$$
f'(z_k)=-\frac{\sin\left(\pi(k+\frac12)\right)}{2\pi(k+\frac12)}=\pm\frac{1}{2\pi(k+\frac12)}\ne0,
$$
so each zero is simple. The zero set is unbounded, and $0$ is not a zero since $\cos0=1$.
:::

:::

::: {.pf-step #series}
$\sum_k\abs{z_k}^{-1}<\infty$, and $\sum_k\abs{z_k}^{-\alpha}$ converges exactly for $\alpha>\frac12$.

::: pf-proof
$\abs{z_k}=\pi^2(k+\frac12)^2\ge\pi^2k^2$, and $\sum_{k\ge1}k^{-2}<\infty$, so $\sum_k\abs{z_k}^{-1}\le\pi^{-2}\sum_{k\ge0}(k+\frac12)^{-2}<\infty$. More generally $\abs{z_k}^{-\alpha}=\pi^{-2\alpha}(k+\frac12)^{-2\alpha}\le\pi^{-2\alpha}k^{-2\alpha}$ for $k\ge1$, so the series converges when $2\alpha>1$; and $\abs{z_k}^{-\alpha}\ge\pi^{-2\alpha}(k+1)^{-2\alpha}$, so it diverges when $2\alpha\le1$, because $\sum_k(k+1)^{-2\alpha}$ diverges for $2\alpha\le1$.
:::

:::

::: {.pf-step #product}
$f(z)=\prod_{k\ge0}\left(1-\dfrac{z}{z_k}\right)$, the product converging uniformly on compact subsets of $\CC$.

::: pf-proof
Euler's product for the cosine is $\cos w=\prod_{k\ge0}\left(1-\frac{4w^2}{\pi^2(2k+1)^2}\right)$ for all $w\in\CC$, uniformly on compacta. Since $\frac{4}{\pi^2(2k+1)^2}=\frac{1}{\pi^2(k+1/2)^2}=\frac1{z_k}$, the right side is $G(w^2)$ where $G(z)=\prod_{k\ge0}(1-z/z_k)$. Because $\sum_k\abs{z/z_k}$ converges locally uniformly (step [](#series){.pf-ref}), $G$ is entire. Since $\cos w$ is even, $G(w^2)=\cos w=f(w^2)$ for every $w$; in particular $G$ and $f$ agree at every $z\ge0$, a set with accumulation points, so $G=f$ by the identity theorem.
:::

:::

::: {.pf-step #order}
The order of $f$ is $\rho=\dfrac12$.

::: pf-proof
Upper bound: $\abs{\cos w}=\frac12\abs{e^{iw}+e^{-iw}}\le e^{\abs{\operatorname{Im}w}}\le e^{\abs{w}}$, so for $\abs{z}\le r$, taking $w=\sqrt z$ with $\abs{w}\le\sqrt r$, $M(r)\le e^{\sqrt r}$; hence $\log\log M(r)\le\log\sqrt r=\frac12\log r$ and $\rho\le\frac12$.
Lower bound: at $z=-r$, $\abs{f(-r)}=\abs{\cos(i\sqrt r)}=\cosh(\sqrt r)\ge\frac12e^{\sqrt r}$, so $M(r)\ge\frac12e^{\sqrt r}$ and $\log\log M(r)\ge\log(\sqrt r-\log2)$, which is $\frac12\log r+o(\log r)$. Hence $\rho\ge\frac12$, and $\rho=\frac12$.
:::

:::

::: {.pf-step #rank}
The rank of $f$ is $0$ and the exponent of convergence of its zeros is $\lambda=\frac12$.

::: pf-proof
The rank is the least $p\ge0$ with $\sum_k\abs{z_k}^{-(p+1)}<\infty$; for $p=0$ the exponent is $p+1=1$ and step [](#series){.pf-ref} gives convergence, so the rank is $0$ (a least element of a set of nonnegative integers containing $0$). The exponent of convergence is $\inf\{\alpha:\sum\abs{z_k}^{-\alpha}<\infty\}$, which by step [](#series){.pf-ref} is the infimum of $\{\alpha:\alpha>\frac12\}$, namely $\frac12$.
:::

:::

::: {.pf-step #genus}
The genus of $f$ is $0$.

::: pf-proof
By step [](#product){.pf-ref}, $f=\prod_{k\ge0}(1-z/z_k)$ is exactly a canonical product of genus $p=0$ with the exponential factor $e^P$ having $P=0$, so $\deg P=0$; by step [](#rank){.pf-ref} $p=0$. Hence the genus $\max(p,\deg P)=0$.
:::

:::

::: {.pf-step}
$\cos(\sqrt z)$ is entire of order $\frac12$, rank $0$ and genus $0$, with simple zeros at $\pi^2(k+\frac12)^2$.

::: pf-proof
Steps [](#entire){.pf-ref}, [](#zeros){.pf-ref}, [](#order){.pf-ref}, [](#rank){.pf-ref} and [](#genus){.pf-ref} give the four assertions asked for. The answers are mutually consistent: the exponent of convergence of the zeros equals the order, $\lambda=\rho=\frac12$, as Hadamard's factorization requires, while the rank depends only on how fast the zeros grow and is $0$ here because $\sum_k\abs{z_k}^{-1}$ converges. The order $\frac12$ is carried by the growth of $f$ and by the density of its zeros, not by the rank.
:::

:::

:::
:::
