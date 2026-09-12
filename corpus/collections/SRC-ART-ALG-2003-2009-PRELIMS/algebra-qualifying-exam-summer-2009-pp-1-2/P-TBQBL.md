---
schema: qual/card@1
id: P-TBQBL
kind: problem
title: 'True-or-false: constructible roots, finite-field extensions, and Galois composita'
classification:
  areas:
  - algebra
  topics:
  - Logic and Quantifiers
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared all five assertions and the request for additional hypotheses with page 2 of the original scan, Fields 2; corrected the area to algebra."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: "Checked the quartic and cubic irreducibility tests and the resolvent identities, the degree-six obstruction, and the exact finite-field subfield condition."
---

::: {.problem}
Indicate whether each of the following if-then statements is true, and give a brief explanation to support your answer.
If the statement is false, and there is a reasonable addition to the hypotheses that would make it true, please indicate that as well.

a. If $f$ is an irreducible 4th degree polynomial with rational coefficients then the roots of $f$ are constructible numbers.

b. If $g$ is an irreducible 6th degree polynomial with rational coefficients then the roots of $g$ are constructible numbers.

c. If $E$ and $F$ are finite fields and $F\subset E$ then $E/F$ is Galois.

d. If $E/F$ and $K/F$ are both Galois extensions then $EK/F$ is a Galois extension.

e. If $E$ and $F$ are finite fields and $|F|$ divides $|E|$ then $E$ has a subfield isomorphic to $F$.
:::

::: solution
The answers are **false, false, true, true, false**.
We use the quadratic-tower criterion for straightedge-and-compass
constructibility [@DF04]. In particular, a constructible algebraic number
lies in a finite tower of quadratic extensions of $\mathbf Q$, and its
degree divides $2^m$ for some $m$. Finitely many constructible numbers lie
in a common such tower: adjoin their quadratic generators successively,
noting that each new extension has degree at most $2$. Their sums and
products are therefore constructible as well.

<1>1. Part (a) is false. An explicit counterexample is
$$
f(x)=x^4-4x^2+x+1.
$$

::: proof
<2>1. Modulo $2$, this polynomial becomes $x^4+x+1$. It has no root in
$\mathbf F_2$. The only monic irreducible quadratic over $\mathbf F_2$ is
$x^2+x+1$, and modulo that quadratic one has $x^3=1$, so
$x^4+x+1\equiv1$. Thus the quartic has neither a linear nor a quadratic
factor over $\mathbf F_2$, proving irreducibility there and hence over
$\mathbf Q$ by Gauss's lemma [@DF04]. It also has four real roots:
its values at $-3,-2,0,1,2$ are respectively $43,-1,1,-1,3$, giving a
root in each of the four intervening intervals.

<2>2. Write its roots as $\alpha_1,\ldots,\alpha_4$ and put
$$
\beta_1=\alpha_1\alpha_2+\alpha_3\alpha_4,\quad
\beta_2=\alpha_1\alpha_3+\alpha_2\alpha_4,\quad
\beta_3=\alpha_1\alpha_4+\alpha_2\alpha_3.
$$
If $e_i$ are the elementary symmetric functions of the $\alpha_j$,
Vieta's identities give $(e_1,e_2,e_3,e_4)=(0,-4,-1,1)$. Expanding the
three displayed expressions gives
$$
\begin{aligned}
\sum_i\beta_i&=e_2=-4,\\
\sum_{i<j}\beta_i\beta_j&=e_1e_3-4e_4=-4,\\
\beta_1\beta_2\beta_3&=e_3^2+e_1^2e_4-4e_2e_4=17.
\end{aligned}
$$
Consequently each $\beta_i$ is a root of
$$
h(y)=y^3+4y^2-4y-17.
$$
Modulo $3$ this is $y^3+y^2+2y+1$, whose values at $0,1,2$ are
$1,2,2$. A cubic without a root over its coefficient field is
irreducible. Hence $h$ is irreducible over $\mathbf Q$, and each
$\beta_i$ has degree $3$.

<2>3. If all four $\alpha_i$ were constructible, their products and sums
would make the $\beta_i$ constructible. Their degree $3$ contradicts
the quadratic-tower criterion. Thus an irreducible quartic need not have
constructible roots, even when all its roots are real.

