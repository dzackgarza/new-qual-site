---
schema: qual/card@1
id: P-JHUSP08ANF
kind: problem
title: "Conformal self-maps of the disk agreeing at two points coincide"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Disc Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the two distinct interior points and the explicit biholomorphic convention with Spring 2008 problem 6 in the retained JHU source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the composition fixing both points, the disk conjugation, and the nonzero fixed point that forces equality in Schwarz's lemma."
---

::: {.problem}
6) Let $D = \{ z \in \mathbf { C } : | z | < 1 \}$ and P and Q be distinct points in D. Prove the following statement: If f and g are conformal (or equivalently biholomorphic) self-maps of D, $f ( P ) = g ( P )$ and $f ( Q ) = g ( Q )$ , then $f \equiv g$
:::

::: {.solution}
<1>1. The comparison map is conjugate to a disk map fixing zero and another point.

::: {.proof}
Since $g$ is biholomorphic, $h=g^{-1}\circ f$ is a
holomorphic disk self-map. The two assumed equalities
give $h(P)=P$ and $h(Q)=Q$. Set
$$
\phi(z)=\frac{z-P}{1-\overline Pz},\qquad
\phi^{-1}(w)=\frac{w+P}{1+\overline Pw}.
$$
Direct substitution gives the inverse identities, and
$$
1-|\phi(z)|^2=
\frac{(1-|P|^2)(1-|z|^2)}{|1-\overline Pz|^2}>0
\quad(z\in D).
$$
The corresponding identity for $\phi^{-1}$ shows that
both maps preserve $D$. Thus $H=\phi\circ h\circ\phi^{-1}$
is a holomorphic disk self-map fixing zero and
$q=\phi(Q)\ne0$.
:::

<1>2. The normalized map is the identity.

::: {.proof}
Schwarz's lemma gives $|H(w)|\leq|w|$ [@SS03]. The
quotient $H(w)/w$ extends holomorphically at zero by
the Taylor expansion and is bounded by one. Its value
at $q$ is $H(q)/q=1$. The maximum modulus principle
therefore makes the quotient identically one [@SS03].
Hence $H(w)=w$ on $D$, and undoing the conjugation
gives $h=\operatorname{id}_D$. Since $h=g^{-1}\circ f$,
this is exactly $f=g$ on the whole disk.
:::
:::
