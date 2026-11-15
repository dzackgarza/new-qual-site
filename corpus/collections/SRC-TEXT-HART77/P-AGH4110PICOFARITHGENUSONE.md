---
schema: qual/card@1
id: P-AGH4110PICOFARITHGENUSONE
kind: problem
title: $\Pic^0 X$ is in bijection with $X_{\reg}$ when $p_a(X)=1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Riemann-Roch
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.10 and the retained solution transcription. The proof
    uses the corrected target Pic^0, derives degree K=0 from IV.1.9, and makes
    explicit why the unique effective degree-one representative is supported at
    a regular point.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Hartshorne IV Ex. 1.10, printed p. 299 (PDF p. 314), reads "the elements of the group Pic^0 X", so the statement and title that name Pic^0 X are the printed ones; the printed page was re-read in the retained PDF for this check.'

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.1.10,
    printed p. 299 (PDF p. 314 of the checked-in extraction). Published treatment
    located outside the twelve retained sets: R. Vakil, The Rising Sea:
    Foundations of Algebraic Geometry, 21 October 2025 version, Section 19.9,
    printed pp. 555--556, read in tmp/sources/vakil-rising-sea-2025-10-21.md.
    Corrected step mapping, after re-reading the three numbered paragraphs:
    (19.9.1), printed p. 555, gives deg omega_C = 0 and h^0(C, omega_C) = 1 so
    omega_C = O_C, and for deg L > 0 Riemann--Roch with Serre duality gives
    h^0(C, L) = deg L, which is the card's step s1 together with the vanishing of
    step s2; (19.9.2), same page, says that each degree 1 point q gives O_C(q),
    that distinct points give distinct bundles because a degree 1 bundle has one
    section up to scalars, and that every degree 1 bundle is O_C(q) for q the
    divisor of zeros of a section -- that is the card's step s5 (injectivity) and
    the existence half of step s6, not steps s3 and s4 as the earlier version of
    this note said; (19.9.3), printed p. 556, twists the degree 1 bundles by
    O(-p) to get the bijection with Pic^0 and defines the group law, which is the
    card's map Phi and its identification with Pic^0. Vakil's standing hypothesis
    is a curve, i.e. a regular projective geometrically integral scheme of
    dimension 1, while Hartshorne's X is only an integral projective
    locally complete intersection of dimension 1 with p_a = 1 and may be
    singular, and the exercise asks for a bijection onto X_reg. The singular case
    is the card's step s6, whose length-one argument shows O_{X,P}/(a) = k, hence
    a principal maximal ideal and P regular; Vakil supplies nothing for it. The
    earlier version of this note recorded the step mapping wrongly in three places
    and this substitutes for it.
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$, which is locally complete intersection, and has $p_a=1$.
Fix a point $P_0 \in X_{\reg}$.
Imitate (1.3.7) to show that the map $P \mapsto \mcl(P-P_0)$ gives a one-to-one correspondence between the points of $X_{\reg}$ and the elements of the group $\Pic^0 X$.

This generalizes (II, 6.11.4) and (II, Ex.
6.7).
:::

::: {.solution}
::: pf

