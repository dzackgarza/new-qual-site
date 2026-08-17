---
schema: qual/card@1
id: P-JP74P
kind: problem
title: "Let $f: \\RR \\to \\CC$ be continuous with period 1."
classification:
  areas:
  - real-analysis
  topics:
  - density
  - integrals
  - fourier-analysis
relations: []
review: draft
solved: true
---

::: problem
Let $f: \RR \to \CC$ be continuous with period 1. Prove that
\[
\lim _{N \rightarrow \infty} \frac{1}{N} \sum_{n=1}^{N} f(n \alpha)=\int_{0}^{1} f(t) d t \quad \forall \alpha \in \RR\setminus\QQ.
\]

> Hint: show this first for the functions $f(t) = e^{2\pi i k t}$ for $k\in \ZZ$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. It suffices to prove the claim for $f(t) = e^{2\pi i k t}$, $k \in \ZZ$, and then extend by linearity and density.
Proof: the exponentials are dense in $C(\RR/\ZZ)$ (Weierstrass/Fejér: trigonometric polynomials are uniformly dense in the continuous $1$-periodic functions); linearity handles finite linear combinations; an $\eps/3$ argument passes the limit.

<1>2. For $f(t) = e^{2\pi i k t}$ with $k = 0$: $\frac{1}{N}\sum_{n=1}^N 1 = 1 = \int_0^1 1\,dt$.
Proof: direct.

<1>3. For $f(t) = e^{2\pi i k t}$ with $k \neq 0$: $\frac{1}{N}\sum_{n=1}^N e^{2\pi i k n \alpha} \to 0 = \int_0^1 e^{2\pi i k t}\,dt$.
Proof: the sum is a geometric series: $\sum_{n=1}^N e^{2\pi i k n\alpha} = e^{2\pi i k\alpha}\frac{e^{2\pi i k N\alpha} - 1}{e^{2\pi i k\alpha} - 1}$, whose modulus is $\le \frac{2}{|e^{2\pi i k\alpha} - 1|}$, independent of $N$; dividing by $N$ and letting $N \to \infty$ gives $0$.
The denominator is nonzero because $\alpha \in \RR\setminus\QQ$ and $k \neq 0$ imply $k\alpha \notin \ZZ$, so $e^{2\pi i k\alpha} \neq 1$.

<1>4. Q.E.D. for trigonometric polynomials and then all of $C(\RR/\ZZ)$ by density.
Proof: <1>2 and <1>3 give the limit for each exponential; finite linear combinations follow by linearity of the averages and the integral; uniform approximation of continuous $f$ by trigonometric polynomials (Fejér's theorem) plus the $\eps/3$ trick gives the full claim.
(This is Weyl's equidistribution criterion for the Kronecker sequence $n\alpha$.)
:::
