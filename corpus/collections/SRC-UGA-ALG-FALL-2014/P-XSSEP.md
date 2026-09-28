---
schema: qual/card@1
id: P-XSSEP
kind: problem
title: Equal degrees of irreducible factors of $f\in\QQ[x]$ in $L[x]$ when $L/\QQ$
  is Galois, and a counterexample otherwise
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Irreducibility Criteria
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $f\in \QQ[x]$ be an irreducible polynomial and $L$ a finite Galois extension of $\QQ$.
Let $f(x) = g_1(x)g_2(x)\cdots g_r(x)$ be a factorization of $f$ into irreducibles in $L[x]$.

a. Prove that each of the factors $g_i(x)$ has the same degree.

b. Give an example showing that if $L$ is not Galois over $\QQ$, the conclusion of part (a) need not hold.
:::

::: {.solution}
(a) Let $M$ be a splitting field of $f$ over $L$. Since $L/\QQ$ is finite
Galois and $f\in\QQ[x]$, the extension $M/\QQ$ is finite Galois. Put
\[
G=\operatorname{Gal}(M/\QQ),
\qquad
H=\operatorname{Gal}(M/L).
\]
Because $L/\QQ$ is Galois, $H\triangleleft G$.

The irreducible factors of $f$ over $L$ correspond to the $H$-orbits on the
roots of $f$: the roots of the minimal polynomial over $L$ of a root $\alpha$
are precisely the elements of $H\cdot\alpha$. Since $f$ is irreducible over
$\QQ$, $G$ acts transitively on the roots of $f$.

If $\alpha$ and $\beta$ are two roots, choose $\sigma\in G$ with
$\sigma(\alpha)=\beta$. Normality of $H$ gives
\[
\sigma(H\cdot\alpha)=H\cdot\beta.
\]
Thus all $H$-orbits on the roots have the same cardinality. Their cardinalities
are exactly the degrees of the irreducible factors $g_i$, so all
$\deg g_i$ are equal.

(b) Take
\[
f(x)=x^3-2,
\qquad
L=\QQ(\sqrt[3]{2}).
\]
The polynomial $f$ is irreducible over $\QQ$ by Eisenstein at $2$, while
$L/\QQ$ is not Galois because $L\subset\RR$ does not contain the nonreal roots
$\zeta_3\sqrt[3]{2}$ and $\zeta_3^2\sqrt[3]{2}$. Over $L$,
\[
x^3-2=(x-\sqrt[3]{2})
\bigl(x^2+\sqrt[3]{2}\,x+\sqrt[3]{4}\bigr).
\]
The quadratic factor is irreducible over the real field $L$, since its two
roots are nonreal. Hence the irreducible factors have degrees $1$ and $2$.
:::
