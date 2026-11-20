---
schema: qual/card@1
id: P-AMD-5TW33AUF
kind: problem
title: Topological degree of a polynomial on the Riemann sphere
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The statement matches Problem 10 under the heading Degree on printed page 263 of
    `assets/attachments/UCSD_290_F14_sheet8.pdf`: a polynomial of algebraic degree $n$, viewed as a
    continuous self-map of the Riemann sphere sending infinity to infinity, asked for its topological
    degree. The card states the answer as the value to determine and adds the constant case $n = 0$,
    which the printed question leaves inside the same question. The collection's provenance is the
    twelve UCSD Math 290 Fall 2014 problem sheets, which carry problems only, so no retained published
    solution covers this card and the argument on it is the card's own.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Sixteen steps in the proof asserted their claim with no justification; each now carries a pf-proof
    deriving it. The constant case closes the chain through the vanishing of $H_2$ of a punctured
    sphere: a non-surjective self-map misses a point $q$, factors through $S^2 \setminus \{q\} \cong
    \RR^2$, and so induces zero on $H_2$. The positive-degree case keeps its route through the
    straight-line homotopy to $a_n z^n$, the polar-coordinate homotopy to $z^n$, and the local-degree
    count at the regular value $1$; the new sentences supply the uniform estimate at infinity that makes
    the straight-line homotopy continuous on $\widehat{\CC} \times [0, 1]$, the convexity that keeps
    $\abs{(1-t)r + t}$ away from zero, and the vanishing of $f_n'$ nowhere on $f_n^{-1}(1)$. Two changes
    beyond the insertions: step s4-1 no longer asserts that $w_0 = 1$ is a regular value before the
    derivative is computed, and the step that only said the local-degree count already proves the result
    is gone, since STYLE-08 admits no step that merely back-references. The statement is unchanged. Not
    checked: no published solution to this sheet exists in the repository, so the argument was verified
    here rather than against a second source.
---

::: {.problem}
Let $p(z) = \sum_{j=0}^n a_j z^j$ be a polynomial of degree $n \ge 1$ with $a_n \neq 0$. Extend $p$ to a continuous self-map of the Riemann sphere $\widehat{\CC} = \CC \cup \{\infty\} \cong S^2$ by setting $p(\infty) = \infty$. Determine the topological degree $\deg(p)$.
:::

::: {.solution}
Let $p(z) = \sum_{j=0}^n a_j z^j$ be a polynomial with complex coefficients and $a_n \neq 0$.
For $n \ge 1$, extend $p$ to the Riemann sphere $\widehat{\CC} = \CC \cup \{\infty\} \cong S^2$ by $p(\infty) = \infty$; for $n = 0$, $p \equiv a_0$ is constant on $\widehat{\CC}$.

::: pf

