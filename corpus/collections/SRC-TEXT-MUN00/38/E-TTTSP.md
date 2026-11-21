---
schema: qual/card@1
id: E-TTTSP
kind: problem
title: Compactifications of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.5, page 1 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the sheet is dated
    2 April 2005 and its section-38 items name no author; Internet Archive snapshot 20181222125939 of
    web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf). Checked against Munkres, Topology (2000), Section 38
    Exercise 5, printed p. 241, with Theorem 38.5 (the characterisation of beta(X) by extension of
    bounded real functions), Theorem 38.4 and the preceding exercise 38.4, and with the order topology of
    S_Omega = [0, Omega). What was corrected: on part (a) the card's earlier increasing-sequence argument
    chose pairs alpha_n < beta_n and then called the supremum of the beta_n a common limit of both
    sequences, which the choice of alpha_n does not give, and it then deduced |f(beta) - f(gamma)| < 1/n
    from two bounds of the form |f(beta) - f(alpha_n)| < 1/n, which only gives 2/n. The card's part (a) is
    here the sheet's argument: from the failure of the epsilon-bound one gets a single strictly increasing
    sequence gamma_n with |f(gamma_n) - f(gamma_{n-1})| >= epsilon, whose supremum lambda is a countable
    ordinal, hence below Omega, and continuity at lambda contradicts it; the 2/n is then taken correctly
    and f is constant on the tail. Parts (b) and (c) are the sheet's; (c) uses part (b) to see that
    beta(S_Omega) - S_Omega is a single point, hence so is Y - S_Omega for any compactification Y, and
    that a compactification adjoining one point to a locally compact Hausdorff space is its one-point
    compactification.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, three for (a), one for (b) and two for (c), each carrying a `pf-proof`;
    the arguments and the attribution are unchanged. Cited by number only: Theorem 29.1 (a
    compactification by one point of a locally compact Hausdorff space is the one-point
    compactification), Theorem 38.4 (maximality of the Stone--Čech compactification), Theorem
    38.5 (its characterisation by extension of bounded continuous real-valued functions), and
    Theorem 26.3 (a compact subspace of a Hausdorff space is closed). Checked: that a countable
    supremum of countable ordinals is countable, which is what puts $\lambda$ and $\alpha$ below
    $\Omega$; the triangle-inequality estimate $2/n$ which is the point of the corrected
    argument; and the description of the neighbourhoods of the added point.
---

::: {.exercise}

(a) Show that every continuous real-valued function defined on $S_\Omega$ is "eventually constant."
[Hint: First prove that for each $\epsilon$, there is an element $\alpha$ of $S_\Omega$ such that $\abs{f(\beta) - f(\alpha)} < \epsilon$ for all $\beta > \alpha$. Then let $\epsilon = 1/n$ for $n \in \ZZ_+$ and consider the corresponding points $\alpha_n$.]

(b) Show that the one-point compactification of $S_\Omega$ and the Stone-Čech compactification are equivalent.

(c) Conclude that every compactification of $S_\Omega$ is equivalent to the one-point compactification.
:::

::: {.solution}

Write $S_\Omega=[0,\Omega)$, where $\Omega$ is the first uncountable ordinal.

::: pf

::: pf-step

(a) Suppose that for some $\varepsilon>0$ the bound fails: for every $\alpha<\Omega$ there is $\beta>\alpha$ with $\abs{f(\beta)-f(\alpha)}\ge\varepsilon$. Then there is a strictly increasing sequence $\gamma_0=0<\gamma_1<\cdots$ with $\abs{f(\gamma_n)-f(\gamma_{n-1})}\ge\varepsilon$ for every $n\ge1$.

::: pf-proof

This is a recursion: having chosen $\gamma_{n-1}$, the failure of the bound at $\alpha=\gamma_{n-1}$ provides $\gamma_n>\gamma_{n-1}$ with $\abs{f(\gamma_n)-f(\gamma_{n-1})}\ge\varepsilon$. Starting from $\gamma_0=0$, which lies in $S_\Omega$.

:::

:::

::: pf-step

(a) With $\lambda=\sup_n\gamma_n$ one has $\lambda<\Omega$, and $\gamma_n\to\lambda$; continuity gives $f(\gamma_n)\to f(\lambda)$, so $\abs{f(\gamma_n)-f(\gamma_{n-1})}<\varepsilon$ for large $n$, a contradiction. Hence for every $\varepsilon>0$ there is $\alpha<\Omega$ with $\abs{f(\beta)-f(\alpha)}<\varepsilon$ for all $\beta>\alpha$.

::: pf-proof

A countable supremum of countable ordinals is a countable ordinal, since a countable union of countable sets is countable, and $\Omega$ is the first uncountable ordinal; so $\lambda<\Omega$ and $\lambda\in S_\Omega$. An increasing sequence with supremum $\lambda$ converges to $\lambda$ in the order topology. Continuity of $f$ at $\lambda$ gives $f(\gamma_n)\to f(\lambda)$, hence $f(\gamma_n)-f(\gamma_{n-1})\to0$ by the triangle inequality, so its absolute value is below $\varepsilon$ for all large $n$, contradicting step 1.

:::

:::

::: pf-step

