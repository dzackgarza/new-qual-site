---
schema: qual/card@1
id: E-SMI-8000E-GG3
kind: problem
title: Two realizations of the field with 125 elements and an isomorphism between them
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement with Smith 8000e Galois-groups problem 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used reciprocal irreducible cubics x^3+x+1 and x^3+x^2+1, and gave the explicit quotient-field isomorphism sending the second generator to the inverse of the first."
---

::: {.exercise}
Find two different irreducible cubic polynomials mod 5, hence two different realizations of the unique field with 125 elements.
Can you find an isomorphism between them?
:::

::: {.solution}
Take
$$
f(X)=X^3+X+1
$$
and
$$
g(X)=X^3+X^2+1
$$
in $\mathbf F_5[X]$.

<1>1. Both cubics are irreducible over $\mathbf F_5$.
::: {.proof}
The polynomial $f$ has no root in $\mathbf F_5$:
$$
f(0),f(1),f(2),f(3),f(4)=1,3,1,1,4.
$$
Hence, being cubic, it is irreducible.

The polynomial $g$ is the reciprocal polynomial of $f$:
$$
g(X)=X^3f(X^{-1}).
$$
If $g$ had a root $a\in\mathbf F_5$, then $a\ne0$ because $g(0)=1$, and
$$
0=g(a)=a^3f(a^{-1})
$$
would make $a^{-1}$ a root of $f$. This is impossible. Thus $g$ also has no
root in $\mathbf F_5$, and hence is irreducible.
:::

<1>2. The two quotient fields each have $125$ elements.
::: {.proof}
Set
$$
K=\mathbf F_5[X]/(f),
\qquad
L=\mathbf F_5[Y]/(g).
$$
Irreducibility makes both quotients fields. Since both defining polynomials
have degree three,
$$
[K:\mathbf F_5]=[L:\mathbf F_5]=3,
$$
so
$$
|K|=|L|=5^3=125.
$$
:::

<1>3. Find an explicit root of $g$ inside $K$.
::: {.proof}
Let
$$
\alpha=X+(f)\in K.
$$
Then
$$
\alpha^3+\alpha+1=0.
$$
In particular $\alpha\ne0$, and multiplying by $\alpha^{-1}$ gives
$$
\alpha^2+1+\alpha^{-1}=0.
$$
Thus
$$
\alpha^{-1}=-\alpha^2-1.
$$
More importantly, dividing the equation
$\alpha^3+\alpha+1=0$ by $\alpha^3$ gives
$$
1+\alpha^{-2}+\alpha^{-3}=0.
$$
If
$$
\beta=\alpha^{-1},
$$
then this is
$$
\beta^3+\beta^2+1=0,
$$
so
$$
g(\beta)=0.
$$
:::

<1>4. Construct the isomorphism explicitly.
::: {.proof}
Let
$$
\gamma=Y+(g)\in L.
$$
Because $g(\beta)=0$, evaluation at $\beta$ induces an
$\mathbf F_5$-algebra homomorphism
$$
\Phi:L\longrightarrow K,
\qquad
\Phi(\gamma)=\beta=\alpha^{-1}.
$$
It is nonzero because $\Phi(1)=1$. A nonzero homomorphism from a field has
zero kernel, so $\Phi$ is injective. Since both fields have $125$ elements,
an injective map between them is automatically surjective. Therefore
$$
\boxed{\Phi:L\xrightarrow{\sim}K,
\qquad \gamma\longmapsto\alpha^{-1}}
$$
is the desired explicit isomorphism.
:::
:::
