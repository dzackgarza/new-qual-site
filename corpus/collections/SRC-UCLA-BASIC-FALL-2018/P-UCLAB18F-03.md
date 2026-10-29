---
schema: qual/card@1
id: P-UCLAB18F-03
kind: problem
title: Riemann integrability under an expanding change of variable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $f:[0,1]\to\RR$ and $g:[0,1]\to[0,1]$ be Riemann integrable.
Suppose that for some $\alpha\in(0,1)$,
$$
|g(x)-g(y)|\ge \alpha|x-y|\qquad(x,y\in[0,1]).
$$
Show that $f\circ g$ is Riemann integrable.
:::

::: {.solution}

Use the Lebesgue criterion for Riemann integrability: a bounded real-valued function on a compact interval is Riemann integrable if and only if its set of discontinuities has Lebesgue measure zero.

::: pf

::: pf-step

The map $g$ is injective.


::: pf-proof

If
$$
g(x)=g(y),
$$
then the hypothesis gives
$$
0
=
|g(x)-g(y)|
\ge
\alpha|x-y|.
$$
Since $\alpha>0$,
$$
x=y.
$$

:::

:::

::: {.pf-step #s1-2}

The inverse
$$
g^{-1}:g([0,1])\to[0,1]
$$
is Lipschitz with constant $1/\alpha$.


::: pf-proof

Let
$$
u=g(x),
\qquad
v=g(y).
$$
Then
$$
|u-v|
=
|g(x)-g(y)|
\ge
\alpha|x-y|.
$$
Thus
$$
|g^{-1}(u)-g^{-1}(v)|
=
|x-y|
\le
\frac1\alpha|u-v|.
$$

:::

:::

::: {.pf-step #s1-3}

If $E\subseteq\RR$ has Lebesgue measure zero and
$$
\phi:E_0\to\RR
$$
is $L$-Lipschitz on a subset $E_0\subseteq\RR$, then
$$
\phi(E\cap E_0)
$$
has measure zero.


::: pf-proof

Fix $\varepsilon>0$.
Since $E$ has measure zero, there are open intervals
$$
I_1,I_2,\ldots
$$
covering $E$ such that
$$
\sum_j |I_j|
<
\frac{\varepsilon}{2L}
$$
when $L>0$.

For each $j$ for which
$$
E_0\cap I_j\ne\varnothing,
$$
the image
$$
\phi(E_0\cap I_j)
$$
has diameter at most
$$
L|I_j|.
$$
Hence it is contained in an interval of length at most
$$
2L|I_j|.
$$
These image intervals cover
$$
\phi(E\cap E_0),
$$
and their total length is less than $\varepsilon$.
Thus the image has measure zero.

If $L=0$, the image consists of at most one point and is automatically null.

:::

:::

::: {.pf-step #s1-4}

Let
$$
D_f
\qquad\text{and}\qquad
D_g
$$
denote the sets of discontinuities of $f$ and $g$.
Then both have measure zero.


::: pf-proof

The functions $f$ and $g$ are Riemann integrable on $[0,1]$, hence bounded.
By the Lebesgue criterion, their discontinuity sets have Lebesgue measure zero.

:::

:::

::: {.pf-step #s1-5}

The set
$$
g^{-1}(D_f\cap g([0,1]))
$$
has measure zero.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
D_f
$$
has measure zero.
By step [](#s1-2){.pf-ref}, the inverse map
$$
g^{-1}:g([0,1])\to[0,1]
$$
is $1/\alpha$-Lipschitz.
Apply step [](#s1-3){.pf-ref} with
$$
E=D_f,
\qquad
E_0=g([0,1]),
\qquad
\phi=g^{-1}.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
x\notin
D_g
\cup
g^{-1}(D_f\cap g([0,1])),
$$
then $f\circ g$ is continuous at $x$.


::: pf-proof

The condition
$$
x\notin D_g
$$
means that $g$ is continuous at $x$.
The second condition means
$$
g(x)\notin D_f,
$$
so $f$ is continuous at $g(x)$.
The composition of functions continuous at the relevant points is continuous.
Hence
$$
f\circ g
$$
is continuous at $x$.

:::

:::

::: {.pf-step #s1-7}

Therefore the discontinuity set of $f\circ g$ is contained in
$$
D_g
\cup
g^{-1}(D_f\cap g([0,1])).
$$


::: pf-proof

This is the contrapositive of step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The discontinuity set of $f\circ g$ has measure zero.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
D_g
$$
has measure zero.
By step [](#s1-5){.pf-ref},
$$
g^{-1}(D_f\cap g([0,1]))
$$
has measure zero.
A finite union of null sets is null.
Apply step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The function
$$
f\circ g
$$
is bounded on $[0,1]$.


::: pf-proof

Riemann integrability of $f$ implies that $f$ is bounded on $[0,1]$.
Since
$$
g([0,1])\subseteq[0,1],
$$
the values
$$
f(g(x))
$$
are bounded by the same bound.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{f\circ g\text{ is Riemann integrable on }[0,1]}.
$$


::: pf-proof

By step [](#s1-9){.pf-ref}, the composition is bounded.
By step [](#s1-8){.pf-ref}, its set of discontinuities has measure zero.
The Lebesgue criterion for Riemann integrability therefore applies.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
