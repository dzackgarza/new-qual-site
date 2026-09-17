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
---

::: {.problem}
Let $k$ be algebraically closed, let $S\coloneqq k[x_0,\ldots,x_n]$, and let $\mfa\subseteq S$ be a homogeneous ideal.
Show that the following conditions are equivalent.

(i) $Z(\mfa) = \emptyset$.

(ii) $\sqrt{\mfa}$ is either $S$ or the irrelevant ideal $S_+ = \bigoplus_{d>0} S_d$.

(iii) $\mfa \supseteq S_d$ for some $d > 0$.
:::

::: {.solution}
Write $J=\mfa$ and distinguish its affine zero set $V_a(J)\subseteq\AA_k^{n+1}$ from its projective zero set $Z(J)\subseteq\PP_k^n$.
The vector subspace $S_d$ consists of the homogeneous polynomials of degree $d$.

<1>1. Conditions (i) and (ii) are equivalent.

::: {.proof}
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
[@Har10a, Theorem I.1.3A].
Conversely, if $\sqrt J=S_+$, a point vanishes on $J$ exactly when it vanishes on its radical, so $V_a(J)=\{0\}$ and $Z(J)=\varnothing$.
Finally $\sqrt J=S$ forces $1\in J$, which is the unit-ideal case already treated.
:::

<1>2. Condition (ii) implies (iii).

::: {.proof}
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

<1>3. Condition (iii) implies (i).

::: {.proof}
If $S_d\subseteq J$ for a positive $d$, then $x_i^d\in J$ for every $i$.
At a point of $\PP^n$, at least one coordinate is nonzero, and its $d$th power is nonzero as well.
Thus these polynomials have no common projective zero, so neither does $J$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves (i) equivalent to (ii), and steps <1>2--<1>3 prove (ii) implies (iii) implies (i).
These implications establish all three equivalences, including the unit ideal.
:::
:::
