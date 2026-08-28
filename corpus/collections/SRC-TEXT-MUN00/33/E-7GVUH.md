---
schema: qual/card@1
id: E-7GVUH
kind: exercise
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
---

::: {.exercise}

Examine the proof of the Urysohn lemma, and show that for given $r$,

$$
f^{-1}(r) = \bigcap_{p > r} U_p - \bigcup_{q < r} U_q,
$$

where $p, q$ range over the rationals.
:::

::: solution
**Goal:** Prove that the level set $f^{-1}(r)$ of the Urysohn function $f(x) = \inf \{p \in \mathbb{Q} \mid x \in U_p\}$ is given by the difference $\bigcap_{p > r, p \in \mathbb{Q}} U_p \setminus \bigcup_{q < r, q \in \mathbb{Q}} U_q$.

<1>1. Definition and properties of the Urysohn function $f$:
    Let $\{U_p\}_{p \in \mathbb{Q}}$ be the nested collection of open sets satisfying $\overline{U}_p \subseteq U_{p'}$ for all rationals $p < p'$, with $U_p = \varnothing$ for $p < 0$ and $U_p = X$ for $p > 1$. The function $f: X \to [0, 1]$ is defined by:
    $$f(x) = \inf \{p \in \mathbb{Q} \mid x \in U_p\}.$$

<1>2. Characterization of the sublevel set $\{x \in X \mid f(x) \le r\}$:
    $f(x) \le r \iff x \in \bigcap_{p > r, p \in \mathbb{Q}} U_p$.
    *Proof:*
    <2>1. If $f(x) \le r$, then for any rational $p > r$, since $\inf\{t \in \mathbb{Q} \mid x \in U_t\} \le r < p$, there exists a rational $t < p$ with $x \in U_t$. Because $t < p$, $U_t \subseteq U_p$, so $x \in U_p$. Thus $x \in \bigcap_{p > r} U_p$.
    <2>2. Conversely, if $x \in \bigcap_{p > r} U_p$, then $x \in U_p$ for every rational $p > r$, which means $f(x) \le p$ for all rational $p > r$. Taking the infimum over all $p > r$ yields $f(x) \le r$.

<1>3. Characterization of the strict sublevel set $\{x \in X \mid f(x) < r\}$:
    $f(x) < r \iff x \in \bigcup_{q < r, q \in \mathbb{Q}} U_q$.
    *Proof:*
    <2>1. If $f(x) < r$, by definition of the infimum, there exists a rational $q$ with $x \in U_q$ such that $q < r$. Hence $x \in \bigcup_{q < r} U_q$.
    <2>2. Conversely, if $x \in \bigcup_{q < r} U_q$, then $x \in U_q$ for some rational $q < r$. Then $f(x) \le q < r$, so $f(x) < r$.

<1>4. Evaluation of the level set $f^{-1}(r)$:
    *Proof:*
    <2>1. For any point $x \in X$, $f(x) = r$ if and only if $f(x) \le r$ and $f(x) \not< r$.
    <2>2. By <1>2 and <1>3:
        $$f(x) = r \iff x \in \left( \bigcap_{p > r, p \in \mathbb{Q}} U_p \right) \quad \text{and} \quad x \notin \left( \bigcup_{q < r, q \in \mathbb{Q}} U_q \right).$$
    <2>3. Set-theoretically, this is equivalent to:
        $$x \in \bigcap_{p > r, p \in \mathbb{Q}} U_p \setminus \bigcup_{q < r, q \in \mathbb{Q}} U_q.$$

<1>5. Conclusion:
    $$f^{-1}(r) = \bigcap_{p > r} U_p - \bigcup_{q < r} U_q.$$
    Q.E.D.
:::
