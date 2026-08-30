---
schema: qual/card@1
id: P-MMAQ-N34EA7FB6T
kind: problem
title: Inverse images of primes are prime, the nilradical is contained in every prime,
  and $\mathrm{Spec}(R/N)\to\mathrm{Spec}(R)$ is bijective
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $R$ and $S$ be commutative rings, and $f:R\rightarrow S$ a ring homomorphism.

- Show that if $I$ is a prime ideal of $S$, then `\begin{align*} f\inv(I)=\{r\in R:f(r)\in I\} \end{align*}`{=tex}

  is a prime ideal of $R$.

- Let $N$ be the set of nilpotent elements of $R$: `\begin{align*} N=\{r\in R:r^m=0\text{ for some }m\geq 1\}. .\end{align*}`{=tex}

  $N$ is called the `\textit{nilradical}`{=tex} of $R$.
  Prove that it is an ideal which is contained in every prime ideal.

- Part (a) lets us define a function `\begin{align*} f^*:\{\text{prime ideals of }S\} &\rightarrow \{\text{prime ideals of }R\}. I &\mapsto f\inv(I). .\end{align*}`{=tex}

  Let $N$ be the nilradical of $R$.
  Show that if $S=R/N$ and $f:R\rightarrow R/N$ is the quotient map, then $f^*$ is a bijection
:::

::: {.solution}
<1>1. Part (a): Proof that $f^{-1}(I)$ is a prime ideal of $R$:
<2>1. Let $I \subset S$ be a prime ideal.
Consider the composite homomorphism $\pi \circ f: R \xrightarrow{f} S \xrightarrow{\pi} S/I$, where $\pi$ is the canonical projection.
Proof: composition of ring homomorphisms.
<2>2. The kernel of $\pi \circ f$ is:
\[
\ker(\pi \circ f) = \{r \in R \mid f(r) \in I\} = f^{-1}(I).
\]
By the First Isomorphism Theorem for rings, $R / f^{-1}(I) \cong \operatorname{Im}(\pi \circ f) \subseteq S/I$.
Proof: First Isomorphism Theorem.
<2>3. Because $I$ is a prime ideal in the commutative ring $S$, the quotient $S/I$ is an integral domain.
Any subring of an integral domain is an integral domain, so $R / f^{-1}(I)$ is an integral domain.
Therefore $f^{-1}(I)$ is a prime ideal of $R$.
Proof: characterization of prime ideals via quotient rings being integral domains.

<1>2. Part (b): Proof that the nilradical $N$ is an ideal contained in every prime ideal:
<2>1. $0 \in N$ since $0^1 = 0$.
If $x \in N$ with $x^m = 0$ and $r \in R$, then $(rx)^m = r^m x^m = r^m \cdot 0 = 0$ (using commutativity of $R$), so $rx \in N$.
Proof: commutativity of $R$.
<2>2. If $x, y \in N$ with $x^m = 0$ and $y^n = 0$, consider $(x + y)^{m + n - 1}$.
By the binomial theorem in a commutative ring:
\[
(x + y)^{m + n - 1} = \sum_{k=0}^{m + n - 1} \binom{m + n - 1}{k} x^k y^{m + n - 1 - k}.
\]
For each term, either $k \ge m$ (so $x^k = 0$) or $(m + n - 1 - k) \ge n$ (so $y^{m+n-1-k} = 0$).
Thus $(x + y)^{m + n - 1} = 0$, so $x + y \in N$.
Therefore $N$ is an ideal of $R$.
Proof: binomial theorem.
<2>3. Let $\mathfrak{p} \subset R$ be any prime ideal, and let $x \in N$ with $x^m = 0$.
Since $0 \in \mathfrak{p}$, we have $x^m \in \mathfrak{p}$.
By primality of $\mathfrak{p}$, $x^m \in \mathfrak{p} \implies x \in \mathfrak{p}$.
Thus $N \subseteq \mathfrak{p}$ for every prime ideal $\mathfrak{p}$.
Proof: primality of $\mathfrak{p}$.

<1>3. Part (c): Proof that $f^*: \operatorname{Spec}(R/N) \to \operatorname{Spec}(R)$ is a bijection:
<2>1. By the Correspondence Theorem for rings, the quotient map $f: R \to R/N$ induces an inclusion-preserving bijection between ideals of $R/N$ and ideals of $R$ containing $\ker(f) = N$:
\[
J \mapsto f^{-1}(J), \qquad \mathfrak{a} \mapsto f(\mathfrak{a}) = \mathfrak{a}/N.
\]
Proof: Correspondence Theorem for ideals.
<2>2. By Part (a), if $J$ is a prime ideal of $R/N$, then $f^{-1}(J)$ is a prime ideal of $R$.
Proof: Part (a).
<2>3. By Part (b), every prime ideal $\mathfrak{p} \in \operatorname{Spec}(R)$ contains $N = \ker(f)$.
For any such prime $\mathfrak{p}$, the quotient isomorphism:
\[
(R/N) / (\mathfrak{p}/N) \cong R/\mathfrak{p}
\]
shows that $\mathfrak{p}/N$ is a prime ideal of $R/N$ because $R/\mathfrak{p}$ is an integral domain.
Proof: Third Isomorphism Theorem for rings.
<2>4. The inverse map is $\mathfrak{p} \mapsto \mathfrak{p}/N$, with $f^{-1}(\mathfrak{p}/N) = \mathfrak{p}$ and $f(f^{-1}(J)) = J$.
Thus $f^*$ is a bijection between $\operatorname{Spec}(R/N)$ and $\operatorname{Spec}(R)$.
Proof: two-sided inverse.

<1>4. Conclusion:
Parts (a), (b), and (c) are fully proved. Q.E.D.
Proof: <1>1 through <1>3.
:::
