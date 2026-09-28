---
schema: qual/card@1
id: E-SMI-8000E-FEB
kind: problem
title: Field theory definitions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all six definition prompts with Smith 8000 Fall 2006 final part B."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Gave standard definitions and two equivalent characterizations each of separability and normality for algebraic extensions."
---

::: {.exercise}
Assume $k$ is a subfield of a field $E$, and $c$ an element of $E$.
Define what is meant by:

(i) $c$ is algebraic over $k$;

(ii) the minimal polynomial of (an algebraic element) $c$ over $k$;

(iii) $E$ is separable (algebraic) over $k$ (give 2 characterizations);

(iv) $E$ is normal (algebraic) over $k$ (give 2 characterizations);

(v) $E$ is an algebraic closure of $k$;

(vi) the Galois group $\operatorname{Gal}_k(E)$, i.e. $\operatorname{Aut}_k(E)$.
:::

::: {.solution}
<1>1. Algebraic element.
::: {.proof}
An element $c\in E$ is **algebraic over $k$** if there exists a nonzero
polynomial
$$
f(X)\in k[X]
$$
such that
$$
f(c)=0.
$$
If no such polynomial exists, $c$ is transcendental over $k$.
:::

<1>2. Minimal polynomial.
::: {.proof}
If $c$ is algebraic over $k$, its **minimal polynomial over $k$** is the
unique monic polynomial
$$
m_{c,k}(X)\in k[X]
$$
of least positive degree such that
$$
m_{c,k}(c)=0.
$$
It is irreducible over $k$, and every polynomial in $k[X]$ vanishing at $c$
is divisible by $m_{c,k}$.
:::

<1>3. Separable algebraic extension.
::: {.proof}
Assume $E/k$ is algebraic. The extension is **separable** if every
$c\in E$ has a separable minimal polynomial over $k$, i.e. the roots of
$m_{c,k}$ in an algebraic closure are all distinct.

Equivalently, every irreducible polynomial
$$
f\in k[X]
$$
which has a root in $E$ is a separable polynomial. In derivative form, this
means
$$
\gcd(f,f')=1
$$
for every such irreducible $f$.
:::

<1>4. Normal algebraic extension.
::: {.proof}
Assume $E/k$ is algebraic and place $E$ inside an algebraic closure
$\overline k$. The extension is **normal** if every irreducible polynomial
$$
f\in k[X]
$$
having one root in $E$ splits completely into linear factors over $E$.

Equivalently, for every $k$-embedding
$$
\sigma:E\hookrightarrow\overline k,
$$
one has
$$
\sigma(E)=E.
$$
Thus the $k$-conjugates of all elements of $E$ remain inside $E$.
:::

<1>5. Algebraic closure.
::: {.proof}
An extension $E/k$ is an **algebraic closure of $k$** if

1. $E/k$ is algebraic, and
2. $E$ is algebraically closed.

Equivalently, every nonconstant polynomial over $E$ has a root in $E$, while
every element of $E$ is algebraic over $k$.
:::

<1>6. Galois group $\operatorname{Gal}_k(E)$.
::: {.proof}
The group
$$
\operatorname{Gal}_k(E)=\operatorname{Aut}_k(E)
$$
is the group, under composition, of all field automorphisms
$$
\sigma:E\longrightarrow E
$$
which fix $k$ pointwise:
$$
\sigma(a)=a
\qquad\text{for every }a\in k.
$$
:::
:::
