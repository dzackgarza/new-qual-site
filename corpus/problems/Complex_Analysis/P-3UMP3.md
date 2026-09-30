---
schema: qual/card@1
id: P-3UMP3
kind: problem
title: $c_n\neq 0$ for large $n$ and $c_n/c_{n+1}\to z_0$ for a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a pole at $z_0$ on the unit circle.
Let $\displaystyle f(z) = \sum_{n = 1}^\infty c_n z^n$ denote the the power series in the open disc.
Show that

(1) $c_n \neq 0$ for all large enough $n$'s, and

(2) $\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.
:::

::: {.solution}
**Goal:** Let $f$ be holomorphic in an open neighborhood $U \supset \overline{\mathbb{D}}$ except for a single pole at $z_0 \in \partial \mathbb{D}$ ($|z_0| = 1$). Let $f(z) = \sum_{n=0}^\infty c_n z^n$ be its Taylor expansion in $\mathbb{D}$.
Prove that:

1. $c_n \neq 0$ for all sufficiently large $n$.

2. $\lim_{n \to \infty} \frac{c_n}{c_{n+1}} = z_0$.

* * *

### Step 1: Laurent Decomposition and Principal Part Expansion

::: pf

::: pf-step
**Isolate the pole at $z_0$ of order $k \geq 1$.**

::: pf-proof

::: pf-step
Near $z_0$, the Laurent principal part is: $$P(z) = \sum_{j=1}^k \frac{A_j}{(z - z_0)^j} = \frac{A_k}{(z - z_0)^k} + \frac{A_{k-1}}{(z - z_0)^{k-1}} + \dots + \frac{A_1}{z - z_0},$$ where $A_k \neq 0$ and $k \geq 1$ is the order of the pole.

::: pf-proof
A pole of order $k$ has a Laurent expansion whose principal part is a finite sum of negative powers from $-k$ to $-1$, with the coefficient $A_k$ of the most negative power non-zero.
:::

:::

::: pf-step
Define $g(z) = f(z) - P(z)$.

::: pf-proof
Subtracting the principal part from $f$ removes the singular terms, leaving a function $g$ to be analyzed.
:::

:::

::: pf-step
The singularity of $g$ at $z_0$ is removable, so $g$ is holomorphic on all of $U \supset \overline{\mathbb{D}}$.

::: pf-proof
By construction $g$ has no negative powers in its Laurent expansion at $z_0$, so its singularity is removable by Riemann's removable singularity theorem; hence $g$ extends holomorphically across $z_0$ to all of $U$.
:::

:::

::: pf-step
Thus $g(z) = \sum_{n=0}^\infty d_n z^n$ is a power series with radius of convergence $R_g > 1$.
In particular, there exists $\rho > 1$ such that $|d_n| = O(\rho^{-n})$ as $n \to \infty$.

::: pf-proof
Since $g$ is holomorphic on $U \supset \overline{\mathbb{D}}$, its Taylor series at $0$ converges on a disk of radius $R_g > 1$; the Cauchy–Hadamard formula then gives $|d_n| \le \rho^{-n}$ for some $\rho$ with $1 < \rho < R_g$.
:::

:::

:::

:::

