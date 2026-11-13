---
schema: qual/card@1
id: E-HAT-3.B-2
kind: problem
title: "Chain homotopy as a chain map on the cone"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.B, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.B Exercise 2, printed p. 280; the statement
    matches the print, including the bracketed hint $h(c)=f(e\otimes c)$, and the differential
    formula $\partial(e\otimes c)=(v_1-v_0)\otimes c-e\otimes\partial c$ agrees with the Koszul sign
    rule applied to the degree-one element $e$. The converse direction, which the card had compressed
    into "the differential formulas show that $f$ commutes with $\partial$ on every summand", is now
    verified on both kinds of generators, and the mutual inverseness of the two constructions is
    stated; the degree count $(I\otimes C)_n=(I_0\otimes C_n)\oplus(I_1\otimes C_{n-1})$ and the fact
    that $h$ raises degree by one are now spelled out rather than left in a one-word proof. No
    published solution of this exercise is in the retained sets — Sam has no §3.B at all, Stanford
    215C solution2 covers only §3.B exercises 1 and 3, Li's contents stop at §3.3, and DeMason's
    chapter-three appendix appears nowhere in his table of contents — recorded in COMPLAINTS.md.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 2 of §3.B on printed p. 280,
    identical in the current online text, and the card states it word for word, including the
    bracketed hint $h(c)=f(e\otimes c)$. The obligation that #123 records is unchanged and stays
    open: no published solution of this exercise was located. Searched without result in the
    retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math
    205B help file, May, Bredon, Weibel's chapters 2--3 extracts, Maxim's Math 752 notes) and in
    Hatcher's text and errata.
---

::: {.problem}
Let $C$ and $C'$ be chain complexes, and let $I$ be the chain complex consisting of $\ZZ$ in dimension 1 and $\ZZ \times \ZZ$ in dimension 0, with the boundary map taking a generator $e$ in dimension 1 to the difference $v_1 - v_0$ of generators $v_i$ of the two $\ZZ$'s in dimension 0. Show that a chain map $f: I \otimes C \to C'$ is precisely the same as a chain homotopy between the two chain maps $f_i: C \to C'$, $c \mapsto f(v_i \otimes c)$, $i = 0, 1$.
[The chain homotopy is $h(c) = f(e \otimes c)$.]
:::

::: {.solution}

::: pf

::: pf-step

$I \otimes C$ has, in degree $n$, the group $(I_0 \otimes C_n) \oplus (I_1 \otimes C_{n-1}) = (v_0 \otimes C_n) \oplus (v_1 \otimes C_n) \oplus (e \otimes C_{n-1})$.

::: pf-proof

$I_0 = \ZZ v_0 \oplus \ZZ v_1$ and $I_1 = \ZZ e$, so $I \otimes C$ in degree $n$ is $(I_0 \otimes C_n) \oplus (I_1 \otimes C_{n-1})$.

:::

:::

::: {.pf-step #s2}

The boundary of $I \otimes C$ is $\partial(v_i \otimes c) = v_i \otimes \partial c$ and $\partial(e \otimes c) = (v_1 - v_0) \otimes c - e \otimes \partial c$.

::: pf-proof

$\partial(e) = v_1 - v_0$, and the boundary of a tensor product is $\partial(a \otimes c) = \partial a \otimes c + (-1)^{\gradeddegree{a}} a \otimes \partial c$.

:::

:::

::: pf-step

A chain map $f: I \otimes C \to C'$ is determined by its values on $v_0 \otimes c$, $v_1 \otimes c$, and $e \otimes c$.

::: pf-proof

The three families $v_0\otimes c$, $v_1\otimes c$ and $e\otimes c$ for $c\in C$ generate $I\otimes C$ as an abelian group, and a homomorphism is determined by its values on generators.

:::

:::

::: {.pf-step #s4}

Define $f_i(c) = f(v_i \otimes c)$ for $i = 0, 1$, and $h(c) = f(e \otimes c)$.

::: pf-proof

The two maps $f_i:C\to C'$ are the maps $c\mapsto f(v_i\otimes c)$, included in $C'$ in degree $\deg c$; the map $h$ sends $c$ to $f(e\otimes c)\in C'_{\deg c+1}$, so $h$ raises degree by one.

:::

:::

::: {.pf-step #s5}

The chain map condition on $e \otimes c$ gives $f_1 - f_0 = \partial h + h \partial$.

::: pf-proof

::: {.pf-step #s5-1}

$f(\partial(e \otimes c)) = \partial f(e \otimes c)$.

::: pf-proof

$f$ is a chain map.

:::

:::

::: {.pf-step #s5-2}

$f(\partial(e \otimes c)) = f((v_1 - v_0) \otimes c - e \otimes \partial c) = f_1(c) - f_0(c) - h(\partial c)$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s5-3}

$\partial f(e \otimes c) = \partial h(c)$.

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: pf-step

Hence $f_1(c) - f_0(c) - h(\partial c) = \partial h(c)$, i.e. $f_1 - f_0 = \partial h + h \partial$.

::: pf-proof

Steps [](#s5-1){.pf-ref}, [](#s5-2){.pf-ref} and [](#s5-3){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s6}

The chain map condition on $v_i \otimes c$ gives that $f_i$ is a chain map.

::: pf-proof

$f(\partial(v_i \otimes c)) = f(v_i \otimes \partial c) = f_i(\partial c)$ equals $\partial f(v_i \otimes c) = \partial f_i(c)$, so $f_i \partial = \partial f_i$.

:::

:::

::: {.pf-step #s7}

Hence $f$ determines a chain homotopy $h$ between the chain maps $f_0$ and $f_1$.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

Conversely, given chain maps $f_0,f_1:C\to C'$ and a homomorphism $h:C\to C'$ of degree one with $f_1-f_0=\partial h+h\partial$, define $f$ on the generators of Step [](#s4){.pf-ref} by $f(v_i\otimes c)=f_i(c)$ and $f(e\otimes c)=h(c)$, extended linearly. It is a chain map, and only the two kinds of generators need checking.

On $v_i\otimes c$ the boundary is $\partial(v_i\otimes c)=v_i\otimes\partial c$ by the formula of Step [](#s2){.pf-ref}, so
$$
f\partial(v_i\otimes c)=f_i(\partial c)=\partial f_i(c)=\partial f(v_i\otimes c),
$$
using that $f_i$ is a chain map.

On $e\otimes c$ the boundary is $\partial(e\otimes c)=(v_1-v_0)\otimes c-e\otimes\partial c$, so
$$
f\partial(e\otimes c)=f_1(c)-f_0(c)-h(\partial c)=\partial h(c)=\partial f(e\otimes c),
$$
using the homotopy relation. These two computations are exactly the inverse of the constructions taking a chain map to $(f_0,f_1,h)$: the $v_i$-values recover $f_i$, the $e$-values recover $h$, and the two computations above are the two halves of the chain map condition for $f$, which is what Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} extract from it. So the two constructions undo each other, and chain maps $I\otimes C\to C'$ correspond bijectively to chain homotopies between chain maps $C\to C'$.

:::
