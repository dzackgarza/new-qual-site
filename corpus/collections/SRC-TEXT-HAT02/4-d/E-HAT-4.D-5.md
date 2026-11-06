---
schema: qual/card@1
id: E-HAT-4.D-5
kind: problem
title: Gysin sequence and Hopf invariant of sphere bundles
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Use the Gysin sequence to show that for a fiber bundle $S^k \to S^m \xrightarrow{p} S^n$ we must have $k = n-1$ and $m = 2n-1$.
Then use the Thom isomorphism to show that the Hopf invariant of $p$ must be $\pm 1$.
[Hence $n = 1, 2, 4, 8$ by Adams' theorem.]
:::

::: {.solution}
Suppose $n>1$. The fiber cannot be $S^0$, since a two-sheeted covering of the simply connected base $S^n$ has disconnected total space. Thus $k>0$. Local triviality gives $m=n+k$, so $m>k+1$ and $m>n$. The sphere bundle is orientable because $S^n$ is simply connected.

Let $e\in H^{k+1}(S^n;\ZZ)$ be its Euler class. The Gysin sequence (p. 438) contains
$$
H^k(S^m)\longrightarrow H^0(S^n)
\xrightarrow{\smile e}H^{k+1}(S^n)
\xrightarrow{p^*}H^{k+1}(S^m).
$$
The outer groups vanish, so cup product with $e$ is an isomorphism. Hence $H^{k+1}(S^n)\cong\ZZ$, which forces $k+1=n$, and $e$ is a generator up to sign. Therefore $k=n-1$ and $m=2n-1$.

Cone each sphere fiber to form an oriented $D^n$-bundle $V$ over $S^n$ whose boundary is the given sphere bundle; being orientable, it has a Thom class with $\ZZ$ coefficients (Theorem 4D.10, p. 442, in the direction orientable $\Rightarrow$ integral Thom class, which is the direction used here; the converse is Exercise 7 of this section). Its Thom space $V/S(V)$ is homotopy equivalent to the mapping cone $C_p$, since $V$ retracts onto its zero section $S^n$, so the Thom class becomes a class
$$
U\in H^n(C_p;\ZZ).
$$
By the Thom isomorphism of Corollary 4D.9 (p. 441), $\Phi\colon H^i(S^n;\ZZ)\to H^{i+n}(V,S(V);\ZZ)$ is an isomorphism with $\Phi(b)=p^*(b)\smile U$, and $\Phi(1)=p^*(1)\smile U=U$; hence $U$ *generates* $H^n(C_p;\ZZ)\cong\ZZ$, which is what the definition of the Hopf invariant requires. The Euler class $e\in H^n(S^n;\ZZ)$ is a generator, and the identity at the end of §4.D (p. 444) says that $\Phi(e)$ is the class corresponding to $c\smile c$ under the Thom isomorphism, that is,
$$
\Phi(e)=U\smile U.
$$
Since $\Phi$ is an isomorphism and $e$ generates, $U^2$ generates $H^{2n}(C_p;\ZZ)$. By the definition of the Hopf invariant (p. 427), which writes the square of a generator $\alpha$ of $H^n(C_p;\ZZ)$ as $\alpha^2=H(p)\beta$ with $\beta$ a generator of $H^{2n}(C_p;\ZZ)$, taking $\alpha=U$ gives $H(p)=\pm1$.

For $n=1$, a connected fiber would make $\pi_1(S^m)\to\pi_1(S^1)$ surjective, while $m=1+k>1$ makes its source zero. Thus $k=0$ and $m=1$. The Hopf-invariant assertion concerns $n>1$.
:::
