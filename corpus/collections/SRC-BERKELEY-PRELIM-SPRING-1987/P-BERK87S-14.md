---
schema: qual/card@1
id: P-BERK87S-14
kind: problem
title: The unique noncyclic group of order four has automorphism group $S_3$
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
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used Lagrange's theorem to show that every nonidentity element of a
    noncyclic group of order four has order two, which identifies the group
    with the Klein four group. Restriction to the three nonidentity elements
    identifies its automorphisms with all permutations of those elements.
---

::: {.problem}
1. Show that, up to isomorphism, there is exactly one noncyclic group $G$ of order $4$.
2. Show that
   \[
   \operatorname{Aut}(G)\cong S_3.
   \]
:::

::: {.solution}
Let $e$ denote the identity of $G$.

::: pf

::: {.pf-step #elements-order-two}
If $G$ is noncyclic of order $4$, every element of $G\setminus\{e\}$
has order $2$.

::: pf-proof
By Lagrange's theorem, the order of a nonidentity element divides $4$, so
it is either $2$ or $4$. An element of order $4$ would generate all of
$G$, contradicting the assumption that $G$ is noncyclic. Hence every
nonidentity element has order $2$.
:::

:::

::: {.pf-step #unique-group}
Up to isomorphism, the only noncyclic group of order $4$ is
$$
\ZZ/2\ZZ\times\ZZ/2\ZZ.
$$

::: pf-proof
Choose distinct nonidentity elements $a,b\in G$. By step [](#elements-order-two){.pf-ref},
$a^2=b^2=e$. The product $ab$ is neither $e$, $a$, nor $b$: the three
possibilities would respectively imply $a=b$, $b=e$, or $a=e$. Thus, if
$c$ denotes the third nonidentity element, then $ab=c$.

Again by step [](#elements-order-two){.pf-ref}, $c^{-1}=c$. Therefore
$$
ba
=(ab)^{-1}
=c^{-1}
=c
=ab,
$$
so $G$ is abelian. The map
$$
e\longmapsto(0,0),\qquad
a\longmapsto(1,0),\qquad
b\longmapsto(0,1),\qquad
c\longmapsto(1,1)
$$
is then an isomorphism from $G$ to
$\ZZ/2\ZZ\times\ZZ/2\ZZ$: it is bijective, and the relations
$a^2=b^2=e$, $ab=ba=c$ imply $c^2=e$, $ac=b$, and $bc=a$, so the
displayed map preserves every product. This proves uniqueness up to
isomorphism.

Set
$$
\Omega\coloneqq G\setminus\{e\}.
$$
By this step, $\Omega$ has three elements.
:::

:::

::: {.pf-step #restriction-injective}
Restriction to $\Omega$ defines an injective homomorphism
$$
\Phi:\Aut(G)\longrightarrow\operatorname{Sym}(\Omega)\cong S_3.
$$

::: pf-proof
Every automorphism fixes $e$ and therefore permutes the three elements of
$\Omega$, so restriction defines $\Phi$. If an automorphism lies in the
kernel of $\Phi$, it fixes every element of $\Omega$ and also fixes $e$;
hence it is the identity automorphism. Thus $\Phi$ is injective.
:::

:::

::: {.pf-step #permutation-extends}
Every permutation of $\Omega$ extends to an automorphism of $G$.

::: pf-proof
Let $\sigma\in\operatorname{Sym}(\Omega)$ and extend it to $G$ by setting
$\sigma(e)=e$. We verify that this extension preserves products.

If one factor is $e$, preservation is immediate. If $x=y\in\Omega$, then
step [](#elements-order-two){.pf-ref} gives
$$
\sigma(xy)=\sigma(e)=e=\sigma(x)^2.
$$
If $x,y\in\Omega$ are distinct, the cancellation argument in step [](#unique-group){.pf-ref}
shows that $xy$ is the unique element of
$\Omega\setminus\{x,y\}$. The elements $\sigma(x)$ and $\sigma(y)$ are
also distinct, and their product is the unique element of
$\Omega\setminus\{\sigma(x),\sigma(y)\}$, namely $\sigma(xy)$. Thus
$$
\sigma(xy)=\sigma(x)\sigma(y)
$$
in every case. Since the extension is bijective, it is an automorphism of
$G$.
:::

:::

::: {.pf-step #aut-iso-boxed}
One has
$$
\boxed{\Aut(G)\cong S_3}.
$$

::: pf-proof
Step [](#restriction-injective){.pf-ref} gives an injective homomorphism
$\Phi:\Aut(G)\to\operatorname{Sym}(\Omega)$, and step [](#permutation-extends){.pf-ref} shows that
every permutation of $\Omega$ is in its image. Hence $\Phi$ is an
isomorphism. Since $\abs{\Omega}=3$,
$\operatorname{Sym}(\Omega)\cong S_3$.
:::

:::

::: pf-qed
Step [](#unique-group){.pf-ref} proves part (1), and step [](#aut-iso-boxed){.pf-ref} proves part (2).
:::

:::
:::
