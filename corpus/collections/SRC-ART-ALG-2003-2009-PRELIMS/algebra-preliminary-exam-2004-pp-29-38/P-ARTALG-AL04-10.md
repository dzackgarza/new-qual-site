---
schema: qual/card@1
id: P-ARTALG-AL04-10
kind: problem
title: Non-Galois degree-3 extension and Galois subfield
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

(a) Give an example of an extension of degree 3 over $\mathbb{Q}$ which is not Galois over $\mathbb{Q}$.

(b) Suppose $K$ is a Galois extension of $\mathbb{Q}$ with $[K:\mathbb{Q}] = 105$, and that $L$ is a subfield of $K$ with $[L:\mathbb{Q}] = 3$.
Show that $L$ is Galois over $\mathbb{Q}$.

::: {.solution}
**Part (a).**

<1>1. $\QQ(\sqrt[3]{2})$ is a degree-$3$ extension of $\QQ$ that is not Galois.
::: {.proof}
$x^3 - 2$ is irreducible over $\QQ$ (Eisenstein at $2$), so $[\QQ(\sqrt[3]{2}):\QQ] = 3$.
:::

<1>2. $\QQ(\sqrt[3]{2})$ is not Galois over $\QQ$.
::: {.proof}
the other roots of $x^3 - 2$ are $\sqrt[3]{2}\omega$ and $\sqrt[3]{2}\omega^2$ (where $\omega$ is a primitive cube root of unity), which are not real, hence not in $\QQ(\sqrt[3]{2}) \subseteq \RR$; so $\QQ(\sqrt[3]{2})$ is not a splitting field, hence not Galois.
:::

**Part (b).**

<1>1. Let $G = \operatorname{Gal}(K/\QQ)$; then $|G| = 105 = 3 \cdot 5 \cdot 7$.
::: {.proof}
$K/\QQ$ is Galois, so $|G| = [K:\QQ]$.
:::

<1>2. $L$ corresponds to a subgroup $H = \operatorname{Gal}(K/L)$ of $G$ of index $3$.
::: {.proof}
$[L:\QQ] = 3$, so $[K:L] = 105/3 = 35$, and $|H| = 35$.
:::

<1>3. $H$ is normal in $G$.
<2>1. $n_7 \equiv 1 \pmod 7$ and $n_7 \mid 15$, so $n_7 \in \{1, 15\}$.
::: {.proof}
Sylow's third theorem.
:::
<2>2. $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 21$, so $n_5 \in \{1, 21\}$.
::: {.proof}
Sylow's third theorem.
:::
<2>3. $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 35$, so $n_3 \in \{1, 7\}$.
::: {.proof}
Sylow's third theorem.
:::
<2>4. $G$ has a normal Sylow $7$-subgroup.
::: {.proof}
if $n_7 = 15$, then $G$ has $15 \cdot 6 = 90$ elements of order $7$; the remaining $15$ elements must form the (unique) Sylow $3$- and $5$-subgroups, forcing $n_3 = n_5 = 1$; but then the Sylow $3$- and $5$-subgroups are normal, and their product is a normal subgroup of order $15$, whose quotient has order $7$ (cyclic), making $G$ abelian, contradicting $n_7 = 15$. Hence $n_7 = 1$.
:::
<2>5. Hence $G$ has a normal subgroup of order $7$.
::: {.proof}
<2>4.
:::

<1>4. $H$ has order $35 = 5 \cdot 7$, and it contains the normal Sylow $7$-subgroup of $G$.
::: {.proof}
$|H| = 35$, so $H$ contains a Sylow $7$-subgroup, which is the unique (normal) one of $G$.
:::

<1>5. $H$ is normal in $G$.
<2>1. $H$ has index $3$ in $G$.
::: {.proof}
<1>2.
:::
<2>2. A subgroup of index $3$ is normal if it contains a normal subgroup of $G$ of index $3$ in $H$... more directly: $H$ has order $35$ and contains the normal subgroup $P_7$ (order $7$) of $G$; the quotient $H/P_7$ has order $5$, and $G/P_7$ has order $15$.
<2>3. $H/P_7$ is a subgroup of $G/P_7$ of order $5$, and $G/P_7$ has order $15 = 3 \cdot 5$; the number of Sylow $5$-subgroups of $G/P_7$ is $1$ (since $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 3$ forces $n_5 = 1$), so $H/P_7$ is the unique (hence normal) Sylow $5$-subgroup of $G/P_7$.
::: {.proof}
Sylow's theorem in the quotient.
:::
<2>4. Hence $H/P_7 \trianglelefteq G/P_7$, so $H \trianglelefteq G$.
::: {.proof}
the preimage of a normal subgroup is normal.
:::

<1>6. Since $H$ is normal in $G$, $L$ is Galois over $\QQ$.
::: {.proof}
fundamental theorem of Galois theory: $L$ is Galois over $\QQ$ iff $H = \operatorname{Gal}(K/L)$ is normal in $G$.
:::

<1>7. Q.E.D.
::: {.proof}
<1>2 (a) and <1>6 (b).
:::
:::
