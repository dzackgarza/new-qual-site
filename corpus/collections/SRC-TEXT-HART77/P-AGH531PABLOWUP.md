---
schema: qual/card@1
id: P-AGH531PABLOWUP
kind: problem
title: Invariance of the arithmetic genus under blowing up a nonsingular subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.1 and the retained Egbert companion calculation. The
    source states the invariance of arithmetic genus under a blowup of a
    smooth centre. The proof uses vanishing of higher direct images of the
    structure sheaf and the definition p_a=(-1)^dim(chi(O)-1).
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    V.3.4 concerns Hilbert-Samuel multiplicity, not blowup cohomology.
    Replaced the false cross-reference with the projective birational
    vanishing theorem of Chatzistamatiou and Rulling, Theorem 1.1.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.1, printed page 394. Checked the reduction: R^j pi_* O = 0 for
    j > 0 and pi_* O = O give H^i(X-tilde, O) = H^i(X, O) by the Leray spectral
    sequence, hence equality of the Euler characteristics and of
    p_a(Z) = (-1)^n (chi(Z,O_Z) - 1), the definition of III.5/IV.1. Searched
    outside the twelve retained sets: Algebraic Geometry II, National Taiwan
    University, 2020 Spring, Chapter V homework, Exercise 1 of section 3, PDF
    p. 9 (tmp/sources/ntu-ag2-chapter5.pdf), proves the vanishing for a centre
    of any codimension by the formal functions theorem over E = P^{r-1};
    Yang Pi-Yeh, Hartshorne Solutions, exercise 5.3.1, printed p. 107
    (tmp/sources/lfwin-hartshorne-solutions.pdf), assumes codimension one and
    is not a proof of the exercise. Not checked: Chatzistamatiou-Rulling
    Theorem 1.1 itself, which is cited and not in tmp/sources; the card's own
    argument needs only that statement.
---

::: {.problem}
Let $X$ be a nonsingular projective variety of any dimension, let $Y$ be a nonsingular subvariety, and let $\pi: \tilde{X} \rightarrow X$ be obtained by blowing up $Y$.
Show that $p_a(\tilde{X})=p_a(X)$.
:::

::: {.solution}
Put
$$
n=\dim X.
$$
Since a blowup is birational,
$$
\dim\widetilde X=n.
$$

::: pf

::: {.pf-step #cohomology-invariance}
For every $i\ge0$,
$$
\boxed{
H^i(\widetilde X,\OO_{\widetilde X})
\cong
H^i(X,\OO_X).}
$$

::: pf-proof
The blowup of a nonsingular variety along a nonsingular centre is
nonsingular, and the blowup morphism $\pi$ is projective and birational.
Both varieties are excellent because they are of finite type over $k$.
[Chatzistamatiou--Rülling, Theorem 1.1](https://arxiv.org/abs/1404.1827)
therefore gives
$$
R^j\pi_*\OO_{\widetilde X}=0\qquad(j>0).
$$
Since $X$ is normal and $\pi$ is proper and birational,
$$
\pi_*\OO_{\widetilde X}=\OO_X.
$$
The Leray spectral sequence now gives the displayed isomorphisms.
:::

:::

::: {.pf-step #euler-char-invariance}
The structure-sheaf Euler characteristic is unchanged:
$$
\boxed{
\chi(\widetilde X,\OO_{\widetilde X})
=
\chi(X,\OO_X).}
$$

::: pf-proof
By definition,
$$
\chi(Z,\OO_Z)
=
\sum_{i\ge0}(-1)^i
\dim_k H^i(Z,\OO_Z)
$$
for a projective variety $Z$.  Step [](#cohomology-invariance){.pf-ref} identifies every summand for
$Z=\widetilde X$ with the corresponding summand for $Z=X$, so the two
alternating sums agree.
:::

:::

::: {.pf-step #arithmetic-genus-equal}
The arithmetic genera agree:
$$
\boxed{p_a(\widetilde X)=p_a(X).}
$$

::: pf-proof
For a nonempty projective scheme of dimension $n$, the arithmetic genus is
[[D-COHEULER]]
$$
p_a(Z)=(-1)^n\bigl(\chi(Z,\OO_Z)-1\bigr).
$$
The varieties $X$ and $\widetilde X$ have the same dimension $n$, and step
[](#euler-char-invariance){.pf-ref} gives equality of their structure-sheaf Euler characteristics.
Substitution into the displayed definition gives
$$
p_a(\widetilde X)
=
(-1)^n\bigl(\chi(\widetilde X,\OO_{\widetilde X})-1\bigr)
=
(-1)^n\bigl(\chi(X,\OO_X)-1\bigr)
=
p_a(X).
$$
:::

:::

::: pf-qed
Steps [](#cohomology-invariance){.pf-ref}, [](#euler-char-invariance){.pf-ref} and [](#arithmetic-genus-equal){.pf-ref} prove the asserted invariance of the arithmetic genus under
blowing up a nonsingular centre.
:::

:::
:::

::: {.remark title="Published solution"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 1 of §3 (solution by Shuang-Yen Lee), PDF p. 9, proves the vanishing for a blowup of a nonsingular subvariety of any codimension: by Exercise III.8.1 it suffices to have $\pi_*\OO_{\widetilde X}=\OO_X$, which is the proof of III.11.4, and $R^i\pi_*\OO_{\widetilde X}=0$ for $i>0$. Outside the centre $\pi$ is an isomorphism; at a point of $Y$ the formal functions theorem identifies the stalk of $R^i\pi_*\OO_{\widetilde X}$ with $\varprojlim H^i(E_n,\OO_{E_n})$, where $E$ is the exceptional divisor and $I^ n/I^{n+1}\cong\operatorname{Sym}^n(I/I^2)\cong\OO_E(n)$ with $E\cong\PP^{r-1}$, $r=\operatorname{codim}(Y,X)$; induction on $n$ from $H^i(\PP^{r-1},\OO(n))=0$ for $i>0$ gives the vanishing, hence $p_a(\widetilde X)=p_a(X)$. Steps [](#cohomology-invariance){.pf-ref} to [](#arithmetic-genus-equal){.pf-ref} reach the same conclusion through $R^j\pi_*\OO_{\widetilde X}=0$ for $j>0$ in all dimensions at once, which is Chatzistamatiou--Rülling's theorem.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.3.1, printed p. 107, writes "since $\operatorname{codim}(Y,X)=1$, $\mathcal I/\mathcal I^2$ is an invertible sheaf on $Y$" and then covers $E$ by $\PP^1_A$'s; the exercise has $Y$ of any codimension, and a codimension-one blowup is an isomorphism, so the argument does not cover the case it is aimed at.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.3.1, PDF p. 273: the whole of his solution is "This follows from 3.4, which says that $H^i(\widetilde X)\approx H^i(X)$ and the fact that $p_a$ is calculated from the Euler characteristic". Result (3.4) and its corollary (3.5) are the monoidal case, where the centre is a point; the exercise blows up a nonsingular subvariety of any codimension, and the invariance of $H^i(X,\OO_X)$ is then the vanishing of the higher direct images of $\OO_{\widetilde X}$ under a projective birational morphism of regular schemes, proved by Chatzistamatiou and Rülling, *Vanishing of the higher direct images of the structure sheaf*, Compositio Math. 151 (2015) 2131--2144, Theorem 1.1. Steps [](#cohomology-invariance){.pf-ref} to [](#arithmetic-genus-equal){.pf-ref} are that reduction, with $p_a(Z)=(-1)^n(\chi(Z,\OO_Z)-1)$.
:::