::: {.pf-step #s1}
Case $n = 0$ (constant polynomial $p(z) = a_0$). Then $\deg(p) = 0$.

::: pf-proof

::: pf-step
If $p$ is constant, its image is the single point $\{a_0\}$.

::: pf-proof
A constant map sends every point of $\CC$ to $a_0$, and a constant polynomial is extended to the sphere by $p(\infty) = a_0$, so the image of $p \colon \widehat{\CC} \to \widehat{\CC}$ is the single point $a_0$.
:::

:::

::: pf-step
A non-surjective map $g \colon S^2 \to S^2$ factors through $S^2 \setminus \{q\} \simeq \RR^2$ for some $q \notin g(S^2)$.

::: pf-proof
Since $g$ is not surjective there is a point $q$ of $S^2$ outside $g(S^2)$. The map $g$ then takes its values in $S^2 \setminus \{q\}$, so it is the composite of $g' \colon S^2 \to S^2 \setminus \{q\}$, $g'(x) = g(x)$, with the inclusion $\iota \colon S^2 \setminus \{q\} \to S^2$; and stereographic projection from $q$ is a homeomorphism $S^2 \setminus \{q\} \to \RR^2$.
:::

:::

::: {.pf-step #zero-induced}
Since $\RR^2$ is contractible, $H_2(\RR^2) = 0$, so the induced map $g_* \colon H_2(S^2) \to H_2(S^2)$ factors through the zero group and is the zero homomorphism.

::: pf-proof
On homology $g_* = \iota_* \circ (g')_*$, where $(g')_*$ maps $H_2(S^2)$ into $H_2(S^2 \setminus \{q\})$. The complement $S^2 \setminus \{q\}$ is homeomorphic to the contractible space $\RR^2$, so its second homology group is zero and $(g')_* = 0$; hence $g_* = 0$.
:::

:::

::: pf-step
Hence $\deg(g) = 0$.

::: pf-proof
The degree of a self-map of $S^2$ is the integer by which its induced endomorphism of $H_2(S^2) \cong \ZZ$ multiplies a fundamental class, and that endomorphism is the zero map by step [](#zero-induced){.pf-ref}; hence $\deg(g) = 0$.
:::

:::

:::

:::

::: {.pf-step #s2}
Case $n \ge 1$ with $a_n \neq 0$. Then $\deg(p) = n$.

::: pf-proof

::: {.pf-step #extension-continuous}
The extension to $\widehat{\CC}$ is continuous: Since $a_n \neq 0$ and $n \ge 1$, $\lim_{\abs{z} \to \infty} \abs{p(z)} = \lim_{\abs{z} \to \infty} \abs{a_n z^n} \abs{1 + \sum_{j=0}^{n-1} \frac{a_j}{a_n z^{n-j}}} = \infty$, so setting $p(\infty) = \infty$ makes $p \colon \widehat{\CC} \to \widehat{\CC}$ continuous.

::: pf-proof
Only continuity at $\infty$ needs an argument, since a polynomial is continuous on $\CC$. As $\abs{z} \to \infty$ the factor $1 + \sum_{j=0}^{n-1} \frac{a_j}{a_n} z^{j-n}$ tends to $1$ while $\abs{a_n z^n} \to \infty$, so $\abs{p(z)} \to \infty$; that is, for every bound $M$ the set where $\abs{p(z)} \le M$ is bounded, so the preimage of every neighbourhood of $\infty = p(\infty)$ is a neighbourhood of $\infty$.
:::

:::

::: pf-step
Construct a homotopy to $q(z) = a_n z^n$: Define $H \colon \widehat{\CC} \times [0, 1] \to \widehat{\CC}$ by $$H(z, t) = a_n z^n + (1-t)\sum_{j=0}^{n-1} a_j z^j \quad \text{for } z \in \CC, \qquad H(\infty, t) = \infty.$$

::: pf-proof
The formula defines a function on $\widehat{\CC} \times [0,1]$: on $\CC \times [0,1]$ it is a polynomial in $z$ whose coefficients depend on $t$, and at $\infty$ the value is declared to be $\infty$. At $t = 0$ it reads $a_n z^n + \sum_{j=0}^{n-1} a_j z^j = p(z)$, and at $t = 1$ it reads $a_n z^n$.
:::

:::

::: pf-step
For each $t \in [0, 1]$, $H(z, t)$ is a polynomial of degree $n$ with leading coefficient $a_n \neq 0$, so $\lim_{\abs{z} \to \infty} \abs{H(z, t)} = \infty$ uniformly for $t$. Thus $H$ is a continuous homotopy of maps $\widehat{\CC} \to \widehat{\CC}$.

::: pf-proof
Each $H(\cdot, t)$ is a polynomial of degree $n$ with leading coefficient $a_n$, so it extends continuously to $\widehat{\CC}$ by step [](#extension-continuous){.pf-ref}. On $\CC \times [0,1]$ the map $H$ is continuous in $(z,t)$ because the coefficients $(1-t)a_j$ depend continuously on $t$. At infinity, $\abs{H(z,t)} \ge \abs{a_n}\abs{z}^n - \sum_{j=0}^{n-1} \abs{a_j}\abs{z}^j \ge \frac{1}{2}\abs{a_n}\abs{z}^n$ for every $\abs{z} \ge R$, where $R$ is chosen so that $\sum_{j=0}^{n-1} \abs{a_j} R^{j-n} \le \frac{1}{2}\abs{a_n}$; the bound $R$ does not depend on $t$, so $H(z,t) \to \infty$ as $z \to \infty$ uniformly in $t$ and $H$ is continuous on $\widehat{\CC} \times [0,1]$.
:::

:::

::: {.pf-step #degree-invariant}
The degree of a map $S^2 \to S^2$ is determined by its induced map on $H_2(S^2) \cong \ZZ$. Since homotopic maps induce the same homomorphism on homology, $\deg(p) = \deg(z \mapsto a_n z^n)$.

::: pf-proof
Homotopic maps induce the same homomorphism on homology, since the prism operator built from $H$ gives $(H(\cdot,0))_* = (H(\cdot,1))_*$ on $H_2$. The degree is the multiplier of $H_2(\widehat{\CC}) \cong \ZZ$, so the two multipliers agree: $\deg(p) = \deg(z \mapsto a_n z^n)$.
:::

:::

:::

:::

::: {.pf-step #s3}
Homotopy to the standard monomial $z \mapsto z^n$.

::: pf-proof

::: pf-step
Write $a_n = r e^{i\theta}$ with $r > 0$ and $\theta \in \RR$.

::: pf-proof
Every nonzero complex number has a polar form $re^{i\theta}$ with $r = \abs{a_n} > 0$ real and $\theta \in \RR$ an argument of $a_n$; and $a_n \neq 0$ by hypothesis.
:::

:::

::: pf-step
Define $K \colon \widehat{\CC} \times [0, 1] \to \widehat{\CC}$ by $K(z, t) = ((1-t)r + t) e^{i(1-t)\theta} z^n$ for $z \in \CC$ and $K(\infty, t) = \infty$.

::: pf-proof
For fixed $t$ the number $c(t) = ((1-t)r + t)e^{i(1-t)\theta}$ is complex, so $K(\cdot, t)$ is the monomial $z \mapsto c(t)z^n$, and $K(\infty, t) = \infty$ is declared. The coefficient $c(t)$ is continuous in $t$.
:::

:::

::: pf-step
Since $(1-t)r + t > 0$ for all $t \in [0, 1]$, the leading coefficient is non-zero for all $t$, so each $K(\cdot, t)$ is a polynomial of degree $n$ extending continuously to $\widehat{\CC}$.

::: pf-proof
The real number $(1-t)r + t$ is a convex combination of $r > 0$ and $1$, so it lies in $[\min(r,1), \max(r,1)]$ and is positive; hence $\abs{c(t)} = (1-t)r + t \neq 0$, the map $K(\cdot,t)$ is a polynomial of degree $n$, and it extends continuously to $\widehat{\CC}$ by step [](#extension-continuous){.pf-ref}.
:::

:::

::: {.pf-step #endpoints}
Moreover $K(z, 0) = r e^{i\theta} z^n = a_n z^n$ and $K(z, 1) = z^n$, so $K$ is a homotopy from $z \mapsto a_n z^n$ to $f_n(z) = z^n$.

::: pf-proof
At $t = 0$ the coefficient is $re^{i\theta} = a_n$, so $K(z, 0) = a_n z^n$; at $t = 1$ it is $1 \cdot e^{0} = 1$, so $K(z, 1) = z^n$; and $K(\infty, t) = \infty$ at both ends.
:::

:::

::: pf-step
Homotopic maps have the same degree, so $\deg(z \mapsto a_n z^n) = \deg(f_n)$.

::: pf-proof
The map $K$ is a homotopy of self-maps of $\widehat{\CC}$ from $z \mapsto a_n z^n$ to $f_n$, by step [](#endpoints){.pf-ref}, and homotopic maps have equal degree by step [](#degree-invariant){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s4}
Compute the degree of $f_n(z) = z^n$ on $\widehat{\CC} \cong S^2$.

::: pf-proof

::: {.pf-step #s4-1}
Method 1 (Local degree / Regular values): the value $w_0 = 1 \in \CC \setminus \{0\}$ is not $\infty$, and the preimage $f_n^{-1}(1) = \{\zeta_k = e^{2\pi i k / n} \mid k = 0, 1, \dots, n-1\}$ consists of $n$ distinct roots of unity.

::: pf-proof
The equation $z^n = 1$ has exactly the $n$ solutions $\zeta_k = e^{2\pi i k/n}$, $k = 0, \dots, n-1$: for $0 \le k < k' < n$ the difference $k' - k$ lies strictly between $0$ and $n$, so $e^{2\pi i(k'-k)/n} \neq 1$ and the solutions are distinct, and a polynomial of degree $n$ has at most $n$ roots, so there are no others.
:::

:::

::: {.pf-step #s4-2}
At each preimage $\zeta_k$, $f_n'(\zeta_k) = n \zeta_k^{n-1} \neq 0$. Since $f_n$ is complex holomorphic, its Jacobian determinant as a real map $\RR^2 \to \RR^2$ is $\abs{f_n'(z)}^2 > 0$, so each local degree is $\deg_{\zeta_k}(f_n) = +1$.

::: pf-proof
The derivative is $f_n'(z) = nz^{n-1}$, and $\zeta_k^{n-1} = \zeta_k^{-1} \neq 0$, so $f_n'(\zeta_k) \neq 0$ and $w_0 = 1$ is a regular value. For a holomorphic $f$ the Jacobian determinant of $f$ as a map $\RR^2 \to \RR^2$ is $\abs{f'(z)}^2$, which is positive at each $\zeta_k$; the Jacobian is then nonzero with positive sign, so $f_n$ preserves orientation near $\zeta_k$ and the local degree there is $+1$.
:::

:::

::: {.pf-step #s4-3}
By the regular value formula, the degree equals the sum of local degrees over the preimage of any regular value: $\deg(f_n) = \sum_{k=0}^{n-1} (+1) = n$.

::: pf-proof
For a map of $S^2$ and a regular value $w$, the degree is the sum of the local degrees over the finitely many preimages of $w$. Here $w_0 = 1$ is regular with the $n$ preimages $\zeta_k$, each of local degree $+1$ by step [](#s4-2){.pf-ref}, so $\deg(f_n) = n$.
:::

:::

:::

:::

::: pf-step
Conclusion.

::: pf-proof

::: pf-step
For $p(z) = \sum_{j=0}^n a_j z^j$ with $a_n \neq 0$: $$\deg(p) = \boxed{n}.$$ (If $p$ is constant, $\deg(p) = 0$).

::: pf-proof
By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\deg(p) = \deg(f_n)$; by step [](#s4){.pf-ref}, $\deg(f_n) = n$; and by step [](#s1){.pf-ref}, the constant case has degree $0$.
:::

:::

:::

:::

:::
:::
