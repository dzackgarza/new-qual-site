---
schema: qual/card@1
id: P-AGH449ISOGENY
kind: problem
title: Isogeny is an equivalence relation with countable isogeny classes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.9 together with IV.4.7. For part (b), checked the
    quotient-by-kernel theorem for separable isogenies and retained the
    Frobenius factor in positive characteristic so that purely inseparable
    isogenies are also counted.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
We say two elliptic curves $X, X'$ are **isogenous** if there is a finite morphism $f: X \to X'$.

a. Show that isogeny is an equivalence relation.

b. For any elliptic curve $X$, show that the set of elliptic curves $X'$ isogenous to $X$, up to isomorphism, is countable.
Hint: $X'$ is uniquely determined by $X$ and $\ker f$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Isogeny is reflexive.

::: pf-proof

For every elliptic curve $X$, the identity
$$
\id_X:X\longrightarrow X
$$
is finite. Hence $X$ is isogenous to itself.

:::

:::

::: {.pf-step #s2}

Isogeny is symmetric.

::: pf-proof

Suppose that
$$
f:X\longrightarrow X'
$$
is finite. It is nonconstant, so $\deg f>0$. By
[[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(a),(f)]], the dual morphism
$$
\hat f:X'\longrightarrow X
$$
has
$$
\deg\hat f=\deg f>0.
$$
A nonconstant morphism of projective nonsingular curves is finite. Thus
$\hat f$ is a finite morphism from $X'$ to $X$.

:::

:::

::: {.pf-step #s3}

Isogeny is transitive.

::: pf-proof

If
$$
X\xrightarrow{f}X'\xrightarrow{g}X''
$$
are finite morphisms, then $g\circ f$ is finite. Hence an elliptic curve
isogenous to one isogenous to $X$ is itself isogenous to $X$. Together with
steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, this proves part (a).

:::

:::

::: {.pf-step #s4}

For counting targets, every finite morphism $f:X\to X'$ may be
replaced by an isogeny preserving the origins without changing $X'$.

::: pf-proof

Let $O\in X$ and $O'\in X'$ be the chosen origins. Translation on $X'$ is
an automorphism. Therefore
$$
g(P)=f(P)-f(O)
$$
is again finite and has the same target curve. It sends $O$ to $O'$, hence
is a homomorphism of elliptic curves.

:::

:::

::: {.pf-step #s5}

A separable isogeny
$$
h:E\longrightarrow E'
$$
is determined, up to isomorphism of its target, by the finite subgroup
$$
G=\ker h\subseteq E(k).
$$

::: pf-proof

For each $T\in G$, translation $\tau_T$ is an automorphism of $E$ over
$E'$. Since $h$ is separable,
$$
[k(E):h^*k(E')]=\deg h=\#G.
$$
The translations by $G$ already give $\#G$ distinct automorphisms of this
function-field extension. Hence
$$
h^*k(E')=k(E)^G.
$$
The right-hand side depends only on $E$ and $G$. A nonsingular projective
curve is determined up to isomorphism by its function field, so the target
$E'$ is determined up to isomorphism by $E$ and $G$.

:::

:::

::: {.pf-step #s6}

For a fixed elliptic curve $E$, there are only countably many pairs
$(r,G)$ in which $r\ge0$ and $G$ is a finite subgroup of
$E^{(p^r)}(k)$.

::: pf-proof

Fix $r$. Every finite subgroup $G\subseteq E^{(p^r)}(k)$ has finite
exponent, say $n$, and therefore
$$
G\subseteq E^{(p^r)}[n](k).
$$
The $n$-torsion set is finite. Hence it has only finitely many subgroups.
Taking the union over $n\ge1$ shows that $E^{(p^r)}(k)$ has only countably
many finite subgroups. Taking the further union over $r\ge0$ remains
countable.

In characteristic zero, only the case $r=0$ is needed.

:::

:::

::: {.pf-step #s7}

Up to isomorphism, only countably many elliptic curves are isogenous
to $X$.

::: pf-proof

By step [](#s4){.pf-ref}, consider only isogenies $g:X\to X'$ preserving origins.
In characteristic zero, $g$ is separable, so step [](#s5){.pf-ref} says that $X'$ is
determined by the finite subgroup $\ker g\subseteq X(k)$. Step [](#s6){.pf-ref} gives
only countably many possibilities.

Now suppose $\characteristic k=p>0$. The separable--inseparable
factorization of $g$ has the form
$$
X
\xrightarrow{F_X^{(r)}}
X^{(p^r)}
\xrightarrow{h}
X',
$$
where $r\ge0$, $F_X^{(r)}$ is the $r$-fold relative Frobenius, and $h$ is
separable. By step [](#s5){.pf-ref}, for fixed $r$ the target $X'$ is determined up to
isomorphism by
$$
G=\ker h\subseteq X^{(p^r)}(k).
$$
Thus every possible $X'$ is determined by one of the countably many pairs
$(r,G)$ from step [](#s6){.pf-ref}. This proves part (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove that isogeny is an equivalence relation, and steps
[](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove that each isogeny class contains only countably many
isomorphism classes of elliptic curves.

:::

:::

:::
