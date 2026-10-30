---
schema: qual/card@1
id: P-TBQBL
kind: problem
title: 'True-or-false: constructible roots, finite-field extensions, and Galois composita'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Finite Fields
  - Field Extensions
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

(a) If $f$ is an irreducible 4th degree polynomial with rational coefficients then the roots of $f$ are constructible numbers.

(b) If $g$ is an irreducible 6th degree polynomial with rational coefficients then the roots of $g$ are constructible numbers.

(c) If $E$ and $F$ are finite fields and $F\subset E$ then $E/F$ is Galois.

(d) If $E/F$ and $K/F$ are both Galois extensions then $EK/F$ is a Galois extension.

(e) If $E$ and $F$ are finite fields and $\cardinality{F}$ divides $\cardinality{E}$ then $E$ has a subfield isomorphic to $F$.
:::

::: {.solution}
The answers are, in order, false, false, true, true, false. For
constructibility, use the standard quadratic-tower criterion: if an
algebraic number over $\QQ$ is constructible, then its degree over $\QQ$
divides a power of $2$ [@DF04].

::: pf

::: {.pf-step #s1}

Part (a) is false. One counterexample is
$$
\boxed{f(x)=x^4-4x^2+x+1}.
$$
A sufficient additional hypothesis is that the quartic is biquadratic.

::: pf-proof

::: {.pf-step #s1-1}

The polynomial $f$ is irreducible over $\QQ$.

::: pf-proof

Modulo $2$,
$$
f(x)\equiv x^4+x+1.
$$
This polynomial has no root in $\FF_2$. The only monic irreducible
quadratic over $\FF_2$ is $x^2+x+1$, and modulo this quadratic one has
$x^3=1$, hence
$$
x^4+x+1\equiv1.
$$
Thus $x^4+x+1$ has neither a linear nor a quadratic factor over $\FF_2$,
so it is irreducible. Gauss's lemma therefore implies that $f$ is
irreducible over $\QQ$ [@DF04].

:::

:::

::: {.pf-step #s1-2}

Not all roots of $f$ are constructible.

::: pf-proof

Let the roots be $\alpha_1,\ldots,\alpha_4$, and define
$$
\begin{aligned}
\beta_1&=\alpha_1\alpha_2+\alpha_3\alpha_4,\\
\beta_2&=\alpha_1\alpha_3+\alpha_2\alpha_4,\\
\beta_3&=\alpha_1\alpha_4+\alpha_2\alpha_3.
\end{aligned}
$$
For the elementary symmetric functions of the roots, Vieta's formulas give
$$
(e_1,e_2,e_3,e_4)=(0,-4,-1,1).
$$
Direct expansion gives
$$
\sum_i\beta_i=-4,
\qquad
\sum_{i<j}\beta_i\beta_j=-4,
\qquad
\beta_1\beta_2\beta_3=17.
$$
Hence every $\beta_i$ is a root of
$$
h(y)=y^3+4y^2-4y-17.
$$
Modulo $3$, this becomes $y^3+y^2+2y+1$, whose values at
$0,1,2$ are $1,2,2$. Thus it has no root in $\FF_3$, so the cubic is
irreducible over $\FF_3$ and therefore $h$ is irreducible over $\QQ$.
Consequently each $\beta_i$ has degree $3$ over $\QQ$.

If all four $\alpha_i$ were constructible, then they would lie in a common
finite tower of quadratic extensions, so their products and sums, in
particular the $\beta_i$, would also be constructible. But a constructible
algebraic number has degree dividing a power of $2$, whereas
$[\QQ(\beta_i):\QQ]=3$. This is a contradiction.

:::

:::

::: {.pf-step #s1-3}

The added hypothesis that
$$
f(x)=ax^4+bx^2+c
\qquad(a,b,c\in\QQ,\ a\ne0)
$$
is sufficient to make the conclusion true.

::: pf-proof

Writing $u=x^2$, the quadratic formula gives
$$
u=\frac{-b\pm\sqrt{b^2-4ac}}{2a},
$$
and then
$$
x=\pm\sqrt{\frac{-b\pm\sqrt{b^2-4ac}}{2a}}.
$$
Thus every root is obtained from rational numbers by field operations and
successive square roots, hence is constructible.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give an irreducible quartic whose roots are not all
constructible, and step [](#s1-3){.pf-ref} gives a reasonable sufficient additional
hypothesis.

:::

:::

:::

::: {.pf-step #s2}

Part (b) is false; in fact, no root of an irreducible degree-$6$
polynomial over $\QQ$ is constructible.

::: pf-proof

If $g\in\QQ[x]$ is irreducible of degree $6$ and $\alpha$ is a root,
then
$$
[\QQ(\alpha):\QQ]=6.
$$
If $\alpha$ were constructible, its degree would divide a power of $2$,
contradicting the factor $3$ in $6$. Thus no additional hypothesis
compatible with both irreducibility and degree $6$ can make the stated
conclusion true.

:::

:::

::: {.pf-step #s3}

Part (c) is true.

::: pf-proof

Let $\cardinality{ F}=q$ and $[E:F]=d$, so
$\cardinality{ E}=q^d$. Every element of $E$ is a root of
$$
X^{q^d}-X.
$$
Indeed, this is immediate for $0$, while for $a\in E^\times$ it follows
from $a^{q^d-1}=1$. Thus $E$ is the splitting field over $F$ of
$X^{q^d}-X$. Its derivative is $-1$, so it has no repeated roots.
Therefore $E/F$ is normal and separable, hence Galois.

:::

:::

::: {.pf-step #s4}

Part (d) is true, where $E$ and $K$ are viewed in a common algebraic
closure of $F$.

::: pf-proof

Because $E/F$ and $K/F$ are Galois, they are algebraic, normal, and
separable. The compositum $EK/F$ is algebraic and separable: every element
of $EK$ lies in an extension generated by finitely many separable elements
from $E\cup K$ [@DF04].

Let $\sigma:EK\to\overline F$ be an $F$-embedding. Its restrictions to
$E$ and $K$ are $F$-embeddings. Normality gives
$$
\sigma(E)=E,
\qquad
\sigma(K)=K.
$$
Hence
$$
\sigma(EK)=\sigma(E)\sigma(K)=EK.
$$
Thus $EK/F$ is normal as well as separable, so it is Galois.

:::

:::

::: {.pf-step #s5}

Part (e) is false. For
$$
\cardinality{ F}=p^a,
\qquad
\cardinality{ E}=p^b,
$$
the correct condition for $E$ to contain a subfield isomorphic to $F$ is
$$
\boxed{a\mid b}.
$$

::: pf-proof

::: {.pf-step #s5-1}

Divisibility of field orders is not sufficient.

::: pf-proof

Take $F=\FF_4$ and $E=\FF_8$. Then $4\mid8$. If $F$ embedded in $E$,
the induced embedding
$$
F^\times\hookrightarrow E^\times
$$
would embed a group of order $3$ into a group of order $7$, impossible by
Lagrange's theorem. Hence $E$ has no subfield isomorphic to $F$.

:::

:::

::: {.pf-step #s5-2}

The condition $a\mid b$ is necessary.

::: pf-proof

If a copy of $F$ is a subfield of $E$, then both fields have prime field
$\FF_p$, and the tower law gives
$$
b=[E:\FF_p]=[E:F][F:\FF_p]=[E:F]a.
$$
Thus $a\mid b$.

:::

:::

::: {.pf-step #s5-3}

The condition $a\mid b$ is sufficient.

::: pf-proof

Write $b=ar$. In characteristic $p$,
$$
X^{p^{ar}}-X
=\sum_{j=0}^{r-1}(X^{p^a}-X)^{p^{aj}},
$$
so $X^{p^a}-X$ divides $X^{p^b}-X$. The latter splits over $E$ into its
$p^b$ distinct roots, so all $p^a$ roots of $X^{p^a}-X$ lie in $E$.
These roots are the fixed points of the $p^a$-power Frobenius map and form
a subfield of $E$ with $p^a$ elements. Any two finite fields with $p^a$
elements are isomorphic, so this subfield is isomorphic to $F$ [@DF04].

:::

:::

::: pf-qed

Steps [](#s5-1){.pf-ref}, [](#s5-2){.pf-ref} and [](#s5-3){.pf-ref} show that order divisibility alone is insufficient and
establish the exact exponent-divisibility condition.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} answer parts (a)--(e), respectively.

:::

:::

:::
