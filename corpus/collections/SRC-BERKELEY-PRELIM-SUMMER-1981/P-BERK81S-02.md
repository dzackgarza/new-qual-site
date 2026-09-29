---
schema: qual/card@1
id: P-BERK81S-02
kind: problem
title: A fixed-point-free involutory automorphism forces an odd abelian group
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The map psi(g)=g^{-1}phi(g) is injective: equality of two values makes
    hg^{-1} fixed by phi, hence equal to the identity. Finiteness makes psi
    surjective. If phi^2=id, applying phi to x=g^{-1}phi(g) gives
    phi(x)=x^{-1}. Since inversion is then an automorphism, G is abelian;
    and every nonidentity element is paired with a distinct inverse, so
    |G| is odd.
---

::: {.problem}
Let $G$ be a finite group and let $\varphi\in\operatorname{Aut}(G)$ fix only the identity element.

1. Show that every element of $G$ has the form
   \[
   g^{-1}\varphi(g)
   \]
   for some $g\in G$.

2. If $\varphi$ has order $2$, show that $\varphi(g)=g^{-1}$ for every $g\in G$, and deduce that $G$ is abelian of odd order.
:::

::: {.solution}
Define
$$
\psi:G\longrightarrow G,
\qquad
\psi(g)=g^{-1}\varphi(g).
$$

::: pf

::: {.pf-step #s1}

The map $\psi$ is injective.

::: pf-proof

Suppose
$$
\psi(g)=\psi(h).
$$
Then
$$
g^{-1}\varphi(g)
=
h^{-1}\varphi(h).
$$
Multiplying on the left by $h$ and on the right by $\varphi(g)^{-1}$
gives
$$
hg^{-1}
=
\varphi(h)\varphi(g)^{-1}.
$$
Because $\varphi$ is a homomorphism,
$$
\varphi(h)\varphi(g)^{-1}
=
\varphi(hg^{-1}).
$$
Thus $hg^{-1}$ is fixed by $\varphi$. The only fixed point is the identity,
so
$$
hg^{-1}=e,
$$
and hence $h=g$.

:::

:::

::: {.pf-step #s2}

The map $\psi$ is surjective.

::: pf-proof

The group $G$ is finite. An injective self-map of a finite set is
surjective, so step [](#s1){.pf-ref} gives surjectivity.

:::

:::

::: {.pf-step #s3}

Every element of $G$ can be written in the form
$$
\boxed{
g^{-1}\varphi(g)
}
$$
for some $g\in G$.

::: pf-proof

This is exactly surjectivity of $\psi$ from step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Assume now that
$$
\varphi^2=\operatorname{id}.
$$
Then for every $x\in G$,
$$
\boxed{
\varphi(x)=x^{-1}.
}
$$

::: pf-proof

By step [](#s3){.pf-ref}, write
$$
x=g^{-1}\varphi(g)
$$
for some $g\in G$. Then
$$
\begin{aligned}
\varphi(x)
&=
\varphi(g)^{-1}\varphi^2(g)\\
&=
\varphi(g)^{-1}g.
\end{aligned}
$$
But
$$
x^{-1}
=
\bigl(g^{-1}\varphi(g)\bigr)^{-1}
=
\varphi(g)^{-1}g.
$$
Hence $\varphi(x)=x^{-1}$.

:::

:::

::: {.pf-step #s5}

The group $G$ is abelian.

::: pf-proof

By step [](#s4){.pf-ref}, the inversion map is the automorphism $\varphi$, so it is a
homomorphism. Therefore for all $g,h\in G$,
$$
(gh)^{-1}
=
g^{-1}h^{-1}.
$$
On the other hand, the inverse of a product always satisfies
$$
(gh)^{-1}
=
h^{-1}g^{-1}.
$$
Thus
$$
g^{-1}h^{-1}=h^{-1}g^{-1}.
$$
Taking inverses gives
$$
gh=hg.
$$

:::

:::

::: {.pf-step #s6}

No nonidentity element of $G$ is equal to its inverse.

::: pf-proof

If
$$
g=g^{-1},
$$
then step [](#s4){.pf-ref} gives
$$
\varphi(g)=g.
$$
The only fixed point of $\varphi$ is the identity, so $g=e$.

:::

:::

::: {.pf-step #s7}

The order of $G$ is odd.

::: pf-proof

By step [](#s6){.pf-ref}, the inversion map pairs every nonidentity element $g$ with a
distinct element $g^{-1}$. Thus
$$
G\sm\{e\}
$$
is a disjoint union of two-element sets
$$
\{g,g^{-1}\}.
$$
Hence
$$
\abs G-1
$$
is even, so $\abs G$ is odd.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (1), while steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s7){.pf-ref} prove all
claims in part (2).

:::

:::

:::
