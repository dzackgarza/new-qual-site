---
schema: qual/card@1
id: P-FWZWG
kind: problem
title: "Show that if $f: D(0, R) \\rightarrow \\mathbb{C}$ is holomorphic, with $|f(z)| \\leq M$ for some $M>0$, then $\\left|\\frac{f(z)-f(0)}{M^{2}-\\overline{f(0)} f(z)}\\right| \\leq \\frac{|z|}{M R}$"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - blaschke-factors
relations: []
review: draft
solved: true
---

::: problem
Show that if $f: D(0, R) \rightarrow \mathbb{C}$ is holomorphic, with $|f(z)| \leq M$ for some $M>0$, then
\[
\left|\frac{f(z)-f(0)}{M^{2}-\overline{f(0)} f(z)}\right| \leq \frac{|z|}{M R} .
\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $f: D(0, R) \to \CC$ is holomorphic with $\abs{f(z)} \leq M$ for some $M > 0$, then $$\abs{\frac{f(z) - f(0)}{M^2 - \overline{f(0)} f(z)}} \leq \frac{\abs z}{MR} \quad (z \in D(0,R)).$$

<1>1. Normalize: define $g(w) := \frac{f(Rw)}{M}$ for $\abs w < 1$; then $g: \DD \to \DD$ is holomorphic.
Proof: $\abs{g(w)} \leq M/M = 1$ on $\DD$; $M > 0$ by hypothesis.

<1>2. Apply the Schwarz--Pick inequality to $g$ at the pair $(0, w)$.
Proof: For any holomorphic $g: \DD \to \DD$, $\abs{\frac{g(w) - g(0)}{1 - \overline{g(0)} g(w)}} \leq \abs w$; this is the invariant form of Schwarz's lemma (equivalently, apply Schwarz to $\phi_{g(0)} \circ g$).

<1>3. Substitute $g(w) = f(Rw)/M$ into the inequality.
<2>1. $\frac{g(w) - g(0)}{1 - \overline{g(0)} g(w)} = \frac{\frac{f(Rw)}{M} - \frac{f(0)}{M}}{1 - \frac{\overline{f(0)} f(Rw)}{M^2}} = \frac{M\qty(f(Rw) - f(0))}{M^2 - \overline{f(0)} f(Rw)}$.
Proof: Multiply numerator and denominator by $M$ and $M^2$ respectively; the $M$ factors cancel in the quotient as written.
<2>2. $\abs{\frac{M\qty(f(Rw) - f(0))}{M^2 - \overline{f(0)} f(Rw)}} \leq \abs w$.
Proof: <1>2 and <2>1. <2>3. $\abs{\frac{f(Rw) - f(0)}{M^2 - \overline{f(0)} f(Rw)}} \leq \frac{\abs w}{M}$.
Proof: Divide <2>2 by $M > 0$.

<1>4. Substitute $z = Rw$.
Proof: For $z \in D(0,R)$, $w = z/R \in \DD$; then <2>3 reads $\abs{\frac{f(z) - f(0)}{M^2 - \overline{f(0)} f(z)}} \leq \frac{\abs z}{MR}$.

<1>5. Q.E.D. Proof: <1>4 is the claim.
(When $f$ is constant, both sides vanish and the inequality is trivial; otherwise $\abs{f(0)} < M$ by the maximum modulus principle, so the denominator $M^2 - \overline{f(0)} f(z)$ is nonzero and the Schwarz--Pick form in <1>2 is well-defined.)
:::
