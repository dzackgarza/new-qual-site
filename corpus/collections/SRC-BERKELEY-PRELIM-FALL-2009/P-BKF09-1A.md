---
schema: qual/card@1
id: P-BKF09-1A
kind: problem
title: Generating function $\sum p(k)z^k$ of a polynomial sequence is rational
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $p(k)$ be a degree $n$ polynomial with complex coefficients defined by
$$
p(k)=p_0+\binom{k}{1}p_1+\binom{k}{2}p_2+\cdots+\binom{k}{n}p_n.
$$
Define
$$
f(z)=\sum_{k=0}^{\infty}p(k)z^k.
$$
Find the radius of convergence of the power series, prove that $f(z)$ is a rational function restricted to the disk of convergence, and give a formula for $f(z)$.
:::

::: {.solution}

The argument is the card's own: the coefficients $\binom{k}{j}$ are the coefficients of $z^{j}(1-z)^{-j-1}$, so $f$ is a sum of rational functions; the radius is the distance to the only pole.

::: pf

::: {.pf-step #binom}

$\displaystyle\sum_{k=0}^{\infty}\binom{k}{j}z^{k}=\frac{z^{j}}{(1-z)^{j+1}}$ for $\abs{z}<1$ and $j\ge0$.

::: pf-proof

$\frac{1}{1-z}=\sum_{k\ge0}z^{k}$ for $\abs{z}<1$, and term-by-term differentiation $j$ times inside the disc of convergence gives $\frac{j!}{(1-z)^{j+1}}=\sum_{k\ge j}k(k-1)\cdots(k-j+1)z^{k-j}$. Dividing by $j!$ and multiplying by $z^{j}$ turns $\frac{k(k-1)\cdots(k-j+1)}{j!}$ into $\binom{k}{j}$ (for $k<j$ both sides are $0$).

:::

:::

::: {.pf-step #rational}

$f(z)=\displaystyle\sum_{j=0}^{n}p_{j}\frac{z^{j}}{(1-z)^{j+1}}=\frac{\sum_{j}p_{j}z^{j}(1-z)^{n-j}}{(1-z)^{n+1}}$ for $\abs{z}<1$.

::: pf-proof

$\abs{p(k)}$ grows at most like a constant times $k^{n}$, so the series converges for $\abs{z}<1$ and may be rearranged; substituting the finite sum $p(k)=\sum_{j}p_{j}\binom{k}{j}$ and interchanging the two finite/infinite summations gives $f(z)=\sum_{j=0}^{n}p_{j}\sum_{k\ge0}\binom{k}{j}z^{k}$, and step [](#binom){.pf-ref} evaluates the inner sum. Putting the terms over the common denominator $(1-z)^{n+1}$ by multiplying $\frac{z^{j}}{(1-z)^{j+1}}$ by $(1-z)^{n-j}$ gives the displayed quotient of polynomials, which is a rational function.

:::

:::

::: {.pf-step #pole}

If some $p_{j}\ne0$, the rational function has a pole at $z=1$ and no other finite pole, so $f$ has radius of convergence exactly $1$; if all $p_{j}=0$ then $f\equiv0$ and the radius is $\infty$.

::: pf-proof

The only zeros of the denominator $(1-z)^{n+1}$ are at $z=1$. Let $J=\max\{j:p_{j}\ne0\}$; then the numerator is $z^{J}(1-z)^{n-J}\sum_{j\le J}p_{j}z^{j-J}(1-z)^{J-j}$, and the factor in parentheses takes the value $p_{J}\ne0$ at $z=1$, while the other factors are nonzero there. So $z=1$ is a pole of order $n+1-J\ge1$, not a removable singularity. The radius of convergence of a power series equals the distance from the centre to the nearest singularity of the function it defines, here $1$.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle f(z)=\sum_{j=0}^{n}\frac{p_{j}z^{j}}{(1-z)^{j+1}}$ on $\abs{z}<1$, a rational function, with radius of convergence $1$ unless all $p_{j}$ vanish.

::: pf-proof

Steps [](#binom){.pf-ref} and [](#rational){.pf-ref} give the formula and its rationality, and step [](#pole){.pf-ref} fixes the radius of convergence:
$$
\boxed{f(z)=\sum_{j=0}^{n}\frac{p_{j}z^{j}}{(1-z)^{j+1}},\qquad R=1\ \text{unless } p\equiv0,\ \text{when } R=\infty.}
$$

:::

:::

:::

:::
