---
schema: qual/card@1
id: T-IJW1K
kind: theorem
title: The cohomology of $\OO_{\PP^n}(d)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Twisting Sheaves
  - Serre Duality
relations:
- kind: uses
  target: D-CB9XS
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- Compute $H^*(\PP^n, \OO(d))$.
- What is $H^0(\PP^1, \Omega^1)$?
- Compute the Čech cohomology of $\OO(d)$ on $\PP^n_A$ monomial by monomial.
---

::: {.theorem}
Let $A$ be a ring, $S = A[x_0,\ldots,x_n]$ and $\PP^n = \PP^n_A$.
Then

- $H^0(\PP^n, \OO(d)) = S_d$, a free $A$-module of rank $\binom{n+d}{n}$ for $d \geq 0$, and $0$ for $d < 0$;

- $H^n(\PP^n, \OO(d))$ is the free $A$-module on the monomials $x_0^{a_0} \cdots x_n^{a_n}$ with every $a_i \leq -1$ and $\sum_i a_i = d$, of rank $\binom{-d-1}{n}$, nonzero exactly for $d \leq -n-1$, and dual to $S_{-d-n-1}$;

- $H^p(\PP^n, \OO(d)) = 0$ for $0 < p < n$ and for $p > n$, for every $d$.
:::

<1>1. Let $U_i = D_+(x_i)$, and for nonempty $I \subseteq \{0, \ldots, n\}$ put $x_I = \prod_{i \in I} x_i$ and $U_I = \bigcap_{i \in I} U_i$. Then $\bigoplus_{d \in \ZZ} \Gamma(U_I, \OO(d)) = S_{x_I}$, and the Čech complex of $\mathcal{G} = \bigoplus_d \OO(d)$ for the affine cover $\{U_i\}$, augmented by $S$ in degree $-1$, is
$$0 \to S \to \prod_{|I| = 1} S_{x_I} \to \prod_{|I| = 2} S_{x_I} \to \cdots \to S_{x_0 \cdots x_n} \to 0 ,$$
whose cohomology in degrees $p \geq 1$ is $\bigoplus_d H^p(\PP^n, \OO(d))$.

::: {.proof}
$U_I = \Spec (S_{x_I})_0$ and $\OO(d)|_{U_I}$ corresponds to $(S_{x_I})_d$. The cover is affine and $\PP^n_A$ is separated, so Čech cohomology of the quasicoherent sheaf $\mathcal{G}$ computes $H^p$ ([[D-PTIW0]]); it vanishes for $p > n$ because the cover has $n+1$ members. The degree-$d$ part of the complex is the Čech complex of $\OO(d)$.
:::

<1>2. The complex is the direct sum, over $a = (a_0, \ldots, a_n) \in \ZZ^{n+1}$, of the subcomplexes $K(a)$ spanned by the monomial $x^a = x_0^{a_0} \cdots x_n^{a_n}$. Writing $N = \{ i : a_i < 0 \}$, $K(a)$ has in degree $p$ the free module on the subsets $I \supseteq N$ with $\abs{I} = p+1$, the case $I = \emptyset$, $p = -1$, occurring exactly when $N = \emptyset$.

::: {.proof}
$S_{x_I}$ is the free $A$-module on the Laurent monomials $x^a$ with $a_i \geq 0$ for $i \notin I$, that is, with $N \subseteq I$, and the Čech differentials, being signed sums of localization maps, send $x^a$ to signed sums of $x^a$.
:::

<1>3. $K(a)$ is exact if $N \neq \{0, \ldots, n\}$, and $K(a) = A$ concentrated in degree $n$ if $N = \{0, \ldots, n\}$.

::: {.proof}
Put $M = \{0, \ldots, n\} \setminus N$. The subsets $I \supseteq N$ are the sets $N \cup J$ with $J \subseteq M$, and with the Čech signs $K(a)$ is isomorphic, up to a shift of degree by $\abs{N}$, to the tensor product over $j \in M$ of the complexes $0 \to A \xrightarrow{\id} A \to 0$.
If $M \neq \emptyset$ this is a tensor product with a contractible complex of free modules, hence contractible and exact; this covers both the case $N = \emptyset$, in which all $a_i \geq 0$, and the mixed case.
If $M = \emptyset$, every $a_i$ is negative, and $K(a)$ is the single module $A \cdot x^a$ in degree $\abs{N} - 1 = n$.
:::

<1>4. Q.E.D.

::: {.proof}
By steps <1>2 and <1>3, the augmented complex has cohomology only in degree $n$, where it is free on the $x^a$ with all $a_i < 0$.
Exactness in degrees $-1$ and $0$ says that $S \to \prod_i S_{x_i}$ is injective with image the kernel of the next map, so $H^0 = S$ and $H^0(\PP^n, \OO(d)) = S_d$; exactness in degrees $0 < p < n$ gives $H^p = 0$.
In degree $d$, the monomials with all $a_i \leq -1$ correspond, by $b_i = -a_i - 1 \geq 0$, to monomials of degree $-d-n-1$ in $n+1$ variables, so the rank is $\binom{-d-1}{n}$, and the pairing $x^a \otimes x^b \mapsto$ coefficient of $x_0^{-1} \cdots x_n^{-1}$ in $x^a x^b$ identifies $H^n(\PP^n, \OO(d))$ with the dual of $S_{-d-n-1}$.
:::

::: {.remark}
This one computation carries the subject.
The top and bottom are exchanged by Serre duality with dualizing sheaf $\omega = \OO(-n-1)$, which is why the answer is stated as a dual rather than as another binomial.

Three corollaries used constantly:

- $H^1(\PP^n, \OO(d)) = 0$ for $n \geq 2$, so the only interesting $H^1$ on projective space is for curves;

- on $\PP^1$: $h^0(\OO(d)) = d+1$ and $h^1(\OO(d)) = h^0(\OO(-d-2))$, so $h^1(\OO(-2)) = 1$;

- $H^0(\PP^1, \Omega^1) = H^0(\PP^1, \OO(-2)) = 0$: the projective line has no global holomorphic differentials, which is the genus of $\PP^1$ being zero.
:::