::: {.pf-step #s1}

The canonical divisor $K$ from Exercise IV.1.9 satisfies
$$
\deg K=0,
\qquad
\ell(K)=1.
$$

::: pf-proof

Since $p_a(X)=1$, the singular-curve Riemann--Roch formula
[[P-AGH419RRSINGULAR|Exercise IV.1.9]] gives, for $D=0$,
$$
\ell(0)-\ell(K)
=
1-p_a(X)
=
0.
$$
Because $\ell(0)=h^0(X,\mco_X)=1$, this gives $\ell(K)=1$.

Apply the same formula with $D=K$:
$$
\ell(K)-\ell(0)
=
\deg K+1-p_a(X)
=
\deg K.
$$
The left-hand side is zero, so $\deg K=0$.

:::

:::

::: {.pf-step #s2}

An invertible sheaf of negative degree on $X$ has no nonzero global
section.

::: pf-proof

Let $\mcl$ be invertible and suppose
$$
0\ne s\in H^0(X,\mcl).
$$
Since $X$ is integral, multiplication by $s$ gives an injection
$$
0
\longrightarrow
\mco_X
\xrightarrow{s}
\mcl
\longrightarrow
\mct
\longrightarrow
0,
$$
where $\mct$ is supported in dimension zero. Therefore
$$
\deg\mcl
=
\chi(\mcl)-\chi(\mco_X)
=
\chi(\mct)
=
\length(\mct)
\ge0.
$$
Thus a line bundle of negative degree cannot have a nonzero section.

:::

:::

::: {.pf-step #s3}

If $E$ is a divisor supported in $X_{\reg}$ with $\deg E=1$, then
$$
\ell(E)=1.
$$

::: pf-proof

Exercise IV.1.9 gives
$$
\ell(E)-\ell(K-E)
=
\deg E+1-p_a(X)
=
1.
$$
By step [](#s1){.pf-ref},
$$
\deg(K-E)=-1.
$$
Hence step [](#s2){.pf-ref} gives $\ell(K-E)=0$, and therefore $\ell(E)=1$.

:::

:::

::: {.pf-step #s4}

The assignment
$$
\Phi:X_{\reg}\longrightarrow\Pic^0X,
\qquad
P\longmapsto[\mcl(P-P_0)]
$$
is well defined.

::: pf-proof

The divisor $P-P_0$ has degree zero. By Exercise IV.1.9(a),
$$
\deg\mcl(P-P_0)=0.
$$
Thus $\mcl(P-P_0)$ lies in $\Pic^0X$.

:::

:::

::: {.pf-step #s5}

The map $\Phi$ is injective.

::: pf-proof

In the regular case this is R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §19.9.2], printed p. 555: distinct degree 1 points determine distinct degree 1 line bundles, "as a degree 1 line bundle has only one section, up to scalar multiples". The card's version of it, which needs no regularity hypothesis beyond $P,Q\in X_{\reg}$, runs as follows.

Suppose
$$
\mcl(P-P_0)\cong\mcl(Q-P_0)
$$
for $P,Q\in X_{\reg}$. Tensoring by $\mcl(P_0)$ gives
$$
\mcl(P)\cong\mcl(Q).
$$
Thus $P$ and $Q$ are linearly equivalent effective divisors.

By step [](#s3){.pf-ref},
$$
\ell(P)=1,
$$
so the complete linear system $\abs{P}$ has dimension zero and contains
only the divisor $P$. Since $Q\in\abs{P}$, we obtain $Q=P$.

:::

:::

::: {.pf-step #s6}

The map $\Phi$ is surjective.

::: pf-proof

R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §19.9.2], printed p. 555, disposes of the regular case: a degree 1 invertible sheaf has a section, and the divisor of zeros of one writes it as $\mco_C(q)$ for a degree 1 point $q$. Hartshorne's $X$ may be singular, so the divisor of zeros has to be shown to be a point of $X_{\reg}$; that is the length-one argument from "Taking Euler characteristics" below, and it is the card's own.

Let $[\mcl]\in\Pic^0X$. By Exercise IV.1.9(c), choose a divisor $D$
supported in $X_{\reg}$ such that
$$
\mcl\cong\mcl(D).
$$
Since $\mcl$ has degree zero, Exercise IV.1.9(a) gives
$$
\deg D=0.
$$
Put
$$
E=D+P_0.
$$
Then $E$ is supported in $X_{\reg}$ and has degree one. Step [](#s3){.pf-ref} gives
$$
\ell(E)=1,
$$
so choose a nonzero section
$$
s\in H^0(X,\mcl(E)).
$$

Because $X$ is integral, $s$ defines an effective Cartier divisor $Z$ and
an exact sequence
$$
0
\longrightarrow
\mco_X
\xrightarrow{s}
\mcl(E)
\longrightarrow
\mco_Z(E)
\longrightarrow
0.
$$
By Exercise IV.1.9(a),
$$
\deg\mcl(E)=\deg E=1.
$$
Taking Euler characteristics in the displayed sequence therefore gives
$$
\length(Z)=1.
$$

Hence $Z$ is supported at a single closed point $P$. Since $k$ is
algebraically closed, the length-one local ring of $Z$ is $k$. Locally at
$P$, the Cartier divisor $Z$ is cut out by one nonzerodivisor $a$ in the
one-dimensional local domain $\mco_{X,P}$, and
$$
\mco_{X,P}/(a)\cong k.
$$
Thus the maximal ideal of $\mco_{X,P}$ is generated by $a$. A
one-dimensional noetherian local ring with principal maximal ideal is
regular, so
$$
P\in X_{\reg}.
$$
Consequently $Z=P$ as an effective Cartier divisor, and
$$
\mcl(E)\cong\mcl(P).
$$
Since $E=D+P_0$,
$$
\mcl
\cong
\mcl(D)
\cong
\mcl(P-P_0)
=
\Phi(P).
$$
Thus $\Phi$ is surjective.

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
X_{\reg}\xrightarrow{\sim}\Pic^0X,
\qquad
P\longmapsto\mcl(P-P_0).
}
$$

::: pf-proof

Step [](#s4){.pf-ref} makes the map well defined, step [](#s5){.pf-ref} proves injectivity, and
step [](#s6){.pf-ref} proves surjectivity.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required one-to-one correspondence with $\Pic^0X$.

:::

:::

:::

::: {.remark title="Published solution"}
R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §19.9], printed pp. 555--556, gives the bijection $\Pic^0 C\leftrightarrow$ degree 1 points for a regular curve $C$ of genus 1: (19.9.1) $\omega_C\cong\mco_C$ and $h^0(C,\mcl)=\deg\mcl$ for $\deg\mcl>0$; (19.9.2) every degree 1 bundle is the divisor of a point, and distinct points give distinct bundles because a degree 1 bundle has one section up to scalars; (19.9.3) twisting by $\mco(-p)$ gives the bijection. Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} transcribe that and add what the exercise's hypothesis on $X$ forces: here $X$ is only a locally complete intersection with $p_a=1$, so the divisor of zeros of a degree 1 section is shown to lie in $X_{\reg}$ by the length-one computation $\mco_{X,P}/(a)\cong k$, which makes the maximal ideal principal and $P$ regular. That step is the card's, and Vakil's regular curves do not require it.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.10, printed pp. 209--210 (entry 4.1.14), takes $\deg K_X=p_a-1$ from IV.1.9(d), so a divisor of degree zero has $K_X-D-P_0$ of degree $-1$ and hence no sections, and concludes that $\dim|D+P_0|=\deg D=0$; the resulting assignment of degree-one divisors to points of $\Pic^0 X$ is the bijection with which the card identifies $\Pic^0 X$ for $p_a=1$.
:::
