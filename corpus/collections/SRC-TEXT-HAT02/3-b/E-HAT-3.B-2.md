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
---

::: {.problem}
Let $C$ and $C'$ be chain complexes, and let $I$ be the chain complex consisting of $\mathbb{Z}$ in dimension 1 and $\mathbb{Z} \times \mathbb{Z}$ in dimension 0, with the boundary map taking a generator $e$ in dimension 1 to the difference $v_1 - v_0$ of generators $v_i$ of the two $\mathbb{Z}$'s in dimension 0. Show that a chain map $f: I \otimes C \to C'$ is precisely the same as a chain homotopy between the two chain maps $f_i: C \to C'$, $c \mapsto f(v_i \otimes c)$, $i = 0, 1$.
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

$\partial(e) = v_1 - v_0$, and the boundary of a tensor product is $\partial(a \otimes c) = \partial a \otimes c + (-1)^{|a|} a \otimes \partial c$.

:::

:::

::: pf-step

A chain map $f: I \otimes C \to C'$ is determined by its values on $v_0 \otimes c$, $v_1 \otimes c$, and $e \otimes c$.

::: pf-proof

these generate $I \otimes C$.

:::

:::

::: {.pf-step #s4}

Define $f_i(c) = f(v_i \otimes c)$ for $i = 0, 1$, and $h(c) = f(e \otimes c)$.

::: pf-proof

definition.

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

Hence $f$ is exactly a chain homotopy $h$ between the chain maps $f_0$ and $f_1$.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
