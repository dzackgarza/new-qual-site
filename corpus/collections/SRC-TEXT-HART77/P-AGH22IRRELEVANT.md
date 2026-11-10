---
schema: qual/card@1
id: P-AGH22IRRELEVANT
kind: problem
title: The irrelevant ideal and the empty projective vanishing locus
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homogeneous Ideals
  - Projective Varieties
  - Radical Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three equivalences with the retained Hartshorne I.2.2 transcription. Separated the unit ideal from the proper homogeneous cone and verified the monomial bound for containment of an entire graded piece, not only the pure powers of the variables.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: Reviewed the recovered proof against the affine Nullstellensatz and checked each implication, including the unit ideal and the bound for all monomials of a fixed degree.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Compared the card's statement in full with the printed Exercise 2.2 (scan
    page 26 of the retained PDF), tails included: hypotheses, every lettered
    part and the closing clauses. The card states the chapter's standing
    hypotheses (k algebraically closed, S = k[x_0,...,x_n]) explicitly, which
    adds no condition.
---

::: {.problem}
Let $k$ be algebraically closed, let $S\coloneqq k[x_0,\ldots,x_n]$, and let $\mfa\subseteq S$ be a homogeneous ideal.
Show that the following conditions are equivalent.

(i) $Z(\mfa) = \emptyset$.

(ii) $\sqrt{\mfa}$ is either $S$ or the ideal $S_+ = \bigoplus_{d>0} S_d$.

(iii) $\mfa \supseteq S_d$ for some $d > 0$.
:::

::: {.solution}
Write $J=\mfa$ and distinguish its affine zero set $V_a(J)\subseteq\AA_k^{n+1}$ from its projective zero set $Z(J)\subseteq\PP_k^n$.
The vector subspace $S_d$ consists of the homogeneous polynomials of degree $d$.

::: pf

::: {.pf-step #i-equiv-ii}
Conditions (i) and (ii) are equivalent.

::: pf-proof
If $J=S$, then $Z(J)=\varnothing$ and $\sqrt J=S$, so both conditions hold.
Now assume $J$ is proper.
It contains no nonzero constant, and homogeneity implies $J\subseteq S_+$.
Thus the origin belongs to $V_a(J)$, and the relation between the affine and projective equations is
$$
V_a(J)=\{0\}\cup\{v\in k^{n+1}\setminus\{0\}:[v]\in Z(J)\}.
$$
Indeed, vanishing of homogeneous generators is unchanged by multiplying a nonzero vector by a nonzero scalar.
Therefore $Z(J)=\varnothing$ exactly when $V_a(J)=\{0\}$.
The [[T-JRTS2|affine Nullstellensatz]] identifies the latter condition with
$$
\sqrt J=I(V_a(J))=I(\{0\})=(x_0,\ldots,x_n)=S_+
$$
[@Har77, Theorem I.1.3A].
Conversely, if $\sqrt J=S_+$, a point vanishes on $J$ exactly when it vanishes on its radical, so $V_a(J)=\{0\}$ and $Z(J)=\varnothing$.
Finally $\sqrt J=S$ forces $1\in J$, which is the unit-ideal case already treated.
:::

:::

::: {.pf-step #ii-implies-iii}
Condition (ii) implies (iii).

::: pf-proof
For $J=S$, any positive $d$ works.
If $\sqrt J=S_+$, choose integers $N_i\ge1$ with $x_i^{N_i}\in J$ for $0\le i\le n$.
Set
$$
D=1+\sum_{i=0}^n(N_i-1)>0.
$$
Every monomial of total degree $D$ has an exponent at least $N_i$ for some $i$; otherwise its degree would be at most $\sum_i(N_i-1)=D-1$.
It is therefore divisible by one of the powers $x_i^{N_i}$ and belongs to $J$.
Since these monomials span $S_D$, the whole graded piece $S_D$ is contained in $J$.
:::

:::

::: {.pf-step #iii-implies-i}
Condition (iii) implies (i).

::: pf-proof
If $S_d\subseteq J$ for a positive $d$, then $x_i^d\in J$ for every $i$.
At a point of $\PP^n$, at least one coordinate is nonzero, and its $d$th power is nonzero as well.
Thus these polynomials have no common projective zero, so neither does $J$.
:::

:::

::: pf-qed
Step [](#i-equiv-ii){.pf-ref} proves (i) equivalent to (ii), and steps [](#ii-implies-iii){.pf-ref} and [](#iii-implies-i){.pf-ref} prove (ii) implies (iii) implies (i).
These implications establish all three equivalences, including the unit ideal.
:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 2.2, PDF p. 2: he takes (i) to (ii) through the affine zero set being empty or the origin and the Nullstellensatz, and (ii) to (iii) by choosing one exponent $m$ with $x_i^m\in\mathfrak a$ for every $i$ and observing that every monomial of degree $m(n+1)$ has some $x_i^m$ as a factor.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 2.2, PDF p. 3, runs the same three implications, but in (ii) to (iii) it takes exponents $d_i$ with $x_i^{d_i}\in\sqrt{\mathfrak a}$, sets $d=\max_i d_i$, and concludes "$x_i^d\in\mathfrak a$ for all $i$, as these generate $S_d$ we have $S_d\subseteq\mathfrak a$": a power of an element of $\sqrt{\mathfrak a}$ need not lie in $\mathfrak a$ without raising it further, and the pure powers $x_i^d$ do not span $S_d$ — $x_1x_2$ is a monomial of degree $2$ outside $(x_0^2,\ldots,x_n^2)$, so the step as printed does not close.
The proof above takes Borcherds' form of (ii) to (iii), with the exponent $D=1+\sum_i(N_i-1)$ and the pigeonhole count that makes every monomial of degree $D$ divisible by one of the powers $x_i^{N_i}$, and it separates the unit ideal from the case $\sqrt{\mathfrak a}=S_+$.
Agree with Borcherds; Troiani's (ii) to (iii) is the step the displayed count supplies.
:::
