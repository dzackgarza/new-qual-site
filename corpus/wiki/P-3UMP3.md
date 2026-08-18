---
schema: qual/card@1
id: P-3UMP3
kind: problem
title: $c_n\neq 0$ for large $n$ and $c_n/c_{n+1}\to z_0$ for a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - power-series
  - poles
  - convergence-tests
relations: []
review: draft
solved: true
---

::: problem
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a pole at $z_0$ on the unit circle.
Let $\displaystyle f(z) = \sum_{n = 1}^\infty c_n z^n$ denote the the power series in the open disc.
Show that

(1) $c_n \neq 0$ for all large enough $n$'s, and

(2) $\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f$ be holomorphic in an open neighborhood $U \supset \overline{\mathbb{D}}$ except for a single pole at $z_0 \in \partial \mathbb{D}$ ($|z_0| = 1$). Let $f(z) = \sum_{n=0}^\infty c_n z^n$ be its Taylor expansion in $\mathbb{D}$.
Prove that:

1. $c_n \neq 0$ for all sufficiently large $n$.

2. $\lim_{n \to \infty} \frac{c_n}{c_{n+1}} = z_0$.

* * *

### Step 1: Laurent Decomposition and Principal Part Expansion

<1>1. **Isolate the pole at $z_0$ of order $k \geq 1$.** <2>1. Near $z_0$, the Laurent principal part is: $$P(z) = \sum_{j=1}^k \frac{A_j}{(z - z_0)^j} = \frac{A_k}{(z - z_0)^k} + \frac{A_{k-1}}{(z - z_0)^{k-1}} + \dots + \frac{A_1}{z - z_0},$$ where $A_k \neq 0$ and $k \geq 1$ is the order of the pole.
*Proof:* Definition of pole of order $k$.
<2>2. Define $g(z) = f(z) - P(z)$.
*Proof:* Algebraic definition.
<2>3. The singularity of $g$ at $z_0$ is removable, so $g$ is holomorphic on all of $U \supset \overline{\mathbb{D}}$.
*Proof:* Riemann's removable singularity theorem.
<2>4. Thus $g(z) = \sum_{n=0}^\infty d_n z^n$ is a power series with radius of convergence $R_g > 1$.
In particular, there exists $\rho > 1$ such that $|d_n| = O(\rho^{-n})$ as $n \to \infty$.
*Proof:* The radius of convergence of a power series extends to the nearest singularity, which lies outside $\overline{\mathbb{D}}$.
<2>5. Q.E.D.

<1>2. **Expand the principal part $P(z)$ inside $\mathbb{D}$.** <2>1. For $|z| < |z_0| = 1$, using the binomial series for $(1 - z/z_0)^{-j}$: $$\frac{1}{(z - z_0)^j} = \frac{(-1)^j}{z_0^j \left(1 - \frac{z}{z_0}\right)^j} = \frac{(-1)^j}{z_0^j} \sum_{n=0}^\infty \binom{n+j-1}{j-1} \left(\frac{z}{z_0}\right)^n = \frac{(-1)^j}{z_0^j} \sum_{n=0}^\infty \binom{n+j-1}{j-1} z_0^{-n} z^n.$$ *Proof:* Standard negative binomial series expansion for $|z/z_0| < 1$.
<2>2. The dominant contribution to the $n$-th Taylor coefficient comes from the highest-order term $j = k$: $$\frac{A_k}{(z - z_0)^k} = \frac{(-1)^k A_k}{z_0^k} \sum_{n=0}^\infty \binom{n+k-1}{k-1} z_0^{-n} z^n.$$ *Proof:* Applying <2>1 for $j = k$.
<2>3. Note that $\binom{n+k-1}{k-1} = \frac{(n+k-1)\cdots(n+1)}{(k-1)!} = \frac{n^{k-1}}{(k-1)!}\left(1 + O(1/n)\right)$ is a polynomial in $n$ of degree $k-1$.
*Proof:* Polynomial expansion of binomial coefficient.
<2>4. For any $j < k$, $\binom{n+j-1}{j-1} = O(n^{k-2})$, which is of lower polynomial order as $n \to \infty$.
*Proof:* Degree of polynomial is $j-1 \leq k-2$.
<2>5. Q.E.D.

