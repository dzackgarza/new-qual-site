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
---

::: {.problem}
Show that the Hopf invariant of a composition $S^{2n-1} \xrightarrow{f} S^{2n-1} \xrightarrow{g} S^n$ is given by $H(gf) = (\deg f) H(g)$, and for a composition $S^{2n-1} \xrightarrow{f} S^n \xrightarrow{g} S^n$ the Hopf invariant satisfies $H(gf) = (\deg g)^2 H(f)$.
:::

::: {.solution}
For a map $h:S^{2n-1}\to S^n$, write $C_h=S^n\cup_h e^{2n}$ (p. 427). Its cohomology is $\ZZ$ in degrees $0$, $n$ and $2n$ and zero otherwise, since the cellular chain complex has one cell in each of those dimensions and the boundary $\ZZ\to\ZZ$ in degree $2n$ is multiplication by $\deg h=0$ as $2n-1>n$ (Theorem 2.35, p. 139). Choose generators $x_h\in H^n(C_h;\ZZ)$ and $y_h\in H^{2n}(C_h;\ZZ)$ compatible with orientations. The Hopf invariant is defined by
$$
x_h^2=H(h)y_h.
$$

First let $f:S^{2n-1}\to S^{2n-1}$ have degree $d$ and $g:S^{2n-1}\to S^n$. The commutative attaching-map square gives a map $C_{gf}\to C_g$ that is the identity on the bottom sphere and has degree $d$ on the top cell. Its cohomology map sends $x_g$ to $x_{gf}$ and $y_g$ to $d y_{gf}$. Pulling back $x_g^2=H(g)y_g$ gives
$$
x_{gf}^2=dH(g)y_{gf},
$$
so $H(gf)=dH(g)$.

Now let $f:S^{2n-1}\to S^n$ and let $g:S^n\to S^n$ have degree $d$. The attaching-map square gives a map $C_f\to C_{gf}$ that restricts to $g$ on the bottom sphere and has degree $1$ on the top cell. Its cohomology map sends $x_{gf}$ to $d x_f$ and $y_{gf}$ to $y_f$. Pulling back $x_{gf}^2=H(gf)y_{gf}$ gives
$$
d^2H(f)y_f=H(gf)y_f.
$$
Therefore $H(gf)=d^2H(f)$.
:::
