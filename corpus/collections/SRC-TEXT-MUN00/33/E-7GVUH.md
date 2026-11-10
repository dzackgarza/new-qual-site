---
schema: qual/card@1
id: E-7GVUH
kind: problem
title: Level sets of the Urysohn function
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.1, page 1 of the file (tmp/sources/munkres-solutions-poulsen-S33.pdf,
    Internet Archive snapshot 20200331153844 of web.math.ku.dk/~moller/e02/3gt/opg/S33.pdf), and
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 33.1, printed pp. 7-9
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 33 Exercise 1, printed p. 212, and the proof of Theorem 33.1. Both sources prove the two
    inclusions by the criterion x in U_p for all p > r versus x in U_q for some q < r. What was
    corrected: Moller separates r = 0 and r = 1 and assumes r in (0,1) otherwise, and Doug's World
    introduces the symbol "Us" for U_p; the card treats all r uniformly through the two
    characterisations f(x) <= r iff x in the intersection and f(x) < r iff x in the union.
---

::: {.exercise}

Examine the proof of the Urysohn lemma, and show that for given $r$,

$$
f^{-1}(r) = \bigcap_{p > r} U_p - \bigcup_{q < r} U_q,
$$

where $p, q$ range over the rationals.
:::

::: {.solution}

::: pf

::: pf-step
Definition and properties of the Urysohn function $f$:
Let $\{U_p\}_{p \in \QQ}$ be the nested collection of open sets satisfying $\overline{U}_p \subseteq U_{p'}$ for all rationals $p < p'$, with $U_p = \varnothing$ for $p < 0$ and $U_p = X$ for $p > 1$. The function $f: X \to [0, 1]$ is defined by:
$$f(x) = \inf \{p \in \QQ \mid x \in U_p\}.$$
:::

::: {.pf-step #sublevel-set-characterization}
Characterization of the sublevel set $\{x \in X \mid f(x) \le r\}$:
$f(x) \le r \iff x \in \bigcap_{p > r, p \in \QQ} U_p$.

::: pf-proof

::: pf-step
If $f(x) \le r$, then for any rational $p > r$, since $\inf\{t \in \QQ \mid x \in U_t\} \le r < p$, there exists a rational $t < p$ with $x \in U_t$. Because $t < p$, $U_t \subseteq U_p$, so $x \in U_p$. Thus $x \in \bigcap_{p > r} U_p$.
:::

::: pf-step
Conversely, if $x \in \bigcap_{p > r} U_p$, then $x \in U_p$ for every rational $p > r$, which means $f(x) \le p$ for all rational $p > r$. Taking the infimum over all $p > r$ yields $f(x) \le r$.
:::

:::

:::

::: {.pf-step #strict-sublevel-set-characterization}
Characterization of the strict sublevel set $\{x \in X \mid f(x) < r\}$:
$f(x) < r \iff x \in \bigcup_{q < r, q \in \QQ} U_q$.

::: pf-proof

::: pf-step
If $f(x) < r$, by definition of the infimum, there exists a rational $q$ with $x \in U_q$ such that $q < r$. Hence $x \in \bigcup_{q < r} U_q$.
:::

::: pf-step
Conversely, if $x \in \bigcup_{q < r} U_q$, then $x \in U_q$ for some rational $q < r$. Then $f(x) \le q < r$, so $f(x) < r$.
:::

:::

:::

::: pf-step
Evaluation of the level set $f^{-1}(r)$:

::: pf-proof

::: pf-step
For any point $x \in X$, $f(x) = r$ if and only if $f(x) \le r$ and $f(x) \not< r$.
:::

::: pf-step
By steps [](#sublevel-set-characterization){.pf-ref} and [](#strict-sublevel-set-characterization){.pf-ref}:
$$f(x) = r \iff x \in \left( \bigcap_{p > r, p \in \QQ} U_p \right) \quad \text{and} \quad x \notin \left( \bigcup_{q < r, q \in \QQ} U_q \right).$$
:::

::: pf-step
Set-theoretically, this is equivalent to:
$$x \in \bigcap_{p > r, p \in \QQ} U_p \setminus \bigcup_{q < r, q \in \QQ} U_q.$$
:::

:::

:::

::: pf-step
Conclusion:
$$f^{-1}(r) = \bigcap_{p > r} U_p - \bigcup_{q < r} U_q.$$
:::

:::

:::
