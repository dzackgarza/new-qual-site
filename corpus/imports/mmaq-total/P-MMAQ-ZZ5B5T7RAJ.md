---
schema: qual/card@1
id: P-MMAQ-ZZ5B5T7RAJ
kind: problem
title: $nx(1-x)^n\to 0$ pointwise but not uniformly on $[0,1]$, and $\lim\int_0^1 n(1-x)^n\sin x\,dx=0$
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-functions
  - convergence-of-integrals
  - integrals
  - uniform-convergence
relations: []
review: draft
solved: true
---

::: problem
Let
$$
f_{n}(x)=n x(1-x)^{n}, \quad n \in \mathbb{N}.
$$

1. Show that $f_n \to 0$ pointwise but not uniformly on $[0, 1]$.

   > Hint: Consider the maximum of $f_n$.

2. $$
   \lim _{n \rightarrow \infty} \int_{0}^{1} n(1-x)^{n} \sin x d x=0
   $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f_n(x) = n x (1-x)^n$ on $[0,1]$: (1) show $f_n \to 0$ pointwise but not uniformly; (2) show $\lim_n \int_0^1 n(1-x)^n \sin x \, dx = 0$.

<1>1. $f_n \to 0$ pointwise on $[0,1]$.
<2>1. $f_n(0) = 0$ for every $n$.
Proof: $n \cdot 0 \cdot 1^n = 0$.
<2>2. For $x \in (0,1]$, $n x (1-x)^n \to 0$.
Proof: with $\rho := 1 - x \in [0,1)$, the factor $x$ is fixed and $n \rho^n \to 0$ (geometric decay dominates polynomial growth).
<2>3. Q.E.D. Proof: <2>1 and <2>2 cover $x = 0$ and $x > 0$.

<1>2. $f_n$ does not converge uniformly to $0$.
<2>1. $f_n$ attains its maximum at $x_n = \frac{1}{n+1}$, with $f_n(x_n) = \frac{n}{n+1}\left(1 - \frac{1}{n+1}\right)^n = \left(\frac{n}{n+1}\right)^{n+1}$.
Proof: $f_n'(x) = n(1-x)^{n-1}\big((1-x) - nx\big)$, which vanishes at $x = \frac{1}{n+1}$; the endpoints give $f_n(0) = f_n(1) = 0 < f_n(x_n)$, so this is the maximum (the hint's suggestion).
<2>2. $\norm{f_n}_\infty = f_n(x_n) \to e^{-1} \neq 0$.
Proof: $\left(\frac{n}{n+1}\right)^{n+1} = \left(1 - \frac{1}{n+1}\right)^{n+1} \to e^{-1}$.
<2>3. Q.E.D. Proof: uniform convergence to $0$ would force $\norm{f_n - 0}_\infty \to 0$, contradicting <2>2.

<1>3. $\lim_n \int_0^1 n(1-x)^n \sin x \, dx = 0$.
<2>1. The integral equals $\int_0^1 n u^n \sin(1-u) \, du$.
Proof: substitute $u = 1 - x$ (then $x = 1 - u$, $dx = -du$, and the bounds flip).
<2>2. On $[0,1]$, $0 \leq \sin(1-u) \leq 1-u$.
Proof: $1 - u \in [0,1] \subseteq [0, \pi]$, where $\sin \geq 0$; and $\sin t \leq t$ for all $t \geq 0$.
<2>3. $0 \leq \int_0^1 n u^n \sin(1-u) \, du \leq \int_0^1 n u^n (1-u) \, du = n\left(\frac{1}{n+1} - \frac{1}{n+2}\right) = \frac{n}{(n+1)(n+2)}$.
Proof: by <2>2, $\int_0^1 u^n (1-u) du = \int_0^1 u^n du - \int_0^1 u^{n+1} du = \frac{1}{n+1} - \frac{1}{n+2}$.
<2>4. Q.E.D. Proof: by <2>3, the integral is squeezed between $0$ and $\frac{n}{(n+1)(n+2)} \to 0$.
:::
