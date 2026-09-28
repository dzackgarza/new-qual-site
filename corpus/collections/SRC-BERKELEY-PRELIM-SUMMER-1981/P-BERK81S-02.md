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

<1>1. The map $\psi$ is injective.

::: {.proof}
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

<1>2. The map $\psi$ is surjective.

::: {.proof}
The group $G$ is finite. An injective self-map of a finite set is
surjective, so step <1>1 gives surjectivity.
:::

<1>3. Every element of $G$ can be written in the form
$$
\boxed{
g^{-1}\varphi(g)
}
$$
for some $g\in G$.

::: {.proof}
This is exactly surjectivity of $\psi$ from step <1>2.
:::

<1>4. Assume now that
$$
\varphi^2=\operatorname{id}.
$$
Then for every $x\in G$,
$$
\boxed{
\varphi(x)=x^{-1}.
}
$$

::: {.proof}
By step <1>3, write
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

<1>5. The group $G$ is abelian.

::: {.proof}
By step <1>4, the inversion map is the automorphism $\varphi$, so it is a
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

<1>6. No nonidentity element of $G$ is equal to its inverse.

::: {.proof}
If
$$
g=g^{-1},
$$
then step <1>4 gives
$$
\varphi(g)=g.
$$
The only fixed point of $\varphi$ is the identity, so $g=e$.
:::

<1>7. The order of $G$ is odd.

::: {.proof}
By step <1>6, the inversion map pairs every nonidentity element $g$ with a
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

<1>8. Q.E.D.

::: {.proof}
Step <1>3 proves part (1), while steps <1>4, <1>5, and <1>7 prove all
claims in part (2).
:::
:::
