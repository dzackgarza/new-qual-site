---
schema: qual/card@1
id: P-CAFA25F
kind: problem
title: 'Constancy of positive harmonic functions on simply connected regions and on $\CC\setminus\theset{0}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Liouville's Theorem
  - Positive Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/QFall2025.pdf, Problem 6 (10 points;
    6, 4): part (i) for a nonempty simply connected region G, G = C if and only if every positive
    harmonic function on G is constant; part (ii) for G = C minus {0}. The card's two parts are the
    printed two.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Supplied the reason the Cayley
    transform of F = h + iv is bounded, namely the displayed computation showing its modulus is
    less than 1 when Re F > 0, and the reason it is defined at all, F + 1 having positive real part
    and so never vanishing. In the converse direction, added that h = Re(psi o phi) is nonconstant,
    which the prose asserted: a constant real part on a connected domain would make the holomorphic
    psi o phi constant and hence phi constant, contradicting injectivity. In (ii) recorded that the
    exponential is onto, which is what carries constancy of H back to h. No retained published
    solution covers this problem.
---

::: {.problem}
(i) Let $G \subset \CC$ be a nonempty simply connected region.
Show that $G = \CC$ if and only if every positive harmonic function $h : G \to \RR$ is constant.

(ii) Let $G = \CC \setminus \{0\}$.
If $h : G \to \RR$ is a positive harmonic function, show that $h$ is constant.
:::

::: {.solution}
This is Problem 6 (10 points; 6, 4) of the UCSD complex-analysis qualifying exam of Fall 2025 (`assets/attachments/QFall2025.pdf`). No published solution set is transcribed: the argument is the card's own.

::: pf

::: {.pf-step #generalc}
(i) If $G=\CC$, every positive harmonic function on $G$ is constant.

::: pf-proof
Let $h>0$ be harmonic on $\CC$. The plane is simply connected, so $h$ has a harmonic conjugate $v$ and $F=h+iv$ is entire with $\operatorname{Re}F=h>0$. Then $F\neq-1$, so $\Phi=\frac{F-1}{F+1}$ is entire, and it maps the right half-plane into the unit disc, because for $\operatorname{Re}F>0$,
$$\abs{\frac{F-1}{F+1}}^{2}=\frac{(\operatorname{Re}F-1)^{2}+(\operatorname{Im}F)^{2}}{(\operatorname{Re}F+1)^{2}+(\operatorname{Im}F)^{2}}<1.$$
So $\Phi$ is a bounded entire function, hence constant by Liouville's theorem, and then $F=(1+\Phi)/(1-\Phi)$ is constant and so is $h=\operatorname{Re}F$.
:::
:::

::: {.pf-step #converse}
(i) If $G\subsetneq\CC$ is a nonempty simply connected region, there is a positive nonconstant harmonic function on $G$.

::: pf-proof
By the Riemann mapping theorem there is a biholomorphism $\phi\colon G\to\DD$; the hypothesis $G\neq\CC$ is what the theorem needs, together with $G$ nonempty, simply connected and proper. The Cayley transform $\psi(w)=\frac{1+w}{1-w}$ maps $\DD$ onto the right half-plane, so $h=\operatorname{Re}(\psi\circ\phi)$ is harmonic and positive on $G$. It is nonconstant: if it were constant, $\psi\circ\phi$ would be a holomorphic function with constant real part on the connected set $G$, hence constant, and then $\phi$ would be constant, contradicting injectivity.
:::
:::

::: {.pf-step #punctured}
(ii) Every positive harmonic $h$ on $\CC\setminus\{0\}$ is constant.

::: pf-proof
The exponential $\exp\colon\CC\to\CC\setminus\{0\}$ is a covering map onto a punctured plane, in particular onto and locally biholomorphic, so $H=h\circ\exp$ is harmonic on $\CC$ and positive. By step [](#generalc){.pf-ref} $H$ is constant, and since $\exp$ is onto, $h$ is constant.
:::
:::
:::

:::
