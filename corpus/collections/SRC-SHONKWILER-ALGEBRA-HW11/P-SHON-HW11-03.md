---
schema: qual/card@1
id: P-SHON-HW11-03
kind: problem
title: Prime-degree extensions and Galois subfields of the normal closure
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 3 of the retained Algebra HW 11 solution packet.
---

::: {.problem}
Let $p$ be prime and let $K\subset L$ be a separable extension of degree $p$ which is not Galois.
Let $\widetilde L$ be the Galois closure of $L/K$.
Show that $\widetilde L$ contains no subfield $M$ which is Galois over $K$ of degree $p$.
:::

::: {.solution}

Let
$$
K\subset L,
\qquad
[L:K]=p,
$$
and let
$$
\widetilde L
$$
be the Galois closure of $L/K$.

::: pf

::: pf-step

Since $L/K$ is finite separable of degree $p$, there exists
$$
\alpha\in L
$$
such that
$$
\boxed{L=K(\alpha)}.
$$


::: pf-proof

Apply the primitive element theorem.

:::

:::

::: pf-step

Let
$$
f(x)\in K[x]
$$
be the minimal polynomial of $\alpha$. Then
$$
\boxed{\deg f=p}.
$$


::: pf-proof

For a simple algebraic extension,
$$
[K(\alpha):K]=\deg m_\alpha.
$$
Use $[L:K]=p$.

:::

:::

::: pf-step

The polynomial $f$ is separable.


::: pf-proof

The extension $L/K$ is separable, so the minimal polynomial of every element of $L$, in particular $\alpha$, is separable.

:::

:::

::: pf-step

The Galois closure $\widetilde L$ is the splitting field of $f$ over $K$.


::: pf-proof

Since $L=K(\alpha)$, the normal closure of $L/K$ is obtained by adjoining all $K$-conjugates of $\alpha$, equivalently all roots of $f$.

:::

:::

::: {.pf-step #s1-5}

The action of
$$
G=\operatorname{Gal}(\widetilde L/K)
$$
on the $p$ roots of $f$ gives an injective homomorphism
$$
\boxed{G\hookrightarrow S_p}.
$$


::: pf-proof

Every $K$-automorphism of $\widetilde L$ permutes the roots of $f$. The action is faithful because $\widetilde L$ is generated over $K$ by those roots.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
[\widetilde L:K]=\cardinality{G}\mid p!}.
$$


::: pf-proof

Since $\widetilde L/K$ is finite Galois,
$$
[\widetilde L:K]=\cardinality{G}.
$$
By step [](#s1-5){.pf-ref}, $G$ is a subgroup of $S_p$, so Lagrange's theorem gives
$$
\cardinality{G}\mid\cardinality{S_p}=p!.
$$

:::

:::

::: pf-step

The compositum
$$
LM
$$
is contained in $\widetilde L$.


::: pf-proof

Both $L$ and $M$ are subfields of $\widetilde L$, so the smallest field containing both is also a subfield of $\widetilde L$.

:::

:::

::: pf-step

The extension
$$
LM/L
$$
is Galois.


::: pf-proof

The extension $M/K$ is finite Galois. Base change from $K$ to $L$ preserves separability and normality of the resulting compositum extension:
$$
LM/L
$$
is finite separable, and every $L$-embedding of $LM$ fixes $L$ and sends $M$ to itself because $M/K$ is normal. Hence $LM/L$ is Galois.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\boxed{
[LM:L]
=
[M:L\cap M]}.
$$


::: pf-proof

This is the standard degree formula for a compositum when $M/K$ is finite:
$$
[LM:L]=[M:L\cap M].
$$

:::

:::

::: {.pf-step #s1-10}

Since
$$
[M:K]=p
$$
is prime,
$$
\boxed{
[LM:L]\in\{1,p\}}.
$$


::: pf-proof

The intermediate field
$$
K\subseteq L\cap M\subseteq M
$$
has degree over $K$ dividing the prime degree $[M:K]=p$. Hence
$$
[L\cap M:K]
$$
is $1$ or $p$, and step [](#s1-9){.pf-ref} gives the two possibilities for $[LM:L]$.

:::

:::

::: {.pf-step #s1-11}

The case
$$
[LM:L]=1
$$
is impossible.


::: pf-proof

If
$$
LM=L,
$$
then
$$
M\subseteq L.
$$
But
$$
[M:K]=[L:K]=p,
$$
so the tower law forces
$$
M=L.
$$
This contradicts the hypotheses that $M/K$ is Galois while $L/K$ is not.

:::

:::

::: pf-step

Therefore
$$
\boxed{
[LM:L]=p}.
$$


::: pf-proof

Step [](#s1-10){.pf-ref} gives only the two possibilities, and step [](#s1-11){.pf-ref} excludes $1$.

:::

:::

::: pf-step

Hence
$$
\boxed{
L\cap M=K}.
$$


::: pf-proof

By step [](#s1-9){.pf-ref},
$$
p=[LM:L]=[M:L\cap M].
$$
Since
$$
[M:K]=p,
$$
the tower law
$$
[M:K]
=
[M:L\cap M]\,[L\cap M:K]
$$
gives
$$
[L\cap M:K]=1.
$$

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
[LM:K]=p^2}.
$$


::: pf-proof

Use the tower
$$
K\subset L\subset LM:
$$
$$
[LM:K]
=
[LM:L][L:K]
=
p\cdot p
=
p^2.
$$

:::

:::

::: {.pf-step #s1-15}

Since
$$
LM\subseteq\widetilde L,
$$
one has
$$
\boxed{
p^2\mid[\widetilde L:K]}.
$$


::: pf-proof

By the tower law,
$$
[\widetilde L:K]
=
[\widetilde L:LM]\,[LM:K].
$$
Apply step [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Combining steps [](#s1-6){.pf-ref} and [](#s1-15){.pf-ref},
$$
\boxed{
p^2\mid p!}.
$$


::: pf-proof

Step [](#s1-15){.pf-ref} gives
$$
p^2\mid[\widetilde L:K],
$$
and step [](#s1-6){.pf-ref} gives
$$
[\widetilde L:K]\mid p!.
$$
Divisibility is transitive.

:::

:::

::: {.pf-step #s1-17}

But
$$
\boxed{
v_p(p!)=1}.
$$


::: pf-proof

Among the factors
$$
1,2,\dots,p,
$$
the only multiple of the prime $p$ is $p$ itself, and it contributes exactly one factor of $p$.

:::

:::

::: {.pf-step #s1-18}

Hence
$$
p^2\nmid p!,
$$
contradicting step [](#s1-16){.pf-ref}.


::: pf-proof

Step [](#s1-17){.pf-ref} says the exponent of $p$ in the prime factorization of $p!$ is exactly $1$, whereas divisibility by $p^2$ would require exponent at least $2$.

:::

:::

::: {.pf-step #s1-19}

Therefore no such field $M$ exists.


::: pf-proof

The assumption of its existence led to the contradiction in step [](#s1-18){.pf-ref}.

:::

:::

::: {.pf-step #s1-20}

Thus
$$
\boxed{
\widetilde L
\text{ contains no subfield }M
\text{ with }
M/K\text{ Galois and }[M:K]=p.}
$$


::: pf-proof

This is step [](#s1-19){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-20){.pf-ref} is the required conclusion.

:::

:::

:::