* * *

### Step 2: Asymptotics of the Coefficients $c_n$

<1>3. **Asymptotic formula for $c_n$.** <2>1. The total coefficient $c_n$ is the sum of the coefficients from $P(z)$ and $g(z)$: $$c_n = \frac{(-1)^k A_k}{z_0^{n+k}} \binom{n+k-1}{k-1} + \sum_{j=1}^{k-1} \frac{(-1)^j A_j}{z_0^{n+j}} \binom{n+j-1}{j-1} + d_n.$$ *Proof:* Sum of series expansions for $f(z) = P(z) + g(z)$.
<2>2. Factoring out the dominant term $B_n = \frac{(-1)^k A_k}{z_0^{n+k}} \frac{n^{k-1}}{(k-1)!}$: $$c_n = \frac{(-1)^k A_k}{z_0^{n+k}} \frac{n^{k-1}}{(k-1)!} \left( 1 + O\left(\frac{1}{n}\right) + O\left(n^{-(k-1)} \rho^{-n}\right) \right) = \frac{(-1)^k A_k}{(k-1)! z_0^k} \cdot \frac{n^{k-1}}{z_0^n} \left( 1 + O\left(\frac{1}{n}\right) \right).$$ *Proof:* Since $\rho > 1$, the remainder $d_n = O(\rho^{-n})$ decays exponentially, which is subsumed by $O(1/n)$.
<2>3. Q.E.D.

* * *

### Step 3: Proof of (1) and (2)

<1>4. **Proof of (1): $c_n \neq 0$ for all large enough $n$.** <2>1. Let $C = \frac{(-1)^k A_k}{(k-1)! z_0^k} \neq 0$ (since $A_k \neq 0$). *Proof:* $A_k \neq 0$ because the pole is of order $k$.
<2>2. By <1>3.<2>2, $\lim_{n \to \infty} \frac{c_n}{C n^{k-1} z_0^{-n}} = 1$.
*Proof:* The factor $1 + O(1/n)$ tends to $1$.
<2>3. Since the limit is $1 \neq 0$, there exists $N \in \mathbb{N}$ such that for all $n \geq N$, $\left| \frac{c_n}{C n^{k-1} z_0^{-n}} \right| \geq \frac{1}{2} > 0$.
*Proof:* Definition of limit with $\varepsilon = 1/2$.
<2>4. Therefore, $c_n \neq 0$ for all $n \geq N$.
*Proof:* Non-zero modulus implies non-zero number.
<2>5. Q.E.D.

<1>5. **Proof of (2): $\lim_{n \to \infty} \frac{c_n}{c_{n+1}} = z_0$.** <2>1. Using the asymptotic formula from <1>3.<2>2 for $c_n$ and $c_{n+1}$: $$\frac{c_n}{c_{n+1}} = \frac{C \frac{n^{k-1}}{z_0^n} \left(1 + O(1/n)\right)}{C \frac{(n+1)^{k-1}}{z_0^{n+1}} \left(1 + O(1/(n+1))\right)} = z_0 \cdot \left(\frac{n}{n+1}\right)^{k-1} \cdot \frac{1 + O(1/n)}{1 + O(1/n)}.$$ *Proof:* Direct ratio and cancellation of constants.
<2>2. Since $\lim_{n \to \infty} \left(\frac{n}{n+1}\right)^{k-1} = 1^{k-1} = 1$, and $\lim_{n \to \infty} \frac{1 + O(1/n)}{1 + O(1/n)} = 1$: $$\lim_{n \to \infty} \frac{c_n}{c_{n+1}} = z_0 \cdot 1 \cdot 1 = z_0.$$ *Proof:* Product of limits.
<2>3. Q.E.D.
:::
