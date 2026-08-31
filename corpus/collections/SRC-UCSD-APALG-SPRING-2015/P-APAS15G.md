---
schema: qual/card@1
id: P-APAS15G
kind: problem
title: Reduced Gröbner bases and a linear basis for $\mathbb{C}[x,y]/I$
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $I \subseteq \mathbb{C}[x, y]$ be the ideal given by $I = \langle y^2 + xy,\ xy^2 + x^2 y + x^2 \rangle$.

(1) Find the reduced Gröbner basis for $I$ with respect to the lexicographic order where $y > x$.

(2) Find the reduced Gröbner basis for the ideal $I \cap \mathbb{C}[x]$.

(3) Find a $\mathbb{C}$-linear basis for the $\mathbb{C}$-vector space $\mathbb{C}[x, y]/I$.
:::

::: {.solution}
<1>1. Part (1): Reduced Gröbner basis for $I$ with lex order $y > x$:
<2>1. Let $f_1 = y^2 + xy$ and $f_2 = xy^2 + x^2 y + x^2$.
With respect to the lexicographic order where $y > x$, the leading monomials are:
\[
\operatorname{LM}(f_1) = y^2, \qquad \operatorname{LM}(f_2) = xy^2.
\]
::: {.proof}
lex term ordering with $y > x$.
:::
<2>2. Compute the $S$-polynomial of $f_1$ and $f_2$:
\[
S(f_1, f_2) = \frac{xy^2}{y^2} f_1 - \frac{xy^2}{xy^2} f_2 = x(y^2 + xy) - (xy^2 + x^2 y + x^2) = (xy^2 + x^2 y) - (xy^2 + x^2 y + x^2) = -x^2.
\]
Let $f_3 = x^2 \in I$, with leading monomial $\operatorname{LM}(f_3) = x^2$.
::: {.proof}
definition of $S$-polynomial.
:::
<2>3. Test the remaining $S$-pair $S(f_1, f_3)$:
Since $\gcd(\operatorname{LM}(f_1), \operatorname{LM}(f_3)) = \gcd(y^2, x^2) = 1$, by Buchberger’s First Criterion the $S$-polynomial $S(f_1, f_3)$ reduces to 0 modulo $\{f_1, f_3\}$.
Concretely, $S(f_1, f_3) = x^2(y^2 + xy) - y^2(x^2) = x^3 y = xy \cdot f_3 \equiv 0 \pmod{f_3}$.
::: {.proof}
Buchberger's Coprime Criterion.
:::
<2>4. Thus $\{f_1, f_3\} = \{y^2 + xy, x^2\}$ is a Gröbner basis for $I$.
Both polynomials are monic, and no monomial of $f_1$ ($y^2$ and $xy$) or $f_3$ ($x^2$) is divisible by the leading monomial of the other ($\operatorname{LM}(f_3) = x^2 \nmid xy$ and $\operatorname{LM}(f_1) = y^2 \nmid 0$).
Therefore the reduced Gröbner basis for $I$ is:
\[
G = \{y^2 + xy, \, x^2\}.
\]
::: {.proof}
definition of reduced Gröbner basis.
:::

<1>2. Part (2): Reduced Gröbner basis for $I \cap \mathbb{C}[x]$:
<2>1. By the Elimination Theorem, for the elimination order $y > x$, a Gröbner basis for the elimination ideal $I_1 = I \cap \mathbb{C}[x]$ is obtained by taking the elements of $G$ containing only the variable $x$:
\[
G \cap \mathbb{C}[x] = \{x^2\}.
\]
Thus the reduced Gröbner basis for $I \cap \mathbb{C}[x]$ is $\{x^2\}$.
::: {.proof}
Elimination Theorem for lex orders.
:::

<1>3. Part (3): $\mathbb{C}$-linear basis for $\mathbb{C}[x, y]/I$:
<2>1. The initial ideal of $I$ is $\operatorname{LT}(I) = \langle \operatorname{LM}(g) \mid g \in G \rangle = \langle y^2, x^2 \rangle$.
::: {.proof}
leading terms of $G$.
:::
<2>2. By Macaulay's Theorem / the Division Algorithm, a $\mathbb{C}$-vector space basis for $\mathbb{C}[x, y]/I$ is given by the set of all monomials not in $\operatorname{LT}(I)$:
\[
\mathcal{B} = \{x^a y^b \mid x^a y^b \notin \langle x^2, y^2 \rangle\} = \{x^a y^b \mid 0 \le a < 2, \, 0 \le b < 2\}.
\]
Evaluating the four combinations of exponents $(a, b) \in \{0, 1\} \times \{0, 1\}$ gives:
\[
\mathcal{B} = \{1, \, x, \, y, \, xy\}.
\]
::: {.proof}
standard monomial basis theorem for polynomial quotient rings.
:::

<1>4. Conclusion:
The reduced Gröbner basis for $I$ is $\{y^2 + xy, x^2\}$, the reduced Gröbner basis for $I \cap \mathbb{C}[x]$ is $\{x^2\}$, and a linear basis for $\mathbb{C}[x, y]/I$ is $\{1, x, y, xy\}$. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