::: {.pf-step #expand-principal-part}
**Expand the principal part $P(z)$ inside $\mathbb{D}$.**

::: pf-proof

::: {.pf-step #principal-part-series-expansion}
For $|z| < |z_0| = 1$, using the binomial series for $(1 - z/z_0)^{-j}$: $$\frac{1}{(z - z_0)^j} = \frac{(-1)^j}{z_0^j \left(1 - \frac{z}{z_0}\right)^j} = \frac{(-1)^j}{z_0^j} \sum_{n=0}^\infty \binom{n+j-1}{j-1} \left(\frac{z}{z_0}\right)^n = \frac{(-1)^j}{z_0^j} \sum_{n=0}^\infty \binom{n+j-1}{j-1} z_0^{-n} z^n.$$

::: pf-proof
Factor $z - z_0 = -z_0(1 - z/z_0)$ and expand $(1 - z/z_0)^{-j}$ by the negative binomial series, valid for $|z/z_0| < 1$.
:::

:::

::: pf-step
The dominant contribution to the $n$-th Taylor coefficient comes from the highest-order term $j = k$: $$\frac{A_k}{(z - z_0)^k} = \frac{(-1)^k A_k}{z_0^k} \sum_{n=0}^\infty \binom{n+k-1}{k-1} z_0^{-n} z^n.$$

::: pf-proof
This is step [](#principal-part-series-expansion){.pf-ref} specialized to $j = k$ and multiplied by $A_k$.
:::

:::

::: pf-step
Note that $\binom{n+k-1}{k-1} = \frac{(n+k-1)\cdots(n+1)}{(k-1)!} = \frac{n^{k-1}}{(k-1)!}\left(1 + O(1/n)\right)$ is a polynomial in $n$ of degree $k-1$.

::: pf-proof
The binomial coefficient $\binom{n+k-1}{k-1}$ is a polynomial in $n$ of degree $k-1$ with leading coefficient $\frac{1}{(k-1)!}$, so it equals $\frac{n^{k-1}}{(k-1)!}(1 + O(1/n))$.
:::

:::

::: pf-step
For any $j < k$, $\binom{n+j-1}{j-1} = O(n^{k-2})$, which is of lower polynomial order as $n \to \infty$.

::: pf-proof
The binomial coefficient $\binom{n+j-1}{j-1}$ is a polynomial in $n$ of degree $j - 1 \le k - 2$, which grows strictly slower than $n^{k-1}$.
:::

:::

:::

:::

:::

* * *

### Step 2: Asymptotics of the Coefficients $c_n$

::: pf

::: pf-step
**Asymptotic formula for $c_n$.**

::: pf-proof

::: pf-step
The total coefficient $c_n$ is the sum of the coefficients from $P(z)$ and $g(z)$: $$c_n = \frac{(-1)^k A_k}{z_0^{n+k}} \binom{n+k-1}{k-1} + \sum_{j=1}^{k-1} \frac{(-1)^j A_j}{z_0^{n+j}} \binom{n+j-1}{j-1} + d_n.$$

::: pf-proof
Since $f(z) = P(z) + g(z)$, the $n$-th Taylor coefficient of $f$ is the sum of the $n$-th coefficients of $P$ (from step [](#expand-principal-part){.pf-ref}) and of $g$ (which is $d_n$).
:::

:::

::: {.pf-step #asymptotic-formula-cn}
Factoring out the dominant term $B_n = \frac{(-1)^k A_k}{z_0^{n+k}} \frac{n^{k-1}}{(k-1)!}$: $$c_n = \frac{(-1)^k A_k}{z_0^{n+k}} \frac{n^{k-1}}{(k-1)!} \left( 1 + O\left(\frac{1}{n}\right) + O\left(n^{-(k-1)} \rho^{-n}\right) \right) = \frac{(-1)^k A_k}{(k-1)! z_0^k} \cdot \frac{n^{k-1}}{z_0^n} \left( 1 + O\left(\frac{1}{n}\right) \right).$$

::: pf-proof
The $j = k$ term dominates: the lower-order terms $j < k$ contribute $O(n^{k-2})$, which is $O(1/n)$ relative to $n^{k-1}$, and the remainder $d_n = O(\rho^{-n})$ with $\rho > 1$ decays exponentially, which is subsumed by $O(1/n)$.
:::

:::

:::

:::

:::

* * *

### Step 3: Proof of (1) and (2)

::: pf

::: pf-step
**Proof of (1): $c_n \neq 0$ for all large enough $n$.**

::: pf-proof

::: pf-step
Let $C = \frac{(-1)^k A_k}{(k-1)! z_0^k} \neq 0$ (since $A_k \neq 0$).

::: pf-proof
$A_k \neq 0$ because the pole is of order $k$, and $z_0 \neq 0$ since $|z_0| = 1$, so $C \neq 0$.
:::

:::

::: pf-step
By step [](#asymptotic-formula-cn){.pf-ref}, $\lim_{n \to \infty} \frac{c_n}{C n^{k-1} z_0^{-n}} = 1$.

::: pf-proof
The asymptotic formula gives $c_n = C n^{k-1} z_0^{-n}(1 + O(1/n))$, and the factor $1 + O(1/n)$ tends to $1$.
:::

:::

::: pf-step
Since the limit is $1 \neq 0$, there exists $N \in \mathbb{N}$ such that for all $n \geq N$, $\left| \frac{c_n}{C n^{k-1} z_0^{-n}} \right| \geq \frac{1}{2} > 0$.

::: pf-proof
By the definition of a limit equal to $1$, taking $\varepsilon = 1/2$ gives an $N$ beyond which the ratio is within $1/2$ of $1$, hence at least $1/2$ in modulus.
:::

:::

::: pf-step
Therefore, $c_n \neq 0$ for all $n \geq N$.

::: pf-proof
If $c_n = 0$ then the ratio would be $0$, contradicting the lower bound $1/2 > 0$; hence $c_n \neq 0$.
:::

:::

:::

:::

::: pf-step
**Proof of (2): $\lim_{n \to \infty} \frac{c_n}{c_{n+1}} = z_0$.**

::: pf-proof

::: pf-step
Using the asymptotic formula from step [](#asymptotic-formula-cn){.pf-ref} for $c_n$ and $c_{n+1}$: $$\frac{c_n}{c_{n+1}} = \frac{C \frac{n^{k-1}}{z_0^n} \left(1 + O(1/n)\right)}{C \frac{(n+1)^{k-1}}{z_0^{n+1}} \left(1 + O(1/(n+1))\right)} = z_0 \cdot \left(\frac{n}{n+1}\right)^{k-1} \cdot \frac{1 + O(1/n)}{1 + O(1/n)}.$$

::: pf-proof
Substituting the asymptotic formulas for $c_n$ and $c_{n+1}$ and cancelling the common constant $C$ and the powers of $z_0$ gives the stated ratio.
:::

:::

::: pf-step
Since $\lim_{n \to \infty} \left(\frac{n}{n+1}\right)^{k-1} = 1^{k-1} = 1$, and $\lim_{n \to \infty} \frac{1 + O(1/n)}{1 + O(1/n)} = 1$: $$\lim_{n \to \infty} \frac{c_n}{c_{n+1}} = z_0 \cdot 1 \cdot 1 = z_0.$$

::: pf-proof
The limit of a product is the product of the limits; each factor tends to $1$, so the product tends to $z_0$.
:::

:::

:::

:::

:::

:::