A sufficient additional hypothesis is that the quartic is biquadratic:
$f(x)=a x^4+b x^2+c$ with $a,b,c\in\mathbf Q$ and $a\ne0$.
Then every root is obtained by the two successive square-root operations
$$
x=\pm\sqrt{\frac{-b\pm\sqrt{b^2-4ac}}{2a}},
$$
so all roots are constructible (with complex numbers interpreted as
points in the plane).
:::

<1>2. Part (b) is false, and in fact no root of an irreducible sextic
over $\mathbf Q$ is constructible.

::: proof
For every root $\alpha$, irreducibility gives
$[\mathbf Q(\alpha):\mathbf Q]=6$. If $\alpha$ lay in a quadratic tower
of total degree $2^m$, the tower law would give $6\mid2^m$, which is
impossible. Thus no additional hypothesis compatible with irreducibility
and degree $6$ can make this assertion true. One must change one of
those requirements, not merely add an unrelated restriction.
:::

<1>3. Part (c) is true.

::: proof
Let $|F|=q$ and $[E:F]=d$, so $|E|=q^d$. Every element of $E$ satisfies
$x^{q^d}=x$: for nonzero elements this follows from the order $q^d-1$
of the multiplicative group, and it also holds at zero. Hence $E$ is
the splitting field over $F$ of $x^{q^d}-x$. The derivative of this
polynomial is $-1$, so its roots are distinct. Thus the extension is
normal, and the minimal polynomial of every element divides a
separable polynomial and is itself separable. Therefore $E/F$ is Galois.
:::

<1>4. Part (d) is true, with $E$ and $K$ viewed in a common algebraic
closure $\overline F$.

::: proof
The compositum $EK$ is algebraic and separable over $F$. Indeed, each of
its elements belongs to a field generated by finitely many separable
elements of $E\cup K$, and a finite extension generated by separable
elements is separable [@DF04].
Every $F$-embedding $\sigma:EK\to\overline F$ restricts to embeddings
of $E$ and $K$. Their normality gives $\sigma(E)=E$ and $\sigma(K)=K$,
so
$$
\sigma(EK)=\sigma(E)\sigma(K)=EK.
$$
Thus $EK/F$ is normal and separable, hence Galois. This argument does
not require the original Galois extensions to have finite degree.
:::

<1>5. Part (e) is false. The correct condition, for $|F|=p^a$ and
$|E|=p^b$, is $a\mid b$, not merely $p^a\mid p^b$.

::: proof
<2>1. Take $F=\mathbf F_4$ and $E=\mathbf F_8$. For explicit models use
$\mathbf F_2[x]/(x^2+x+1)$ and $\mathbf F_2[y]/(y^3+y+1)$; the
polynomials have no root in $\mathbf F_2$ and are therefore irreducible
in degrees $2$ and $3$. Although $4\mid8$, a field embedding $F\to E$
would embed the multiplicative group of order $3$ into one of order
$7$, contradicting Lagrange's theorem.

<2>2. More generally, an embedding of $F$ into $E$ identifies their prime
fields. The tower law then gives
$$
b=[E:\mathbf F_p]=[E:F]\,[F:\mathbf F_p]=[E:F]a,
$$
so $a\mid b$ is necessary.

Conversely, suppose $b=ar$. In characteristic $p$ the identity
$$
X^{p^{ar}}-X=\sum_{j=0}^{r-1}(X^{p^a}-X)^{p^{aj}}
$$
shows that $X^{p^a}-X$ divides $X^{p^b}-X$. The latter splits into
distinct linear factors over $E$, so the former has exactly $p^a$
distinct roots in $E$. Its root set is closed under addition,
subtraction, multiplication, and inverses of nonzero elements, since
it is the fixed set of the $p^a$-power Frobenius map. It is therefore
a subfield of order $p^a$. It is isomorphic to $F$: both are splitting
fields of $X^{p^a}-X$ over $\mathbf F_p$, and splitting fields are
unique up to an isomorphism fixing the coefficient field [@DF04].
Thus the additional exponent-divisibility hypothesis is both necessary
and sufficient.
:::
:::
