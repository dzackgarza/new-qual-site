---
schema: qual/card@1
id: P-BKF11-6A
kind: problem
title: Centerless groups have centerless automorphism groups
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked conjugation of inner automorphisms by arbitrary automorphisms and
    the criterion for two inner automorphisms to be equal.
---

::: {.problem}
Let $G$ be a group.
Show that if $G$ has trivial center, then its automorphism group $\Aut(G)$ has trivial center.
:::

::: {.solution}
Assume
$$
Z(G)=\{e\}.
$$
For $a\in G$, let
$$
c_a\colon G\to G,
\qquad
c_a(x)\coloneqq axa^{-1}
$$
be the inner automorphism determined by $a$.

::: pf

::: {.pf-step #s1}

For every $h\in\Aut(G)$ and $a\in G$,
$$
h\circ c_a\circ h^{-1}=c_{h(a)}.
$$

::: pf-proof

For every $x\in G$,
$$
\begin{aligned}
(h\circ c_a\circ h^{-1})(x)
&=h\bigl(a h^{-1}(x)a^{-1}\bigr)\\
&=h(a)x h(a)^{-1}\\
&=c_{h(a)}(x).
\end{aligned}
$$
Thus the two automorphisms agree on every element of $G$.

:::

:::

::: {.pf-step #s2}

For $a,b\in G$,
$$
c_a=c_b
$$
if and only if
$$
b^{-1}a\in Z(G).
$$

::: pf-proof

Suppose first that $c_a=c_b$. Then for every $x\in G$,
$$
axa^{-1}=bxb^{-1}.
$$
Multiplying on the left by $b^{-1}$ and on the right by $a$ gives
$$
(b^{-1}a)x=x(b^{-1}a).
$$
Hence $b^{-1}a\in Z(G)$.

Conversely, if $b^{-1}a\in Z(G)$, write $a=bz$ with $z\in Z(G)$.
Then for every $x\in G$,
$$
axa^{-1}
=bzxz^{-1}b^{-1}
=bxb^{-1},
$$
so $c_a=c_b$.

:::

:::

::: {.pf-step #s3}

Every element of $Z(\Aut(G))$ is the identity automorphism.

::: pf-proof

Let $h\in Z(\Aut(G))$. Since every $c_a$ belongs to $\Aut(G)$,
centrality gives
$$
h\circ c_a\circ h^{-1}=c_a
$$
for every $a\in G$. By step [](#s1){.pf-ref},
$$
c_{h(a)}=c_a.
$$
Step [](#s2){.pf-ref} therefore gives
$$
a^{-1}h(a)\in Z(G)=\{e\}.
$$
Thus $h(a)=a$ for every $a\in G$, so
$$
h=\operatorname{id}_G.
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{Z(\Aut(G))=\{\operatorname{id}_G\}}.
$$

::: pf-proof

The identity automorphism belongs to the center of every automorphism
group, and step [](#s3){.pf-ref} shows that no other automorphism does.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is exactly the required conclusion.

:::

:::

:::