(a) For each $n\ge1$ choose $\alpha_n<\Omega$ with $\abs{f(\beta)-f(\alpha_n)}<1/n$ for all $\beta>\alpha_n$, and let $\alpha=\sup_n\alpha_n<\Omega$. If $\beta,\gamma>\alpha$ then
$$
\abs{f(\beta)-f(\gamma)}\le\abs{f(\beta)-f(\alpha_n)}+\abs{f(\gamma)-f(\alpha_n)}<\frac2n
$$
for every $n$, hence $f(\beta)=f(\gamma)$: the function $f$ is constant on the tail $(\alpha,\Omega)$.

::: pf-proof

The choice of $\alpha_n$ is step 2 with $\varepsilon=1/n$. $\alpha$ is a countable supremum of countable ordinals, hence countable and below $\Omega$. For $\beta,\gamma>\alpha$ and any $n$ we have $\beta,\gamma>\alpha\ge\alpha_n$, so both bounds of the definition of $\alpha_n$ apply, and the triangle inequality gives the displayed estimate; it holds for every $n$, so the nonnegative number $\abs{f(\beta)-f(\gamma)}$ is smaller than $2/n$ for all $n$ and must be $0$.

:::

:::

::: pf-step

(b) Let $S_\Omega^*=S_\Omega\cup\{\Omega\}$ be the one-point compactification, which is the ordinal interval $[0,\Omega]$. Every bounded continuous real-valued function on $S_\Omega$ is eventually constant by (a), so it extends continuously to $\Omega$ by that value, and by the characterisation of the Stone--Čech compactification (Theorems 38.2 and 38.5) $S_\Omega^*$ is equivalent to $\beta S_\Omega$.

::: pf-proof

$S_\Omega$ is locally compact and Hausdorff, and adjoining the largest ordinal gives the compact space $[0,\Omega]$, so $S_\Omega^*=[0,\Omega]$ is its one-point compactification (Theorem 29.1). If $f$ is bounded and continuous, step 3 gives a tail $(\alpha,\Omega)$ on which $f$ equals a constant $c$; setting $f(\Omega)=c$ makes the extension continuous at $\Omega$, because a neighbourhood of $c$ contains $f((\alpha,\Omega))$ and $(\alpha,\Omega]$ is a neighbourhood of $\Omega$. Theorem 38.5 says that a compactification of $X$ to which every bounded continuous real-valued function on $X$ extends is equivalent to $\beta X$; the extension property just verified is that hypothesis.

:::

:::

::: pf-step

(c) Let $Y$ be any compactification of $S_\Omega$. By maximality of the Stone--Čech compactification there is a continuous surjection $q:\beta S_\Omega\to Y$ that is the identity on $S_\Omega$; since $\beta S_\Omega-S_\Omega=\{\Omega\}$ by (b), the set $Y-S_\Omega=q(\{\Omega\})$ has at most one point, and it is nonempty because $S_\Omega$ is not compact.

::: pf-proof

$\beta S_\Omega$ is the maximal compactification (Theorem 38.4): for every compactification $Y$ of $X$ there is a continuous surjection $\beta X\to Y$ restricting to the identity on $X$. By step 4 the remainder $\beta S_\Omega-S_\Omega$ is the single point $\Omega$. Since $q$ restricts to the identity on $S_\Omega$ and is onto, $Y-S_\Omega=q(\beta S_\Omega-S_\Omega)=q(\{\Omega\})$, a set with at most one element. It has one, because otherwise $Y=S_\Omega$ would be compact, and $S_\Omega$ is not compact: the increasing sequence $\gamma_n$ of step 1 has no cluster point in $S_\Omega$, whose elements are all countable ordinals.

:::

:::

::: pf-step

(c) So $Y-S_\Omega=\{p\}$, and since $S_\Omega$ is locally compact and Hausdorff, the open sets of $Y$ meeting $Y-S_\Omega$ are the complements in $Y$ of the compact subsets of $S_\Omega$, which is the topology of the one-point compactification; thus $Y$ is equivalent to $S_\Omega^*$.

::: pf-proof

Write $Y=S_\Omega\cup\{p\}$. The open sets of $Y$ contained in $S_\Omega$ are the open sets of $S_\Omega$, since $S_\Omega$ is a subspace. For a neighbourhood $U$ of $p$, the complement $Y-U$ is closed in the compact space $Y$, hence compact, and it is a subset of $S_\Omega$; conversely, for a compact $K\subseteq S_\Omega$ the set $Y-K$ is open in $Y$ because $K$ is closed in $Y$ (Theorem 26.3: a compact subspace of a Hausdorff space is closed), and it contains $p$. This is exactly the description of the open sets of the one-point compactification of a locally compact Hausdorff space (Theorem 29.1), so the identity on $S_\Omega$ extends to a homeomorphism $Y\to S_\Omega^*$.

:::

:::

::: pf-step

The three parts are proved: every continuous real-valued function on $S_\Omega$ is eventually constant, $\beta S_\Omega$ is the one-point compactification, and every compactification of $S_\Omega$ is equivalent to it.

::: pf-proof

Part (a) is steps 1--3, part (b) is step 4 and part (c) steps 5--6.

:::

:::

:::
:::
