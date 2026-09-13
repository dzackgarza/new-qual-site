---
schema: qual/card@1
id: T-CRVHASSE
kind: theorem
title: The Hasse invariant criterion and the Hasse polynomial $h_p(\lambda)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Characteristic p
  - Cohomology
relations:
- kind: uses
  target: D-CRVHASSE
- kind: uses
  target: T-IJW1K
- kind: related-to
  target: T-CRVJINV
review: draft
prompts:
- Given a plane cubic in characteristic $p$, how do you compute its Hasse invariant?
- Write down the Hasse polynomial for the Legendre family.
- Why does the criterion involve $f^{p-1}$ and the monomial $(xyz)^{p-1}$?
- How many supersingular curves are there in characteristic $p$?
---

::: {.theorem title="The coefficient criterion"}
Let $\operatorname{ch} k = p > 0$ and let $E = V(f) \subseteq \PP^2$ be a smooth cubic, $f$ homogeneous of degree $3$.
Then $E$ has Hasse invariant zero, that is $E$ is supersingular, if and only if
\[
\text{the coefficient of } (xyz)^{p-1} \text{ in } f^{p-1} \text{ is } 0 .
\]
:::

::: {.theorem title="The Legendre family"}
For $p \neq 2$ and $E \colon y^2 = x(x-1)(x-\lambda)$ with $\lambda \neq 0,1$, put $m \da \tfrac{p-1}{2}$ and
\[
h_p(\lambda) \da \sum_{i=0}^{m} \binom{m}{i}^2 \lambda^i .
\]
Then $E$ is supersingular exactly when $h_p(\lambda) = 0$.
Consequently, for each $p$ there are at most $\left\lfloor p/12 \right\rfloor + 2$ supersingular elliptic curves over $\bar k$ up to isomorphism.
:::

::: {.remark title="Where the criterion comes from"}
Every step is forced, which is why this is a reasonable thing to be asked to reconstruct.

The ideal sheaf of a plane cubic is $\OO_{\PP^2}(-3)$, so
\[
0 \to \OO_{\PP^2}(-3) \xrightarrow{\ f\ } \OO_{\PP^2} \to \OO_E \to 0 .
\]
Since $h^1(\OO_{\PP^2}) = h^2(\OO_{\PP^2}) = 0$, the long exact sequence gives $H^1(\OO_E) \iso H^2(\PP^2; \OO(-3))$.
That group is one-dimensional with basis the Čech class $\tfrac{1}{xyz}$ --- it is the unique monomial of degree $-3$ with all three exponents negative.
So the line whose endomorphism is being tested has a canonical monomial basis, and the test becomes a computation with monomials.

Frobenius on $\PP^2$ sends $\tfrac{1}{xyz} \mapsto \tfrac{1}{(xyz)^p}$.
Transporting along the diagram that compares $E = V(f)$ with $V(f^p)$ multiplies by $f^{p-1}$, so the image is the class of
\[
\frac{f^{p-1}}{(xyz)^{p}} .
\]
In $H^2(\PP^2; \OO(-3))$ every monomial with a non-negative exponent is zero, so only the term of $f^{p-1}$ equal to $(xyz)^{p-1}$ survives, and it contributes that coefficient times $\tfrac{1}{xyz}$.
The criterion is then the definition read off: $F^* = 0$ exactly when that coefficient vanishes.

The degree bookkeeping is worth checking once, since it is the part that looks like a coincidence: $f^{p-1}$ has degree $3(p-1)$, and $(xyz)^{p-1}$ has degree $3(p-1)$ as well, so the monomial is available for every $p$.
:::

::: {.remark title="Using the Legendre form"}
Dehomogenising, the criterion for $y^2 = g(x)$ with $\deg g = 3$ becomes: supersingular exactly when the coefficient of $x^{p-1}$ in $g(x)^{(p-1)/2}$ vanishes.
Expanding $\big(x(x-1)(x-\lambda)\big)^m$ and collecting gives $(-1)^m h_p(\lambda)$, so the sign is irrelevant and the vanishing is $h_p(\lambda) = 0$.

Two sanity checks worth carrying:

- $p = 3$: $m = 1$, $h_3(\lambda) = 1 + \lambda$, so $\lambda = -1$, and there $\lambda^2 - \lambda + 1 = 3 = 0$, giving $j = 0$ --- the one supersingular curve in characteristic $3$.

- $p = 5$: $m = 2$, $h_5(\lambda) = \lambda^2 + 4\lambda + 1$, whose roots lie in $\FF_{25}$ and satisfy $\lambda^2 - \lambda + 1 = -5\lambda = 0$, again giving $j = 0$.

The count follows because $h_p$ has degree $m = \tfrac{p-1}{2}$ and the map $\lambda \mapsto j$ is generically six-to-one, so the supersingular $j$-values number about $p/12$; the exact count is $\left\lfloor p/12 \right\rfloor$ adjusted by $0, 1, 1, 2$ according to $p \equiv 1, 5, 7, 11 \bmod 12$, which the stated bound covers.
Supersingular curves therefore exist for every $p$ and are always finite in number; $h_p$ has simple roots, so no value of $\lambda$ is counted twice.
:::
