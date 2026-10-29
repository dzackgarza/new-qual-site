---
schema: qual/card@1
id: P-UCLAB03S-03
kind: problem
title: A subset of the real line that is neither F-sigma nor G-delta
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Examination, May 2003 PDF.
---

::: {.problem}
Find a subset $S\subset\RR$ such that both of the following hold:

(i) $S$ is not a countable union of closed sets;

(ii) $S$ is not a countable intersection of open sets.
:::

::: {.solution}

Let
$$
S=(\QQ\cap(-\infty,0))\cup((\RR\setminus\QQ)\cap(0,\infty)).
$$

::: pf

::: {.pf-step #s1-1}

The set $\QQ\cap(-\infty,0)$ is not a countable intersection of open subsets of $(-\infty,0)$.


::: pf-proof

Suppose instead that
$$
\QQ\cap(-\infty,0)=\bigcap_{n=1}^{\infty}U_n
$$
with each $U_n$ open in $(-\infty,0)$. Since $\QQ\cap(-\infty,0)$ is dense in $(-\infty,0)$, every $U_n$ is dense there.

Enumerate $\QQ\cap(-\infty,0)=\{q_1,q_2,\ldots\}$. Each set
$$
(-\infty,0)\setminus\{q_m\}
$$
is open and dense in $(-\infty,0)$. Because $(-\infty,0)$ is a Baire space, the intersection
$$
\bigcap_{n=1}^{\infty}U_n
\cap
\bigcap_{m=1}^{\infty}\bigl(( -\infty,0)\setminus\{q_m\}\bigr)
$$
is nonempty. But the first intersection equals $\QQ\cap(-\infty,0)$, while the second excludes every rational point, so their intersection is empty. This contradiction proves the claim.

:::

:::

::: {.pf-step #s1-2}

The set $(\RR\setminus\QQ)\cap(0,\infty)$ is not a countable union of closed subsets of $(0,\infty)$.


::: pf-proof

Suppose instead that
$$
(\RR\setminus\QQ)\cap(0,\infty)
=
\bigcup_{n=1}^{\infty}F_n
$$
with each $F_n$ closed in $(0,\infty)$. Since $F_n$ contains no rational point and the rationals are dense in $(0,\infty)$, $F_n$ has empty interior. Hence each $F_n$ is nowhere dense in $(0,\infty)$.

The set $\QQ\cap(0,\infty)$ is countable, so it is also a countable union of nowhere dense singletons. Therefore
$$
(0,\infty)
=
\bigl((\RR\setminus\QQ)\cap(0,\infty)\bigr)
\cup
\bigl(\QQ\cap(0,\infty)\bigr)
$$
would be a countable union of nowhere dense subsets of itself, contradicting the Baire category theorem.

:::

:::

::: {.pf-step #s1-3}

The set $S$ is not a countable union of closed subsets of $\RR$.


::: pf-proof

Suppose
$$
S=\bigcup_{n=1}^{\infty}C_n
$$
with each $C_n$ closed in $\RR$. Intersecting with the open subspace $(0,\infty)$ gives
$$
S\cap(0,\infty)
=
\bigcup_{n=1}^{\infty}(C_n\cap(0,\infty)),
$$
where each $C_n\cap(0,\infty)$ is closed in $(0,\infty)$. By the definition of $S$,
$$
S\cap(0,\infty)=(\RR\setminus\QQ)\cap(0,\infty),
$$
contradicting step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The set $S$ is not a countable intersection of open subsets of $\RR$.


::: pf-proof

Suppose
$$
S=\bigcap_{n=1}^{\infty}V_n
$$
with each $V_n$ open in $\RR$. Intersecting with the open subspace $(-\infty,0)$ gives
$$
S\cap(-\infty,0)
=
\bigcap_{n=1}^{\infty}(V_n\cap(-\infty,0)),
$$
where each $V_n\cap(-\infty,0)$ is open in $(-\infty,0)$. By the definition of $S$,
$$
S\cap(-\infty,0)=\QQ\cap(-\infty,0),
$$
contradicting step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{S=(\QQ\cap(-\infty,0))\cup((\RR\setminus\QQ)\cap(0,\infty))}
$$
satisfies both required conditions.


::: pf-proof

Step [](#s1-3){.pf-ref} proves condition (i), and step [](#s1-4){.pf-ref} proves condition (ii).

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested subset.

:::

:::

:::
