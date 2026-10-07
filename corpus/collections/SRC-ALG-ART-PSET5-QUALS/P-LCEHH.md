---
schema: qual/card@1
id: P-LCEHH
kind: problem
title: A tower of extensions with Galois group $D_4$ in which normality is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
---

::: {.problem}

Give an example of a tower of field extensions $F \subseteq E \subseteq K \subseteq L$, with $L/F$ Galois and $\mathrm{Gal}(L/F) \cong D_4$ (the dihedral group of order 8), such that $E/F$ is normal, $K/E$ is normal, but $K/F$ is not normal (i.e. exhibit a failure of transitivity of normality).
:::

::: {.solution}
Let
$$
\alpha=\sqrt[4]{2},
\qquad
F=\QQ,
\qquad
E=\QQ(\alpha^2),
\qquad
K=\QQ(\alpha),
\qquad
L=\QQ(\alpha,i).
$$

<1>1. The extension $L/F$ is Galois with Galois group isomorphic to $D_4$.
::: {.proof}
The field $L$ is the splitting field over $\QQ$ of
$$
x^4-2,
$$
whose roots are $\alpha,i\alpha,-\alpha,-i\alpha$. Define automorphisms
$$
\sigma(\alpha)=i\alpha,
\qquad
\sigma(i)=i,
$$
and
$$
\tau(\alpha)=\alpha,
\qquad
\tau(i)=-i.
$$
Then $\sigma$ has order $4$, $\tau$ has order $2$, and
$$
\tau\sigma\tau^{-1}=\sigma^{-1}.
$$
Moreover $[L:\QQ]=8$: the polynomial $x^4-2$ is Eisenstein at $2$, so $[\QQ(\alpha):\QQ]=4$, and $\QQ(\alpha)\subset\RR$ does not contain $i$, so adjoining $i$ doubles the degree. Hence these eight automorphisms exhaust $\Gal(L/F)$, and
$$
\Gal(L/F)\cong D_4.
$$
:::

<1>2. The extension $E/F$ is normal.
::: {.proof}
Since $\alpha^2=\sqrt2$,
$$
E=\QQ(\sqrt2).
$$
This is the splitting field over $\QQ$ of $x^2-2$, hence it is Galois and therefore normal over $F$.
:::

<1>3. The extension $K/E$ is normal.
::: {.proof}
Over $E$, the element $\alpha$ satisfies
$$
x^2-\sqrt2.
$$
Its two roots are $\alpha$ and $-\alpha$, both lying in $K$. Thus $K$ is the splitting field of this polynomial over $E$, so $K/E$ is Galois and in particular normal.
:::

<1>4. The extension $K/F$ is not normal.
::: {.proof}
The minimal polynomial of $\alpha$ over $\QQ$ is $x^4-2$. One of its conjugates is $i\alpha$, but
$$
K=\QQ(\alpha)\subset\RR,
$$
so $i\alpha\notin K$. Hence $x^4-2$ does not split over $K$, and $K/F$ is not normal.
:::

<1>5. Therefore
$$
\boxed{
\QQ\subset\QQ(\sqrt2)\subset\QQ(\sqrt[4]{2})\subset\QQ(\sqrt[4]{2},i)
}
$$
is a tower in which $E/F$ and $K/E$ are normal but $K/F$ is not normal, while $\Gal(L/F)\cong D_4$.
::: {.proof}
This combines step <1>1, step <1>2, step <1>3, and step <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>5 is the requested example.
:::
:::
