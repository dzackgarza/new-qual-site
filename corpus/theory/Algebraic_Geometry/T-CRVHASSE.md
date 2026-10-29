---
schema: qual/card@1
id: T-CRVHASSE
kind: theorem
title: The Hasse invariant criterion and the Hasse polynomial $h_p(\lambda)$
slogan: 'Supersingularity is a coefficient test: extract $(xyz)^{p-1}$ from $f^{p-1}$, or solve $h_p(\lambda)=0$ in Legendre form.'
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
Let $k$ be a field of characteristic $p>0$ and let $E = V(f) \subseteq \PP^2_k$ be a smooth cubic, with $f$ homogeneous of degree $3$.
Then $E$ has Hasse invariant zero, that is $E$ is supersingular, if and only if
$$
\text{the coefficient of } (xyz)^{p-1} \text{ in } f^{p-1} \text{ is } 0 .
$$
:::

::: {.theorem title="The Legendre family"}
For $p \neq 2$ and $E \colon y^2 = x(x-1)(x-\lambda)$ with $\lambda \neq 0,1$, put
$$
m\coloneqq\frac{p-1}{2},
\qquad
h_p(\lambda)\coloneqq\sum_{i=0}^{m}\binom{m}{i}^2\lambda^i.
$$
Then $E$ is supersingular exactly when $h_p(\lambda) = 0$.
:::

::: {.remark title="Where the criterion comes from"}
The Hasse invariant is the action of Frobenius on the one-dimensional space $H^1(\OO_E)$, and the coefficient criterion computes it in Čech cohomology.

The ideal sheaf of a plane cubic is $\OO_{\PP^2}(-3)$, so
$$
0 \to \OO_{\PP^2}(-3) \xrightarrow{\ f\ } \OO_{\PP^2} \to \OO_E \to 0 .
$$
Since $h^1(\OO_{\PP^2}) = h^2(\OO_{\PP^2}) = 0$, the long exact sequence gives $H^1(\OO_E) \iso H^2(\PP^2; \OO(-3))$.
That group is one-dimensional with basis the Čech class $\tfrac{1}{xyz}$ --- it is the unique monomial of degree $-3$ with all three exponents negative.
So $H^1(\OO_E)$ has a canonical monomial basis, and the test becomes a computation with monomials.

Frobenius on $\PP^2$ sends $\tfrac{1}{xyz} \mapsto \tfrac{1}{(xyz)^p}$.
Frobenius carries the presentation of $E = V(f)$ to that of $V(f^p)$, and the inclusion $E \subseteq V(f^p)$ induces multiplication by $f^{p-1}$ from $H^2(\PP^2; \OO(-3p))$ to $H^2(\PP^2; \OO(-3))$, so the image is the class of
$$
\frac{f^{p-1}}{(xyz)^{p}} .
$$
In $H^2(\PP^2; \OO(-3))$ every monomial with a non-negative exponent is zero, so only the term of $f^{p-1}$ equal to $(xyz)^{p-1}$ survives, and it contributes that coefficient times $\tfrac{1}{xyz}$.
The criterion is then the definition read off: $F^* = 0$ exactly when that coefficient vanishes.

The degree bookkeeping explains why the distinguished monomial can occur: both $f^{p-1}$ and $(xyz)^{p-1}$ have degree $3(p-1)$.
:::

::: {.remark title="Using the Legendre form"}
Dehomogenising, the criterion for $y^2 = g(x)$ with $\deg g = 3$ becomes: supersingular exactly when the coefficient of $x^{p-1}$ in $g(x)^{(p-1)/2}$ vanishes.
Expanding $\big(x(x-1)(x-\lambda)\big)^m$ and collecting gives $(-1)^m h_p(\lambda)$, so the sign is irrelevant and the vanishing is $h_p(\lambda) = 0$.

Two low-characteristic checks are:

- $p = 3$: $m = 1$, $h_3(\lambda) = 1 + \lambda$, so $\lambda = -1$, and there $\lambda^2 - \lambda + 1 = 3 = 0$, giving $j = 0$ --- the one supersingular curve in characteristic $3$.

- $p = 5$: $m = 2$, $h_5(\lambda) = \lambda^2 + 4\lambda + 1$, whose roots lie in $\FF_{25}$ and satisfy $\lambda^2 - \lambda + 1 = -5\lambda = 0$, again giving $j = 0$.

For $p>3$, the exact number of supersingular $j$-invariants over $\overline{\FF}_p$ is
$$
\left\lfloor\frac p{12}\right\rfloor+\varepsilon_p,
\qquad
\varepsilon_p=
\begin{cases}
0,&p\equiv1\pmod{12},\\
1,&p\equiv5,7\pmod{12},\\
2,&p\equiv11\pmod{12}.
\end{cases}
$$
For $p=2$ and $p=3$ there is one supersingular $j$-invariant. In particular the supersingular locus is nonempty and finite in every characteristic. The Deuring polynomial $h_p$ has simple roots for odd $p$, and its roots parametrize the supersingular members of the Legendre family before quotienting by the usual six transformations of $\lambda$ that preserve the $j$-invariant.
:::
