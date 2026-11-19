---
schema: qual/card@1
id: E-HAT-4.B-1
kind: problem
title: "Hopf invariant of compositions"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-08
  note: >-
    Read Hatcher p.427: C_h=S^n\cup_h e^{2n} first with m=n, then 'When m>n'
    the cohomology is Z in 0,n,2n and the generators x_h in H^n and y_h in
    H^{2n} are obtained there, then specialized to m=2n-1. Thus the Hopf
    invariant as defined has n>1 (2n-1>n), where deg h=0 gives the Z's. The
    odd-n vanishing H=0 for odd n (p.427, x^2=-x^2) is within that n>1 domain,
    not a definition for arbitrary degree-d S^1->S^1 maps, whose cones need not
    have H^1=H^2=Z. The exercise is read with that n>1 domain.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    The composition proof is correct for its n>1 domain: C_{gf}->C_g (identity on
    S^n, degree d on 2n-cell) and C_f->C_{gf} (degree d on S^n, degree 1 on
    2n-cell) give the two pullback identities. No n=1 case is missing; the
    previous claim that n>=2 omitted n=1 and was repairable by odd vanishing
    misread the domain, since odd vanishing does not supply the missing H^n,
    H^{2n}=Z. No change to the proof text is needed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: $C_h$ has three cells and its only
    possible boundary is multiplication by $\deg h=0$ because $2n-1>n$ makes $h$ null; the Hopf
    invariant is the coefficient of $x_h^2$ on the generator $y_h$ and is well defined under the
    $\pm1$ ambiguity of generators; and the two attaching squares give the coefficient statements
    $x_g\mapsto x_{gf}$, $y_g\mapsto d\,y_{gf}$ and $x_{gf}\mapsto d\,x_f$, $y_{gf}\mapsto y_f$, from
    which $d\,H(g)$ and $d^2H(f)$ follow. Added: the well-definedness of $H(h)$ under change of
    generators, the exact form of the boundary map as the degree of the collapsed attaching map, and
    the division by the generator $y_f$, which is legitimate because $H^{2n}$ is infinite cyclic.
    No defect found in the statement, §4.B Exercise 1; no retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 436 carries the running head 427.
    The durable part of the locator is that printed page; the file path names this machine's copy and
    `tmp/sources` does not survive a VM reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 4.B of Hatcher, *Algebraic Topology* (2002), printed p. 427, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

Show that the Hopf invariant of a composition $S^{2n-1} \xrightarrow{f} S^{2n-1} \xrightarrow{g} S^n$ is given by $H(gf) = (\deg f) H(g)$, and for a composition $S^{2n-1} \xrightarrow{f} S^n \xrightarrow{g} S^n$ the Hopf invariant satisfies $H(gf) = (\deg g)^2 H(f)$.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own, from the definition of the Hopf invariant on p. 427 and the cellular cohomology of the mapping cone.

::: pf

::: {.pf-step #cohomology}
For $h\colon S^{2n-1}\to S^n$ with $n>1$, the complex $C_h=S^n\cup_h e^{2n}$ has $H^k(C_h;\ZZ)=\ZZ$ for $k=0,n,2n$ and $0$ otherwise.

::: pf-proof
$C_h$ is a CW complex with one $0$-cell, one $n$-cell and one $2n$-cell, so its cellular chain complex is $\ZZ$ in degrees $0,n,2n$. The only possibly nonzero boundary is $\partial_{2n}\colon\ZZ\to\ZZ$, which is multiplication by the degree of the attaching map $h$ composed with the collapse $S^n\to S^n/S^{n-1}$; since $2n-1>n$, the map $h$ is nullhomotopic, so its degree on the top-dimensional sphere is $0$. Hence all boundaries vanish, the homology is $\ZZ$ in the three degrees, and by the universal coefficient theorem so is the cohomology.
:::

:::

::: {.pf-step #definition}
Choose generators $x_h\in H^n(C_h;\ZZ)$ and $y_h\in H^{2n}(C_h;\ZZ)$ compatibly with orientations; then $x_h^2=H(h)\,y_h$ defines the integer $H(h)$.

::: pf-proof
The cup product $x_h^2$ lies in $H^{2n}(C_h;\ZZ)=\ZZ\,y_h$, the group being infinite cyclic by step [](#cohomology){.pf-ref}, so $x_h^2$ is a unique integer multiple of the generator $y_h$. Changing the choice of generators multiplies $x_h$ by $\pm1$ and $y_h$ by $\pm1$, leaving the ratio unchanged.
:::

:::

::: {.pf-step #first}
If $f\colon S^{2n-1}\to S^{2n-1}$ has degree $d$ and $g\colon S^{2n-1}\to S^n$, then $H(gf)=d\,H(g)$.

::: pf-proof
The attaching map of $C_{gf}$ is $gf$, so the attaching square gives a cellular map $\varphi\colon C_{gf}\to C_g$ that is the identity on $S^n$ and has degree $d$ on the $2n$-cell. On cohomology $\varphi^*$ sends $x_g$ to $x_{gf}$, the bottom cell being fixed, and sends $y_g$ to $d\,y_{gf}$, the top cell having degree $d$. Applying $\varphi^*$ to $x_g^2=H(g)y_g$ gives $x_{gf}^2=d\,H(g)\,y_{gf}$, and comparing with $x_{gf}^2=H(gf)y_{gf}$ from step [](#definition){.pf-ref}, together with the fact that $y_{gf}$ is a generator and so not a torsion element, gives $H(gf)=d\,H(g)$.
:::

:::

::: {.pf-step #second}
If $f\colon S^{2n-1}\to S^n$ and $g\colon S^n\to S^n$ has degree $d$, then $H(gf)=d^2\,H(f)$.

::: pf-proof
The attaching square now gives a cellular map $\psi\colon C_f\to C_{gf}$ that restricts to $g$ on the bottom sphere and has degree $1$ on the top cell, since the attaching map $gf$ is the composite of $f$ with $g$. On cohomology $\psi^*$ sends $x_{gf}$ to $d\,x_f$, the bottom sphere carrying $g$ of degree $d$, and $y_{gf}$ to $y_f$, the top cell carrying a degree-$1$ map. Applying $\psi^*$ to $x_{gf}^2=H(gf)y_{gf}$ gives $d^2x_f^2=H(gf)y_f$, that is $d^2H(f)y_f=H(gf)y_f$; dividing by the generator $y_f$ gives $H(gf)=d^2H(f)$.
:::

:::

::: {.pf-step}
$\boxed{H(gf)=\deg(f)\,H(g)\quad\text{and}\quad H(gf)=(\deg g)^2\,H(f)}$ for the two indicated compositions.

::: pf-proof
The two identities are steps [](#first){.pf-ref} and [](#second){.pf-ref}; in each, the degree statement is read off from which cells the induced map of mapping cones fixes and which it multiplies, and the cup-product computation then compares coefficients on the generator of $H^{2n}$.
:::

:::

:::
:::
