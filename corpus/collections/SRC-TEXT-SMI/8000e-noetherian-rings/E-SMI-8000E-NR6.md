---
schema: qual/card@1
id: E-SMI-8000E-NR6
kind: problem
title: Unions of chains of proper ideals are proper
classification:
  areas:
  - algebra
  topics:
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the chain-union statement with the local 8000e PDF and extraction, Noetherian-rings problem 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used total ordering to place any two elements in one chain member, and used the identity element to show the union remains proper."
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: "The printed statement omits nonemptiness; the empty union is not an ideal."
- event: source-corrected
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith 8000e.pdf page 5, problem 6: "If {I_j}
    is any linearly ordered indexed set of proper ideals in a ring R ... then their
    union is a proper ideal." Two hypotheses are missing and both are now on the
    statement. Nonemptiness was already added, since the empty union is not an
    ideal. With identity is added here: the proof of properness needs
    1_R ∈ U ⇒ 1_R ∈ I_j for some j, and without an identity the claim is false, as
    the closing remark shows with the additive group of Z under zero
    multiplication and the chain 2Z ⊃ 4Z ⊃ 8Z ⊃ ..., whose union is all of R.
    The ideal axioms and the symmetric two-sided argument were checked and are
    correct under the identity hypothesis.
---
---

::: {.exercise}
If $\theset{I_j}$ is any nonempty linearly ordered indexed set of proper ideals in a ring $R$ with identity — i.e. for any two ideals $I_j$ and $I_k$, one is contained in the other — then their union is a proper ideal.

The identity hypothesis is needed and is supplied here: without it the union of a chain of proper ideals can be all of $R$, as the closing remark shows.
:::

::: {.solution}
Let
$$
J=\bigcup_j I_j.
$$

::: pf

::: pf-step

The union $J$ is an ideal of $R$.

::: pf-proof

First, $0\in I_j$ for every $j$, so $0\in J$.

Let $x,y\in J$. Then $x\in I_j$ and $y\in I_k$ for some $j,k$. Because the
family is linearly ordered by inclusion, either
$$
I_j\subseteq I_k
$$
or
$$
I_k\subseteq I_j.
$$
In either case there is one chain member containing both $x$ and $y$. Since
that member is an ideal, it contains
$$
x-y.
$$
Thus $x-y\in J$.

If $r\in R$ and $x\in J$, choose $j$ with $x\in I_j$. Then
$$
rx\in I_j\subseteq J.
$$
Hence $J$ is an ideal.

:::

:::

::: pf-step

The ideal $J$ is proper.

::: pf-proof

If $J=R$, then in particular
$$
1\in J.
$$
Thus $1\in I_j$ for some $j$, which would imply
$$
I_j=R,
$$
contradicting the hypothesis that every $I_j$ is proper. Therefore
$$
J\ne R.
$$

:::

:::

:::

Hence
$$
\boxed{\bigcup_j I_j\text{ is a proper ideal of }R.}
$$
:::

::: remark
The identity is what makes the union proper. Without it the statement fails: let $R$ be the additive group $\ZZ$ with all products defined to be $0$, a ring without identity in which every additive subgroup is an ideal, and take the chain $2\ZZ \supsetneq 4\ZZ \supsetneq 8\ZZ \supsetneq \cdots$ of proper ideals. Its union is $\ZZ = R$, which is not a proper ideal. Smith's remaining problems in this section are stated for rings with identity, and step 2 above uses $1_R \in J \Rightarrow J = R$ exactly as the identity hypothesis allows.
:::
